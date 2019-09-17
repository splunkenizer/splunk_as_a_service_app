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


class ExtensionsV1beta1DeploymentSpec(object):
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
        'min_ready_seconds': 'int',
        'paused': 'bool',
        'progress_deadline_seconds': 'int',
        'replicas': 'int',
        'revision_history_limit': 'int',
        'rollback_to': 'ExtensionsV1beta1RollbackConfig',
        'selector': 'V1LabelSelector',
        'strategy': 'ExtensionsV1beta1DeploymentStrategy',
        'template': 'V1PodTemplateSpec'
    }

    attribute_map = {
        'min_ready_seconds': 'minReadySeconds',
        'paused': 'paused',
        'progress_deadline_seconds': 'progressDeadlineSeconds',
        'replicas': 'replicas',
        'revision_history_limit': 'revisionHistoryLimit',
        'rollback_to': 'rollbackTo',
        'selector': 'selector',
        'strategy': 'strategy',
        'template': 'template'
    }

    def __init__(self, min_ready_seconds=None, paused=None, progress_deadline_seconds=None, replicas=None, revision_history_limit=None, rollback_to=None, selector=None, strategy=None, template=None):
        """
        ExtensionsV1beta1DeploymentSpec - a model defined in Swagger
        """

        self._min_ready_seconds = None
        self._paused = None
        self._progress_deadline_seconds = None
        self._replicas = None
        self._revision_history_limit = None
        self._rollback_to = None
        self._selector = None
        self._strategy = None
        self._template = None
        self.discriminator = None

        if min_ready_seconds is not None:
          self.min_ready_seconds = min_ready_seconds
        if paused is not None:
          self.paused = paused
        if progress_deadline_seconds is not None:
          self.progress_deadline_seconds = progress_deadline_seconds
        if replicas is not None:
          self.replicas = replicas
        if revision_history_limit is not None:
          self.revision_history_limit = revision_history_limit
        if rollback_to is not None:
          self.rollback_to = rollback_to
        if selector is not None:
          self.selector = selector
        if strategy is not None:
          self.strategy = strategy
        self.template = template

    @property
    def min_ready_seconds(self):
        """
        Gets the min_ready_seconds of this ExtensionsV1beta1DeploymentSpec.
        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)

        :return: The min_ready_seconds of this ExtensionsV1beta1DeploymentSpec.
        :rtype: int
        """
        return self._min_ready_seconds

    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds):
        """
        Sets the min_ready_seconds of this ExtensionsV1beta1DeploymentSpec.
        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)

        :param min_ready_seconds: The min_ready_seconds of this ExtensionsV1beta1DeploymentSpec.
        :type: int
        """

        self._min_ready_seconds = min_ready_seconds

    @property
    def paused(self):
        """
        Gets the paused of this ExtensionsV1beta1DeploymentSpec.
        Indicates that the deployment is paused and will not be processed by the deployment controller.

        :return: The paused of this ExtensionsV1beta1DeploymentSpec.
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """
        Sets the paused of this ExtensionsV1beta1DeploymentSpec.
        Indicates that the deployment is paused and will not be processed by the deployment controller.

        :param paused: The paused of this ExtensionsV1beta1DeploymentSpec.
        :type: bool
        """

        self._paused = paused

    @property
    def progress_deadline_seconds(self):
        """
        Gets the progress_deadline_seconds of this ExtensionsV1beta1DeploymentSpec.
        The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. This is set to the max value of int32 (i.e. 2147483647) by default, which means \"no deadline\".

        :return: The progress_deadline_seconds of this ExtensionsV1beta1DeploymentSpec.
        :rtype: int
        """
        return self._progress_deadline_seconds

    @progress_deadline_seconds.setter
    def progress_deadline_seconds(self, progress_deadline_seconds):
        """
        Sets the progress_deadline_seconds of this ExtensionsV1beta1DeploymentSpec.
        The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. This is set to the max value of int32 (i.e. 2147483647) by default, which means \"no deadline\".

        :param progress_deadline_seconds: The progress_deadline_seconds of this ExtensionsV1beta1DeploymentSpec.
        :type: int
        """

        self._progress_deadline_seconds = progress_deadline_seconds

    @property
    def replicas(self):
        """
        Gets the replicas of this ExtensionsV1beta1DeploymentSpec.
        Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.

        :return: The replicas of this ExtensionsV1beta1DeploymentSpec.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this ExtensionsV1beta1DeploymentSpec.
        Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.

        :param replicas: The replicas of this ExtensionsV1beta1DeploymentSpec.
        :type: int
        """

        self._replicas = replicas

    @property
    def revision_history_limit(self):
        """
        Gets the revision_history_limit of this ExtensionsV1beta1DeploymentSpec.
        The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. This is set to the max value of int32 (i.e. 2147483647) by default, which means \"retaining all old RelicaSets\".

        :return: The revision_history_limit of this ExtensionsV1beta1DeploymentSpec.
        :rtype: int
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit):
        """
        Sets the revision_history_limit of this ExtensionsV1beta1DeploymentSpec.
        The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. This is set to the max value of int32 (i.e. 2147483647) by default, which means \"retaining all old RelicaSets\".

        :param revision_history_limit: The revision_history_limit of this ExtensionsV1beta1DeploymentSpec.
        :type: int
        """

        self._revision_history_limit = revision_history_limit

    @property
    def rollback_to(self):
        """
        Gets the rollback_to of this ExtensionsV1beta1DeploymentSpec.
        DEPRECATED. The config this deployment is rolling back to. Will be cleared after rollback is done.

        :return: The rollback_to of this ExtensionsV1beta1DeploymentSpec.
        :rtype: ExtensionsV1beta1RollbackConfig
        """
        return self._rollback_to

    @rollback_to.setter
    def rollback_to(self, rollback_to):
        """
        Sets the rollback_to of this ExtensionsV1beta1DeploymentSpec.
        DEPRECATED. The config this deployment is rolling back to. Will be cleared after rollback is done.

        :param rollback_to: The rollback_to of this ExtensionsV1beta1DeploymentSpec.
        :type: ExtensionsV1beta1RollbackConfig
        """

        self._rollback_to = rollback_to

    @property
    def selector(self):
        """
        Gets the selector of this ExtensionsV1beta1DeploymentSpec.
        Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment.

        :return: The selector of this ExtensionsV1beta1DeploymentSpec.
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this ExtensionsV1beta1DeploymentSpec.
        Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment.

        :param selector: The selector of this ExtensionsV1beta1DeploymentSpec.
        :type: V1LabelSelector
        """

        self._selector = selector

    @property
    def strategy(self):
        """
        Gets the strategy of this ExtensionsV1beta1DeploymentSpec.
        The deployment strategy to use to replace existing pods with new ones.

        :return: The strategy of this ExtensionsV1beta1DeploymentSpec.
        :rtype: ExtensionsV1beta1DeploymentStrategy
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """
        Sets the strategy of this ExtensionsV1beta1DeploymentSpec.
        The deployment strategy to use to replace existing pods with new ones.

        :param strategy: The strategy of this ExtensionsV1beta1DeploymentSpec.
        :type: ExtensionsV1beta1DeploymentStrategy
        """

        self._strategy = strategy

    @property
    def template(self):
        """
        Gets the template of this ExtensionsV1beta1DeploymentSpec.
        Template describes the pods that will be created.

        :return: The template of this ExtensionsV1beta1DeploymentSpec.
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this ExtensionsV1beta1DeploymentSpec.
        Template describes the pods that will be created.

        :param template: The template of this ExtensionsV1beta1DeploymentSpec.
        :type: V1PodTemplateSpec
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")

        self._template = template

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
        if not isinstance(other, ExtensionsV1beta1DeploymentSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
