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

class PackageBaseSecurityReportSummary(object):
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
        'critical': 'float',
        'high': 'float',
        'medium': 'float',
        'low': 'float',
        'unknown': 'float'
    }

    attribute_map = {
        'critical': 'critical',
        'high': 'high',
        'medium': 'medium',
        'low': 'low',
        'unknown': 'unknown'
    }

    def __init__(self, critical=None, high=None, medium=None, low=None, unknown=None):  # noqa: E501
        """PackageBaseSecurityReportSummary - a model defined in Swagger"""  # noqa: E501
        self._critical = None
        self._high = None
        self._medium = None
        self._low = None
        self._unknown = None
        self.discriminator = None
        if critical is not None:
            self.critical = critical
        if high is not None:
            self.high = high
        if medium is not None:
            self.medium = medium
        if low is not None:
            self.low = low
        if unknown is not None:
            self.unknown = unknown

    @property
    def critical(self):
        """Gets the critical of this PackageBaseSecurityReportSummary.  # noqa: E501


        :return: The critical of this PackageBaseSecurityReportSummary.  # noqa: E501
        :rtype: float
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this PackageBaseSecurityReportSummary.


        :param critical: The critical of this PackageBaseSecurityReportSummary.  # noqa: E501
        :type: float
        """

        self._critical = critical

    @property
    def high(self):
        """Gets the high of this PackageBaseSecurityReportSummary.  # noqa: E501


        :return: The high of this PackageBaseSecurityReportSummary.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this PackageBaseSecurityReportSummary.


        :param high: The high of this PackageBaseSecurityReportSummary.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def medium(self):
        """Gets the medium of this PackageBaseSecurityReportSummary.  # noqa: E501


        :return: The medium of this PackageBaseSecurityReportSummary.  # noqa: E501
        :rtype: float
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this PackageBaseSecurityReportSummary.


        :param medium: The medium of this PackageBaseSecurityReportSummary.  # noqa: E501
        :type: float
        """

        self._medium = medium

    @property
    def low(self):
        """Gets the low of this PackageBaseSecurityReportSummary.  # noqa: E501


        :return: The low of this PackageBaseSecurityReportSummary.  # noqa: E501
        :rtype: float
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this PackageBaseSecurityReportSummary.


        :param low: The low of this PackageBaseSecurityReportSummary.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def unknown(self):
        """Gets the unknown of this PackageBaseSecurityReportSummary.  # noqa: E501


        :return: The unknown of this PackageBaseSecurityReportSummary.  # noqa: E501
        :rtype: float
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this PackageBaseSecurityReportSummary.


        :param unknown: The unknown of this PackageBaseSecurityReportSummary.  # noqa: E501
        :type: float
        """

        self._unknown = unknown

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
        if issubclass(PackageBaseSecurityReportSummary, dict):
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
        if not isinstance(other, PackageBaseSecurityReportSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
