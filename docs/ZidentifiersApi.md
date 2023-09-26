# sparkfly_client.ZidentifiersApi

All URIs are relative to *https://api.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_z_identifier**](ZidentifiersApi.md#create_z_identifier) | **GET** /v1.0/members/{member_id}/offers/{offer_id}/zidentifiers | Create an identifier linking Offer, Member, Channel
[**get_z_identifier**](ZidentifiersApi.md#get_z_identifier) | **GET** /v1.0/members/zidentifiers/{zid} | Get Zidentifier


# **create_z_identifier**
> ZIdentifierResponse create_z_identifier(member_id, offer_id, x_channel_id)

Create an identifier linking Offer, Member, Channel

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.z_identifier_response import ZIdentifierResponse
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
    api_instance = sparkfly_client.ZidentifiersApi(api_client)
    member_id = 56 # int | The id of the member
    offer_id = 56 # int | The id of the offer
    x_channel_id = 56 # int | The id of the channel

    try:
        # Create an identifier linking Offer, Member, Channel
        api_response = api_instance.create_z_identifier(member_id, offer_id, x_channel_id)
        print("The response of ZidentifiersApi->create_z_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZidentifiersApi->create_z_identifier: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **offer_id** | **int**| The id of the offer | 
 **x_channel_id** | **int**| The id of the channel | 

### Return type

[**ZIdentifierResponse**](ZIdentifierResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ZIdentifier to create |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_z_identifier**
> ZIdentifierResponse get_z_identifier(zid)

Get Zidentifier

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.z_identifier_response import ZIdentifierResponse
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
    api_instance = sparkfly_client.ZidentifiersApi(api_client)
    zid = 56 # int | The id linking Offer, Member, and Channel

    try:
        # Get Zidentifier
        api_response = api_instance.get_z_identifier(zid)
        print("The response of ZidentifiersApi->get_z_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZidentifiersApi->get_z_identifier: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zid** | **int**| The id linking Offer, Member, and Channel | 

### Return type

[**ZIdentifierResponse**](ZIdentifierResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zidentifier to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

