# sparkfly_client.OffersChannelsApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_offers_offer_id_channels_channel_id_get**](OffersChannelsApi.md#v10_offers_offer_id_channels_channel_id_get) | **GET** /v1.0/offers/:offer_id/channels/:channel_id | Eligible Channel Show
[**v10_offers_offer_id_channels_channel_id_put**](OffersChannelsApi.md#v10_offers_offer_id_channels_channel_id_put) | **PUT** /v1.0/offers/:offer_id/channels/:channel_id | Eligible Channel Update
[**v10_offers_offer_id_channels_delete**](OffersChannelsApi.md#v10_offers_offer_id_channels_delete) | **DELETE** /v1.0/offers/:offer_id/channels | Remove eligible Channels from offer
[**v10_offers_offer_id_channels_get**](OffersChannelsApi.md#v10_offers_offer_id_channels_get) | **GET** /v1.0/offers/:offer_id/channels | Eligible Channels List
[**v10_offers_offer_id_channels_post**](OffersChannelsApi.md#v10_offers_offer_id_channels_post) | **POST** /v1.0/offers/:offer_id/channels | Set eligible Channels for offer
[**v10_offers_offer_id_channels_put**](OffersChannelsApi.md#v10_offers_offer_id_channels_put) | **PUT** /v1.0/offers/:offer_id/channels | Add eligible Channels for offer


# **v10_offers_offer_id_channels_channel_id_get**
> EligibleChannelResponse v10_offers_offer_id_channels_channel_id_get(offer_id, channel_id)

Eligible Channel Show

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.eligible_channel_response import EligibleChannelResponse
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
    api_instance = sparkfly_client.OffersChannelsApi(api_client)
    offer_id = 56 # int | The id of the offer
    channel_id = 56 # int | The id of the channel

    try:
        # Eligible Channel Show
        api_response = api_instance.v10_offers_offer_id_channels_channel_id_get(offer_id, channel_id)
        print("The response of OffersChannelsApi->v10_offers_offer_id_channels_channel_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersChannelsApi->v10_offers_offer_id_channels_channel_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **channel_id** | **int**| The id of the channel | 

### Return type

[**EligibleChannelResponse**](EligibleChannelResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Eligible Channel to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_offers_offer_id_channels_channel_id_put**
> EligibleChannelResponse v10_offers_offer_id_channels_channel_id_put(offer_id, channel_id, eligible_channel_input_request=eligible_channel_input_request)

Eligible Channel Update

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.eligible_channel_input_request import EligibleChannelInputRequest
from sparkfly_client.models.eligible_channel_response import EligibleChannelResponse
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
    api_instance = sparkfly_client.OffersChannelsApi(api_client)
    offer_id = 56 # int | The id of the offer
    channel_id = 56 # int | The id of the channel
    eligible_channel_input_request = sparkfly_client.EligibleChannelInputRequest() # EligibleChannelInputRequest | Eligible channel update (optional)

    try:
        # Eligible Channel Update
        api_response = api_instance.v10_offers_offer_id_channels_channel_id_put(offer_id, channel_id, eligible_channel_input_request=eligible_channel_input_request)
        print("The response of OffersChannelsApi->v10_offers_offer_id_channels_channel_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersChannelsApi->v10_offers_offer_id_channels_channel_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **channel_id** | **int**| The id of the channel | 
 **eligible_channel_input_request** | [**EligibleChannelInputRequest**](EligibleChannelInputRequest.md)| Eligible channel update | [optional] 

### Return type

[**EligibleChannelResponse**](EligibleChannelResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful update |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_offers_offer_id_channels_delete**
> OfferChannelsResponse v10_offers_offer_id_channels_delete(offer_id, offer_channel_ids_input_request=offer_channel_ids_input_request)

Remove eligible Channels from offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_channel_ids_input_request import OfferChannelIdsInputRequest
from sparkfly_client.models.offer_channels_response import OfferChannelsResponse
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
    api_instance = sparkfly_client.OffersChannelsApi(api_client)
    offer_id = 56 # int | The id of the offer
    offer_channel_ids_input_request = sparkfly_client.OfferChannelIdsInputRequest() # OfferChannelIdsInputRequest | Channel IDs to remove from Offer (optional)

    try:
        # Remove eligible Channels from offer
        api_response = api_instance.v10_offers_offer_id_channels_delete(offer_id, offer_channel_ids_input_request=offer_channel_ids_input_request)
        print("The response of OffersChannelsApi->v10_offers_offer_id_channels_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersChannelsApi->v10_offers_offer_id_channels_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **offer_channel_ids_input_request** | [**OfferChannelIdsInputRequest**](OfferChannelIdsInputRequest.md)| Channel IDs to remove from Offer | [optional] 

### Return type

[**OfferChannelsResponse**](OfferChannelsResponse.md)

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

# **v10_offers_offer_id_channels_get**
> OfferChannelsResponse v10_offers_offer_id_channels_get(offer_id)

Eligible Channels List

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_channels_response import OfferChannelsResponse
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
    api_instance = sparkfly_client.OffersChannelsApi(api_client)
    offer_id = 56 # int | The id of the offer

    try:
        # Eligible Channels List
        api_response = api_instance.v10_offers_offer_id_channels_get(offer_id)
        print("The response of OffersChannelsApi->v10_offers_offer_id_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersChannelsApi->v10_offers_offer_id_channels_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 

### Return type

[**OfferChannelsResponse**](OfferChannelsResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channels to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_offers_offer_id_channels_post**
> OfferChannelsResponse v10_offers_offer_id_channels_post(offer_id, offer_channel_ids_input_request=offer_channel_ids_input_request)

Set eligible Channels for offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_channel_ids_input_request import OfferChannelIdsInputRequest
from sparkfly_client.models.offer_channels_response import OfferChannelsResponse
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
    api_instance = sparkfly_client.OffersChannelsApi(api_client)
    offer_id = 56 # int | The id of the offer
    offer_channel_ids_input_request = sparkfly_client.OfferChannelIdsInputRequest() # OfferChannelIdsInputRequest | Channel IDs to set to Offer (optional)

    try:
        # Set eligible Channels for offer
        api_response = api_instance.v10_offers_offer_id_channels_post(offer_id, offer_channel_ids_input_request=offer_channel_ids_input_request)
        print("The response of OffersChannelsApi->v10_offers_offer_id_channels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersChannelsApi->v10_offers_offer_id_channels_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **offer_channel_ids_input_request** | [**OfferChannelIdsInputRequest**](OfferChannelIdsInputRequest.md)| Channel IDs to set to Offer | [optional] 

### Return type

[**OfferChannelsResponse**](OfferChannelsResponse.md)

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

# **v10_offers_offer_id_channels_put**
> OfferChannelsResponse v10_offers_offer_id_channels_put(offer_id, offer_channel_ids_input_request=offer_channel_ids_input_request)

Add eligible Channels for offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_channel_ids_input_request import OfferChannelIdsInputRequest
from sparkfly_client.models.offer_channels_response import OfferChannelsResponse
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
    api_instance = sparkfly_client.OffersChannelsApi(api_client)
    offer_id = 56 # int | The id of the offer
    offer_channel_ids_input_request = sparkfly_client.OfferChannelIdsInputRequest() # OfferChannelIdsInputRequest | Channel IDs to Add to Offer (optional)

    try:
        # Add eligible Channels for offer
        api_response = api_instance.v10_offers_offer_id_channels_put(offer_id, offer_channel_ids_input_request=offer_channel_ids_input_request)
        print("The response of OffersChannelsApi->v10_offers_offer_id_channels_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersChannelsApi->v10_offers_offer_id_channels_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **offer_channel_ids_input_request** | [**OfferChannelIdsInputRequest**](OfferChannelIdsInputRequest.md)| Channel IDs to Add to Offer | [optional] 

### Return type

[**OfferChannelsResponse**](OfferChannelsResponse.md)

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

