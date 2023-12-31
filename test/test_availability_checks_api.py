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
from swagger_client.api.availability_checks_api import AvailabilityChecksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAvailabilityChecksApi(unittest.TestCase):
    """AvailabilityChecksApi unit test stubs"""

    def setUp(self):
        self.api = AvailabilityChecksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_availability(self):
        """Test case for check_availability

        Check the availability of a given value for the provided resource kind  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
