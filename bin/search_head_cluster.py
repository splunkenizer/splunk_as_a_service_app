import os
import sys

bin_path = os.path.join(os.path.dirname(__file__))
if bin_path not in sys.path:
    sys.path.insert(0, bin_path)

from kubernetes import client as kuberneteslib
import yaml
import errors


def wait_until_ready(splunk, kubernetes, stack_id, stack_config):
    search_head_cluster = get(splunk, kubernetes, stack_id, stack_config)
    if not search_head_cluster:
        raise Exception("could not find search head cluster")
    status = search_head_cluster["status"]
    # captain: ...
    # captainReady: true
    # deployerPhase: Ready
    # initialized: true
    # maintenanceMode: false
    # members:
    # - active_historical_search_count: 0
    #     active_realtime_search_count: 0
    #     adhoc_searchhead: false
    #     is_registered: true
    #     name: ...
    #     status: Up
    # minPeersJoined: true
    # phase: Ready
    # readyReplicas: 3
    # replicas: 3
    # selector: ...
    target_search_head_count = int(stack_config["search_head_count"])
    actualy_ready_replica = status["readyReplicas"]
    if target_search_head_count != actualy_ready_replica:
        raise errors.RetryOperation("waiting for target number of search heads (expected %s, got %s)" % (
            target_search_head_count,
            actualy_ready_replica,
        ))
    deployer_phase = status["deployerPhase"]
    if deployer_phase != "Ready":
        raise errors.RetryOperation("waiting for deployer to become ready (currently it's in %s phase)" % (
            deployer_phase
        ))
    captain_ready = status["captainReady"]
    if not captain_ready:
        raise errors.RetryOperation("search head cluster captain not yet ready")
    phase = status["phase"]
    if phase != "Ready":
        raise errors.RetryOperation("waiting for search head cluster to become ready (currently it's in %s phase)" % (
            phase
        ))


def get(splunk, kubernetes, stack_id, stack_config):
    custom_objects_api = kuberneteslib.CustomObjectsApi(kubernetes)
    search_head_clusters = custom_objects_api.list_namespaced_custom_object(
        group="enterprise.splunk.com",
        version="v1",
        plural="searchheadclusters",
        namespace=stack_config["namespace"],
        label_selector="app=saas,stack_id=%s" % stack_id,
    )["items"]
    if len(search_head_clusters) > 1:
        raise Exception("found more than 1 search head cluster: %s" % len(search_head_clusters))
    if len(search_head_clusters) == 0:
        return None
    search_head_cluster = search_head_clusters[0]
    return search_head_cluster


def update(splunk, kubernetes, stack_id, stack_config):
    custom_objects_api = kuberneteslib.CustomObjectsApi(kubernetes)
    search_head_cluster = get(splunk, kubernetes, stack_id, stack_config)
    if not search_head_cluster:
        raise Exception("could not find search head cluster")
    search_head_cluster_spec = search_head_cluster["spec"]
    operations = []
    target_replica = int(stack_config["search_head_count"])
    if search_head_cluster_spec["replicas"] != target_replica:
        operations.append({
            "op": "replace",
            "path": "/spec/replicas",
            "value": target_replica,
        })
    if len(operations) > 0:
        custom_objects_api.patch_namespaced_custom_object(
            group="enterprise.splunk.com",
            version="v1",
            namespace=stack_config["namespace"],
            name=search_head_cluster["metadata"]["name"],
            plural="searchheadclusters",
            body=operations,
        )


def deploy(splunk, kubernetes, stack_id, stack_config, cluster_config):
    search_head_cluster = get(splunk, kubernetes, stack_id, stack_config)
    if search_head_cluster:
        return
    splunk_defaults = {
    }
    spec = {
        "replicas": int(stack_config["search_head_count"]),
        "image": cluster_config.default_splunk_image,
        "imagePullPolicy": "Always",
        "resources": {
            "requests": {
                "memory": stack_config["memory_per_instance"],
                "cpu": stack_config["cpu_per_instance"],
            },
            "limits": {
                "memory": stack_config["memory_per_instance"],
                "cpu": stack_config["cpu_per_instance"],
            },
        },
        "etcStorage": '%sGi' % stack_config["etc_storage_in_gb"],
        "varStorage": '%sGi' % stack_config["other_var_storage_in_gb"],
        "defaults": yaml.dump(splunk_defaults),
        "indexerClusterRef": {
            "name": "%s" % stack_id,
        }
    }
    if stack_config["license_master_mode"] == "remote":
        splunk_defaults.update({
            "splunk": {
                "license_master_url": cluster_config.license_master_url
                }
            })
    if len(splunk_defaults) > 0:
        spec["defaults"] = yaml.dump(splunk_defaults)
    if cluster_config.node_selector:
        labels = cluster_config.node_selector.split(",")
        match_expressions = []
        for label in labels:
            if label:
                kv = label.split("=")
                if len(kv) != 2:
                    raise errors.ApplicationError(
                        "invalid node selector format (%s)" % cluster_config.node_selector)
                match_expressions.append({
                    "key": kv[0],
                    "operator": "In",
                    "values": [kv[1]],
                })
        spec["affinity"] = {
            "nodeAffinity": {
                "requiredDuringSchedulingIgnoredDuringExecution": {
                    "nodeSelectorTerms": [
                        {
                            "matchExpressions": match_expressions,
                        }
                    ],
                }
            }
        }
    if "storage_class" in cluster_config and cluster_config.storage_class:
        spec["storageClassName"] = cluster_config.storage_class
    if stack_config["license_master_mode"] == "local":
        spec["licenseMasterRef"] = {
            "name": stack_id
        }
    custom_objects_api = kuberneteslib.CustomObjectsApi(kubernetes)
    custom_objects_api.create_namespaced_custom_object(
        group="enterprise.splunk.com",
        version="v1",
        namespace=stack_config["namespace"],
        plural="searchheadclusters",
        body={
            "apiVersion": "enterprise.splunk.com/v1",
            "kind": "SearchHeadCluster",
            "metadata": {
                "name": stack_id,
                "finalizers": ["enterprise.splunk.com/delete-pvc"],
                "labels": {
                    "app": "saas",
                    "stack_id": stack_id,
                }
            },
            "spec": spec,
        },
    )
