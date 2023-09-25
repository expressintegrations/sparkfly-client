# sparkfly_client.MemberListsMembersApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_member_list_members**](MemberListsMembersApi.md#delete_member_list_members) | **DELETE** /v1.0/member_lists/{member_list_id}/members | Remove an eligible member for member_list
[**get_member_list_members**](MemberListsMembersApi.md#get_member_list_members) | **GET** /v1.0/member_lists/{member_list_id}/members | Get all Members for Member List
[**set_member_list_members**](MemberListsMembersApi.md#set_member_list_members) | **POST** /v1.0/member_lists/{member_list_id}/members | Set eligible members for Member List
[**update_member_list_members**](MemberListsMembersApi.md#update_member_list_members) | **PUT** /v1.0/member_lists/{member_list_id}/members | Add eligible members for Member List


# **delete_member_list_members**
> MemberListMembersResponse delete_member_list_members(member_list_id, member_list_member_ids_input_request=member_list_member_ids_input_request)

Remove an eligible member for member_list

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.member_list_member_ids_input_request import MemberListMemberIdsInputRequest
from sparkfly_client.models.member_list_members_response import MemberListMembersResponse
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
    api_instance = sparkfly_client.MemberListsMembersApi(api_client)
    member_list_id = 56 # int | The id of the member list
    member_list_member_ids_input_request = sparkfly_client.MemberListMemberIdsInputRequest() # MemberListMemberIdsInputRequest | Member to remove from member list (optional)

    try:
        # Remove an eligible member for member_list
        api_response = api_instance.delete_member_list_members(member_list_id, member_list_member_ids_input_request=member_list_member_ids_input_request)
        print("The response of MemberListsMembersApi->delete_member_list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberListsMembersApi->delete_member_list_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_list_id** | **int**| The id of the member list | 
 **member_list_member_ids_input_request** | [**MemberListMemberIdsInputRequest**](MemberListMemberIdsInputRequest.md)| Member to remove from member list | [optional] 

### Return type

[**MemberListMembersResponse**](MemberListMembersResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful removal |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_list_members**
> MemberListMembersResponse get_member_list_members(member_list_id)

Get all Members for Member List

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.member_list_members_response import MemberListMembersResponse
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
    api_instance = sparkfly_client.MemberListsMembersApi(api_client)
    member_list_id = 56 # int | The id of the member list

    try:
        # Get all Members for Member List
        api_response = api_instance.get_member_list_members(member_list_id)
        print("The response of MemberListsMembersApi->get_member_list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberListsMembersApi->get_member_list_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_list_id** | **int**| The id of the member list | 

### Return type

[**MemberListMembersResponse**](MemberListMembersResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | members to be returned |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Etag -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Auth-Token -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_member_list_members**
> MemberListMembersResponse set_member_list_members(member_list_id, member_list_member_ids_input_request=member_list_member_ids_input_request)

Set eligible members for Member List

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.member_list_member_ids_input_request import MemberListMemberIdsInputRequest
from sparkfly_client.models.member_list_members_response import MemberListMembersResponse
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
    api_instance = sparkfly_client.MemberListsMembersApi(api_client)
    member_list_id = 56 # int | The id of the member list
    member_list_member_ids_input_request = sparkfly_client.MemberListMemberIdsInputRequest() # MemberListMemberIdsInputRequest | Member to set to member list (optional)

    try:
        # Set eligible members for Member List
        api_response = api_instance.set_member_list_members(member_list_id, member_list_member_ids_input_request=member_list_member_ids_input_request)
        print("The response of MemberListsMembersApi->set_member_list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberListsMembersApi->set_member_list_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_list_id** | **int**| The id of the member list | 
 **member_list_member_ids_input_request** | [**MemberListMemberIdsInputRequest**](MemberListMemberIdsInputRequest.md)| Member to set to member list | [optional] 

### Return type

[**MemberListMembersResponse**](MemberListMembersResponse.md)

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

# **update_member_list_members**
> MemberListMembersResponse update_member_list_members(member_list_id, member_list_member_ids_input_request=member_list_member_ids_input_request)

Add eligible members for Member List

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.member_list_member_ids_input_request import MemberListMemberIdsInputRequest
from sparkfly_client.models.member_list_members_response import MemberListMembersResponse
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
    api_instance = sparkfly_client.MemberListsMembersApi(api_client)
    member_list_id = 56 # int | The id of the member list
    member_list_member_ids_input_request = sparkfly_client.MemberListMemberIdsInputRequest() # MemberListMemberIdsInputRequest | Member to add to member list (optional)

    try:
        # Add eligible members for Member List
        api_response = api_instance.update_member_list_members(member_list_id, member_list_member_ids_input_request=member_list_member_ids_input_request)
        print("The response of MemberListsMembersApi->update_member_list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberListsMembersApi->update_member_list_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_list_id** | **int**| The id of the member list | 
 **member_list_member_ids_input_request** | [**MemberListMemberIdsInputRequest**](MemberListMemberIdsInputRequest.md)| Member to add to member list | [optional] 

### Return type

[**MemberListMembersResponse**](MemberListMembersResponse.md)

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

