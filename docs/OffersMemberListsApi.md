# sparkfly_client.OffersMemberListsApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_offers_offer_id_member_lists_delete**](OffersMemberListsApi.md#v10_offers_offer_id_member_lists_delete) | **DELETE** /v1.0/offers/:offer_id/member_lists | Remove eligible Member Lists from offer
[**v10_offers_offer_id_member_lists_get**](OffersMemberListsApi.md#v10_offers_offer_id_member_lists_get) | **GET** /v1.0/offers/:offer_id/member_lists | Eligible Member Lists List
[**v10_offers_offer_id_member_lists_post**](OffersMemberListsApi.md#v10_offers_offer_id_member_lists_post) | **POST** /v1.0/offers/:offer_id/member_lists | Set eligible Member Lists for offer
[**v10_offers_offer_id_member_lists_put**](OffersMemberListsApi.md#v10_offers_offer_id_member_lists_put) | **PUT** /v1.0/offers/:offer_id/member_lists | Add eligible Member Lists for offer


# **v10_offers_offer_id_member_lists_delete**
> OfferMemberListsResponse v10_offers_offer_id_member_lists_delete(offer_id, offer_member_list_ids_input_request=offer_member_list_ids_input_request)

Remove eligible Member Lists from offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_member_list_ids_input_request import OfferMemberListIdsInputRequest
from sparkfly_client.models.offer_member_lists_response import OfferMemberListsResponse
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
    api_instance = sparkfly_client.OffersMemberListsApi(api_client)
    offer_id = 56 # int | The id of the offer
    offer_member_list_ids_input_request = sparkfly_client.OfferMemberListIdsInputRequest() # OfferMemberListIdsInputRequest | Member List IDs to remove from Offer (optional)

    try:
        # Remove eligible Member Lists from offer
        api_response = api_instance.v10_offers_offer_id_member_lists_delete(offer_id, offer_member_list_ids_input_request=offer_member_list_ids_input_request)
        print("The response of OffersMemberListsApi->v10_offers_offer_id_member_lists_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersMemberListsApi->v10_offers_offer_id_member_lists_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **offer_member_list_ids_input_request** | [**OfferMemberListIdsInputRequest**](OfferMemberListIdsInputRequest.md)| Member List IDs to remove from Offer | [optional] 

### Return type

[**OfferMemberListsResponse**](OfferMemberListsResponse.md)

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

# **v10_offers_offer_id_member_lists_get**
> OfferMemberListsResponse v10_offers_offer_id_member_lists_get(offer_id)

Eligible Member Lists List

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_member_lists_response import OfferMemberListsResponse
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
    api_instance = sparkfly_client.OffersMemberListsApi(api_client)
    offer_id = 56 # int | The id of the offer

    try:
        # Eligible Member Lists List
        api_response = api_instance.v10_offers_offer_id_member_lists_get(offer_id)
        print("The response of OffersMemberListsApi->v10_offers_offer_id_member_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersMemberListsApi->v10_offers_offer_id_member_lists_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 

### Return type

[**OfferMemberListsResponse**](OfferMemberListsResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member Lists to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_offers_offer_id_member_lists_post**
> OfferMemberListsResponse v10_offers_offer_id_member_lists_post(offer_id, offer_member_list_ids_input_request=offer_member_list_ids_input_request)

Set eligible Member Lists for offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_member_list_ids_input_request import OfferMemberListIdsInputRequest
from sparkfly_client.models.offer_member_lists_response import OfferMemberListsResponse
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
    api_instance = sparkfly_client.OffersMemberListsApi(api_client)
    offer_id = 56 # int | The id of the offer
    offer_member_list_ids_input_request = sparkfly_client.OfferMemberListIdsInputRequest() # OfferMemberListIdsInputRequest | Member List IDs to set to Offer (optional)

    try:
        # Set eligible Member Lists for offer
        api_response = api_instance.v10_offers_offer_id_member_lists_post(offer_id, offer_member_list_ids_input_request=offer_member_list_ids_input_request)
        print("The response of OffersMemberListsApi->v10_offers_offer_id_member_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersMemberListsApi->v10_offers_offer_id_member_lists_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **offer_member_list_ids_input_request** | [**OfferMemberListIdsInputRequest**](OfferMemberListIdsInputRequest.md)| Member List IDs to set to Offer | [optional] 

### Return type

[**OfferMemberListsResponse**](OfferMemberListsResponse.md)

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

# **v10_offers_offer_id_member_lists_put**
> OfferMemberListsResponse v10_offers_offer_id_member_lists_put(offer_id, offer_member_list_ids_input_request=offer_member_list_ids_input_request)

Add eligible Member Lists for offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_member_list_ids_input_request import OfferMemberListIdsInputRequest
from sparkfly_client.models.offer_member_lists_response import OfferMemberListsResponse
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
    api_instance = sparkfly_client.OffersMemberListsApi(api_client)
    offer_id = 56 # int | The id of the offer
    offer_member_list_ids_input_request = sparkfly_client.OfferMemberListIdsInputRequest() # OfferMemberListIdsInputRequest | Member List IDs to Add to Offer (optional)

    try:
        # Add eligible Member Lists for offer
        api_response = api_instance.v10_offers_offer_id_member_lists_put(offer_id, offer_member_list_ids_input_request=offer_member_list_ids_input_request)
        print("The response of OffersMemberListsApi->v10_offers_offer_id_member_lists_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersMemberListsApi->v10_offers_offer_id_member_lists_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **offer_member_list_ids_input_request** | [**OfferMemberListIdsInputRequest**](OfferMemberListIdsInputRequest.md)| Member List IDs to Add to Offer | [optional] 

### Return type

[**OfferMemberListsResponse**](OfferMemberListsResponse.md)

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

