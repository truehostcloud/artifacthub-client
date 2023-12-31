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

class TektonPipelinePackageData(object):
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
        'pipelines_min_version': 'str',
        'manifest_raw': 'dict(str, str)',
        'tasks': 'TektonPipelinePackageDataTasks',
        'examples': 'dict(str, object)',
        'platforms': 'list[str]'
    }

    attribute_map = {
        'pipelines_min_version': 'pipelines.minVersion',
        'manifest_raw': 'manifestRaw',
        'tasks': 'tasks',
        'examples': 'examples',
        'platforms': 'platforms'
    }

    def __init__(self, pipelines_min_version=None, manifest_raw=None, tasks=None, examples=None, platforms=None):  # noqa: E501
        """TektonPipelinePackageData - a model defined in Swagger"""  # noqa: E501
        self._pipelines_min_version = None
        self._manifest_raw = None
        self._tasks = None
        self._examples = None
        self._platforms = None
        self.discriminator = None
        if pipelines_min_version is not None:
            self.pipelines_min_version = pipelines_min_version
        if manifest_raw is not None:
            self.manifest_raw = manifest_raw
        if tasks is not None:
            self.tasks = tasks
        if examples is not None:
            self.examples = examples
        if platforms is not None:
            self.platforms = platforms

    @property
    def pipelines_min_version(self):
        """Gets the pipelines_min_version of this TektonPipelinePackageData.  # noqa: E501


        :return: The pipelines_min_version of this TektonPipelinePackageData.  # noqa: E501
        :rtype: str
        """
        return self._pipelines_min_version

    @pipelines_min_version.setter
    def pipelines_min_version(self, pipelines_min_version):
        """Sets the pipelines_min_version of this TektonPipelinePackageData.


        :param pipelines_min_version: The pipelines_min_version of this TektonPipelinePackageData.  # noqa: E501
        :type: str
        """

        self._pipelines_min_version = pipelines_min_version

    @property
    def manifest_raw(self):
        """Gets the manifest_raw of this TektonPipelinePackageData.  # noqa: E501


        :return: The manifest_raw of this TektonPipelinePackageData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._manifest_raw

    @manifest_raw.setter
    def manifest_raw(self, manifest_raw):
        """Sets the manifest_raw of this TektonPipelinePackageData.


        :param manifest_raw: The manifest_raw of this TektonPipelinePackageData.  # noqa: E501
        :type: dict(str, str)
        """

        self._manifest_raw = manifest_raw

    @property
    def tasks(self):
        """Gets the tasks of this TektonPipelinePackageData.  # noqa: E501


        :return: The tasks of this TektonPipelinePackageData.  # noqa: E501
        :rtype: TektonPipelinePackageDataTasks
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this TektonPipelinePackageData.


        :param tasks: The tasks of this TektonPipelinePackageData.  # noqa: E501
        :type: TektonPipelinePackageDataTasks
        """

        self._tasks = tasks

    @property
    def examples(self):
        """Gets the examples of this TektonPipelinePackageData.  # noqa: E501


        :return: The examples of this TektonPipelinePackageData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._examples

    @examples.setter
    def examples(self, examples):
        """Sets the examples of this TektonPipelinePackageData.


        :param examples: The examples of this TektonPipelinePackageData.  # noqa: E501
        :type: dict(str, object)
        """

        self._examples = examples

    @property
    def platforms(self):
        """Gets the platforms of this TektonPipelinePackageData.  # noqa: E501


        :return: The platforms of this TektonPipelinePackageData.  # noqa: E501
        :rtype: list[str]
        """
        return self._platforms

    @platforms.setter
    def platforms(self, platforms):
        """Sets the platforms of this TektonPipelinePackageData.


        :param platforms: The platforms of this TektonPipelinePackageData.  # noqa: E501
        :type: list[str]
        """

        self._platforms = platforms

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
        if issubclass(TektonPipelinePackageData, dict):
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
        if not isinstance(other, TektonPipelinePackageData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
