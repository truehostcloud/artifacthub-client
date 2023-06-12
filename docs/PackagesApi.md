# swagger_client.PackagesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_production_usage**](PackagesApi.md#add_production_usage) | **POST** /packages/{repoKindParam}/{repoName}/{packageName}/production-usage/${orgName} | Add organization to package&#x27;s production users list
[**delete_production_usage**](PackagesApi.md#delete_production_usage) | **DELETE** /packages/{repoKindParam}/{repoName}/{packageName}/production-usage/${orgName} | Delete organization from package&#x27;s production usage list
[**generate_changelog_md**](PackagesApi.md#generate_changelog_md) | **GET** /packages/{repoKindParam}/{repoName}/{packageName}/changelog.md | Get package&#x27;s changelog in markdown format
[**get_argo_templates_details**](PackagesApi.md#get_argo_templates_details) | **GET** /packages/argo-template/{repoName}/{packageName} | Get package details
[**get_argo_templates_version_details**](PackagesApi.md#get_argo_templates_version_details) | **GET** /packages/argo-template/{repoName}/{packageName}/{version} | Get package version details
[**get_backstage_plugins_details**](PackagesApi.md#get_backstage_plugins_details) | **GET** /packages/backstage/{repoName}/{packageName} | Get package details
[**get_backstage_plugins_version_details**](PackagesApi.md#get_backstage_plugins_version_details) | **GET** /packages/backstage/{repoName}/{packageName}/{version} | Get package version details
[**get_chart_values**](PackagesApi.md#get_chart_values) | **GET** /packages/{packageID}/{version}/values | Get chart values
[**get_container_image_details**](PackagesApi.md#get_container_image_details) | **GET** /packages/container/{repoName}/{packageName} | Get container image details
[**get_container_image_version_details**](PackagesApi.md#get_container_image_version_details) | **GET** /packages/container/{repoName}/{packageName}/{version} | Get container image details
[**get_core_dns_plugin_details**](PackagesApi.md#get_core_dns_plugin_details) | **GET** /packages/coredns/{repoName}/{packageName} | Get package details
[**get_core_dns_plugin_version_details**](PackagesApi.md#get_core_dns_plugin_version_details) | **GET** /packages/coredns/{repoName}/{packageName}/{version} | Get package details
[**get_falco_rules_details**](PackagesApi.md#get_falco_rules_details) | **GET** /packages/falco/{repoName}/{packageName} | Get package details
[**get_falco_rules_version_details**](PackagesApi.md#get_falco_rules_version_details) | **GET** /packages/falco/{repoName}/{packageName}/{version} | Get package version details
[**get_gatekeeper_policies_details**](PackagesApi.md#get_gatekeeper_policies_details) | **GET** /packages/gatekeeper/{repoName}/{packageName} | Get package details
[**get_gatekeeper_policies_version_details**](PackagesApi.md#get_gatekeeper_policies_version_details) | **GET** /packages/gatekeeper/{repoName}/{packageName}/{version} | Get package version details
[**get_helm_chart_templates**](PackagesApi.md#get_helm_chart_templates) | **GET** /packages/{packageID}/{version}/templates | Get the templates for a Helm chart package
[**get_helm_package_details**](PackagesApi.md#get_helm_package_details) | **GET** /packages/helm/{repoName}/{packageName} | Get package details
[**get_helm_package_version_details**](PackagesApi.md#get_helm_package_version_details) | **GET** /packages/helm/{repoName}/{packageName}/{version} | Get package version details
[**get_helm_plugin_details**](PackagesApi.md#get_helm_plugin_details) | **GET** /packages/helm-plugin/{repoName}/{packageName} | Get package details
[**get_helm_plugin_version_details**](PackagesApi.md#get_helm_plugin_version_details) | **GET** /packages/helm-plugin/{repoName}/{packageName}/{version} | Get package version details
[**get_keda_scaler_details**](PackagesApi.md#get_keda_scaler_details) | **GET** /packages/keda-scaler/{repoName}/{packageName} | Get package details
[**get_keda_scaler_version_details**](PackagesApi.md#get_keda_scaler_version_details) | **GET** /packages/keda-scaler/{repoName}/{packageName}/{version} | Get package version details
[**get_keptn_integrations_details**](PackagesApi.md#get_keptn_integrations_details) | **GET** /packages/keptn/{repoName}/{packageName} | Get package details
[**get_keptn_integrations_version_details**](PackagesApi.md#get_keptn_integrations_version_details) | **GET** /packages/keptn/{repoName}/{packageName}/{version} | Get package version details
[**get_knative_client_plugin_integrations_details**](PackagesApi.md#get_knative_client_plugin_integrations_details) | **GET** /packages/knative-client-plugin/{repoName}/{packageName} | Get package details
[**get_knative_client_plugins_version_details**](PackagesApi.md#get_knative_client_plugins_version_details) | **GET** /packages/knative-client-plugin/{repoName}/{packageName}/{version} | Get package version details
[**get_kube_armor_policies_details**](PackagesApi.md#get_kube_armor_policies_details) | **GET** /packages/kubearmor/{repoName}/{packageName} | Get package details
[**get_kube_armor_policies_version_details**](PackagesApi.md#get_kube_armor_policies_version_details) | **GET** /packages/kubearmor/{repoName}/{packageName}/{version} | Get package version details
[**get_kubectl_plugin_details**](PackagesApi.md#get_kubectl_plugin_details) | **GET** /packages/krew/{repoName}/{packageName} | Get package details
[**get_kubectl_plugin_version_details**](PackagesApi.md#get_kubectl_plugin_version_details) | **GET** /packages/krew/{repoName}/{packageName}/{version} | Get package version details
[**get_kubewarden_policies_details**](PackagesApi.md#get_kubewarden_policies_details) | **GET** /packages/kubewarden/{repoName}/{packageName} | Get package details
[**get_kubewarden_policies_version_details**](PackagesApi.md#get_kubewarden_policies_version_details) | **GET** /packages/kubewarden/{repoName}/{packageName}/{version} | Get package version details
[**get_kyverno_policies_details**](PackagesApi.md#get_kyverno_policies_details) | **GET** /packages/kyverno/{repoName}/{packageName} | Get package details
[**get_kyverno_policies_version_details**](PackagesApi.md#get_kyverno_policies_version_details) | **GET** /packages/kyverno/{repoName}/{packageName}/{version} | Get package version details
[**get_olm_operator_details**](PackagesApi.md#get_olm_operator_details) | **GET** /packages/olm/{repoName}/{packageName} | Get package details
[**get_olm_operator_version_details**](PackagesApi.md#get_olm_operator_version_details) | **GET** /packages/olm/{repoName}/{packageName}/{version} | Get package version details
[**get_opa_policies_details**](PackagesApi.md#get_opa_policies_details) | **GET** /packages/opa/{repoName}/{packageName} | Get package details
[**get_opa_policies_version_details**](PackagesApi.md#get_opa_policies_version_details) | **GET** /packages/opa/{repoName}/{packageName}/{version} | Get package version details
[**get_package_changelog**](PackagesApi.md#get_package_changelog) | **GET** /packages/{packageID}/changelog | Get package changelogs
[**get_package_security_report**](PackagesApi.md#get_package_security_report) | **GET** /packages/{packageID}/{version}/security-report | Get package security report
[**get_package_stars**](PackagesApi.md#get_package_stars) | **GET** /packages/{packageID}/stars | Get package stars
[**get_package_stats**](PackagesApi.md#get_package_stats) | **GET** /packages/stats | Get the number of packages and releases registered
[**get_package_summary**](PackagesApi.md#get_package_summary) | **GET** /packages/{repoKindParam}/{repoName}/{packageName}/summary | Get package summary details
[**get_package_values_schema**](PackagesApi.md#get_package_values_schema) | **GET** /packages/{packageID}/{version}/values-schema | Get package values schema
[**get_package_views**](PackagesApi.md#get_package_views) | **GET** /packages/{packageID}/views | Get the views of the package provided
[**get_production_usage**](PackagesApi.md#get_production_usage) | **GET** /packages/{repoKindParam}/{repoName}/{packageName}/production-usage | Get a summary of which of the organizations the user belongs to are using the package in production
[**get_random_packages**](PackagesApi.md#get_random_packages) | **GET** /packages/random | Get some random packages
[**get_starred_packages_by_user**](PackagesApi.md#get_starred_packages_by_user) | **GET** /packages/starred | Get packages starred by user
[**get_tekton_pipeline_details**](PackagesApi.md#get_tekton_pipeline_details) | **GET** /packages/tekton-pipeline/{repoName}/{packageName} | Get package details
[**get_tekton_pipeline_version_details**](PackagesApi.md#get_tekton_pipeline_version_details) | **GET** /packages/tekton-pipeline/{repoName}/{packageName}/{version} | Get package version details
[**get_tekton_task_details**](PackagesApi.md#get_tekton_task_details) | **GET** /packages/tekton-task/{repoName}/{packageName} | Get package details
[**get_tekton_task_version_details**](PackagesApi.md#get_tekton_task_version_details) | **GET** /packages/tekton-task/{repoName}/{packageName}/{version} | Get package version details
[**get_tinkerbell_actions_details**](PackagesApi.md#get_tinkerbell_actions_details) | **GET** /packages/tbaction/{repoName}/{packageName} | Get package details
[**get_tinkerbell_actions_version_details**](PackagesApi.md#get_tinkerbell_actions_version_details) | **GET** /packages/tbaction/{repoName}/{packageName}/{version} | Get package version details
[**search_packages**](PackagesApi.md#search_packages) | **GET** /packages/search | Search packages that meet the provided criteria
[**toggle_package_star**](PackagesApi.md#toggle_package_star) | **PUT** /packages/{packageID}/stars | Toggle package&#x27;s star

# **add_production_usage**
> add_production_usage(repo_kind_param, repo_name, package_name, org_name)

Add organization to package's production users list

Add organization to package's production users list

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
api_instance = swagger_client.PackagesApi(swagger_client.ApiClient(configuration))
repo_kind_param = swagger_client.RepositoryKindParam() # RepositoryKindParam | Package kind name
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
org_name = 'org_name_example' # str | Organization name

try:
    # Add organization to package's production users list
    api_instance.add_production_usage(repo_kind_param, repo_name, package_name, org_name)
except ApiException as e:
    print("Exception when calling PackagesApi->add_production_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_kind_param** | [**RepositoryKindParam**](.md)| Package kind name | 
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **org_name** | **str**| Organization name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_production_usage**
> delete_production_usage(repo_kind_param, repo_name, package_name, org_name)

Delete organization from package's production usage list

Delete organization from package's production usage list

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
api_instance = swagger_client.PackagesApi(swagger_client.ApiClient(configuration))
repo_kind_param = swagger_client.RepositoryKindParam() # RepositoryKindParam | Package kind name
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
org_name = 'org_name_example' # str | Organization name

try:
    # Delete organization from package's production usage list
    api_instance.delete_production_usage(repo_kind_param, repo_name, package_name, org_name)
except ApiException as e:
    print("Exception when calling PackagesApi->delete_production_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_kind_param** | [**RepositoryKindParam**](.md)| Package kind name | 
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **org_name** | **str**| Organization name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_changelog_md**
> str generate_changelog_md(repo_kind_param, repo_name, package_name)

Get package's changelog in markdown format

Get package's changelog in markdown format

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_kind_param = swagger_client.RepositoryKindParam() # RepositoryKindParam | Package kind name
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package's changelog in markdown format
    api_response = api_instance.generate_changelog_md(repo_kind_param, repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->generate_changelog_md: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_kind_param** | [**RepositoryKindParam**](.md)| Package kind name | 
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/markdown, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_argo_templates_details**
> ArgoTemplate get_argo_templates_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_argo_templates_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_argo_templates_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**ArgoTemplate**](ArgoTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_argo_templates_version_details**
> ArgoTemplate get_argo_templates_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_argo_templates_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_argo_templates_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**ArgoTemplate**](ArgoTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backstage_plugins_details**
> BackstagePlugin get_backstage_plugins_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_backstage_plugins_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_backstage_plugins_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**BackstagePlugin**](BackstagePlugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backstage_plugins_version_details**
> BackstagePlugin get_backstage_plugins_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_backstage_plugins_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_backstage_plugins_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**BackstagePlugin**](BackstagePlugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chart_values**
> str get_chart_values(package_id, version)

Get chart values

Get chart values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID
version = 'version_example' # str | Package version

try:
    # Get chart values
    api_response = api_instance.get_chart_values(package_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_chart_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 
 **version** | **str**| Package version | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_image_details**
> ContainerImage get_container_image_details(repo_name, package_name)

Get container image details

Get container image details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get container image details
    api_response = api_instance.get_container_image_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_container_image_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**ContainerImage**](ContainerImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_image_version_details**
> ContainerImage get_container_image_version_details(repo_name, package_name, version)

Get container image details

Get container image details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get container image details
    api_response = api_instance.get_container_image_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_container_image_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**ContainerImage**](ContainerImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_core_dns_plugin_details**
> CoreDNSPackage get_core_dns_plugin_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_core_dns_plugin_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_core_dns_plugin_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**CoreDNSPackage**](CoreDNSPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_core_dns_plugin_version_details**
> CoreDNSPackage get_core_dns_plugin_version_details(repo_name, package_name, version)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package details
    api_response = api_instance.get_core_dns_plugin_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_core_dns_plugin_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**CoreDNSPackage**](CoreDNSPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_falco_rules_details**
> FalcoPackage get_falco_rules_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_falco_rules_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_falco_rules_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**FalcoPackage**](FalcoPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_falco_rules_version_details**
> FalcoPackage get_falco_rules_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_falco_rules_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_falco_rules_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**FalcoPackage**](FalcoPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gatekeeper_policies_details**
> GatekeeperPolicy get_gatekeeper_policies_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_gatekeeper_policies_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_gatekeeper_policies_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**GatekeeperPolicy**](GatekeeperPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gatekeeper_policies_version_details**
> GatekeeperPolicy get_gatekeeper_policies_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_gatekeeper_policies_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_gatekeeper_policies_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**GatekeeperPolicy**](GatekeeperPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_chart_templates**
> InlineResponse2004 get_helm_chart_templates(package_id, version)

Get the templates for a Helm chart package

Get the templates for a Helm chart package

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID
version = 'version_example' # str | Package version

try:
    # Get the templates for a Helm chart package
    api_response = api_instance.get_helm_chart_templates(package_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_helm_chart_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 
 **version** | **str**| Package version | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_package_details**
> HelmPackage get_helm_package_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_helm_package_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_helm_package_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**HelmPackage**](HelmPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_package_version_details**
> HelmPackage get_helm_package_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_helm_package_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_helm_package_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**HelmPackage**](HelmPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_plugin_details**
> HelmPluginPackage get_helm_plugin_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_helm_plugin_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_helm_plugin_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**HelmPluginPackage**](HelmPluginPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_plugin_version_details**
> HelmPluginPackage get_helm_plugin_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_helm_plugin_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_helm_plugin_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**HelmPluginPackage**](HelmPluginPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keda_scaler_details**
> KedaScalerPackage get_keda_scaler_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_keda_scaler_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_keda_scaler_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**KedaScalerPackage**](KedaScalerPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keda_scaler_version_details**
> KedaScalerPackage get_keda_scaler_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_keda_scaler_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_keda_scaler_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**KedaScalerPackage**](KedaScalerPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keptn_integrations_details**
> KeptnIntegrationsPackage get_keptn_integrations_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_keptn_integrations_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_keptn_integrations_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**KeptnIntegrationsPackage**](KeptnIntegrationsPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keptn_integrations_version_details**
> KeptnIntegrationsPackage get_keptn_integrations_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_keptn_integrations_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_keptn_integrations_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**KeptnIntegrationsPackage**](KeptnIntegrationsPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knative_client_plugin_integrations_details**
> KnativeClientPluginsPackage get_knative_client_plugin_integrations_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_knative_client_plugin_integrations_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_knative_client_plugin_integrations_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**KnativeClientPluginsPackage**](KnativeClientPluginsPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knative_client_plugins_version_details**
> KnativeClientPluginsPackage get_knative_client_plugins_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_knative_client_plugins_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_knative_client_plugins_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**KnativeClientPluginsPackage**](KnativeClientPluginsPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kube_armor_policies_details**
> KubeArmorPoliciesPackage get_kube_armor_policies_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_kube_armor_policies_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_kube_armor_policies_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**KubeArmorPoliciesPackage**](KubeArmorPoliciesPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kube_armor_policies_version_details**
> KubeArmorPoliciesPackage get_kube_armor_policies_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_kube_armor_policies_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_kube_armor_policies_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**KubeArmorPoliciesPackage**](KubeArmorPoliciesPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubectl_plugin_details**
> KrewPluginsPackage get_kubectl_plugin_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_kubectl_plugin_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_kubectl_plugin_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**KrewPluginsPackage**](KrewPluginsPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubectl_plugin_version_details**
> KrewPluginsPackage get_kubectl_plugin_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_kubectl_plugin_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_kubectl_plugin_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**KrewPluginsPackage**](KrewPluginsPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubewarden_policies_details**
> KubewardenPoliciesPackage get_kubewarden_policies_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_kubewarden_policies_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_kubewarden_policies_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**KubewardenPoliciesPackage**](KubewardenPoliciesPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubewarden_policies_version_details**
> KubewardenPoliciesPackage get_kubewarden_policies_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_kubewarden_policies_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_kubewarden_policies_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**KubewardenPoliciesPackage**](KubewardenPoliciesPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kyverno_policies_details**
> KyvernoPolicy get_kyverno_policies_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_kyverno_policies_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_kyverno_policies_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**KyvernoPolicy**](KyvernoPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kyverno_policies_version_details**
> KyvernoPolicy get_kyverno_policies_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_kyverno_policies_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_kyverno_policies_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**KyvernoPolicy**](KyvernoPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_olm_operator_details**
> OLMPackage get_olm_operator_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_olm_operator_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_olm_operator_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**OLMPackage**](OLMPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_olm_operator_version_details**
> OLMPackage get_olm_operator_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_olm_operator_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_olm_operator_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**OLMPackage**](OLMPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opa_policies_details**
> OPAPackage get_opa_policies_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_opa_policies_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_opa_policies_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**OPAPackage**](OPAPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opa_policies_version_details**
> OPAPackage get_opa_policies_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_opa_policies_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_opa_policies_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**OPAPackage**](OPAPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_changelog**
> list[InlineResponse2003] get_package_changelog(package_id)

Get package changelogs

Get package changelogs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID

try:
    # Get package changelogs
    api_response = api_instance.get_package_changelog(package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_package_changelog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_security_report**
> dict(str, object) get_package_security_report(package_id, version)

Get package security report

Get package security report

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID
version = 'version_example' # str | Package version

try:
    # Get package security report
    api_response = api_instance.get_package_security_report(package_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_package_security_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 
 **version** | **str**| Package version | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_stars**
> InlineResponse2002 get_package_stars(package_id)

Get package stars

Get package stars

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID

try:
    # Get package stars
    api_response = api_instance.get_package_stars(package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_package_stars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_stats**
> InlineResponse200 get_package_stats()

Get the number of packages and releases registered

Get the number of packages and releases registered

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()

try:
    # Get the number of packages and releases registered
    api_response = api_instance.get_package_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_package_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_summary**
> PackageSummary get_package_summary(repo_kind_param, repo_name, package_name)

Get package summary details

Get package summary details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_kind_param = swagger_client.RepositoryKindParam() # RepositoryKindParam | Package kind name
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package summary details
    api_response = api_instance.get_package_summary(repo_kind_param, repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_package_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_kind_param** | [**RepositoryKindParam**](.md)| Package kind name | 
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**PackageSummary**](PackageSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_values_schema**
> dict(str, object) get_package_values_schema(package_id, version)

Get package values schema

Get package values schema

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID
version = 'version_example' # str | Package version

try:
    # Get package values schema
    api_response = api_instance.get_package_values_schema(package_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_package_values_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 
 **version** | **str**| Package version | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_views**
> dict(str, object) get_package_views(package_id)

Get the views of the package provided

Get the views of the package provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID

try:
    # Get the views of the package provided
    api_response = api_instance.get_package_views(package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_package_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_usage**
> list[ProductionUsageOrganization] get_production_usage(repo_kind_param, repo_name, package_name)

Get a summary of which of the organizations the user belongs to are using the package in production

Get a summary of which of the organizations the user belongs to are using the package in production

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_kind_param = swagger_client.RepositoryKindParam() # RepositoryKindParam | Package kind name
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get a summary of which of the organizations the user belongs to are using the package in production
    api_response = api_instance.get_production_usage(repo_kind_param, repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_production_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_kind_param** | [**RepositoryKindParam**](.md)| Package kind name | 
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**list[ProductionUsageOrganization]**](ProductionUsageOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/markdown, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random_packages**
> list[PackageSummary] get_random_packages()

Get some random packages

Get some random packages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()

try:
    # Get some random packages
    api_response = api_instance.get_random_packages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_random_packages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PackageSummary]**](PackageSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_starred_packages_by_user**
> list[PackageSummary] get_starred_packages_by_user(offset=offset, limit=limit)

Get packages starred by user

Get packages starred by user

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
api_instance = swagger_client.PackagesApi(swagger_client.ApiClient(configuration))
offset = 0 # int | The number of items to skip before starting to collect the result set (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Get packages starred by user
    api_response = api_instance.get_starred_packages_by_user(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_starred_packages_by_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**list[PackageSummary]**](PackageSummary.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tekton_pipeline_details**
> TektonPipelinePackage get_tekton_pipeline_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_tekton_pipeline_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_tekton_pipeline_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**TektonPipelinePackage**](TektonPipelinePackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tekton_pipeline_version_details**
> TektonPipelinePackage get_tekton_pipeline_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_tekton_pipeline_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_tekton_pipeline_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**TektonPipelinePackage**](TektonPipelinePackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tekton_task_details**
> TektonTaskPackage get_tekton_task_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_tekton_task_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_tekton_task_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**TektonTaskPackage**](TektonTaskPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tekton_task_version_details**
> TektonTaskPackage get_tekton_task_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_tekton_task_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_tekton_task_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**TektonTaskPackage**](TektonTaskPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tinkerbell_actions_details**
> TBActionPackage get_tinkerbell_actions_details(repo_name, package_name)

Get package details

Get package details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name

try:
    # Get package details
    api_response = api_instance.get_tinkerbell_actions_details(repo_name, package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_tinkerbell_actions_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 

### Return type

[**TBActionPackage**](TBActionPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tinkerbell_actions_version_details**
> TBActionPackage get_tinkerbell_actions_version_details(repo_name, package_name, version)

Get package version details

Get package version details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
repo_name = 'repo_name_example' # str | Repository name
package_name = 'package_name_example' # str | Package name
version = 'version_example' # str | Package version

try:
    # Get package version details
    api_response = api_instance.get_tinkerbell_actions_version_details(repo_name, package_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_tinkerbell_actions_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **package_name** | **str**| Package name | 
 **version** | **str**| Package version | 

### Return type

[**TBActionPackage**](TBActionPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_packages**
> InlineResponse2001 search_packages(facets, offset=offset, limit=limit, ts_query_web=ts_query_web, kind=kind, category=category, user=user, org=org, repo=repo, license=license, capabilities=capabilities, deprecated=deprecated, operators=operators, verified_publisher=verified_publisher, official=official, cncf=cncf, sort=sort)

Search packages that meet the provided criteria

Search packages that meet the provided criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PackagesApi()
facets = false # bool | Whether we should get facets or not (default to false)
offset = 0 # int | The number of items to skip before starting to collect the result set (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)
ts_query_web = 'ts_query_web_example' # str | Text search query (websearch format) (optional)
kind = [swagger_client.RepositoryKind()] # list[RepositoryKind] | Repository kind:   * `0` - Helm charts   * `1` - Falco rules   * `2` - OPA policies   * `3` - OLM operators   * `4` - Tinkerbell actions   * `5` - Krew kubectl plugins   * `6` - Helm plugins   * `7` - Tekton tasks   * `8` - KEDA scalers   * `9` - Core DNS plugins   * `10` - Keptn integrations   * `11` - Tekton pipelines   * `12` - Container images   * `13` - Kubewarden policies   * `14` - Gatekeeper policies   * `15` - Kyverno policies   * `16` - Knative client plugins   * `17` - Backstage plugins   * `18` - Argo templates   * `19` - KubeArmor templates  (optional)
category = [56] # list[int] | Package category:   * `1` - AI / Machine learning   * `2` - Database   * `3` - Integration and delivery   * `4` - Monitoring and logging   * `5` - Networking   * `6` - Security   * `7` - Storage   * `8` - Streaming and messaging  (optional)
user = ['user_example'] # list[str] | List of aliases (optional)
org = ['org_example'] # list[str] | List of organization names (optional)
repo = ['repo_example'] # list[str] | List of repository names (optional)
license = ['license_example'] # list[str] | List of SPDX identifiers (optional)
capabilities = ['capabilities_example'] # list[str] | List of operator capability levels (optional)
deprecated = false # bool | Whether to include deprecated packages or not (optional) (default to false)
operators = true # bool | Whether to get only operators (optional)
verified_publisher = true # bool | Whether to get only verified publisher (optional)
official = true # bool | Whether to get only official repositories (optional)
cncf = true # bool | Whether to get only pacakges published by CNCF projects (optional)
sort = 'sort_example' # str | Sort criteria (optional)

try:
    # Search packages that meet the provided criteria
    api_response = api_instance.search_packages(facets, offset=offset, limit=limit, ts_query_web=ts_query_web, kind=kind, category=category, user=user, org=org, repo=repo, license=license, capabilities=capabilities, deprecated=deprecated, operators=operators, verified_publisher=verified_publisher, official=official, cncf=cncf, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->search_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facets** | **bool**| Whether we should get facets or not | [default to false]
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]
 **ts_query_web** | **str**| Text search query (websearch format) | [optional] 
 **kind** | [**list[RepositoryKind]**](RepositoryKind.md)| Repository kind:   * &#x60;0&#x60; - Helm charts   * &#x60;1&#x60; - Falco rules   * &#x60;2&#x60; - OPA policies   * &#x60;3&#x60; - OLM operators   * &#x60;4&#x60; - Tinkerbell actions   * &#x60;5&#x60; - Krew kubectl plugins   * &#x60;6&#x60; - Helm plugins   * &#x60;7&#x60; - Tekton tasks   * &#x60;8&#x60; - KEDA scalers   * &#x60;9&#x60; - Core DNS plugins   * &#x60;10&#x60; - Keptn integrations   * &#x60;11&#x60; - Tekton pipelines   * &#x60;12&#x60; - Container images   * &#x60;13&#x60; - Kubewarden policies   * &#x60;14&#x60; - Gatekeeper policies   * &#x60;15&#x60; - Kyverno policies   * &#x60;16&#x60; - Knative client plugins   * &#x60;17&#x60; - Backstage plugins   * &#x60;18&#x60; - Argo templates   * &#x60;19&#x60; - KubeArmor templates  | [optional] 
 **category** | [**list[int]**](int.md)| Package category:   * &#x60;1&#x60; - AI / Machine learning   * &#x60;2&#x60; - Database   * &#x60;3&#x60; - Integration and delivery   * &#x60;4&#x60; - Monitoring and logging   * &#x60;5&#x60; - Networking   * &#x60;6&#x60; - Security   * &#x60;7&#x60; - Storage   * &#x60;8&#x60; - Streaming and messaging  | [optional] 
 **user** | [**list[str]**](str.md)| List of aliases | [optional] 
 **org** | [**list[str]**](str.md)| List of organization names | [optional] 
 **repo** | [**list[str]**](str.md)| List of repository names | [optional] 
 **license** | [**list[str]**](str.md)| List of SPDX identifiers | [optional] 
 **capabilities** | [**list[str]**](str.md)| List of operator capability levels | [optional] 
 **deprecated** | **bool**| Whether to include deprecated packages or not | [optional] [default to false]
 **operators** | **bool**| Whether to get only operators | [optional] 
 **verified_publisher** | **bool**| Whether to get only verified publisher | [optional] 
 **official** | **bool**| Whether to get only official repositories | [optional] 
 **cncf** | **bool**| Whether to get only pacakges published by CNCF projects | [optional] 
 **sort** | **str**| Sort criteria | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_package_star**
> toggle_package_star(package_id)

Toggle package's star

Toggle package's star

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
api_instance = swagger_client.PackagesApi(swagger_client.ApiClient(configuration))
package_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Package ID

try:
    # Toggle package's star
    api_instance.toggle_package_star(package_id)
except ApiException as e:
    print("Exception when calling PackagesApi->toggle_package_star: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | [**str**](.md)| Package ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

