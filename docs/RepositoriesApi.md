# swagger_client.RepositoriesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_organization_repository**](RepositoriesApi.md#add_organization_repository) | **POST** /repositories/org/{orgName} | Add organization&#x27;s repository
[**add_user_repository**](RepositoriesApi.md#add_user_repository) | **POST** /repositories/user | Add user&#x27;s repository
[**claim_repository_ownership**](RepositoriesApi.md#claim_repository_ownership) | **PUT** /repositories/user/{repoName}/claim-ownership | Claim the ownership of a given repository
[**claim_repository_ownership_from_organization**](RepositoriesApi.md#claim_repository_ownership_from_organization) | **PUT** /repositories/org/{orgName}/{repoName}/claim-ownership | Claim the ownership of a given repository
[**delete_organization_repository**](RepositoriesApi.md#delete_organization_repository) | **DELETE** /repositories/org/{orgName}/{repoName} | Delete organization&#x27;s repository
[**delete_user_repository**](RepositoriesApi.md#delete_user_repository) | **DELETE** /repositories/user/{repoName} | Delete user&#x27;s repository
[**search_repositories**](RepositoriesApi.md#search_repositories) | **GET** /repositories/search | Search repositories that meet the provided criteria
[**transfer_repository_ownership**](RepositoriesApi.md#transfer_repository_ownership) | **PUT** /repositories/org/{orgName}/{repoName}/transfer | Transfer organization&#x27;s repository to a different owner
[**transfer_repository_ownership_to_organization**](RepositoriesApi.md#transfer_repository_ownership_to_organization) | **PUT** /repositories/user/{repoName}/transfer | Transfer user&#x27;s repository ownership to an organization
[**update_organization_repository**](RepositoriesApi.md#update_organization_repository) | **PUT** /repositories/org/{orgName}/{repoName} | Update organization&#x27;s repository
[**update_user_repository**](RepositoriesApi.md#update_user_repository) | **PUT** /repositories/user/{repoName} | Update user&#x27;s repository

# **add_organization_repository**
> add_organization_repository(body, org_name)

Add organization's repository

Add organization's repository

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
body = NULL # object | Repository request body
org_name = 'org_name_example' # str | Organization name

try:
    # Add organization's repository
    api_instance.add_organization_repository(body, org_name)
except ApiException as e:
    print("Exception when calling RepositoriesApi->add_organization_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Repository request body | 
 **org_name** | **str**| Organization name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_repository**
> add_user_repository(body)

Add user's repository

Add user's repository

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
body = NULL # object | Repository request body

try:
    # Add user's repository
    api_instance.add_user_repository(body)
except ApiException as e:
    print("Exception when calling RepositoriesApi->add_user_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Repository request body | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_repository_ownership**
> claim_repository_ownership(repo_name, org=org)

Claim the ownership of a given repository

Claim the ownership of a given repository

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Repository name
org = 'org_example' # str | The org to transfer or from claiming the repository (optional)

try:
    # Claim the ownership of a given repository
    api_instance.claim_repository_ownership(repo_name, org=org)
except ApiException as e:
    print("Exception when calling RepositoriesApi->claim_repository_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **org** | **str**| The org to transfer or from claiming the repository | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_repository_ownership_from_organization**
> claim_repository_ownership_from_organization(org_name, repo_name, org=org)

Claim the ownership of a given repository

Claim the ownership of a given repository

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name
repo_name = 'repo_name_example' # str | Repository name
org = 'org_example' # str | The org to transfer or from claiming the repository (optional)

try:
    # Claim the ownership of a given repository
    api_instance.claim_repository_ownership_from_organization(org_name, repo_name, org=org)
except ApiException as e:
    print("Exception when calling RepositoriesApi->claim_repository_ownership_from_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 
 **repo_name** | **str**| Repository name | 
 **org** | **str**| The org to transfer or from claiming the repository | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_repository**
> delete_organization_repository(org_name, repo_name)

Delete organization's repository

Delete organization's repository

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name
repo_name = 'repo_name_example' # str | Repository name

try:
    # Delete organization's repository
    api_instance.delete_organization_repository(org_name, repo_name)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_organization_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 
 **repo_name** | **str**| Repository name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_repository**
> delete_user_repository(repo_name)

Delete user's repository

Delete user's repository

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Repository name

try:
    # Delete user's repository
    api_instance.delete_user_repository(repo_name)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_user_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_repositories**
> list[Repository] search_repositories(offset=offset, limit=limit, kind=kind, user=user, org=org, name=name, url=url)

Search repositories that meet the provided criteria

Search repositories that meet the provided criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoriesApi()
offset = 0 # int | The number of items to skip before starting to collect the result set (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)
kind = [swagger_client.RepositoryKind()] # list[RepositoryKind] | Repository kind:   * `0` - Helm charts   * `1` - Falco rules   * `2` - OPA policies   * `3` - OLM operators   * `4` - Tinkerbell actions   * `5` - Krew kubectl plugins   * `6` - Helm plugins   * `7` - Tekton tasks   * `8` - KEDA scalers   * `9` - Core DNS plugins   * `10` - Keptn integrations   * `11` - Tekton pipelines   * `12` - Container images   * `13` - Kubewarden policies   * `14` - Gatekeeper policies   * `15` - Kyverno policies   * `16` - Knative client plugins   * `17` - Backstage plugins   * `18` - Argo templates   * `19` - KubeArmor templates  (optional)
user = ['user_example'] # list[str] | List of aliases (optional)
org = ['org_example'] # list[str] | List of organization names (optional)
name = 'name_example' # str | Repository name (optional)
url = 'url_example' # str | Repository url (optional)

try:
    # Search repositories that meet the provided criteria
    api_response = api_instance.search_repositories(offset=offset, limit=limit, kind=kind, user=user, org=org, name=name, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->search_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]
 **kind** | [**list[RepositoryKind]**](RepositoryKind.md)| Repository kind:   * &#x60;0&#x60; - Helm charts   * &#x60;1&#x60; - Falco rules   * &#x60;2&#x60; - OPA policies   * &#x60;3&#x60; - OLM operators   * &#x60;4&#x60; - Tinkerbell actions   * &#x60;5&#x60; - Krew kubectl plugins   * &#x60;6&#x60; - Helm plugins   * &#x60;7&#x60; - Tekton tasks   * &#x60;8&#x60; - KEDA scalers   * &#x60;9&#x60; - Core DNS plugins   * &#x60;10&#x60; - Keptn integrations   * &#x60;11&#x60; - Tekton pipelines   * &#x60;12&#x60; - Container images   * &#x60;13&#x60; - Kubewarden policies   * &#x60;14&#x60; - Gatekeeper policies   * &#x60;15&#x60; - Kyverno policies   * &#x60;16&#x60; - Knative client plugins   * &#x60;17&#x60; - Backstage plugins   * &#x60;18&#x60; - Argo templates   * &#x60;19&#x60; - KubeArmor templates  | [optional] 
 **user** | [**list[str]**](str.md)| List of aliases | [optional] 
 **org** | [**list[str]**](str.md)| List of organization names | [optional] 
 **name** | **str**| Repository name | [optional] 
 **url** | **str**| Repository url | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_repository_ownership**
> transfer_repository_ownership(org_name, repo_name, org=org)

Transfer organization's repository to a different owner

Transfer organization's repository to a different owner

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Organization name
repo_name = 'repo_name_example' # str | Repository name
org = 'org_example' # str | The org to transfer or from claiming the repository (optional)

try:
    # Transfer organization's repository to a different owner
    api_instance.transfer_repository_ownership(org_name, repo_name, org=org)
except ApiException as e:
    print("Exception when calling RepositoriesApi->transfer_repository_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Organization name | 
 **repo_name** | **str**| Repository name | 
 **org** | **str**| The org to transfer or from claiming the repository | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_repository_ownership_to_organization**
> transfer_repository_ownership_to_organization(repo_name, org=org)

Transfer user's repository ownership to an organization

Transfer user's repository ownership to an organization

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Repository name
org = 'org_example' # str | The org to transfer or from claiming the repository (optional)

try:
    # Transfer user's repository ownership to an organization
    api_instance.transfer_repository_ownership_to_organization(repo_name, org=org)
except ApiException as e:
    print("Exception when calling RepositoriesApi->transfer_repository_ownership_to_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **org** | **str**| The org to transfer or from claiming the repository | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_repository**
> update_organization_repository(body, org_name, repo_name)

Update organization's repository

Update organization's repository

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
body = NULL # object | Repository request body
org_name = 'org_name_example' # str | Organization name
repo_name = 'repo_name_example' # str | Repository name

try:
    # Update organization's repository
    api_instance.update_organization_repository(body, org_name, repo_name)
except ApiException as e:
    print("Exception when calling RepositoriesApi->update_organization_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Repository request body | 
 **org_name** | **str**| Organization name | 
 **repo_name** | **str**| Repository name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_repository**
> update_user_repository(body, repo_name)

Update user's repository

Update user's repository

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
body = NULL # object | Repository request body
repo_name = 'repo_name_example' # str | Repository name

try:
    # Update user's repository
    api_instance.update_user_repository(body, repo_name)
except ApiException as e:
    print("Exception when calling RepositoriesApi->update_user_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Repository request body | 
 **repo_name** | **str**| Repository name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

