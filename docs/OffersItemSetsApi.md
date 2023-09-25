# sparkfly_client.OffersItemSetsApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_offer_eligible_item_set**](OffersItemSetsApi.md#delete_offer_eligible_item_set) | **DELETE** /v1.0/offers/{offer_id}/eligible_item_sets/{eligible_item_set_id} | Remove eligible Item Set from offer
[**get_offer_eligible_item_set**](OffersItemSetsApi.md#get_offer_eligible_item_set) | **GET** /v1.0/offers/{offer_id}/eligible_item_sets/{eligible_item_set_id} | Retrieve eligible Item Set for offer
[**set_offer_eligible_item_sets**](OffersItemSetsApi.md#set_offer_eligible_item_sets) | **POST** /v1.0/offers/{offer_id}/eligible_item_sets | Eligible Item Set for Offer - Create
[**update_offer_eligible_item_set**](OffersItemSetsApi.md#update_offer_eligible_item_set) | **PUT** /v1.0/offers/{offer_id}/eligible_item_sets/{eligible_item_set_id} | Update eligible Item Set for offer


# **delete_offer_eligible_item_set**
> delete_offer_eligible_item_set(offer_id, eligible_item_set_id)

Remove eligible Item Set from offer

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
    api_instance = sparkfly_client.OffersItemSetsApi(api_client)
    offer_id = 56 # int | The id of the offer
    eligible_item_set_id = 56 # int | The id of the eligible item set

    try:
        # Remove eligible Item Set from offer
        api_instance.delete_offer_eligible_item_set(offer_id, eligible_item_set_id)
    except Exception as e:
        print("Exception when calling OffersItemSetsApi->delete_offer_eligible_item_set: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **eligible_item_set_id** | **int**| The id of the eligible item set | 

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
**200** | Successful removal |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Item set was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_eligible_item_set**
> EligibleItemSetResponse get_offer_eligible_item_set(offer_id, eligible_item_set_id)

Retrieve eligible Item Set for offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.eligible_item_set_response import EligibleItemSetResponse
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
    api_instance = sparkfly_client.OffersItemSetsApi(api_client)
    offer_id = 56 # int | The id of the offer
    eligible_item_set_id = 56 # int | The id of the eligible item set

    try:
        # Retrieve eligible Item Set for offer
        api_response = api_instance.get_offer_eligible_item_set(offer_id, eligible_item_set_id)
        print("The response of OffersItemSetsApi->get_offer_eligible_item_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersItemSetsApi->get_offer_eligible_item_set: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **eligible_item_set_id** | **int**| The id of the eligible item set | 

### Return type

[**EligibleItemSetResponse**](EligibleItemSetResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful retrieval |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_offer_eligible_item_sets**
> EligibleItemSetResponse set_offer_eligible_item_sets(offer_id, eligible_item_set_input_request=eligible_item_set_input_request)

Eligible Item Set for Offer - Create

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.eligible_item_set_input_request import EligibleItemSetInputRequest
from sparkfly_client.models.eligible_item_set_response import EligibleItemSetResponse
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
    api_instance = sparkfly_client.OffersItemSetsApi(api_client)
    offer_id = 56 # int | The id of the offer
    eligible_item_set_input_request = sparkfly_client.EligibleItemSetInputRequest() # EligibleItemSetInputRequest | Item Set to create for Offer (optional)

    try:
        # Eligible Item Set for Offer - Create
        api_response = api_instance.set_offer_eligible_item_sets(offer_id, eligible_item_set_input_request=eligible_item_set_input_request)
        print("The response of OffersItemSetsApi->set_offer_eligible_item_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersItemSetsApi->set_offer_eligible_item_sets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **eligible_item_set_input_request** | [**EligibleItemSetInputRequest**](EligibleItemSetInputRequest.md)| Item Set to create for Offer | [optional] 

### Return type

[**EligibleItemSetResponse**](EligibleItemSetResponse.md)

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

# **update_offer_eligible_item_set**
> EligibleItemSetResponse update_offer_eligible_item_set(offer_id, eligible_item_set_id, eligible_item_set_input_request=eligible_item_set_input_request)

Update eligible Item Set for offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.eligible_item_set_input_request import EligibleItemSetInputRequest
from sparkfly_client.models.eligible_item_set_response import EligibleItemSetResponse
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
    api_instance = sparkfly_client.OffersItemSetsApi(api_client)
    offer_id = 56 # int | The id of the offer
    eligible_item_set_id = 56 # int | The id of the eligible item set
    eligible_item_set_input_request = sparkfly_client.EligibleItemSetInputRequest() # EligibleItemSetInputRequest | Item Set IDs to Update for Offer (optional)

    try:
        # Update eligible Item Set for offer
        api_response = api_instance.update_offer_eligible_item_set(offer_id, eligible_item_set_id, eligible_item_set_input_request=eligible_item_set_input_request)
        print("The response of OffersItemSetsApi->update_offer_eligible_item_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersItemSetsApi->update_offer_eligible_item_set: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **eligible_item_set_id** | **int**| The id of the eligible item set | 
 **eligible_item_set_input_request** | [**EligibleItemSetInputRequest**](EligibleItemSetInputRequest.md)| Item Set IDs to Update for Offer | [optional] 

### Return type

[**EligibleItemSetResponse**](EligibleItemSetResponse.md)

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
**404** | Item set was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

