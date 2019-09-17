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


class V2beta2PodsMetricSource(object):
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
        'metric': 'V2beta2MetricIdentifier',
        'target': 'V2beta2MetricTarget'
    }

    attribute_map = {
        'metric': 'metric',
        'target': 'target'
    }

    def __init__(self, metric=None, target=None):
        """
        V2beta2PodsMetricSource - a model defined in Swagger
        """

        self._metric = None
        self._target = None
        self.discriminator = None

        self.metric = metric
        self.target = target

    @property
    def metric(self):
        """
        Gets the metric of this V2beta2PodsMetricSource.
        metric identifies the target metric by name and selector

        :return: The metric of this V2beta2PodsMetricSource.
        :rtype: V2beta2MetricIdentifier
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this V2beta2PodsMetricSource.
        metric identifies the target metric by name and selector

        :param metric: The metric of this V2beta2PodsMetricSource.
        :type: V2beta2MetricIdentifier
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")

        self._metric = metric

    @property
    def target(self):
        """
        Gets the target of this V2beta2PodsMetricSource.
        target specifies the target value for the given metric

        :return: The target of this V2beta2PodsMetricSource.
        :rtype: V2beta2MetricTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this V2beta2PodsMetricSource.
        target specifies the target value for the given metric

        :param target: The target of this V2beta2PodsMetricSource.
        :type: V2beta2MetricTarget
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")

        self._target = target

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
        if not isinstance(other, V2beta2PodsMetricSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
