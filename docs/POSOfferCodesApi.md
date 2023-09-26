# sparkfly_client.POSOfferCodesApi

All URIs are relative to *https://api.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pos_offer_code**](POSOfferCodesApi.md#get_pos_offer_code) | **GET** /v1.0/pos_offer_codes/{pos_offer_code_id} | Get POS Offer Code
[**get_pos_offer_codes**](POSOfferCodesApi.md#get_pos_offer_codes) | **GET** /v1.0/pos_offer_codes | List POS Offer Codes


# **get_pos_offer_code**
> PosOfferCodeResponse get_pos_offer_code(pos_offer_code_id)

Get POS Offer Code

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.pos_offer_code_response import PosOfferCodeResponse
from sparkfly_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sparkfly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_client.Configuration(
    host = "https://api.sparkfly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Auth-Token
configuration.api_key['X-Auth-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with sparkfly_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_client.POSOfferCodesApi(api_client)
    pos_offer_code_id = 56 # int | The id of the POS Offer Code

    try:
        # Get POS Offer Code
        api_response = api_instance.get_pos_offer_code(pos_offer_code_id)
        print("The response of POSOfferCodesApi->get_pos_offer_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POSOfferCodesApi->get_pos_offer_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pos_offer_code_id** | **int**| The id of the POS Offer Code | 

### Return type

[**PosOfferCodeResponse**](PosOfferCodeResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | POS Offer Code to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pos_offer_codes**
> PosOfferCodeList get_pos_offer_codes()

List POS Offer Codes

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.pos_offer_code_list import PosOfferCodeList
from sparkfly_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sparkfly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_client.Configuration(
    host = "https://api.sparkfly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Auth-Token
configuration.api_key['X-Auth-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with sparkfly_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_client.POSOfferCodesApi(api_client)

    try:
        # List POS Offer Codes
        api_response = api_instance.get_pos_offer_codes()
        print("The response of POSOfferCodesApi->get_pos_offer_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POSOfferCodesApi->get_pos_offer_codes: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PosOfferCodeList**](PosOfferCodeList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | POS Offer Codes to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

