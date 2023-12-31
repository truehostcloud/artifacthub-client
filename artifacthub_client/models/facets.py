# coding: utf-8

"""
    Artifact Hub

    Find, install and publish Kubernetes packages  # noqa: E501

    OpenAPI spec version: 1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Facets(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'filter_key': 'str',
        'title': 'str',
        'options': 'list[FacetsOptions]'
    }

    attribute_map = {
        'filter_key': 'filter_key',
        'title': 'title',
        'options': 'options'
    }

    def __init__(self, filter_key=None, title=None, options=None):  # noqa: E501
        """Facets - a model defined in Swagger"""  # noqa: E501
        self._filter_key = None
        self._title = None
        self._options = None
        self.discriminator = None
        self.filter_key = filter_key
        self.title = title
        self.options = options

    @property
    def filter_key(self):
        """Gets the filter_key of this Facets.  # noqa: E501


        :return: The filter_key of this Facets.  # noqa: E501
        :rtype: str
        """
        return self._filter_key

    @filter_key.setter
    def filter_key(self, filter_key):
        """Sets the filter_key of this Facets.


        :param filter_key: The filter_key of this Facets.  # noqa: E501
        :type: str
        """
        if filter_key is None:
            raise ValueError("Invalid value for `filter_key`, must not be `None`")  # noqa: E501

        self._filter_key = filter_key

    @property
    def title(self):
        """Gets the title of this Facets.  # noqa: E501


        :return: The title of this Facets.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Facets.


        :param title: The title of this Facets.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def options(self):
        """Gets the options of this Facets.  # noqa: E501


        :return: The options of this Facets.  # noqa: E501
        :rtype: list[FacetsOptions]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Facets.


        :param options: The options of this Facets.  # noqa: E501
        :type: list[FacetsOptions]
        """
        if options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Facets, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Facets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
