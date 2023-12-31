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

class GatekeeperPolicyData(object):
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
        'template': 'str',
        'examples': 'list[GatekeeperPolicyDataExamples]'
    }

    attribute_map = {
        'template': 'template',
        'examples': 'examples'
    }

    def __init__(self, template=None, examples=None):  # noqa: E501
        """GatekeeperPolicyData - a model defined in Swagger"""  # noqa: E501
        self._template = None
        self._examples = None
        self.discriminator = None
        if template is not None:
            self.template = template
        if examples is not None:
            self.examples = examples

    @property
    def template(self):
        """Gets the template of this GatekeeperPolicyData.  # noqa: E501


        :return: The template of this GatekeeperPolicyData.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this GatekeeperPolicyData.


        :param template: The template of this GatekeeperPolicyData.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def examples(self):
        """Gets the examples of this GatekeeperPolicyData.  # noqa: E501


        :return: The examples of this GatekeeperPolicyData.  # noqa: E501
        :rtype: list[GatekeeperPolicyDataExamples]
        """
        return self._examples

    @examples.setter
    def examples(self, examples):
        """Sets the examples of this GatekeeperPolicyData.


        :param examples: The examples of this GatekeeperPolicyData.  # noqa: E501
        :type: list[GatekeeperPolicyDataExamples]
        """

        self._examples = examples

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
        if issubclass(GatekeeperPolicyData, dict):
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
        if not isinstance(other, GatekeeperPolicyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
