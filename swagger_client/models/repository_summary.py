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

class RepositorySummary(object):
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
        'repository_id': 'str',
        'kind': 'RepositoryKind',
        'name': 'str',
        'display_name': 'str',
        'url': 'str',
        'verified_publisher': 'bool',
        'official': 'bool',
        'cncf': 'bool',
        'private': 'bool',
        'scanner_disabled': 'bool',
        'user_alias': 'str',
        'organization_name': 'str',
        'organization_display_name': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'kind': 'kind',
        'name': 'name',
        'display_name': 'display_name',
        'url': 'url',
        'verified_publisher': 'verified_publisher',
        'official': 'official',
        'cncf': 'cncf',
        'private': 'private',
        'scanner_disabled': 'scanner_disabled',
        'user_alias': 'user_alias',
        'organization_name': 'organization_name',
        'organization_display_name': 'organization_display_name'
    }

    def __init__(self, repository_id=None, kind=None, name=None, display_name=None, url=None, verified_publisher=None, official=None, cncf=None, private=None, scanner_disabled=None, user_alias=None, organization_name=None, organization_display_name=None):  # noqa: E501
        """RepositorySummary - a model defined in Swagger"""  # noqa: E501
        self._repository_id = None
        self._kind = None
        self._name = None
        self._display_name = None
        self._url = None
        self._verified_publisher = None
        self._official = None
        self._cncf = None
        self._private = None
        self._scanner_disabled = None
        self._user_alias = None
        self._organization_name = None
        self._organization_display_name = None
        self.discriminator = None
        self.repository_id = repository_id
        self.kind = kind
        self.name = name
        if display_name is not None:
            self.display_name = display_name
        self.url = url
        self.verified_publisher = verified_publisher
        self.official = official
        if cncf is not None:
            self.cncf = cncf
        if private is not None:
            self.private = private
        self.scanner_disabled = scanner_disabled
        if user_alias is not None:
            self.user_alias = user_alias
        if organization_name is not None:
            self.organization_name = organization_name
        if organization_display_name is not None:
            self.organization_display_name = organization_display_name

    @property
    def repository_id(self):
        """Gets the repository_id of this RepositorySummary.  # noqa: E501


        :return: The repository_id of this RepositorySummary.  # noqa: E501
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this RepositorySummary.


        :param repository_id: The repository_id of this RepositorySummary.  # noqa: E501
        :type: str
        """
        if repository_id is None:
            raise ValueError("Invalid value for `repository_id`, must not be `None`")  # noqa: E501

        self._repository_id = repository_id

    @property
    def kind(self):
        """Gets the kind of this RepositorySummary.  # noqa: E501


        :return: The kind of this RepositorySummary.  # noqa: E501
        :rtype: RepositoryKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this RepositorySummary.


        :param kind: The kind of this RepositorySummary.  # noqa: E501
        :type: RepositoryKind
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this RepositorySummary.  # noqa: E501


        :return: The name of this RepositorySummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositorySummary.


        :param name: The name of this RepositorySummary.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this RepositorySummary.  # noqa: E501


        :return: The display_name of this RepositorySummary.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this RepositorySummary.


        :param display_name: The display_name of this RepositorySummary.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def url(self):
        """Gets the url of this RepositorySummary.  # noqa: E501


        :return: The url of this RepositorySummary.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RepositorySummary.


        :param url: The url of this RepositorySummary.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def verified_publisher(self):
        """Gets the verified_publisher of this RepositorySummary.  # noqa: E501


        :return: The verified_publisher of this RepositorySummary.  # noqa: E501
        :rtype: bool
        """
        return self._verified_publisher

    @verified_publisher.setter
    def verified_publisher(self, verified_publisher):
        """Sets the verified_publisher of this RepositorySummary.


        :param verified_publisher: The verified_publisher of this RepositorySummary.  # noqa: E501
        :type: bool
        """
        if verified_publisher is None:
            raise ValueError("Invalid value for `verified_publisher`, must not be `None`")  # noqa: E501

        self._verified_publisher = verified_publisher

    @property
    def official(self):
        """Gets the official of this RepositorySummary.  # noqa: E501


        :return: The official of this RepositorySummary.  # noqa: E501
        :rtype: bool
        """
        return self._official

    @official.setter
    def official(self, official):
        """Sets the official of this RepositorySummary.


        :param official: The official of this RepositorySummary.  # noqa: E501
        :type: bool
        """
        if official is None:
            raise ValueError("Invalid value for `official`, must not be `None`")  # noqa: E501

        self._official = official

    @property
    def cncf(self):
        """Gets the cncf of this RepositorySummary.  # noqa: E501


        :return: The cncf of this RepositorySummary.  # noqa: E501
        :rtype: bool
        """
        return self._cncf

    @cncf.setter
    def cncf(self, cncf):
        """Sets the cncf of this RepositorySummary.


        :param cncf: The cncf of this RepositorySummary.  # noqa: E501
        :type: bool
        """

        self._cncf = cncf

    @property
    def private(self):
        """Gets the private of this RepositorySummary.  # noqa: E501


        :return: The private of this RepositorySummary.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this RepositorySummary.


        :param private: The private of this RepositorySummary.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def scanner_disabled(self):
        """Gets the scanner_disabled of this RepositorySummary.  # noqa: E501


        :return: The scanner_disabled of this RepositorySummary.  # noqa: E501
        :rtype: bool
        """
        return self._scanner_disabled

    @scanner_disabled.setter
    def scanner_disabled(self, scanner_disabled):
        """Sets the scanner_disabled of this RepositorySummary.


        :param scanner_disabled: The scanner_disabled of this RepositorySummary.  # noqa: E501
        :type: bool
        """
        if scanner_disabled is None:
            raise ValueError("Invalid value for `scanner_disabled`, must not be `None`")  # noqa: E501

        self._scanner_disabled = scanner_disabled

    @property
    def user_alias(self):
        """Gets the user_alias of this RepositorySummary.  # noqa: E501


        :return: The user_alias of this RepositorySummary.  # noqa: E501
        :rtype: str
        """
        return self._user_alias

    @user_alias.setter
    def user_alias(self, user_alias):
        """Sets the user_alias of this RepositorySummary.


        :param user_alias: The user_alias of this RepositorySummary.  # noqa: E501
        :type: str
        """

        self._user_alias = user_alias

    @property
    def organization_name(self):
        """Gets the organization_name of this RepositorySummary.  # noqa: E501


        :return: The organization_name of this RepositorySummary.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this RepositorySummary.


        :param organization_name: The organization_name of this RepositorySummary.  # noqa: E501
        :type: str
        """

        self._organization_name = organization_name

    @property
    def organization_display_name(self):
        """Gets the organization_display_name of this RepositorySummary.  # noqa: E501


        :return: The organization_display_name of this RepositorySummary.  # noqa: E501
        :rtype: str
        """
        return self._organization_display_name

    @organization_display_name.setter
    def organization_display_name(self, organization_display_name):
        """Sets the organization_display_name of this RepositorySummary.


        :param organization_display_name: The organization_display_name of this RepositorySummary.  # noqa: E501
        :type: str
        """

        self._organization_display_name = organization_display_name

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
        if issubclass(RepositorySummary, dict):
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
        if not isinstance(other, RepositorySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
