# sparkfly_client.MerchantsStoreListsApi

All URIs are relative to *https://api.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_merchant_store_list**](MerchantsStoreListsApi.md#create_merchant_store_list) | **POST** /v1.0/merchants/{merchant_id}/store_lists | Create an Store List for merchant
[**delete_merchant_store_list**](MerchantsStoreListsApi.md#delete_merchant_store_list) | **DELETE** /v1.0/merchants/{merchant_id}/store_lists/{store_list_id} | Delete Store List by ID for merchant
[**delete_merchant_store_list_stores**](MerchantsStoreListsApi.md#delete_merchant_store_list_stores) | **DELETE** /v1.0/merchants/store_lists/{store_list_id}/stores | Remove an eligible Store for store_list
[**get_merchant_store_list**](MerchantsStoreListsApi.md#get_merchant_store_list) | **GET** /v1.0/merchants/{merchant_id}/store_lists/{store_list_id} | Get Store List by ID for merchant
[**get_merchant_store_list_stores**](MerchantsStoreListsApi.md#get_merchant_store_list_stores) | **GET** /v1.0/merchants/store_lists/{store_list_id}/stores | Get all Stores for Store List
[**get_merchant_store_list_stores_detailed**](MerchantsStoreListsApi.md#get_merchant_store_list_stores_detailed) | **GET** /v1.0/merchants/{merchant_id}/store_lists/{store_list_id}/stores | Get all Stores for Store List (detailed)
[**get_merchant_store_lists**](MerchantsStoreListsApi.md#get_merchant_store_lists) | **GET** /v1.0/merchants/{merchant_id}/store_lists | Get all Store Lists for merchant
[**set_merchant_store_list_stores**](MerchantsStoreListsApi.md#set_merchant_store_list_stores) | **POST** /v1.0/merchants/store_lists/{store_list_id}/stores | Set eligible Stores for Store List
[**update_merchant_store_list**](MerchantsStoreListsApi.md#update_merchant_store_list) | **PUT** /v1.0/merchants/{merchant_id}/store_lists/{store_list_id} | Update Store List by ID for merchant
[**update_merchant_store_list_stores**](MerchantsStoreListsApi.md#update_merchant_store_list_stores) | **PUT** /v1.0/merchants/store_lists/{store_list_id}/stores | Add eligible Stores for Store List


# **create_merchant_store_list**
> StoreListObjectResponse create_merchant_store_list(merchant_id, store_list_input_request=store_list_input_request)

Create an Store List for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.store_list_input_request import StoreListInputRequest
from sparkfly_client.models.store_list_object_response import StoreListObjectResponse
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_list_input_request = sparkfly_client.StoreListInputRequest() # StoreListInputRequest | Store List to add (optional)

    try:
        # Create an Store List for merchant
        api_response = api_instance.create_merchant_store_list(merchant_id, store_list_input_request=store_list_input_request)
        print("The response of MerchantsStoreListsApi->create_merchant_store_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->create_merchant_store_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_list_input_request** | [**StoreListInputRequest**](StoreListInputRequest.md)| Store List to add | [optional] 

### Return type

[**StoreListObjectResponse**](StoreListObjectResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Store List successfully created |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_merchant_store_list**
> delete_merchant_store_list(merchant_id, store_list_id)

Delete Store List by ID for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_list_id = 56 # int | The id of the store list

    try:
        # Delete Store List by ID for merchant
        api_instance.delete_merchant_store_list(merchant_id, store_list_id)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->delete_merchant_store_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_list_id** | **int**| The id of the store list | 

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
**404** | Store List was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_merchant_store_list_stores**
> MerchantStoreListStoresResponse delete_merchant_store_list_stores(store_list_id, merchant_store_list_store_ids_input_request=merchant_store_list_store_ids_input_request)

Remove an eligible Store for store_list

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.merchant_store_list_store_ids_input_request import MerchantStoreListStoreIdsInputRequest
from sparkfly_client.models.merchant_store_list_stores_response import MerchantStoreListStoresResponse
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    store_list_id = 56 # int | The id of the store list
    merchant_store_list_store_ids_input_request = sparkfly_client.MerchantStoreListStoreIdsInputRequest() # MerchantStoreListStoreIdsInputRequest | Store to remove from Store list (optional)

    try:
        # Remove an eligible Store for store_list
        api_response = api_instance.delete_merchant_store_list_stores(store_list_id, merchant_store_list_store_ids_input_request=merchant_store_list_store_ids_input_request)
        print("The response of MerchantsStoreListsApi->delete_merchant_store_list_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->delete_merchant_store_list_stores: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_list_id** | **int**| The id of the store list | 
 **merchant_store_list_store_ids_input_request** | [**MerchantStoreListStoreIdsInputRequest**](MerchantStoreListStoreIdsInputRequest.md)| Store to remove from Store list | [optional] 

### Return type

[**MerchantStoreListStoresResponse**](MerchantStoreListStoresResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful removal of stores from store list |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant_store_list**
> StoreListObjectResponse get_merchant_store_list(merchant_id, store_list_id)

Get Store List by ID for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.store_list_object_response import StoreListObjectResponse
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_list_id = 56 # int | The id of the store list

    try:
        # Get Store List by ID for merchant
        api_response = api_instance.get_merchant_store_list(merchant_id, store_list_id)
        print("The response of MerchantsStoreListsApi->get_merchant_store_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->get_merchant_store_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_list_id** | **int**| The id of the store list | 

### Return type

[**StoreListObjectResponse**](StoreListObjectResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store List to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Store List was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant_store_list_stores**
> MerchantStoreListStoresResponse get_merchant_store_list_stores(store_list_id, name=name)

Get all Stores for Store List

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.merchant_store_list_stores_response import MerchantStoreListStoresResponse
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    store_list_id = 56 # int | The id of the store list
    name = 'name_example' # str | The name by which to search (optional)

    try:
        # Get all Stores for Store List
        api_response = api_instance.get_merchant_store_list_stores(store_list_id, name=name)
        print("The response of MerchantsStoreListsApi->get_merchant_store_list_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->get_merchant_store_list_stores: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_list_id** | **int**| The id of the store list | 
 **name** | **str**| The name by which to search | [optional] 

### Return type

[**MerchantStoreListStoresResponse**](MerchantStoreListStoresResponse.md)

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

# **get_merchant_store_list_stores_detailed**
> MerchantStoreListStoresList get_merchant_store_list_stores_detailed(merchant_id, store_list_id)

Get all Stores for Store List (detailed)

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.merchant_store_list_stores_list import MerchantStoreListStoresList
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_list_id = 56 # int | The id of the store list

    try:
        # Get all Stores for Store List (detailed)
        api_response = api_instance.get_merchant_store_list_stores_detailed(merchant_id, store_list_id)
        print("The response of MerchantsStoreListsApi->get_merchant_store_list_stores_detailed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->get_merchant_store_list_stores_detailed: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_list_id** | **int**| The id of the store list | 

### Return type

[**MerchantStoreListStoresList**](MerchantStoreListStoresList.md)

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

# **get_merchant_store_lists**
> MerchantStoreListList get_merchant_store_lists(merchant_id)

Get all Store Lists for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.merchant_store_list_list import MerchantStoreListList
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    merchant_id = 56 # int | The id of the merchant

    try:
        # Get all Store Lists for merchant
        api_response = api_instance.get_merchant_store_lists(merchant_id)
        print("The response of MerchantsStoreListsApi->get_merchant_store_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->get_merchant_store_lists: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 

### Return type

[**MerchantStoreListList**](MerchantStoreListList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of Store Lists for merchant |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_merchant_store_list_stores**
> MerchantStoreListStoresResponse set_merchant_store_list_stores(store_list_id, merchant_store_list_store_ids_input_request=merchant_store_list_store_ids_input_request)

Set eligible Stores for Store List

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.merchant_store_list_store_ids_input_request import MerchantStoreListStoreIdsInputRequest
from sparkfly_client.models.merchant_store_list_stores_response import MerchantStoreListStoresResponse
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    store_list_id = 56 # int | The id of the store list
    merchant_store_list_store_ids_input_request = sparkfly_client.MerchantStoreListStoreIdsInputRequest() # MerchantStoreListStoreIdsInputRequest | Store to set to Store list (optional)

    try:
        # Set eligible Stores for Store List
        api_response = api_instance.set_merchant_store_list_stores(store_list_id, merchant_store_list_store_ids_input_request=merchant_store_list_store_ids_input_request)
        print("The response of MerchantsStoreListsApi->set_merchant_store_list_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->set_merchant_store_list_stores: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_list_id** | **int**| The id of the store list | 
 **merchant_store_list_store_ids_input_request** | [**MerchantStoreListStoreIdsInputRequest**](MerchantStoreListStoreIdsInputRequest.md)| Store to set to Store list | [optional] 

### Return type

[**MerchantStoreListStoresResponse**](MerchantStoreListStoresResponse.md)

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

# **update_merchant_store_list**
> StoreListObjectResponse update_merchant_store_list(merchant_id, store_list_id, store_list_input_request=store_list_input_request)

Update Store List by ID for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.store_list_input_request import StoreListInputRequest
from sparkfly_client.models.store_list_object_response import StoreListObjectResponse
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    store_list_id = 56 # int | The id of the store list
    store_list_input_request = sparkfly_client.StoreListInputRequest() # StoreListInputRequest | Fields of Store List to update in system (optional)

    try:
        # Update Store List by ID for merchant
        api_response = api_instance.update_merchant_store_list(merchant_id, store_list_id, store_list_input_request=store_list_input_request)
        print("The response of MerchantsStoreListsApi->update_merchant_store_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->update_merchant_store_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **store_list_id** | **int**| The id of the store list | 
 **store_list_input_request** | [**StoreListInputRequest**](StoreListInputRequest.md)| Fields of Store List to update in system | [optional] 

### Return type

[**StoreListObjectResponse**](StoreListObjectResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated store list |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Store List was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_merchant_store_list_stores**
> MerchantStoreListStoresResponse update_merchant_store_list_stores(store_list_id, merchant_store_list_store_ids_input_request=merchant_store_list_store_ids_input_request)

Add eligible Stores for Store List

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.merchant_store_list_store_ids_input_request import MerchantStoreListStoreIdsInputRequest
from sparkfly_client.models.merchant_store_list_stores_response import MerchantStoreListStoresResponse
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
    api_instance = sparkfly_client.MerchantsStoreListsApi(api_client)
    store_list_id = 56 # int | The id of the store list
    merchant_store_list_store_ids_input_request = sparkfly_client.MerchantStoreListStoreIdsInputRequest() # MerchantStoreListStoreIdsInputRequest | Store to add to Store list (optional)

    try:
        # Add eligible Stores for Store List
        api_response = api_instance.update_merchant_store_list_stores(store_list_id, merchant_store_list_store_ids_input_request=merchant_store_list_store_ids_input_request)
        print("The response of MerchantsStoreListsApi->update_merchant_store_list_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsStoreListsApi->update_merchant_store_list_stores: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_list_id** | **int**| The id of the store list | 
 **merchant_store_list_store_ids_input_request** | [**MerchantStoreListStoreIdsInputRequest**](MerchantStoreListStoreIdsInputRequest.md)| Store to add to Store list | [optional] 

### Return type

[**MerchantStoreListStoresResponse**](MerchantStoreListStoresResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful add of stores to store list |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

