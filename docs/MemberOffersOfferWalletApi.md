# sparkfly_client.MemberOffersOfferWalletApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_member_offer_state**](MemberOffersOfferWalletApi.md#create_member_offer_state) | **POST** /v1.0/members/{member_id}/offer_states | Create a new Member Offer State and provide optional activation and expiration dates
[**get_member_offer_state**](MemberOffersOfferWalletApi.md#get_member_offer_state) | **GET** /v1.0/members/{member_id}/offer_states/{offer_state_id} | Get an individual Offer State for a Member
[**get_member_offer_states**](MemberOffersOfferWalletApi.md#get_member_offer_states) | **GET** /v1.0/members/{member_id}/offer_states | Get the entire list of Offer States for a Member
[**get_members_with_offer_states**](MemberOffersOfferWalletApi.md#get_members_with_offer_states) | **GET** /v1.0/members/offer_states | Retrieve Offer States
[**update_member_offer_state**](MemberOffersOfferWalletApi.md#update_member_offer_state) | **PUT** /v1.0/members/{member_id}/offer_states/{offer_state_id} | Update an individual Offer State for a Member - in order to change the availability
[**void_member_offer_state**](MemberOffersOfferWalletApi.md#void_member_offer_state) | **POST** /v1.0/members/{member_id}/offer_states/{offer_state_id}/void | Voids an individual Offer State for a Member by Member ID
[**void_offer_state_by_member_identifier**](MemberOffersOfferWalletApi.md#void_offer_state_by_member_identifier) | **POST** /v1.0/members/offer_states/{offer_state_id}/void | Voids an individual Offer State for a Member by Member Identifier


# **create_member_offer_state**
> OfferStateResponse create_member_offer_state(member_id, channel_id, offer_id, token=token, offer_state_input_request=offer_state_input_request)

Create a new Member Offer State and provide optional activation and expiration dates

This is used to create an individual offer state linking an offer to a member and set optional custom activation and expiration dates for the offer. This can be used to add an offer to a member - A few examples are when a member saves an offer to their account or reaches a particular milestone (i.e. after 10 visits).  If a token parameter is passed, the request will transfer an existing and transferable offer_state with the provided token to this member. A token would have been retrieved through some external integration process with the service interacting with the API.

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_state_input_request import OfferStateInputRequest
from sparkfly_client.models.offer_state_response import OfferStateResponse
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
    api_instance = sparkfly_client.MemberOffersOfferWalletApi(api_client)
    member_id = 56 # int | The id of the member
    channel_id = 56 # int | The id of the channel
    offer_id = 56 # int | The id of the offer
    token = 'token_example' # str | the token of the offer_state to search by (optional)
    offer_state_input_request = sparkfly_client.OfferStateInputRequest() # OfferStateInputRequest | Offer State to add to system (optional)

    try:
        # Create a new Member Offer State and provide optional activation and expiration dates
        api_response = api_instance.create_member_offer_state(member_id, channel_id, offer_id, token=token, offer_state_input_request=offer_state_input_request)
        print("The response of MemberOffersOfferWalletApi->create_member_offer_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberOffersOfferWalletApi->create_member_offer_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **channel_id** | **int**| The id of the channel | 
 **offer_id** | **int**| The id of the offer | 
 **token** | **str**| the token of the offer_state to search by | [optional] 
 **offer_state_input_request** | [**OfferStateInputRequest**](OfferStateInputRequest.md)| Offer State to add to system | [optional] 

### Return type

[**OfferStateResponse**](OfferStateResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Offer State successfully created and New Offer State returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_offer_state**
> OfferStateResponse get_member_offer_state(member_id, offer_state_id)

Get an individual Offer State for a Member

This is used to retrieve an individual offer state linked to a member. This can be used to display individual details for a particular offer state.

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_state_response import OfferStateResponse
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
    api_instance = sparkfly_client.MemberOffersOfferWalletApi(api_client)
    member_id = 56 # int | The id of the member
    offer_state_id = 56 # int | The id of the offer state

    try:
        # Get an individual Offer State for a Member
        api_response = api_instance.get_member_offer_state(member_id, offer_state_id)
        print("The response of MemberOffersOfferWalletApi->get_member_offer_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberOffersOfferWalletApi->get_member_offer_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **offer_state_id** | **int**| The id of the offer state | 

### Return type

[**OfferStateResponse**](OfferStateResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member&#39;s offer state returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_offer_states**
> OfferStateList get_member_offer_states(member_id, channel_id)

Get the entire list of Offer States for a Member

This is used to retrieve a list of offer states linked to a member. This list can be used to display the list to the member within a channel (i.e. App)

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_state_list import OfferStateList
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
    api_instance = sparkfly_client.MemberOffersOfferWalletApi(api_client)
    member_id = 56 # int | The id of the member
    channel_id = 56 # int | The id of the channel

    try:
        # Get the entire list of Offer States for a Member
        api_response = api_instance.get_member_offer_states(member_id, channel_id)
        print("The response of MemberOffersOfferWalletApi->get_member_offer_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberOffersOfferWalletApi->get_member_offer_states: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **channel_id** | **int**| The id of the channel | 

### Return type

[**OfferStateList**](OfferStateList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member&#39;s offer states list returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_with_offer_states**
> OfferStateList get_members_with_offer_states(token=token, credential_identifier=credential_identifier)

Retrieve Offer States

This is used to retrieve offer states. This call is normally used to search for particular offer states that can be added to a member.

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_state_list import OfferStateList
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
    api_instance = sparkfly_client.MemberOffersOfferWalletApi(api_client)
    token = 'token_example' # str | the token of the offer_state to search by (optional)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)

    try:
        # Retrieve Offer States
        api_response = api_instance.get_members_with_offer_states(token=token, credential_identifier=credential_identifier)
        print("The response of MemberOffersOfferWalletApi->get_members_with_offer_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberOffersOfferWalletApi->get_members_with_offer_states: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| the token of the offer_state to search by | [optional] 
 **credential_identifier** | **str**| The identifier of the credential | [optional] 

### Return type

[**OfferStateList**](OfferStateList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found offer states list returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_offer_state**
> OfferStateResponse update_member_offer_state(member_id, offer_state_id, offer_state_input_request=offer_state_input_request)

Update an individual Offer State for a Member - in order to change the availability

This is used to update the activation date and expiration date for an offer_state

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_state_input_request import OfferStateInputRequest
from sparkfly_client.models.offer_state_response import OfferStateResponse
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
    api_instance = sparkfly_client.MemberOffersOfferWalletApi(api_client)
    member_id = 56 # int | The id of the member
    offer_state_id = 56 # int | The id of the offer state
    offer_state_input_request = sparkfly_client.OfferStateInputRequest() # OfferStateInputRequest | The Offer State details to set - Object is required, fields are optional (optional)

    try:
        # Update an individual Offer State for a Member - in order to change the availability
        api_response = api_instance.update_member_offer_state(member_id, offer_state_id, offer_state_input_request=offer_state_input_request)
        print("The response of MemberOffersOfferWalletApi->update_member_offer_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberOffersOfferWalletApi->update_member_offer_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **offer_state_id** | **int**| The id of the offer state | 
 **offer_state_input_request** | [**OfferStateInputRequest**](OfferStateInputRequest.md)| The Offer State details to set - Object is required, fields are optional | [optional] 

### Return type

[**OfferStateResponse**](OfferStateResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Offer State successfully updated and updated Offer State returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_member_offer_state**
> void_member_offer_state(member_id, offer_state_id)

Voids an individual Offer State for a Member by Member ID

This is used to void an individual offer state linked to a member (by ID).

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
    api_instance = sparkfly_client.MemberOffersOfferWalletApi(api_client)
    member_id = 56 # int | The id of the member
    offer_state_id = 56 # int | The id of the offer state

    try:
        # Voids an individual Offer State for a Member by Member ID
        api_instance.void_member_offer_state(member_id, offer_state_id)
    except Exception as e:
        print("Exception when calling MemberOffersOfferWalletApi->void_member_offer_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **offer_state_id** | **int**| The id of the offer state | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Member or Offer State not found |  -  |
**422** | Offer State already voided |  -  |
**500** | Internal error voiding the Offer State |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_offer_state_by_member_identifier**
> void_offer_state_by_member_identifier(offer_state_id, member_identifier)

Voids an individual Offer State for a Member by Member Identifier

This is used to void an individual offer state linked to a member (by identifier).

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
    api_instance = sparkfly_client.MemberOffersOfferWalletApi(api_client)
    offer_state_id = 56 # int | The id of the offer state
    member_identifier = 'member_identifier_example' # str | The identifier of the member

    try:
        # Voids an individual Offer State for a Member by Member Identifier
        api_instance.void_offer_state_by_member_identifier(offer_state_id, member_identifier)
    except Exception as e:
        print("Exception when calling MemberOffersOfferWalletApi->void_offer_state_by_member_identifier: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_state_id** | **int**| The id of the offer state | 
 **member_identifier** | **str**| The identifier of the member | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Member or Offer State not found |  -  |
**422** | Offer State already voided |  -  |
**500** | Internal error voiding the Offer State |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

