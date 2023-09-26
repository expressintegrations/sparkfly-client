# sparkfly_client.OffersMerchantsApi

All URIs are relative to *https://api.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_offer_merchants**](OffersMerchantsApi.md#delete_offer_merchants) | **DELETE** /v1.0/offers/{offer_id}/merchants | Remove eligible Merchants from offer
[**get_offer_merchants**](OffersMerchantsApi.md#get_offer_merchants) | **GET** /v1.0/offers/{offer_id}/merchants | Eligible Merchants List
[**set_offer_merchants**](OffersMerchantsApi.md#set_offer_merchants) | **POST** /v1.0/offers/{offer_id}/merchants | Set eligible Merchants for offer
[**update_offer_merchants**](OffersMerchantsApi.md#update_offer_merchants) | **PUT** /v1.0/offers/{offer_id}/merchants | Add eligible Merchants for offer


# **delete_offer_merchants**
> OfferMerchantsResponse delete_offer_merchants(offer_id, offer_merchant_ids_input_request=offer_merchant_ids_input_request)

Remove eligible Merchants from offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_merchant_ids_input_request import OfferMerchantIdsInputRequest
from sparkfly_client.models.offer_merchants_response import OfferMerchantsResponse
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
    api_instance = sparkfly_client.OffersMerchantsApi(api_client)
    offer_id = 56 # int | The id of the offer
    offer_merchant_ids_input_request = sparkfly_client.OfferMerchantIdsInputRequest() # OfferMerchantIdsInputRequest | Merchant IDs to remove from Offer (optional)

    try:
        # Remove eligible Merchants from offer
        api_response = api_instance.delete_offer_merchants(offer_id, offer_merchant_ids_input_request=offer_merchant_ids_input_request)
        print("The response of OffersMerchantsApi->delete_offer_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersMerchantsApi->delete_offer_merchants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **offer_merchant_ids_input_request** | [**OfferMerchantIdsInputRequest**](OfferMerchantIdsInputRequest.md)| Merchant IDs to remove from Offer | [optional] 

### Return type

[**OfferMerchantsResponse**](OfferMerchantsResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful removal |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_merchants**
> OfferMerchantsResponse get_offer_merchants(offer_id)

Eligible Merchants List

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_merchants_response import OfferMerchantsResponse
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
    api_instance = sparkfly_client.OffersMerchantsApi(api_client)
    offer_id = 56 # int | The id of the offer

    try:
        # Eligible Merchants List
        api_response = api_instance.get_offer_merchants(offer_id)
        print("The response of OffersMerchantsApi->get_offer_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersMerchantsApi->get_offer_merchants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 

### Return type

[**OfferMerchantsResponse**](OfferMerchantsResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Merchants to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_offer_merchants**
> OfferMerchantsResponse set_offer_merchants(offer_id, offer_merchant_ids_input_request=offer_merchant_ids_input_request)

Set eligible Merchants for offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_merchant_ids_input_request import OfferMerchantIdsInputRequest
from sparkfly_client.models.offer_merchants_response import OfferMerchantsResponse
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
    api_instance = sparkfly_client.OffersMerchantsApi(api_client)
    offer_id = 56 # int | The id of the offer
    offer_merchant_ids_input_request = sparkfly_client.OfferMerchantIdsInputRequest() # OfferMerchantIdsInputRequest | Merchant IDs to set to Offer (optional)

    try:
        # Set eligible Merchants for offer
        api_response = api_instance.set_offer_merchants(offer_id, offer_merchant_ids_input_request=offer_merchant_ids_input_request)
        print("The response of OffersMerchantsApi->set_offer_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersMerchantsApi->set_offer_merchants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **offer_merchant_ids_input_request** | [**OfferMerchantIdsInputRequest**](OfferMerchantIdsInputRequest.md)| Merchant IDs to set to Offer | [optional] 

### Return type

[**OfferMerchantsResponse**](OfferMerchantsResponse.md)

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

# **update_offer_merchants**
> OfferMerchantsResponse update_offer_merchants(offer_id, offer_merchant_ids_input_request=offer_merchant_ids_input_request)

Add eligible Merchants for offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_merchant_ids_input_request import OfferMerchantIdsInputRequest
from sparkfly_client.models.offer_merchants_response import OfferMerchantsResponse
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
    api_instance = sparkfly_client.OffersMerchantsApi(api_client)
    offer_id = 56 # int | The id of the offer
    offer_merchant_ids_input_request = sparkfly_client.OfferMerchantIdsInputRequest() # OfferMerchantIdsInputRequest | Merchant IDs to Add to Offer (optional)

    try:
        # Add eligible Merchants for offer
        api_response = api_instance.update_offer_merchants(offer_id, offer_merchant_ids_input_request=offer_merchant_ids_input_request)
        print("The response of OffersMerchantsApi->update_offer_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersMerchantsApi->update_offer_merchants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **offer_merchant_ids_input_request** | [**OfferMerchantIdsInputRequest**](OfferMerchantIdsInputRequest.md)| Merchant IDs to Add to Offer | [optional] 

### Return type

[**OfferMerchantsResponse**](OfferMerchantsResponse.md)

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

