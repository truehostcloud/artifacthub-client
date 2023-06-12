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

from swagger_client.api_client import ApiClient


class SubscriptionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_opt_out_entry(self, body, **kwargs):  # noqa: E501
        """Add opt-out entry  # noqa: E501

        Add opt-out entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_opt_out_entry(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: Opt-out entry request body (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_opt_out_entry_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_opt_out_entry_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_opt_out_entry_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add opt-out entry  # noqa: E501

        Add opt-out entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_opt_out_entry_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: Opt-out entry request body (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_opt_out_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_opt_out_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyId', 'ApiKeySecret']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/opt-out', 'POST',
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

    def add_package_subscription(self, body, **kwargs):  # noqa: E501
        """Add subscription  # noqa: E501

        Add subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_package_subscription(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: Subscription request body (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_package_subscription_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_package_subscription_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_package_subscription_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add subscription  # noqa: E501

        Add subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_package_subscription_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: Subscription request body (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_package_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_package_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyId', 'ApiKeySecret']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions', 'POST',
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

    def delete_opt_out_entry(self, opt_out_id, **kwargs):  # noqa: E501
        """Delete opt-out entry  # noqa: E501

        Delete opt-out entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_opt_out_entry(opt_out_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str opt_out_id: Opt-out entry ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_opt_out_entry_with_http_info(opt_out_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_opt_out_entry_with_http_info(opt_out_id, **kwargs)  # noqa: E501
            return data

    def delete_opt_out_entry_with_http_info(self, opt_out_id, **kwargs):  # noqa: E501
        """Delete opt-out entry  # noqa: E501

        Delete opt-out entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_opt_out_entry_with_http_info(opt_out_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str opt_out_id: Opt-out entry ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['opt_out_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_opt_out_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'opt_out_id' is set
        if ('opt_out_id' not in params or
                params['opt_out_id'] is None):
            raise ValueError("Missing the required parameter `opt_out_id` when calling `delete_opt_out_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'opt_out_id' in params:
            path_params['optOutID'] = params['opt_out_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyId', 'ApiKeySecret']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/opt-out/{optOutID}', 'DELETE',
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

    def delete_package_subscription(self, package_id, event_kind, **kwargs):  # noqa: E501
        """Delete subscription  # noqa: E501

        Delete subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_package_subscription(package_id, event_kind, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str package_id: Package ID (required)
        :param EventKindId event_kind: Event kind (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_package_subscription_with_http_info(package_id, event_kind, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_package_subscription_with_http_info(package_id, event_kind, **kwargs)  # noqa: E501
            return data

    def delete_package_subscription_with_http_info(self, package_id, event_kind, **kwargs):  # noqa: E501
        """Delete subscription  # noqa: E501

        Delete subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_package_subscription_with_http_info(package_id, event_kind, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str package_id: Package ID (required)
        :param EventKindId event_kind: Event kind (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['package_id', 'event_kind']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_package_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'package_id' is set
        if ('package_id' not in params or
                params['package_id'] is None):
            raise ValueError("Missing the required parameter `package_id` when calling `delete_package_subscription`")  # noqa: E501
        # verify the required parameter 'event_kind' is set
        if ('event_kind' not in params or
                params['event_kind'] is None):
            raise ValueError("Missing the required parameter `event_kind` when calling `delete_package_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'package_id' in params:
            query_params.append(('packageID', params['package_id']))  # noqa: E501
        if 'event_kind' in params:
            query_params.append(('event_kind', params['event_kind']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyId', 'ApiKeySecret']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions', 'DELETE',
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

    def get_package_user_subscriptions(self, package_id, **kwargs):  # noqa: E501
        """Get user's subscriptions for the given package  # noqa: E501

        Get user's subscriptions for the given package  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_package_user_subscriptions(package_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str package_id: Package ID (required)
        :return: list[InlineResponse2006]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_package_user_subscriptions_with_http_info(package_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_package_user_subscriptions_with_http_info(package_id, **kwargs)  # noqa: E501
            return data

    def get_package_user_subscriptions_with_http_info(self, package_id, **kwargs):  # noqa: E501
        """Get user's subscriptions for the given package  # noqa: E501

        Get user's subscriptions for the given package  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_package_user_subscriptions_with_http_info(package_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str package_id: Package ID (required)
        :return: list[InlineResponse2006]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['package_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_package_user_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'package_id' is set
        if ('package_id' not in params or
                params['package_id'] is None):
            raise ValueError("Missing the required parameter `package_id` when calling `get_package_user_subscriptions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'package_id' in params:
            path_params['packageID'] = params['package_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyId', 'ApiKeySecret']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/{packageID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse2006]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_opt_out_entries(self, **kwargs):  # noqa: E501
        """Get user's opt-out entries  # noqa: E501

        Get user's opt-out entries  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_opt_out_entries(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The number of items to skip before starting to collect the result set
        :param int limit: The number of items to return
        :return: list[InlineResponse2007]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_opt_out_entries_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_opt_out_entries_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_opt_out_entries_with_http_info(self, **kwargs):  # noqa: E501
        """Get user's opt-out entries  # noqa: E501

        Get user's opt-out entries  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_opt_out_entries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The number of items to skip before starting to collect the result set
        :param int limit: The number of items to return
        :return: list[InlineResponse2007]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_opt_out_entries" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyId', 'ApiKeySecret']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/opt-out', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse2007]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_subscriptions(self, **kwargs):  # noqa: E501
        """Get user's subscriptions  # noqa: E501

        Get user's subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_subscriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The number of items to skip before starting to collect the result set
        :param int limit: The number of items to return
        :return: list[InlineResponse2005]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_subscriptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_subscriptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_subscriptions_with_http_info(self, **kwargs):  # noqa: E501
        """Get user's subscriptions  # noqa: E501

        Get user's subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_subscriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The number of items to skip before starting to collect the result set
        :param int limit: The number of items to return
        :return: list[InlineResponse2005]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyId', 'ApiKeySecret']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse2005]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
