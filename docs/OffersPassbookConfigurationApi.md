# sparkfly_client.OffersPassbookConfigurationApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_offers_offer_id_passbook_configuration_delete**](OffersPassbookConfigurationApi.md#v10_offers_offer_id_passbook_configuration_delete) | **DELETE** /v1.0/offers/:offer_id/passbook_configuration | Passbook Configuration Delete for Offer
[**v10_offers_offer_id_passbook_configuration_get**](OffersPassbookConfigurationApi.md#v10_offers_offer_id_passbook_configuration_get) | **GET** /v1.0/offers/:offer_id/passbook_configuration | Get Passbook Configuration for Offer
[**v10_offers_offer_id_passbook_configuration_post**](OffersPassbookConfigurationApi.md#v10_offers_offer_id_passbook_configuration_post) | **POST** /v1.0/offers/:offer_id/passbook_configuration | Passbook Configuration Create
[**v10_offers_offer_id_passbook_configuration_put**](OffersPassbookConfigurationApi.md#v10_offers_offer_id_passbook_configuration_put) | **PUT** /v1.0/offers/:offer_id/passbook_configuration | Update Passbook Configuration for Offer


# **v10_offers_offer_id_passbook_configuration_delete**
> v10_offers_offer_id_passbook_configuration_delete(offer_id)

Passbook Configuration Delete for Offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_client.Configuration(
    host = "https://api-staging.sparkfly.com"
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
    api_instance = sparkfly_client.OffersPassbookConfigurationApi(api_client)
    offer_id = 56 # int | The id of the offer

    try:
        # Passbook Configuration Delete for Offer
        api_instance.v10_offers_offer_id_passbook_configuration_delete(offer_id)
    except Exception as e:
        print("Exception when calling OffersPassbookConfigurationApi->v10_offers_offer_id_passbook_configuration_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 

### Return type

void (empty response body)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful deletion |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_offers_offer_id_passbook_configuration_get**
> PassbookConfigurationResponse v10_offers_offer_id_passbook_configuration_get(offer_id)

Get Passbook Configuration for Offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.passbook_configuration_response import PassbookConfigurationResponse
from sparkfly_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_client.Configuration(
    host = "https://api-staging.sparkfly.com"
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
    api_instance = sparkfly_client.OffersPassbookConfigurationApi(api_client)
    offer_id = 56 # int | The id of the offer

    try:
        # Get Passbook Configuration for Offer
        api_response = api_instance.v10_offers_offer_id_passbook_configuration_get(offer_id)
        print("The response of OffersPassbookConfigurationApi->v10_offers_offer_id_passbook_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersPassbookConfigurationApi->v10_offers_offer_id_passbook_configuration_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 

### Return type

[**PassbookConfigurationResponse**](PassbookConfigurationResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Passbook Configuration to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_offers_offer_id_passbook_configuration_post**
> PassbookConfigurationResponse v10_offers_offer_id_passbook_configuration_post(offer_id, passbook_configuration_input_request=passbook_configuration_input_request)

Passbook Configuration Create

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.passbook_configuration_input_request import PassbookConfigurationInputRequest
from sparkfly_client.models.passbook_configuration_response import PassbookConfigurationResponse
from sparkfly_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_client.Configuration(
    host = "https://api-staging.sparkfly.com"
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
    api_instance = sparkfly_client.OffersPassbookConfigurationApi(api_client)
    offer_id = 56 # int | The id of the offer
    passbook_configuration_input_request = sparkfly_client.PassbookConfigurationInputRequest() # PassbookConfigurationInputRequest | Passbook Configuration to Create (optional)

    try:
        # Passbook Configuration Create
        api_response = api_instance.v10_offers_offer_id_passbook_configuration_post(offer_id, passbook_configuration_input_request=passbook_configuration_input_request)
        print("The response of OffersPassbookConfigurationApi->v10_offers_offer_id_passbook_configuration_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersPassbookConfigurationApi->v10_offers_offer_id_passbook_configuration_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **passbook_configuration_input_request** | [**PassbookConfigurationInputRequest**](PassbookConfigurationInputRequest.md)| Passbook Configuration to Create | [optional] 

### Return type

[**PassbookConfigurationResponse**](PassbookConfigurationResponse.md)

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

# **v10_offers_offer_id_passbook_configuration_put**
> PassbookConfigurationResponse v10_offers_offer_id_passbook_configuration_put(offer_id, passbook_configuration_input_request=passbook_configuration_input_request)

Update Passbook Configuration for Offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.passbook_configuration_input_request import PassbookConfigurationInputRequest
from sparkfly_client.models.passbook_configuration_response import PassbookConfigurationResponse
from sparkfly_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_client.Configuration(
    host = "https://api-staging.sparkfly.com"
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
    api_instance = sparkfly_client.OffersPassbookConfigurationApi(api_client)
    offer_id = 56 # int | The id of the offer
    passbook_configuration_input_request = sparkfly_client.PassbookConfigurationInputRequest() # PassbookConfigurationInputRequest | Passbook Configuration to Update (optional)

    try:
        # Update Passbook Configuration for Offer
        api_response = api_instance.v10_offers_offer_id_passbook_configuration_put(offer_id, passbook_configuration_input_request=passbook_configuration_input_request)
        print("The response of OffersPassbookConfigurationApi->v10_offers_offer_id_passbook_configuration_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersPassbookConfigurationApi->v10_offers_offer_id_passbook_configuration_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **passbook_configuration_input_request** | [**PassbookConfigurationInputRequest**](PassbookConfigurationInputRequest.md)| Passbook Configuration to Update | [optional] 

### Return type

[**PassbookConfigurationResponse**](PassbookConfigurationResponse.md)

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

