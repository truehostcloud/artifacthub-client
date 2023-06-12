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

class InlineResponse2007(object):
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
        'opt_out_id': 'str',
        'repository': 'RepositorySummary',
        'event_kind': 'EventKindId'
    }

    attribute_map = {
        'opt_out_id': 'opt_out_id',
        'repository': 'repository',
        'event_kind': 'event_kind'
    }

    def __init__(self, opt_out_id=None, repository=None, event_kind=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501
        self._opt_out_id = None
        self._repository = None
        self._event_kind = None
        self.discriminator = None
        self.opt_out_id = opt_out_id
        self.repository = repository
        self.event_kind = event_kind

    @property
    def opt_out_id(self):
        """Gets the opt_out_id of this InlineResponse2007.  # noqa: E501


        :return: The opt_out_id of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._opt_out_id

    @opt_out_id.setter
    def opt_out_id(self, opt_out_id):
        """Sets the opt_out_id of this InlineResponse2007.


        :param opt_out_id: The opt_out_id of this InlineResponse2007.  # noqa: E501
        :type: str
        """
        if opt_out_id is None:
            raise ValueError("Invalid value for `opt_out_id`, must not be `None`")  # noqa: E501

        self._opt_out_id = opt_out_id

    @property
    def repository(self):
        """Gets the repository of this InlineResponse2007.  # noqa: E501


        :return: The repository of this InlineResponse2007.  # noqa: E501
        :rtype: RepositorySummary
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this InlineResponse2007.


        :param repository: The repository of this InlineResponse2007.  # noqa: E501
        :type: RepositorySummary
        """
        if repository is None:
            raise ValueError("Invalid value for `repository`, must not be `None`")  # noqa: E501

        self._repository = repository

    @property
    def event_kind(self):
        """Gets the event_kind of this InlineResponse2007.  # noqa: E501


        :return: The event_kind of this InlineResponse2007.  # noqa: E501
        :rtype: EventKindId
        """
        return self._event_kind

    @event_kind.setter
    def event_kind(self, event_kind):
        """Sets the event_kind of this InlineResponse2007.


        :param event_kind: The event_kind of this InlineResponse2007.  # noqa: E501
        :type: EventKindId
        """
        if event_kind is None:
            raise ValueError("Invalid value for `event_kind`, must not be `None`")  # noqa: E501

        self._event_kind = event_kind

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
        if issubclass(InlineResponse2007, dict):
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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
