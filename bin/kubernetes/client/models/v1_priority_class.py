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


class V1PriorityClass(object):
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
        'api_version': 'str',
        'description': 'str',
        'global_default': 'bool',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'value': 'int'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'description': 'description',
        'global_default': 'globalDefault',
        'kind': 'kind',
        'metadata': 'metadata',
        'value': 'value'
    }

    def __init__(self, api_version=None, description=None, global_default=None, kind=None, metadata=None, value=None):
        """
        V1PriorityClass - a model defined in Swagger
        """

        self._api_version = None
        self._description = None
        self._global_default = None
        self._kind = None
        self._metadata = None
        self._value = None
        self.discriminator = None

        if api_version is not None:
          self.api_version = api_version
        if description is not None:
          self.description = description
        if global_default is not None:
          self.global_default = global_default
        if kind is not None:
          self.kind = kind
        if metadata is not None:
          self.metadata = metadata
        self.value = value

    @property
    def api_version(self):
        """
        Gets the api_version of this V1PriorityClass.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1PriorityClass.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1PriorityClass.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1PriorityClass.
        :type: str
        """

        self._api_version = api_version

    @property
    def description(self):
        """
        Gets the description of this V1PriorityClass.
        description is an arbitrary string that usually provides guidelines on when this priority class should be used.

        :return: The description of this V1PriorityClass.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this V1PriorityClass.
        description is an arbitrary string that usually provides guidelines on when this priority class should be used.

        :param description: The description of this V1PriorityClass.
        :type: str
        """

        self._description = description

    @property
    def global_default(self):
        """
        Gets the global_default of this V1PriorityClass.
        globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.

        :return: The global_default of this V1PriorityClass.
        :rtype: bool
        """
        return self._global_default

    @global_default.setter
    def global_default(self, global_default):
        """
        Sets the global_default of this V1PriorityClass.
        globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.

        :param global_default: The global_default of this V1PriorityClass.
        :type: bool
        """

        self._global_default = global_default

    @property
    def kind(self):
        """
        Gets the kind of this V1PriorityClass.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1PriorityClass.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1PriorityClass.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1PriorityClass.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1PriorityClass.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :return: The metadata of this V1PriorityClass.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1PriorityClass.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1PriorityClass.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def value(self):
        """
        Gets the value of this V1PriorityClass.
        The value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.

        :return: The value of this V1PriorityClass.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this V1PriorityClass.
        The value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.

        :param value: The value of this V1PriorityClass.
        :type: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

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
        if not isinstance(other, V1PriorityClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
