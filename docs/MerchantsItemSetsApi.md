# sparkfly_client.MerchantsItemSetsApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_merchants_merchant_id_item_sets_get**](MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_get) | **GET** /v1.0/merchants/:merchant_id/item_sets | Get all item sets for merchant
[**v10_merchants_merchant_id_item_sets_item_set_id_delete**](MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_item_set_id_delete) | **DELETE** /v1.0/merchants/:merchant_id/item_sets/:item_set_id | Delete item set by ID for merchant
[**v10_merchants_merchant_id_item_sets_item_set_id_get**](MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_item_set_id_get) | **GET** /v1.0/merchants/:merchant_id/item_sets/:item_set_id | Get item set by ID for merchant
[**v10_merchants_merchant_id_item_sets_item_set_id_put**](MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_item_set_id_put) | **PUT** /v1.0/merchants/:merchant_id/item_sets/:item_set_id | Update item set by ID for merchant
[**v10_merchants_merchant_id_item_sets_post**](MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_post) | **POST** /v1.0/merchants/:merchant_id/item_sets | Create an item set for merchant


# **v10_merchants_merchant_id_item_sets_get**
> MerchantItemSetList v10_merchants_merchant_id_item_sets_get(merchant_id)

Get all item sets for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.merchant_item_set_list import MerchantItemSetList
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
    api_instance = sparkfly_client.MerchantsItemSetsApi(api_client)
    merchant_id = 56 # int | The id of the merchant

    try:
        # Get all item sets for merchant
        api_response = api_instance.v10_merchants_merchant_id_item_sets_get(merchant_id)
        print("The response of MerchantsItemSetsApi->v10_merchants_merchant_id_item_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsItemSetsApi->v10_merchants_merchant_id_item_sets_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 

### Return type

[**MerchantItemSetList**](MerchantItemSetList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of item sets for merchant |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_merchant_id_item_sets_item_set_id_delete**
> v10_merchants_merchant_id_item_sets_item_set_id_delete(merchant_id, item_set_id)

Delete item set by ID for merchant

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
    api_instance = sparkfly_client.MerchantsItemSetsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    item_set_id = 56 # int | The id of the item set

    try:
        # Delete item set by ID for merchant
        api_instance.v10_merchants_merchant_id_item_sets_item_set_id_delete(merchant_id, item_set_id)
    except Exception as e:
        print("Exception when calling MerchantsItemSetsApi->v10_merchants_merchant_id_item_sets_item_set_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **item_set_id** | **int**| The id of the item set | 

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
**404** | Item set was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_merchant_id_item_sets_item_set_id_get**
> ItemSetResponse v10_merchants_merchant_id_item_sets_item_set_id_get(merchant_id, item_set_id)

Get item set by ID for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.item_set_response import ItemSetResponse
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
    api_instance = sparkfly_client.MerchantsItemSetsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    item_set_id = 56 # int | The id of the item set

    try:
        # Get item set by ID for merchant
        api_response = api_instance.v10_merchants_merchant_id_item_sets_item_set_id_get(merchant_id, item_set_id)
        print("The response of MerchantsItemSetsApi->v10_merchants_merchant_id_item_sets_item_set_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsItemSetsApi->v10_merchants_merchant_id_item_sets_item_set_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **item_set_id** | **int**| The id of the item set | 

### Return type

[**ItemSetResponse**](ItemSetResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item set to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Item set was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_merchant_id_item_sets_item_set_id_put**
> ItemSetResponse v10_merchants_merchant_id_item_sets_item_set_id_put(merchant_id, item_set_id, item_set_input_request=item_set_input_request)

Update item set by ID for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.item_set_input_request import ItemSetInputRequest
from sparkfly_client.models.item_set_response import ItemSetResponse
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
    api_instance = sparkfly_client.MerchantsItemSetsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    item_set_id = 56 # int | The id of the item set
    item_set_input_request = sparkfly_client.ItemSetInputRequest() # ItemSetInputRequest | Fields of item set to update in system (optional)

    try:
        # Update item set by ID for merchant
        api_response = api_instance.v10_merchants_merchant_id_item_sets_item_set_id_put(merchant_id, item_set_id, item_set_input_request=item_set_input_request)
        print("The response of MerchantsItemSetsApi->v10_merchants_merchant_id_item_sets_item_set_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsItemSetsApi->v10_merchants_merchant_id_item_sets_item_set_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **item_set_id** | **int**| The id of the item set | 
 **item_set_input_request** | [**ItemSetInputRequest**](ItemSetInputRequest.md)| Fields of item set to update in system | [optional] 

### Return type

[**ItemSetResponse**](ItemSetResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated item set |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Item set was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_merchants_merchant_id_item_sets_post**
> ItemSetResponse v10_merchants_merchant_id_item_sets_post(merchant_id, item_set_input_request=item_set_input_request)

Create an item set for merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.item_set_input_request import ItemSetInputRequest
from sparkfly_client.models.item_set_response import ItemSetResponse
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
    api_instance = sparkfly_client.MerchantsItemSetsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    item_set_input_request = sparkfly_client.ItemSetInputRequest() # ItemSetInputRequest | Item set to add (optional)

    try:
        # Create an item set for merchant
        api_response = api_instance.v10_merchants_merchant_id_item_sets_post(merchant_id, item_set_input_request=item_set_input_request)
        print("The response of MerchantsItemSetsApi->v10_merchants_merchant_id_item_sets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsItemSetsApi->v10_merchants_merchant_id_item_sets_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **item_set_input_request** | [**ItemSetInputRequest**](ItemSetInputRequest.md)| Item set to add | [optional] 

### Return type

[**ItemSetResponse**](ItemSetResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Item set successfully created |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

