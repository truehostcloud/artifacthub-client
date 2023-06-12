# coding: utf-8

"""
    Artifact Hub

    Find, install and publish Kubernetes packages  # noqa: E501

    OpenAPI spec version: 1.14.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from artifacthub_client.api_client import ApiClient


class AvailabilityChecksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_availability(self, resource_kind, v, **kwargs):  # noqa: E501
        """Check the availability of a given value for the provided resource kind  # noqa: E501

        Check the availability of a given value for the provided resource kind  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_availability(resource_kind, v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResourceKindName resource_kind: Resource kind name (required)
        :param str v: Value to check (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_availability_with_http_info(resource_kind, v, **kwargs)  # noqa: E501
        else:
            (data) = self.check_availability_with_http_info(resource_kind, v, **kwargs)  # noqa: E501
            return data

    def check_availability_with_http_info(self, resource_kind, v, **kwargs):  # noqa: E501
        """Check the availability of a given value for the provided resource kind  # noqa: E501

        Check the availability of a given value for the provided resource kind  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_availability_with_http_info(resource_kind, v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResourceKindName resource_kind: Resource kind name (required)
        :param str v: Value to check (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resource_kind', 'v']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_availability" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource_kind' is set
        if ('resource_kind' not in params or
                params['resource_kind'] is None):
            raise ValueError("Missing the required parameter `resource_kind` when calling `check_availability`")  # noqa: E501
        # verify the required parameter 'v' is set
        if ('v' not in params or
                params['v'] is None):
            raise ValueError("Missing the required parameter `v` when calling `check_availability`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'resource_kind' in params:
            path_params['resourceKind'] = params['resource_kind']  # noqa: E501

        query_params = []
        if 'v' in params:
            query_params.append(('v', params['v']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/check-availability/{resourceKind}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
