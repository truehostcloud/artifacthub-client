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

class WebhookSummaryWithPackagesPackages(object):
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
        'package_id': 'str'
    }

    attribute_map = {
        'package_id': 'package_id'
    }

    def __init__(self, package_id=None):  # noqa: E501
        """WebhookSummaryWithPackagesPackages - a model defined in Swagger"""  # noqa: E501
        self._package_id = None
        self.discriminator = None
        self.package_id = package_id

    @property
    def package_id(self):
        """Gets the package_id of this WebhookSummaryWithPackagesPackages.  # noqa: E501


        :return: The package_id of this WebhookSummaryWithPackagesPackages.  # noqa: E501
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this WebhookSummaryWithPackagesPackages.


        :param package_id: The package_id of this WebhookSummaryWithPackagesPackages.  # noqa: E501
        :type: str
        """
        if package_id is None:
            raise ValueError("Invalid value for `package_id`, must not be `None`")  # noqa: E501

        self._package_id = package_id

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
        if issubclass(WebhookSummaryWithPackagesPackages, dict):
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
        if not isinstance(other, WebhookSummaryWithPackagesPackages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
