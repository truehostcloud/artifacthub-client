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
from artifacthub_client.models.repository_summary import RepositorySummary  # noqa: F401,E501

class Repository(RepositorySummary):
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
        'digest': 'str',
        'last_tracking_ts': 'int',
        'last_tracking_errors': 'str',
        'last_scanning_ts': 'int',
        'last_scanning_errors': 'str',
        'disabled': 'bool',
        'branch': 'str',
        'data': 'RepositoryData'
    }
    if hasattr(RepositorySummary, "swagger_types"):
        swagger_types.update(RepositorySummary.swagger_types)

    attribute_map = {
        'digest': 'digest',
        'last_tracking_ts': 'last_tracking_ts',
        'last_tracking_errors': 'last_tracking_errors',
        'last_scanning_ts': 'last_scanning_ts',
        'last_scanning_errors': 'last_scanning_errors',
        'disabled': 'disabled',
        'branch': 'branch',
        'data': 'data'
    }
    if hasattr(RepositorySummary, "attribute_map"):
        attribute_map.update(RepositorySummary.attribute_map)

    def __init__(self, digest=None, last_tracking_ts=None, last_tracking_errors=None, last_scanning_ts=None, last_scanning_errors=None, disabled=None, branch=None, data=None, *args, **kwargs):  # noqa: E501
        """Repository - a model defined in Swagger"""  # noqa: E501
        self._digest = None
        self._last_tracking_ts = None
        self._last_tracking_errors = None
        self._last_scanning_ts = None
        self._last_scanning_errors = None
        self._disabled = None
        self._branch = None
        self._data = None
        self.discriminator = None
        self.digest = digest
        self.last_tracking_ts = last_tracking_ts
        if last_tracking_errors is not None:
            self.last_tracking_errors = last_tracking_errors
        self.last_scanning_ts = last_scanning_ts
        if last_scanning_errors is not None:
            self.last_scanning_errors = last_scanning_errors
        self.disabled = disabled
        if branch is not None:
            self.branch = branch
        if data is not None:
            self.data = data
        RepositorySummary.__init__(self, *args, **kwargs)

    @property
    def digest(self):
        """Gets the digest of this Repository.  # noqa: E501


        :return: The digest of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this Repository.


        :param digest: The digest of this Repository.  # noqa: E501
        :type: str
        """
        if digest is None:
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest

    @property
    def last_tracking_ts(self):
        """Gets the last_tracking_ts of this Repository.  # noqa: E501


        :return: The last_tracking_ts of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._last_tracking_ts

    @last_tracking_ts.setter
    def last_tracking_ts(self, last_tracking_ts):
        """Sets the last_tracking_ts of this Repository.


        :param last_tracking_ts: The last_tracking_ts of this Repository.  # noqa: E501
        :type: int
        """
        if last_tracking_ts is None:
            raise ValueError("Invalid value for `last_tracking_ts`, must not be `None`")  # noqa: E501

        self._last_tracking_ts = last_tracking_ts

    @property
    def last_tracking_errors(self):
        """Gets the last_tracking_errors of this Repository.  # noqa: E501


        :return: The last_tracking_errors of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._last_tracking_errors

    @last_tracking_errors.setter
    def last_tracking_errors(self, last_tracking_errors):
        """Sets the last_tracking_errors of this Repository.


        :param last_tracking_errors: The last_tracking_errors of this Repository.  # noqa: E501
        :type: str
        """

        self._last_tracking_errors = last_tracking_errors

    @property
    def last_scanning_ts(self):
        """Gets the last_scanning_ts of this Repository.  # noqa: E501


        :return: The last_scanning_ts of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._last_scanning_ts

    @last_scanning_ts.setter
    def last_scanning_ts(self, last_scanning_ts):
        """Sets the last_scanning_ts of this Repository.


        :param last_scanning_ts: The last_scanning_ts of this Repository.  # noqa: E501
        :type: int
        """
        if last_scanning_ts is None:
            raise ValueError("Invalid value for `last_scanning_ts`, must not be `None`")  # noqa: E501

        self._last_scanning_ts = last_scanning_ts

    @property
    def last_scanning_errors(self):
        """Gets the last_scanning_errors of this Repository.  # noqa: E501


        :return: The last_scanning_errors of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._last_scanning_errors

    @last_scanning_errors.setter
    def last_scanning_errors(self, last_scanning_errors):
        """Sets the last_scanning_errors of this Repository.


        :param last_scanning_errors: The last_scanning_errors of this Repository.  # noqa: E501
        :type: str
        """

        self._last_scanning_errors = last_scanning_errors

    @property
    def disabled(self):
        """Gets the disabled of this Repository.  # noqa: E501


        :return: The disabled of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this Repository.


        :param disabled: The disabled of this Repository.  # noqa: E501
        :type: bool
        """
        if disabled is None:
            raise ValueError("Invalid value for `disabled`, must not be `None`")  # noqa: E501

        self._disabled = disabled

    @property
    def branch(self):
        """Gets the branch of this Repository.  # noqa: E501


        :return: The branch of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this Repository.


        :param branch: The branch of this Repository.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def data(self):
        """Gets the data of this Repository.  # noqa: E501


        :return: The data of this Repository.  # noqa: E501
        :rtype: RepositoryData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Repository.


        :param data: The data of this Repository.  # noqa: E501
        :type: RepositoryData
        """

        self._data = data

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
        if issubclass(Repository, dict):
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
        if not isinstance(other, Repository):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
