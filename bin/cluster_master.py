import os
import sys

bin_path = os.path.join(os.path.dirname(__file__))
if bin_path not in sys.path:
    sys.path.insert(0, bin_path)

from kubernetes import client as kuberneteslib
import yaml
import errors


def wait_until_ready(splunk, kubernetes, stack_id, stack_config):
    cluster_master = get(splunk, kubernetes, stack_id, stack_config)
    if not cluster_master:
        raise Exception("could not find cluster master")
    if not "status" in cluster_master:
        raise errors.RetryOperation("waiting for cluster master status")
    status = cluster_master["status"]
    phase = status["phase"]
    if phase != "Ready":
        raise errors.RetryOperation("waiting for cluster master to become ready (currently it's in %s phase)" % (
            phase
        ))


def get(splunk, kubernetes, stack_id, stack_config):
    custom_objects_api = kuberneteslib.CustomObjectsApi(kubernetes)
    cluster_master = custom_objects_api.list_namespaced_custom_object(
        group="enterprise.splunk.com",
        version="v1",
        plural="clustermasters",
        namespace=stack_config["namespace"],
        label_selector="app=saas,stack_id=%s" % stack_id,
    )["items"]
    if len(cluster_master) > 1:
        raise Exception("found more than 1 cluster master: %s" % len(cluster_master))
    if len(cluster_master) == 0:
        return None
    cluster_master = cluster_master[0]
    return cluster_master


def update(splunk, kubernetes, stack_id, stack_config):
    pass


def deploy(splunk, kubernetes, stack_id, stack_config, cluster_config):
    cluster_master = get(splunk, kubernetes, stack_id, stack_config)
    if cluster_master:
        return
    splunk_defaults = {
    }
    spec = {
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
        "varStorage": '%sGi' % stack_config["other_var_storage_in_gb"]
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
        plural="clustermasters",
        body={
            "apiVersion": "enterprise.splunk.com/v1",
            "kind": "ClusterMaster",
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
