# sparkfly_client.MerchantsItemSetsItemsApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_merchants_merchant_id_item_sets_item_set_id_items_get**](MerchantsItemSetsItemsApi.md#v10_merchants_merchant_id_item_sets_item_set_id_items_get) | **GET** /v1.0/merchants/:merchant_id/item_sets/:item_set_id/items | Get items for item set for merchant


# **v10_merchants_merchant_id_item_sets_item_set_id_items_get**
> ItemListResponse v10_merchants_merchant_id_item_sets_item_set_id_items_get(merchant_id, item_set_id)

Get items for item set for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.item_list_response import ItemListResponse
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
    api_instance = sparkfly_client.MerchantsItemSetsItemsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    item_set_id = 56 # int | The id of the item set

    try:
        # Get items for item set for merchant
        api_response = api_instance.v10_merchants_merchant_id_item_sets_item_set_id_items_get(merchant_id, item_set_id)
        print("The response of MerchantsItemSetsItemsApi->v10_merchants_merchant_id_item_sets_item_set_id_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsItemSetsItemsApi->v10_merchants_merchant_id_item_sets_item_set_id_items_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **item_set_id** | **int**| The id of the item set | 

### Return type

[**ItemListResponse**](ItemListResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of items |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
