# swagger_client.UsersApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_profile**](UsersApi.md#get_user_profile) | **GET** /users/profile | Get user&#x27;s profile
[**register_user**](UsersApi.md#register_user) | **POST** /users | Register a new user
[**reset_password**](UsersApi.md#reset_password) | **PUT** /users/reset-password | Reset the user&#x27;s password
[**reset_password_code**](UsersApi.md#reset_password_code) | **POST** /users/password-reset-code | Register a code to reset the password
[**update_user_password**](UsersApi.md#update_user_password) | **PUT** /users/password | Update user&#x27;s password
[**update_user_profile**](UsersApi.md#update_user_profile) | **PUT** /users/profile | Update user&#x27;s profile
[**verify_email**](UsersApi.md#verify_email) | **POST** /users/verify-email | Verify user&#x27;s email address
[**verify_password_code**](UsersApi.md#verify_password_code) | **POST** /users/verify-password-reset-code | Verify a reset password code

# **get_user_profile**
> User get_user_profile()

Get user's profile

Get user's profile

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Get user's profile
    api_response = api_instance.get_user_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> register_user(body)

Register a new user

Register a new user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UsersBody() # UsersBody | 

try:
    # Register a new user
    api_instance.register_user(body)
except ApiException as e:
    print("Exception when calling UsersApi->register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersBody**](UsersBody.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(body=body)

Reset the user's password

Reset the user's password

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UsersResetpasswordBody() # UsersResetpasswordBody |  (optional)

try:
    # Reset the user's password
    api_instance.reset_password(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersResetpasswordBody**](UsersResetpasswordBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_code**
> reset_password_code(body=body)

Register a code to reset the password

Register a code to reset the password

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UsersPasswordresetcodeBody() # UsersPasswordresetcodeBody |  (optional)

try:
    # Register a code to reset the password
    api_instance.reset_password_code(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->reset_password_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersPasswordresetcodeBody**](UsersPasswordresetcodeBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_password**
> update_user_password(body=body)

Update user's password

Update user's password

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersPasswordBody() # UsersPasswordBody |  (optional)

try:
    # Update user's password
    api_instance.update_user_password(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersPasswordBody**](UsersPasswordBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile**
> update_user_profile(body=body)

Update user's profile

Update user's profile

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.User() # User |  (optional)

try:
    # Update user's profile
    api_instance.update_user_profile(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyId](../README.md#ApiKeyId), [ApiKeySecret](../README.md#ApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email**
> verify_email(body=body)

Verify user's email address

Verify user's email address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UsersVerifyemailBody() # UsersVerifyemailBody |  (optional)

try:
    # Verify user's email address
    api_instance.verify_email(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->verify_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersVerifyemailBody**](UsersVerifyemailBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_password_code**
> verify_password_code(body=body)

Verify a reset password code

Verify a reset password code

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UsersVerifypasswordresetcodeBody() # UsersVerifypasswordresetcodeBody |  (optional)

try:
    # Verify a reset password code
    api_instance.verify_password_code(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->verify_password_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersVerifypasswordresetcodeBody**](UsersVerifypasswordresetcodeBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

