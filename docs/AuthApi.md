# sparkfly_client.AuthApi

All URIs are relative to *https://api.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthApi.md#authenticate) | **GET** /auth | authenticate and receive auth token


# **authenticate**
> authenticate(x_auth_identity, x_auth_key)

authenticate and receive auth token

### Example

```python
import time
import os
import sparkfly_client
from sparkfly_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sparkfly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_client.Configuration(
    host = "https://api.sparkfly.com"
)


# Enter a context with an instance of the API client
with sparkfly_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_client.AuthApi(api_client)
    x_auth_identity = 'x_auth_identity_example' # str | the identity of the account
    x_auth_key = 'x_auth_key_example' # str | the key of the account

    try:
        # authenticate and receive auth token
        api_instance.authenticate(x_auth_identity, x_auth_key)
    except Exception as e:
        print("Exception when calling AuthApi->authenticate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_identity** | **str**| the identity of the account | 
 **x_auth_key** | **str**| the key of the account | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Authentication - Read the X-Auth-Token response header |  * Cache-Control -  <br>  * Date -  <br>  * Server -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized - Invalid credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

