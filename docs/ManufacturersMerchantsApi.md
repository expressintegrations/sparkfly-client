# sparkfly_client.ManufacturersMerchantsApi

All URIs are relative to *https://api.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_manufacturer_merchants**](ManufacturersMerchantsApi.md#delete_manufacturer_merchants) | **DELETE** /v1.0/manufacturers/{manufacturer_id}/merchants | Remove an eligible merchant for manufacturer
[**get_manufacturer_merchants**](ManufacturersMerchantsApi.md#get_manufacturer_merchants) | **GET** /v1.0/manufacturers/{manufacturer_id}/merchants | Get all merchants for manufacturer
[**set_manufacturer_merchants**](ManufacturersMerchantsApi.md#set_manufacturer_merchants) | **POST** /v1.0/manufacturers/{manufacturer_id}/merchants | Set eligible merchants for manufacturer
[**update_manufacturer_merchants**](ManufacturersMerchantsApi.md#update_manufacturer_merchants) | **PUT** /v1.0/manufacturers/{manufacturer_id}/merchants | Add an eligible merchant for manufacturer


# **delete_manufacturer_merchants**
> ManufacturerMerchantsResponse delete_manufacturer_merchants(manufacturer_id, manufacturer_merchant_ids_input_request=manufacturer_merchant_ids_input_request)

Remove an eligible merchant for manufacturer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.manufacturer_merchant_ids_input_request import ManufacturerMerchantIdsInputRequest
from sparkfly_client.models.manufacturer_merchants_response import ManufacturerMerchantsResponse
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
    api_instance = sparkfly_client.ManufacturersMerchantsApi(api_client)
    manufacturer_id = 56 # int | The id of the manufacturer
    manufacturer_merchant_ids_input_request = sparkfly_client.ManufacturerMerchantIdsInputRequest() # ManufacturerMerchantIdsInputRequest | Merchant to remove from manufacturer (optional)

    try:
        # Remove an eligible merchant for manufacturer
        api_response = api_instance.delete_manufacturer_merchants(manufacturer_id, manufacturer_merchant_ids_input_request=manufacturer_merchant_ids_input_request)
        print("The response of ManufacturersMerchantsApi->delete_manufacturer_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManufacturersMerchantsApi->delete_manufacturer_merchants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manufacturer_id** | **int**| The id of the manufacturer | 
 **manufacturer_merchant_ids_input_request** | [**ManufacturerMerchantIdsInputRequest**](ManufacturerMerchantIdsInputRequest.md)| Merchant to remove from manufacturer | [optional] 

### Return type

[**ManufacturerMerchantsResponse**](ManufacturerMerchantsResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manufacturer_merchants**
> ManufacturerMerchantsResponse get_manufacturer_merchants(manufacturer_id)

Get all merchants for manufacturer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.manufacturer_merchants_response import ManufacturerMerchantsResponse
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
    api_instance = sparkfly_client.ManufacturersMerchantsApi(api_client)
    manufacturer_id = 56 # int | The id of the manufacturer

    try:
        # Get all merchants for manufacturer
        api_response = api_instance.get_manufacturer_merchants(manufacturer_id)
        print("The response of ManufacturersMerchantsApi->get_manufacturer_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManufacturersMerchantsApi->get_manufacturer_merchants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manufacturer_id** | **int**| The id of the manufacturer | 

### Return type

[**ManufacturerMerchantsResponse**](ManufacturerMerchantsResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | merchants to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_manufacturer_merchants**
> ManufacturerMerchantsResponse set_manufacturer_merchants(manufacturer_id, manufacturer_merchant_ids_input_request=manufacturer_merchant_ids_input_request)

Set eligible merchants for manufacturer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.manufacturer_merchant_ids_input_request import ManufacturerMerchantIdsInputRequest
from sparkfly_client.models.manufacturer_merchants_response import ManufacturerMerchantsResponse
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
    api_instance = sparkfly_client.ManufacturersMerchantsApi(api_client)
    manufacturer_id = 56 # int | The id of the manufacturer
    manufacturer_merchant_ids_input_request = sparkfly_client.ManufacturerMerchantIdsInputRequest() # ManufacturerMerchantIdsInputRequest | Merchants to set for manufacturer (optional)

    try:
        # Set eligible merchants for manufacturer
        api_response = api_instance.set_manufacturer_merchants(manufacturer_id, manufacturer_merchant_ids_input_request=manufacturer_merchant_ids_input_request)
        print("The response of ManufacturersMerchantsApi->set_manufacturer_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManufacturersMerchantsApi->set_manufacturer_merchants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manufacturer_id** | **int**| The id of the manufacturer | 
 **manufacturer_merchant_ids_input_request** | [**ManufacturerMerchantIdsInputRequest**](ManufacturerMerchantIdsInputRequest.md)| Merchants to set for manufacturer | [optional] 

### Return type

[**ManufacturerMerchantsResponse**](ManufacturerMerchantsResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_manufacturer_merchants**
> ManufacturerMerchantsResponse update_manufacturer_merchants(manufacturer_id, manufacturer_merchant_ids_input_request=manufacturer_merchant_ids_input_request)

Add an eligible merchant for manufacturer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.manufacturer_merchant_ids_input_request import ManufacturerMerchantIdsInputRequest
from sparkfly_client.models.manufacturer_merchants_response import ManufacturerMerchantsResponse
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
    api_instance = sparkfly_client.ManufacturersMerchantsApi(api_client)
    manufacturer_id = 56 # int | The id of the manufacturer
    manufacturer_merchant_ids_input_request = sparkfly_client.ManufacturerMerchantIdsInputRequest() # ManufacturerMerchantIdsInputRequest | Merchant to add to manufacturer (optional)

    try:
        # Add an eligible merchant for manufacturer
        api_response = api_instance.update_manufacturer_merchants(manufacturer_id, manufacturer_merchant_ids_input_request=manufacturer_merchant_ids_input_request)
        print("The response of ManufacturersMerchantsApi->update_manufacturer_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManufacturersMerchantsApi->update_manufacturer_merchants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manufacturer_id** | **int**| The id of the manufacturer | 
 **manufacturer_merchant_ids_input_request** | [**ManufacturerMerchantIdsInputRequest**](ManufacturerMerchantIdsInputRequest.md)| Merchant to add to manufacturer | [optional] 

### Return type

[**ManufacturerMerchantsResponse**](ManufacturerMerchantsResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

