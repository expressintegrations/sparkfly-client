# sparkfly_client.OfferEngineApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_activities_offers_get**](OfferEngineApi.md#v10_activities_offers_get) | **GET** /v1.0/activities/offers | Retrieve Offer Activities for Member
[**v10_members_member_id_activities_redemptions_get**](OfferEngineApi.md#v10_members_member_id_activities_redemptions_get) | **GET** /v1.0/members/:member_id/activities/redemptions | Retrieve Redeemed Redemptions for Member
[**v10_members_member_id_stores_store_id_activities_redemptions_get**](OfferEngineApi.md#v10_members_member_id_stores_store_id_activities_redemptions_get) | **GET** /v1.0/members/:member_id/stores/:store_id/activities/redemptions | Retrieve Redeemed Redemptions for Member for Store
[**v10_members_member_id_stores_store_id_check_incheck_in_latlatcheck_in_lnglng_post**](OfferEngineApi.md#v10_members_member_id_stores_store_id_check_incheck_in_latlatcheck_in_lnglng_post) | **POST** /v1.0/members/:member_id/stores/:store_id/check-in?check_in[lat]&#x3D;:lat&amp;check_in[lng]&#x3D;:lng | Check-In Member to Store
[**v10_members_member_id_stores_store_id_get**](OfferEngineApi.md#v10_members_member_id_stores_store_id_get) | **GET** /v1.0/members/:member_id/stores/:store_id | Retrieve Store for Member


# **v10_activities_offers_get**
> OfferActivityList v10_activities_offers_get(member_id)

Retrieve Offer Activities for Member

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_activity_list import OfferActivityList
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
    api_instance = sparkfly_client.OfferEngineApi(api_client)
    member_id = 56 # int | The id of the member

    try:
        # Retrieve Offer Activities for Member
        api_response = api_instance.v10_activities_offers_get(member_id)
        print("The response of OfferEngineApi->v10_activities_offers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferEngineApi->v10_activities_offers_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 

### Return type

[**OfferActivityList**](OfferActivityList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of offer activity |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_members_member_id_activities_redemptions_get**
> RedemptionList v10_members_member_id_activities_redemptions_get(member_id)

Retrieve Redeemed Redemptions for Member

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.redemption_list import RedemptionList
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
    api_instance = sparkfly_client.OfferEngineApi(api_client)
    member_id = 56 # int | The id of the member

    try:
        # Retrieve Redeemed Redemptions for Member
        api_response = api_instance.v10_members_member_id_activities_redemptions_get(member_id)
        print("The response of OfferEngineApi->v10_members_member_id_activities_redemptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferEngineApi->v10_members_member_id_activities_redemptions_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 

### Return type

[**RedemptionList**](RedemptionList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of redemptions |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_members_member_id_stores_store_id_activities_redemptions_get**
> RedemptionList v10_members_member_id_stores_store_id_activities_redemptions_get(member_id, store_id)

Retrieve Redeemed Redemptions for Member for Store

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.redemption_list import RedemptionList
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
    api_instance = sparkfly_client.OfferEngineApi(api_client)
    member_id = 56 # int | The id of the member
    store_id = 56 # int | The id of the store

    try:
        # Retrieve Redeemed Redemptions for Member for Store
        api_response = api_instance.v10_members_member_id_stores_store_id_activities_redemptions_get(member_id, store_id)
        print("The response of OfferEngineApi->v10_members_member_id_stores_store_id_activities_redemptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferEngineApi->v10_members_member_id_stores_store_id_activities_redemptions_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **store_id** | **int**| The id of the store | 

### Return type

[**RedemptionList**](RedemptionList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of redemptions |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_members_member_id_stores_store_id_check_incheck_in_latlatcheck_in_lnglng_post**
> v10_members_member_id_stores_store_id_check_incheck_in_latlatcheck_in_lnglng_post(member_id, store_id, lat, lng)

Check-In Member to Store

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
    api_instance = sparkfly_client.OfferEngineApi(api_client)
    member_id = 56 # int | The id of the member
    store_id = 56 # int | The id of the store
    lat = 'lat_example' # str | The latitude for the location to check
    lng = 'lng_example' # str | The longitude for the location to check

    try:
        # Check-In Member to Store
        api_instance.v10_members_member_id_stores_store_id_check_incheck_in_latlatcheck_in_lnglng_post(member_id, store_id, lat, lng)
    except Exception as e:
        print("Exception when calling OfferEngineApi->v10_members_member_id_stores_store_id_check_incheck_in_latlatcheck_in_lnglng_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **store_id** | **int**| The id of the store | 
 **lat** | **str**| The latitude for the location to check | 
 **lng** | **str**| The longitude for the location to check | 

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
**200** | successful check in of member to store |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_members_member_id_stores_store_id_get**
> MemberStoreResponse v10_members_member_id_stores_store_id_get(member_id, store_id, x_channel_id)

Retrieve Store for Member

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.member_store_response import MemberStoreResponse
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
    api_instance = sparkfly_client.OfferEngineApi(api_client)
    member_id = 56 # int | The id of the member
    store_id = 56 # int | The id of the store
    x_channel_id = 56 # int | The id of the channel

    try:
        # Retrieve Store for Member
        api_response = api_instance.v10_members_member_id_stores_store_id_get(member_id, store_id, x_channel_id)
        print("The response of OfferEngineApi->v10_members_member_id_stores_store_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferEngineApi->v10_members_member_id_stores_store_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **store_id** | **int**| The id of the store | 
 **x_channel_id** | **int**| The id of the channel | 

### Return type

[**MemberStoreResponse**](MemberStoreResponse.md)

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

