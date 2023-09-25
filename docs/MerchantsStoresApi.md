# sparkfly_client.MerchantsStoresApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_merchants_merchant_id_stores_get**](MerchantsStoresApi.md#v10_merchants_merchant_id_stores_get) | **GET** /v1.0/merchants/:merchant_id/stores | Get all Stores for merchant
[**v10_merchants_merchant_id_stores_post**](MerchantsStoresApi.md#v10_merchants_merchant_id_stores_post) | **POST** /v1.0/merchants/:merchant_id/stores | Create an Store for merchant
[**v10_merchants_merchant_id_stores_store_id_delete**](MerchantsStoresApi.md#v10_merchants_merchant_id_stores_store_id_delete) | **DELETE** /v1.0/merchants/:merchant_id/stores/:store_id | Delete Store by ID for merchant
[**v10_merchants_merchant_id_stores_store_id_get**](MerchantsStoresApi.md#v10_merchants_merchant_id_stores_store_id_get) | **GET** /v1.0/merchants/:merchant_id/stores/:store_id | Get Store by ID for merchant
[**v10_merchants_merchant_id_stores_store_id_offers_get**](MerchantsStoresApi.md#v10_merchants_merchant_id_stores_store_id_offers_get) | **GET** /v1.0/merchants/:merchant_id/stores/:store_id/offers | List Offer IDs for Merchant and Store
[**v10_merchants_merchant_id_stores_store_id_put**](MerchantsStoresApi.md#v10_merchants_merchant_id_stores_store_id_put) | **PUT** /v1.0/merchants/:merchant_id/stores/:store_id | Update Store by ID for merchant
[**v10_merchants_stores_index_get**](MerchantsStoresApi.md#v10_merchants_stores_index_get) | **GET** /v1.0/merchants/stores/index | Get and Filter Stores WITH Active Offers (stores/index)
[**v10_merchants_stores_nearby_index_get**](MerchantsStoresApi.md#v10_merchants_stores_nearby_index_get) | **GET** /v1.0/merchants/stores/nearby/index | Get and Filter Stores WITH Active Offers (stores/nearby/index)
[**v10_merchants_stores_nearby_lat_lng_index_get**](MerchantsStoresApi.md#v10_merchants_stores_nearby_lat_lng_index_get) | **GET** /v1.0/merchants/stores/nearby/:lat/:lng/index | Get and Filter Stores WITH Active Offers (stores/nearby/:lat/:lng/index)
[**v10_merchants_stores_store_id_get**](MerchantsStoresApi.md#v10_merchants_stores_store_id_get) | **GET** /v1.0/merchants/stores/:store_id | Get Store by ID (without merchant)


# **v10_merchants_merchant_id_stores_get**
> StoreListResponse v10_merchants_merchant_id_stores_get(merchant_id, name=name)

Get all Stores for merchant

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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    name = 'name_example' # str | The store name to search by (optional)

    try:
        # Get all Stores for merchant
        api_response = api_instance.v10_merchants_merchant_id_stores_get(merchant_id, name=name)
        print("The response of MerchantsStoresApi->v10_merchants_merchant_id_stores_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_merchant_id_stores_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **name** | **str**| The store name to search by | [optional] 

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
**200** | successful retrieval of Stores for merchant |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_merchant_id_stores_post**
> StoreResponse v10_merchants_merchant_id_stores_post(merchant_id, store_input_request=store_input_request)

Create an Store for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.store_input_request import StoreInputRequest
from sparkfly_client.models.store_response import StoreResponse
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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_input_request = sparkfly_client.StoreInputRequest() # StoreInputRequest | Store to add (optional)

    try:
        # Create an Store for merchant
        api_response = api_instance.v10_merchants_merchant_id_stores_post(merchant_id, store_input_request=store_input_request)
        print("The response of MerchantsStoresApi->v10_merchants_merchant_id_stores_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_merchant_id_stores_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_input_request** | [**StoreInputRequest**](StoreInputRequest.md)| Store to add | [optional] 

### Return type

[**StoreResponse**](StoreResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Store successfully created |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_merchant_id_stores_store_id_delete**
> v10_merchants_merchant_id_stores_store_id_delete(merchant_id, store_id)

Delete Store by ID for merchant

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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_id = 56 # int | The id of the store

    try:
        # Delete Store by ID for merchant
        api_instance.v10_merchants_merchant_id_stores_store_id_delete(merchant_id, store_id)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_merchant_id_stores_store_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_id** | **int**| The id of the store | 

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
**200** | Successful deletion |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Store was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_merchant_id_stores_store_id_get**
> StoreResponse v10_merchants_merchant_id_stores_store_id_get(merchant_id, store_id)

Get Store by ID for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.store_response import StoreResponse
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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_id = 56 # int | The id of the store

    try:
        # Get Store by ID for merchant
        api_response = api_instance.v10_merchants_merchant_id_stores_store_id_get(merchant_id, store_id)
        print("The response of MerchantsStoresApi->v10_merchants_merchant_id_stores_store_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_merchant_id_stores_store_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_id** | **int**| The id of the store | 

### Return type

[**StoreResponse**](StoreResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Store was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_merchant_id_stores_store_id_offers_get**
> MerchantStoreOfferIdList v10_merchants_merchant_id_stores_store_id_offers_get(merchant_id, store_id)

List Offer IDs for Merchant and Store

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.merchant_store_offer_id_list import MerchantStoreOfferIdList
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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_id = 56 # int | The id of the store

    try:
        # List Offer IDs for Merchant and Store
        api_response = api_instance.v10_merchants_merchant_id_stores_store_id_offers_get(merchant_id, store_id)
        print("The response of MerchantsStoresApi->v10_merchants_merchant_id_stores_store_id_offers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_merchant_id_stores_store_id_offers_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_id** | **int**| The id of the store | 

### Return type

[**MerchantStoreOfferIdList**](MerchantStoreOfferIdList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of Offers for merchant store |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_merchant_id_stores_store_id_put**
> StoreResponse v10_merchants_merchant_id_stores_store_id_put(merchant_id, store_id, store_input_request=store_input_request)

Update Store by ID for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.store_input_request import StoreInputRequest
from sparkfly_client.models.store_response import StoreResponse
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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_id = 56 # int | The id of the store
    store_input_request = sparkfly_client.StoreInputRequest() # StoreInputRequest | Fields of Store to update in system (optional)

    try:
        # Update Store by ID for merchant
        api_response = api_instance.v10_merchants_merchant_id_stores_store_id_put(merchant_id, store_id, store_input_request=store_input_request)
        print("The response of MerchantsStoresApi->v10_merchants_merchant_id_stores_store_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_merchant_id_stores_store_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_id** | **int**| The id of the store | 
 **store_input_request** | [**StoreInputRequest**](StoreInputRequest.md)| Fields of Store to update in system | [optional] 

### Return type

[**StoreResponse**](StoreResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated store |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Store was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_stores_index_get**
> StoreListResponse v10_merchants_stores_index_get(lat, lng, by_tag_ids=by_tag_ids, sort_by=sort_by)

Get and Filter Stores WITH Active Offers (stores/index)

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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    lat = 'lat_example' # str | The latitude for the location to check
    lng = 'lng_example' # str | The longitude for the location to check
    by_tag_ids = 'by_tag_ids_example' # str | Store Tag IDs to filter by (optional)
    sort_by = 'sort_by_example' # str | Sort offers by 1 of their attributes ( name, start_running_at, status ) (optional)

    try:
        # Get and Filter Stores WITH Active Offers (stores/index)
        api_response = api_instance.v10_merchants_stores_index_get(lat, lng, by_tag_ids=by_tag_ids, sort_by=sort_by)
        print("The response of MerchantsStoresApi->v10_merchants_stores_index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_stores_index_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **str**| The latitude for the location to check | 
 **lng** | **str**| The longitude for the location to check | 
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
**200** | successful retrieval of Stores |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_stores_nearby_index_get**
> StoreListResponse v10_merchants_stores_nearby_index_get(lat, lng, by_tag_ids=by_tag_ids, sort_by=sort_by)

Get and Filter Stores WITH Active Offers (stores/nearby/index)

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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    lat = 'lat_example' # str | The latitude for the location to check
    lng = 'lng_example' # str | The longitude for the location to check
    by_tag_ids = 'by_tag_ids_example' # str | Store Tag IDs to filter by (optional)
    sort_by = 'sort_by_example' # str | Sort offers by 1 of their attributes ( name, start_running_at, status ) (optional)

    try:
        # Get and Filter Stores WITH Active Offers (stores/nearby/index)
        api_response = api_instance.v10_merchants_stores_nearby_index_get(lat, lng, by_tag_ids=by_tag_ids, sort_by=sort_by)
        print("The response of MerchantsStoresApi->v10_merchants_stores_nearby_index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_stores_nearby_index_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **str**| The latitude for the location to check | 
 **lng** | **str**| The longitude for the location to check | 
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
**200** | successful retrieval of Stores |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_stores_nearby_lat_lng_index_get**
> StoreListResponse v10_merchants_stores_nearby_lat_lng_index_get(lat, lng, by_tag_ids=by_tag_ids, sort_by=sort_by)

Get and Filter Stores WITH Active Offers (stores/nearby/:lat/:lng/index)

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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    lat = 'lat_example' # str | The latitude for the location to check
    lng = 'lng_example' # str | The longitude for the location to check
    by_tag_ids = 'by_tag_ids_example' # str | Store Tag IDs to filter by (optional)
    sort_by = 'sort_by_example' # str | Sort offers by 1 of their attributes ( name, start_running_at, status ) (optional)

    try:
        # Get and Filter Stores WITH Active Offers (stores/nearby/:lat/:lng/index)
        api_response = api_instance.v10_merchants_stores_nearby_lat_lng_index_get(lat, lng, by_tag_ids=by_tag_ids, sort_by=sort_by)
        print("The response of MerchantsStoresApi->v10_merchants_stores_nearby_lat_lng_index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_stores_nearby_lat_lng_index_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **str**| The latitude for the location to check | 
 **lng** | **str**| The longitude for the location to check | 
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
**200** | successful retrieval of Stores |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_stores_store_id_get**
> StoreResponse v10_merchants_stores_store_id_get(store_id)

Get Store by ID (without merchant)

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.store_response import StoreResponse
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
    api_instance = sparkfly_client.MerchantsStoresApi(api_client)
    store_id = 56 # int | The id of the store

    try:
        # Get Store by ID (without merchant)
        api_response = api_instance.v10_merchants_stores_store_id_get(store_id)
        print("The response of MerchantsStoresApi->v10_merchants_stores_store_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoresApi->v10_merchants_stores_store_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **int**| The id of the store | 

### Return type

[**StoreResponse**](StoreResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Store was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

