# swagger_client.WebhooksApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_organization_webhook**](WebhooksApi.md#add_organization_webhook) | **POST** /webhooks/org/{orgName} | Add organization&#x27;s webhook
[**add_user_webhook**](WebhooksApi.md#add_user_webhook) | **POST** /webhooks/user | Add user&#x27;s webhook
[**delete_organization_webhook**](WebhooksApi.md#delete_organization_webhook) | **DELETE** /webhooks/org/{orgName}/{webhookID} | Delete organization&#x27;s webhook
[**delete_user_webhook**](WebhooksApi.md#delete_user_webhook) | **DELETE** /webhooks/user/{webhookID} | Delete user&#x27;s webhook
[**get_organization_webhook_details**](WebhooksApi.md#get_organization_webhook_details) | **GET** /webhooks/org/{orgName}/{webhookID} | Get organization&#x27;s webhook
[**get_organization_webhooks**](WebhooksApi.md#get_organization_webhooks) | **GET** /webhooks/org/{orgName} | Get organization&#x27;s webhooks
[**get_user_webhook_detail**](WebhooksApi.md#get_user_webhook_detail) | **GET** /webhooks/user/{webhookID} | Get user&#x27;s webhook
[**get_user_webhooks**](WebhooksApi.md#get_user_webhooks) | **GET** /webhooks/user | Get user&#x27;s webhooks
[**trigger_webhook_test**](WebhooksApi.md#trigger_webhook_test) | **POST** /webhooks/test | Trigger webhook test
[**update_organization_webhook**](WebhooksApi.md#update_organization_webhook) | **PUT** /webhooks/org/{orgName}/{webhookID} | Update organization&#x27;s webhook
[**update_user_webhook**](WebhooksApi.md#update_user_webhook) | **PUT** /webhooks/user/{webhookID} | Update user&#x27;s webhook

# **add_organization_webhook**
> add_organization_webhook(body, org_name)

Add organization's webhook

Add organization's webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebhookSummaryWithPackages() # WebhookSummaryWithPackages | Webhook body
org_name = 'org_name_example' # str | Organization name

try:
    # Add organization's webhook
    api_instance.add_organization_webhook(body, org_name)
except ApiException as e:
    print("Exception when calling WebhooksApi->add_organization_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookSummaryWithPackages**](WebhookSummaryWithPackages.md)| Webhook body | 
 **org_name** | **str**| Organization name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_webhook**
> add_user_webhook(body)

Add user's webhook

Add user's webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebhookSummaryWithPackages() # WebhookSummaryWithPackages | Webhook body

try:
    # Add user's webhook
    api_instance.add_user_webhook(body)
except ApiException as e:
    print("Exception when calling WebhooksApi->add_user_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookSummaryWithPackages**](WebhookSummaryWithPackages.md)| Webhook body | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_webhook**
> delete_organization_webhook(org_name, webhook_id)

Delete organization's webhook

Delete organization's webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name
webhook_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook ID

try:
    # Delete organization's webhook
    api_instance.delete_organization_webhook(org_name, webhook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_organization_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 
 **webhook_id** | [**str**](.md)| Webhook ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_webhook**
> delete_user_webhook(webhook_id)

Delete user's webhook

Delete user's webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
webhook_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook ID

try:
    # Delete user's webhook
    api_instance.delete_user_webhook(webhook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_user_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**](.md)| Webhook ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_webhook_details**
> Webhook get_organization_webhook_details(org_name, webhook_id)

Get organization's webhook

Get organization's webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name
webhook_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook ID

try:
    # Get organization's webhook
    api_response = api_instance.get_organization_webhook_details(org_name, webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_organization_webhook_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 
 **webhook_id** | [**str**](.md)| Webhook ID | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_webhooks**
> list[Webhook] get_organization_webhooks(org_name)

Get organization's webhooks

Get organization's webhooks

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name

try:
    # Get organization's webhooks
    api_response = api_instance.get_organization_webhooks(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_organization_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 

### Return type

[**list[Webhook]**](Webhook.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_webhook_detail**
> Webhook get_user_webhook_detail(webhook_id)

Get user's webhook

Get user's webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
webhook_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook ID

try:
    # Get user's webhook
    api_response = api_instance.get_user_webhook_detail(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_user_webhook_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**](.md)| Webhook ID | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_webhooks**
> list[Webhook] get_user_webhooks()

Get user's webhooks

Get user's webhooks

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))

try:
    # Get user's webhooks
    api_response = api_instance.get_user_webhooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_user_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Webhook]**](Webhook.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_webhook_test**
> trigger_webhook_test(body=body)

Trigger webhook test

Trigger webhook test

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebhookTest() # WebhookTest |  (optional)

try:
    # Trigger webhook test
    api_instance.trigger_webhook_test(body=body)
except ApiException as e:
    print("Exception when calling WebhooksApi->trigger_webhook_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookTest**](WebhookTest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_webhook**
> update_organization_webhook(body, org_name, webhook_id)

Update organization's webhook

Update organization's webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebhookSummaryWithPackages() # WebhookSummaryWithPackages | Webhook body
org_name = 'org_name_example' # str | Organization name
webhook_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook ID

try:
    # Update organization's webhook
    api_instance.update_organization_webhook(body, org_name, webhook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_organization_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookSummaryWithPackages**](WebhookSummaryWithPackages.md)| Webhook body | 
 **org_name** | **str**| Organization name | 
 **webhook_id** | [**str**](.md)| Webhook ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_webhook**
> update_user_webhook(body, webhook_id)

Update user's webhook

Update user's webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebhookSummaryWithPackages() # WebhookSummaryWithPackages | Webhook body
webhook_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook ID

try:
    # Update user's webhook
    api_instance.update_user_webhook(body, webhook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_user_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookSummaryWithPackages**](WebhookSummaryWithPackages.md)| Webhook body | 
 **webhook_id** | [**str**](.md)| Webhook ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

