# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1PodStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'conditions': 'list[V1PodCondition]',
        'container_statuses': 'list[V1ContainerStatus]',
        'host_ip': 'str',
        'init_container_statuses': 'list[V1ContainerStatus]',
        'message': 'str',
        'nominated_node_name': 'str',
        'phase': 'str',
        'pod_ip': 'str',
        'qos_class': 'str',
        'reason': 'str',
        'start_time': 'datetime'
    }

    attribute_map = {
        'conditions': 'conditions',
        'container_statuses': 'containerStatuses',
        'host_ip': 'hostIP',
        'init_container_statuses': 'initContainerStatuses',
        'message': 'message',
        'nominated_node_name': 'nominatedNodeName',
        'phase': 'phase',
        'pod_ip': 'podIP',
        'qos_class': 'qosClass',
        'reason': 'reason',
        'start_time': 'startTime'
    }

    def __init__(self, conditions=None, container_statuses=None, host_ip=None, init_container_statuses=None, message=None, nominated_node_name=None, phase=None, pod_ip=None, qos_class=None, reason=None, start_time=None):
        """
        V1PodStatus - a model defined in Swagger
        """

        self._conditions = None
        self._container_statuses = None
        self._host_ip = None
        self._init_container_statuses = None
        self._message = None
        self._nominated_node_name = None
        self._phase = None
        self._pod_ip = None
        self._qos_class = None
        self._reason = None
        self._start_time = None
        self.discriminator = None

        if conditions is not None:
          self.conditions = conditions
        if container_statuses is not None:
          self.container_statuses = container_statuses
        if host_ip is not None:
          self.host_ip = host_ip
        if init_container_statuses is not None:
          self.init_container_statuses = init_container_statuses
        if message is not None:
          self.message = message
        if nominated_node_name is not None:
          self.nominated_node_name = nominated_node_name
        if phase is not None:
          self.phase = phase
        if pod_ip is not None:
          self.pod_ip = pod_ip
        if qos_class is not None:
          self.qos_class = qos_class
        if reason is not None:
          self.reason = reason
        if start_time is not None:
          self.start_time = start_time

    @property
    def conditions(self):
        """
        Gets the conditions of this V1PodStatus.
        Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions

        :return: The conditions of this V1PodStatus.
        :rtype: list[V1PodCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1PodStatus.
        Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions

        :param conditions: The conditions of this V1PodStatus.
        :type: list[V1PodCondition]
        """

        self._conditions = conditions

    @property
    def container_statuses(self):
        """
        Gets the container_statuses of this V1PodStatus.
        The list has one entry per container in the manifest. Each entry is currently the output of `docker inspect`. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status

        :return: The container_statuses of this V1PodStatus.
        :rtype: list[V1ContainerStatus]
        """
        return self._container_statuses

    @container_statuses.setter
    def container_statuses(self, container_statuses):
        """
        Sets the container_statuses of this V1PodStatus.
        The list has one entry per container in the manifest. Each entry is currently the output of `docker inspect`. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status

        :param container_statuses: The container_statuses of this V1PodStatus.
        :type: list[V1ContainerStatus]
        """

        self._container_statuses = container_statuses

    @property
    def host_ip(self):
        """
        Gets the host_ip of this V1PodStatus.
        IP address of the host to which the pod is assigned. Empty if not yet scheduled.

        :return: The host_ip of this V1PodStatus.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """
        Sets the host_ip of this V1PodStatus.
        IP address of the host to which the pod is assigned. Empty if not yet scheduled.

        :param host_ip: The host_ip of this V1PodStatus.
        :type: str
        """

        self._host_ip = host_ip

    @property
    def init_container_statuses(self):
        """
        Gets the init_container_statuses of this V1PodStatus.
        The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status

        :return: The init_container_statuses of this V1PodStatus.
        :rtype: list[V1ContainerStatus]
        """
        return self._init_container_statuses

    @init_container_statuses.setter
    def init_container_statuses(self, init_container_statuses):
        """
        Sets the init_container_statuses of this V1PodStatus.
        The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status

        :param init_container_statuses: The init_container_statuses of this V1PodStatus.
        :type: list[V1ContainerStatus]
        """

        self._init_container_statuses = init_container_statuses

    @property
    def message(self):
        """
        Gets the message of this V1PodStatus.
        A human readable message indicating details about why the pod is in this condition.

        :return: The message of this V1PodStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1PodStatus.
        A human readable message indicating details about why the pod is in this condition.

        :param message: The message of this V1PodStatus.
        :type: str
        """

        self._message = message

    @property
    def nominated_node_name(self):
        """
        Gets the nominated_node_name of this V1PodStatus.
        nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.

        :return: The nominated_node_name of this V1PodStatus.
        :rtype: str
        """
        return self._nominated_node_name

    @nominated_node_name.setter
    def nominated_node_name(self, nominated_node_name):
        """
        Sets the nominated_node_name of this V1PodStatus.
        nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.

        :param nominated_node_name: The nominated_node_name of this V1PodStatus.
        :type: str
        """

        self._nominated_node_name = nominated_node_name

    @property
    def phase(self):
        """
        Gets the phase of this V1PodStatus.
        The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase

        :return: The phase of this V1PodStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1PodStatus.
        The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase

        :param phase: The phase of this V1PodStatus.
        :type: str
        """

        self._phase = phase

    @property
    def pod_ip(self):
        """
        Gets the pod_ip of this V1PodStatus.
        IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.

        :return: The pod_ip of this V1PodStatus.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        """
        Sets the pod_ip of this V1PodStatus.
        IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.

        :param pod_ip: The pod_ip of this V1PodStatus.
        :type: str
        """

        self._pod_ip = pod_ip

    @property
    def qos_class(self):
        """
        Gets the qos_class of this V1PodStatus.
        The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md

        :return: The qos_class of this V1PodStatus.
        :rtype: str
        """
        return self._qos_class

    @qos_class.setter
    def qos_class(self, qos_class):
        """
        Sets the qos_class of this V1PodStatus.
        The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md

        :param qos_class: The qos_class of this V1PodStatus.
        :type: str
        """

        self._qos_class = qos_class

    @property
    def reason(self):
        """
        Gets the reason of this V1PodStatus.
        A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'

        :return: The reason of this V1PodStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1PodStatus.
        A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'

        :param reason: The reason of this V1PodStatus.
        :type: str
        """

        self._reason = reason

    @property
    def start_time(self):
        """
        Gets the start_time of this V1PodStatus.
        RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.

        :return: The start_time of this V1PodStatus.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this V1PodStatus.
        RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.

        :param start_time: The start_time of this V1PodStatus.
        :type: datetime
        """

        self._start_time = start_time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1PodStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
