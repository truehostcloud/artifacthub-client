# swagger_client.OrganizationsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_organization_invitation**](OrganizationsApi.md#accept_organization_invitation) | **GET** /orgs/{orgName}/accept-invitation | Confirm user&#x27;s membership to an organization
[**add_organization**](OrganizationsApi.md#add_organization) | **POST** /orgs | Register new organization
[**add_organization_member**](OrganizationsApi.md#add_organization_member) | **POST** /orgs/{orgName}/member/{userAlias} | Add a new member to the organization
[**delete_organization**](OrganizationsApi.md#delete_organization) | **DELETE** /orgs/{orgName} | Delete organization
[**delete_organization_member**](OrganizationsApi.md#delete_organization_member) | **DELETE** /orgs/{orgName}/member/{userAlias} | Delete a member from the organization
[**get_allowed_actions**](OrganizationsApi.md#get_allowed_actions) | **GET** /orgs/{orgName}/user-allowed-actions | Get actions which user is allowed to perform in the provided organization
[**get_organization_auth_policy**](OrganizationsApi.md#get_organization_auth_policy) | **GET** /orgs/{orgName}/authorization-policy | Get organization&#x27;s authorization policy
[**get_organization_members**](OrganizationsApi.md#get_organization_members) | **GET** /orgs/{orgName}/members | Get organization members
[**get_organization_profile**](OrganizationsApi.md#get_organization_profile) | **GET** /orgs/{orgName} | Get organization profile
[**get_user_organizations**](OrganizationsApi.md#get_user_organizations) | **GET** /orgs/user | Get organizations the user belongs to
[**update_organization_auth_policy**](OrganizationsApi.md#update_organization_auth_policy) | **PUT** /orgs/{orgName}/authorization-policy | Update organization&#x27;s authorization policy
[**update_organization_profile**](OrganizationsApi.md#update_organization_profile) | **PUT** /orgs/{orgName} | Updates organization profile

# **accept_organization_invitation**
> accept_organization_invitation(org_name)

Confirm user's membership to an organization

Confirm user's membership to an organization

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name

try:
    # Confirm user's membership to an organization
    api_instance.accept_organization_invitation(org_name)
except ApiException as e:
    print("Exception when calling OrganizationsApi->accept_organization_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_organization**
> add_organization(body)

Register new organization

Register new organization

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganizationSummary() # OrganizationSummary | 

try:
    # Register new organization
    api_instance.add_organization(body)
except ApiException as e:
    print("Exception when calling OrganizationsApi->add_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationSummary**](OrganizationSummary.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_organization_member**
> add_organization_member(org_name, user_alias)

Add a new member to the organization

Add a new member to the organization

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name
user_alias = 'user_alias_example' # str | User alias

try:
    # Add a new member to the organization
    api_instance.add_organization_member(org_name, user_alias)
except ApiException as e:
    print("Exception when calling OrganizationsApi->add_organization_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 
 **user_alias** | **str**| User alias | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization**
> delete_organization(org_name)

Delete organization

Delete organization

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name

try:
    # Delete organization
    api_instance.delete_organization(org_name)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_member**
> delete_organization_member(org_name, user_alias)

Delete a member from the organization

Delete a member from the organization

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name
user_alias = 'user_alias_example' # str | User alias

try:
    # Delete a member from the organization
    api_instance.delete_organization_member(org_name, user_alias)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_organization_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 
 **user_alias** | **str**| User alias | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allowed_actions**
> list[AuthorizerAction] get_allowed_actions(org_name)

Get actions which user is allowed to perform in the provided organization

Get actions which user is allowed to perform in the provided organization

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name

try:
    # Get actions which user is allowed to perform in the provided organization
    api_response = api_instance.get_allowed_actions(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_allowed_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 

### Return type

[**list[AuthorizerAction]**](AuthorizerAction.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_auth_policy**
> AuthorizationPolicy get_organization_auth_policy(org_name)

Get organization's authorization policy

Get organization's authorization policy

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name

try:
    # Get organization's authorization policy
    api_response = api_instance.get_organization_auth_policy(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_auth_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 

### Return type

[**AuthorizationPolicy**](AuthorizationPolicy.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_members**
> list[Member] get_organization_members(org_name)

Get organization members

Get organization members

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name

try:
    # Get organization members
    api_response = api_instance.get_organization_members(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 

### Return type

[**list[Member]**](Member.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_profile**
> OrganizationSummary get_organization_profile(org_name)

Get organization profile

Get organization profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
org_name = 'org_name_example' # str | Organization name

try:
    # Get organization profile
    api_response = api_instance.get_organization_profile(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 

### Return type

[**OrganizationSummary**](OrganizationSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_organizations**
> list[Organization] get_user_organizations(offset=offset, limit=limit)

Get organizations the user belongs to

Get organizations the user belongs to

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
offset = 0 # int | The number of items to skip before starting to collect the result set (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Get organizations the user belongs to
    api_response = api_instance.get_user_organizations(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_user_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**list[Organization]**](Organization.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_auth_policy**
> update_organization_auth_policy(body, org_name)

Update organization's authorization policy

Update organization's authorization policy

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthorizationPolicy() # AuthorizationPolicy | 
org_name = 'org_name_example' # str | Organization name

try:
    # Update organization's authorization policy
    api_instance.update_organization_auth_policy(body, org_name)
except ApiException as e:
    print("Exception when calling OrganizationsApi->update_organization_auth_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationPolicy**](AuthorizationPolicy.md)|  | 
 **org_name** | **str**| Organization name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_profile**
> update_organization_profile(body, org_name)

Updates organization profile

Updates organization profile

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganizationSummary() # OrganizationSummary | 
org_name = 'org_name_example' # str | Organization name

try:
    # Updates organization profile
    api_instance.update_organization_profile(body, org_name)
except ApiException as e:
    print("Exception when calling OrganizationsApi->update_organization_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationSummary**](OrganizationSummary.md)|  | 
 **org_name** | **str**| Organization name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

