# sparkfly_client.LoyaltyPointsApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_points_card_status_get**](LoyaltyPointsApi.md#v10_points_card_status_get) | **GET** /v1.0/points/card_status | Check Card Status
[**v10_points_transfer_post**](LoyaltyPointsApi.md#v10_points_transfer_post) | **POST** /v1.0/points/transfer | Transfer Loyalty Points


# **v10_points_card_status_get**
> PointsCardStatus v10_points_card_status_get(identifier, channel_id)

Check Card Status

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.points_card_status import PointsCardStatus
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
    api_instance = sparkfly_client.LoyaltyPointsApi(api_client)
    identifier = 'identifier_example' # str | The identifier of the member
    channel_id = 56 # int | The id of the channel

    try:
        # Check Card Status
        api_response = api_instance.v10_points_card_status_get(identifier, channel_id)
        print("The response of LoyaltyPointsApi->v10_points_card_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltyPointsApi->v10_points_card_status_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The identifier of the member | 
 **channel_id** | **int**| The id of the channel | 

### Return type

[**PointsCardStatus**](PointsCardStatus.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of card status |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_points_transfer_post**
> PointsCardStatus v10_points_transfer_post(identifier, points, txid, channel_id)

Transfer Loyalty Points

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.points_card_status import PointsCardStatus
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
    api_instance = sparkfly_client.LoyaltyPointsApi(api_client)
    identifier = 'identifier_example' # str | The identifier of the member
    points = 56 # int | Number of points to transfer
    txid = 'txid_example' # str | Unique transaction id for the transfer for logging and to protect duplicates
    channel_id = 56 # int | The id of the channel

    try:
        # Transfer Loyalty Points
        api_response = api_instance.v10_points_transfer_post(identifier, points, txid, channel_id)
        print("The response of LoyaltyPointsApi->v10_points_transfer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltyPointsApi->v10_points_transfer_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The identifier of the member | 
 **points** | **int**| Number of points to transfer | 
 **txid** | **str**| Unique transaction id for the transfer for logging and to protect duplicates | 
 **channel_id** | **int**| The id of the channel | 

### Return type

[**PointsCardStatus**](PointsCardStatus.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful transfer |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

