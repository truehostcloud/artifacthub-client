# swagger_client.StatsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_artifact_hub_stats**](StatsApi.md#get_artifact_hub_stats) | **GET** /stats | Get Artifact Hub stats

# **get_artifact_hub_stats**
> InlineResponse2008 get_artifact_hub_stats()

Get Artifact Hub stats

Get Artifact Hub stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsApi()

try:
    # Get Artifact Hub stats
    api_response = api_instance.get_artifact_hub_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_artifact_hub_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

