# swagger_client.SubscriptionsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_opt_out_entry**](SubscriptionsApi.md#add_opt_out_entry) | **POST** /subscriptions/opt-out | Add opt-out entry
[**add_package_subscription**](SubscriptionsApi.md#add_package_subscription) | **POST** /subscriptions | Add subscription
[**delete_opt_out_entry**](SubscriptionsApi.md#delete_opt_out_entry) | **DELETE** /subscriptions/opt-out/{optOutID} | Delete opt-out entry
[**delete_package_subscription**](SubscriptionsApi.md#delete_package_subscription) | **DELETE** /subscriptions | Delete subscription
[**get_package_user_subscriptions**](SubscriptionsApi.md#get_package_user_subscriptions) | **GET** /subscriptions/{packageID} | Get user&#x27;s subscriptions for the given package
[**get_user_opt_out_entries**](SubscriptionsApi.md#get_user_opt_out_entries) | **GET** /subscriptions/opt-out | Get user&#x27;s opt-out entries
[**get_user_subscriptions**](SubscriptionsApi.md#get_user_subscriptions) | **GET** /subscriptions | Get user&#x27;s subscriptions

# **add_opt_out_entry**
> add_opt_out_entry(body)

Add opt-out entry

Add opt-out entry

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyId
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-ID'] = 'Bearer'
# Configure API key authorization: ApiKeySecret
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-SECRET'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-SECRET'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = NULL # object | Opt-out entry request body

try:
    # Add opt-out entry
    api_instance.add_opt_out_entry(body)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_opt_out_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Opt-out entry request body | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_package_subscription**
> add_package_subscription(body)

Add subscription

Add subscription

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyId
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-ID'] = 'Bearer'
# Configure API key authorization: ApiKeySecret
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-SECRET'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-SECRET'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = NULL # object | Subscription request body

try:
    # Add subscription
    api_instance.add_package_subscription(body)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_package_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Subscription request body | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_opt_out_entry**
> delete_opt_out_entry(opt_out_id)

Delete opt-out entry

Delete opt-out entry

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyId
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-ID'] = 'Bearer'
# Configure API key authorization: ApiKeySecret
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-SECRET'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-SECRET'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
opt_out_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Opt-out entry ID

try:
    # Delete opt-out entry
    api_instance.delete_opt_out_entry(opt_out_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_opt_out_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_out_id** | [**str**](.md)| Opt-out entry ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_package_subscription**
> delete_package_subscription(package_id, event_kind)

Delete subscription

Delete subscription

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyId
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-ID'] = 'Bearer'
# Configure API key authorization: ApiKeySecret
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-SECRET'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-SECRET'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID
event_kind = swagger_client.EventKindId() # EventKindId | Event kind

try:
    # Delete subscription
    api_instance.delete_package_subscription(package_id, event_kind)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_package_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 
 **event_kind** | [**EventKindId**](.md)| Event kind | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_user_subscriptions**
> list[InlineResponse2006] get_package_user_subscriptions(package_id)

Get user's subscriptions for the given package

Get user's subscriptions for the given package

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyId
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-ID'] = 'Bearer'
# Configure API key authorization: ApiKeySecret
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-SECRET'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-SECRET'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID

try:
    # Get user's subscriptions for the given package
    api_response = api_instance.get_package_user_subscriptions(package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_package_user_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_opt_out_entries**
> list[InlineResponse2007] get_user_opt_out_entries(offset=offset, limit=limit)

Get user's opt-out entries

Get user's opt-out entries

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyId
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-ID'] = 'Bearer'
# Configure API key authorization: ApiKeySecret
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-SECRET'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-SECRET'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
offset = 0 # int | The number of items to skip before starting to collect the result set (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Get user's opt-out entries
    api_response = api_instance.get_user_opt_out_entries(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_user_opt_out_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**list[InlineResponse2007]**](InlineResponse2007.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscriptions**
> list[InlineResponse2005] get_user_subscriptions(offset=offset, limit=limit)

Get user's subscriptions

Get user's subscriptions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyId
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-ID'] = 'Bearer'
# Configure API key authorization: ApiKeySecret
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY-SECRET'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY-SECRET'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
offset = 0 # int | The number of items to skip before starting to collect the result set (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Get user's subscriptions
    api_response = api_instance.get_user_subscriptions(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_user_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**list[InlineResponse2005]**](InlineResponse2005.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

