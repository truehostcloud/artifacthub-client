# coding: utf-8

"""
    Artifact Hub

    Find, install and publish Kubernetes packages  # noqa: E501

    OpenAPI spec version: 1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.stats_api import StatsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStatsApi(unittest.TestCase):
    """StatsApi unit test stubs"""

    def setUp(self):
        self.api = StatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_artifact_hub_stats(self):
        """Test case for get_artifact_hub_stats

        Get Artifact Hub stats  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()