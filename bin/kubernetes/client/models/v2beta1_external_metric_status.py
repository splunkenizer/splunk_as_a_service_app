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


class V2beta1ExternalMetricStatus(object):
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
        'current_average_value': 'str',
        'current_value': 'str',
        'metric_name': 'str',
        'metric_selector': 'V1LabelSelector'
    }

    attribute_map = {
        'current_average_value': 'currentAverageValue',
        'current_value': 'currentValue',
        'metric_name': 'metricName',
        'metric_selector': 'metricSelector'
    }

    def __init__(self, current_average_value=None, current_value=None, metric_name=None, metric_selector=None):
        """
        V2beta1ExternalMetricStatus - a model defined in Swagger
        """

        self._current_average_value = None
        self._current_value = None
        self._metric_name = None
        self._metric_selector = None
        self.discriminator = None

        if current_average_value is not None:
          self.current_average_value = current_average_value
        self.current_value = current_value
        self.metric_name = metric_name
        if metric_selector is not None:
          self.metric_selector = metric_selector

    @property
    def current_average_value(self):
        """
        Gets the current_average_value of this V2beta1ExternalMetricStatus.
        currentAverageValue is the current value of metric averaged over autoscaled pods.

        :return: The current_average_value of this V2beta1ExternalMetricStatus.
        :rtype: str
        """
        return self._current_average_value

    @current_average_value.setter
    def current_average_value(self, current_average_value):
        """
        Sets the current_average_value of this V2beta1ExternalMetricStatus.
        currentAverageValue is the current value of metric averaged over autoscaled pods.

        :param current_average_value: The current_average_value of this V2beta1ExternalMetricStatus.
        :type: str
        """

        self._current_average_value = current_average_value

    @property
    def current_value(self):
        """
        Gets the current_value of this V2beta1ExternalMetricStatus.
        currentValue is the current value of the metric (as a quantity)

        :return: The current_value of this V2beta1ExternalMetricStatus.
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """
        Sets the current_value of this V2beta1ExternalMetricStatus.
        currentValue is the current value of the metric (as a quantity)

        :param current_value: The current_value of this V2beta1ExternalMetricStatus.
        :type: str
        """
        if current_value is None:
            raise ValueError("Invalid value for `current_value`, must not be `None`")

        self._current_value = current_value

    @property
    def metric_name(self):
        """
        Gets the metric_name of this V2beta1ExternalMetricStatus.
        metricName is the name of a metric used for autoscaling in metric system.

        :return: The metric_name of this V2beta1ExternalMetricStatus.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this V2beta1ExternalMetricStatus.
        metricName is the name of a metric used for autoscaling in metric system.

        :param metric_name: The metric_name of this V2beta1ExternalMetricStatus.
        :type: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")

        self._metric_name = metric_name

    @property
    def metric_selector(self):
        """
        Gets the metric_selector of this V2beta1ExternalMetricStatus.
        metricSelector is used to identify a specific time series within a given metric.

        :return: The metric_selector of this V2beta1ExternalMetricStatus.
        :rtype: V1LabelSelector
        """
        return self._metric_selector

    @metric_selector.setter
    def metric_selector(self, metric_selector):
        """
        Sets the metric_selector of this V2beta1ExternalMetricStatus.
        metricSelector is used to identify a specific time series within a given metric.

        :param metric_selector: The metric_selector of this V2beta1ExternalMetricStatus.
        :type: V1LabelSelector
        """

        self._metric_selector = metric_selector

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
        if not isinstance(other, V2beta1ExternalMetricStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
