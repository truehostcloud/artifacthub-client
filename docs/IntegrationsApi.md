# swagger_client.IntegrationsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_harbor_replication_dump**](IntegrationsApi.md#get_harbor_replication_dump) | **GET** /harbor-replication | Get Harbor replication dump
[**get_helm_exporter_dump**](IntegrationsApi.md#get_helm_exporter_dump) | **GET** /helm-exporter | Get Helm exporter dump
[**get_nova_dump**](IntegrationsApi.md#get_nova_dump) | **GET** /nova | Get Nova dump

# **get_harbor_replication_dump**
> list[object] get_harbor_replication_dump()

Get Harbor replication dump

Get Harbor replication dump

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationsApi()

try:
    # Get Harbor replication dump
    api_response = api_instance.get_harbor_replication_dump()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_harbor_replication_dump: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_exporter_dump**
> list[object] get_helm_exporter_dump()

Get Helm exporter dump

Get the latest version available of all charts listed in Artifact Hub.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationsApi()

try:
    # Get Helm exporter dump
    api_response = api_instance.get_helm_exporter_dump()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_helm_exporter_dump: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nova_dump**
> list[object] get_nova_dump()

Get Nova dump

Get all charts listed in Artifact Hub.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationsApi()

try:
    # Get Nova dump
    api_response = api_instance.get_nova_dump()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_nova_dump: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

