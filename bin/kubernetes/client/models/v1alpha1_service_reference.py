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


class V1alpha1ServiceReference(object):
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
        'name': 'str',
        'namespace': 'str',
        'path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'path': 'path'
    }

    def __init__(self, name=None, namespace=None, path=None):
        """
        V1alpha1ServiceReference - a model defined in Swagger
        """

        self._name = None
        self._namespace = None
        self._path = None
        self.discriminator = None

        self.name = name
        self.namespace = namespace
        if path is not None:
          self.path = path

    @property
    def name(self):
        """
        Gets the name of this V1alpha1ServiceReference.
        `name` is the name of the service. Required

        :return: The name of this V1alpha1ServiceReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1alpha1ServiceReference.
        `name` is the name of the service. Required

        :param name: The name of this V1alpha1ServiceReference.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def namespace(self):
        """
        Gets the namespace of this V1alpha1ServiceReference.
        `namespace` is the namespace of the service. Required

        :return: The namespace of this V1alpha1ServiceReference.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this V1alpha1ServiceReference.
        `namespace` is the namespace of the service. Required

        :param namespace: The namespace of this V1alpha1ServiceReference.
        :type: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")

        self._namespace = namespace

    @property
    def path(self):
        """
        Gets the path of this V1alpha1ServiceReference.
        `path` is an optional URL path which will be sent in any request to this service.

        :return: The path of this V1alpha1ServiceReference.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1alpha1ServiceReference.
        `path` is an optional URL path which will be sent in any request to this service.

        :param path: The path of this V1alpha1ServiceReference.
        :type: str
        """

        self._path = path

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
        if not isinstance(other, V1alpha1ServiceReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
