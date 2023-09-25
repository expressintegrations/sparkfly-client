# sparkfly_client.OffersStoresApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nearby_offer_stores**](OffersStoresApi.md#get_nearby_offer_stores) | **GET** /v1.0/offers/{offer_id}/stores | Get nearby Stores for Offer


# **get_nearby_offer_stores**
> StoreListResponse get_nearby_offer_stores(offer_id, lat, lng, x_channel_id, by_tag_ids=by_tag_ids, sort_by=sort_by)

Get nearby Stores for Offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.store_list_response import StoreListResponse
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
    api_instance = sparkfly_client.OffersStoresApi(api_client)
    offer_id = 56 # int | The id of the offer
    lat = 'lat_example' # str | The latitude for the location to check
    lng = 'lng_example' # str | The longitude for the location to check
    x_channel_id = 56 # int | The id of the channel
    by_tag_ids = 'by_tag_ids_example' # str | Store Tag IDs to filter by (optional)
    sort_by = 'sort_by_example' # str | Sort offers by 1 of their attributes ( name, start_running_at, status ) (optional)

    try:
        # Get nearby Stores for Offer
        api_response = api_instance.get_nearby_offer_stores(offer_id, lat, lng, x_channel_id, by_tag_ids=by_tag_ids, sort_by=sort_by)
        print("The response of OffersStoresApi->get_nearby_offer_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersStoresApi->get_nearby_offer_stores: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **int**| The id of the offer | 
 **lat** | **str**| The latitude for the location to check | 
 **lng** | **str**| The longitude for the location to check | 
 **x_channel_id** | **int**| The id of the channel | 
 **by_tag_ids** | **str**| Store Tag IDs to filter by | [optional] 
 **sort_by** | **str**| Sort offers by 1 of their attributes ( name, start_running_at, status ) | [optional] 

### Return type

[**StoreListResponse**](StoreListResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stores to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

