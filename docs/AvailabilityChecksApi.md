# swagger_client.AvailabilityChecksApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_availability**](AvailabilityChecksApi.md#check_availability) | **HEAD** /check-availability/{resourceKind} | Check the availability of a given value for the provided resource kind

# **check_availability**
> check_availability(resource_kind, v)

Check the availability of a given value for the provided resource kind

Check the availability of a given value for the provided resource kind

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AvailabilityChecksApi()
resource_kind = swagger_client.ResourceKindName() # ResourceKindName | Resource kind name
v = 'v_example' # str | Value to check

try:
    # Check the availability of a given value for the provided resource kind
    api_instance.check_availability(resource_kind, v)
except ApiException as e:
    print("Exception when calling AvailabilityChecksApi->check_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_kind** | [**ResourceKindName**](.md)| Resource kind name | 
 **v** | **str**| Value to check | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

