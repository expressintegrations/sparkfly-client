# sparkfly_client.CredentialsApi

All URIs are relative to *https://api.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential**](CredentialsApi.md#create_credential) | **POST** /v1.0/credentials | Creates a credential
[**delete_credential**](CredentialsApi.md#delete_credential) | **DELETE** /v1.0/credentials/{credential_id} | Delete Credential
[**get_credential**](CredentialsApi.md#get_credential) | **GET** /v1.0/credentials/{credential_id} | Get Credential
[**get_credentials**](CredentialsApi.md#get_credentials) | **GET** /v1.0/credentials | List Credentials
[**get_offer_eligibility_for_member**](CredentialsApi.md#get_offer_eligibility_for_member) | **GET** /v1.0/credentials/eligible | Determine if a member is eligible for an offer
[**redeem_credential**](CredentialsApi.md#redeem_credential) | **PUT** /v1.0/credentials/{credential_id}/redeem | Redeem a credential
[**update_credential**](CredentialsApi.md#update_credential) | **PUT** /v1.0/credentials/{credential_id} | Updates a credential
[**void_credential**](CredentialsApi.md#void_credential) | **PUT** /v1.0/credentials/{credential_id}/void | Void a credential


# **create_credential**
> CredentialResponse create_credential(credential_input_request=credential_input_request)

Creates a credential

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.credential_input_request import CredentialInputRequest
from sparkfly_client.models.credential_response import CredentialResponse
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
    api_instance = sparkfly_client.CredentialsApi(api_client)
    credential_input_request = sparkfly_client.CredentialInputRequest() # CredentialInputRequest | Fields of credential to create in system (optional)

    try:
        # Creates a credential
        api_response = api_instance.create_credential(credential_input_request=credential_input_request)
        print("The response of CredentialsApi->create_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_credential: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_input_request** | [**CredentialInputRequest**](CredentialInputRequest.md)| Fields of credential to create in system | [optional] 

### Return type

[**CredentialResponse**](CredentialResponse.md)

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

# **delete_credential**
> CredentialResponse delete_credential(credential_id)

Delete Credential

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.credential_response import CredentialResponse
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
    api_instance = sparkfly_client.CredentialsApi(api_client)
    credential_id = 56 # int | The id of the credential

    try:
        # Delete Credential
        api_response = api_instance.delete_credential(credential_id)
        print("The response of CredentialsApi->delete_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_credential: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **int**| The id of the credential | 

### Return type

[**CredentialResponse**](CredentialResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful deletion of credential |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Credential was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential**
> CredentialResponse get_credential(credential_id)

Get Credential

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.credential_response import CredentialResponse
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
    api_instance = sparkfly_client.CredentialsApi(api_client)
    credential_id = 56 # int | The id of the credential

    try:
        # Get Credential
        api_response = api_instance.get_credential(credential_id)
        print("The response of CredentialsApi->get_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credential: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **int**| The id of the credential | 

### Return type

[**CredentialResponse**](CredentialResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of credential |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Credential was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credentials**
> CredentialList get_credentials(member_id=member_id, offer_id=offer_id, store_id=store_id)

List Credentials

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.credential_list import CredentialList
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
    api_instance = sparkfly_client.CredentialsApi(api_client)
    member_id = 56 # int | The id of the member (optional)
    offer_id = 56 # int | The id of the offer (optional)
    store_id = 56 # int | The id of the store (optional)

    try:
        # List Credentials
        api_response = api_instance.get_credentials(member_id=member_id, offer_id=offer_id, store_id=store_id)
        print("The response of CredentialsApi->get_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | [optional] 
 **offer_id** | **int**| The id of the offer | [optional] 
 **store_id** | **int**| The id of the store | [optional] 

### Return type

[**CredentialList**](CredentialList.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of credentials |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_eligibility_for_member**
> CredentialEligibilityResponse get_offer_eligibility_for_member(member_id, offer_id)

Determine if a member is eligible for an offer

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.credential_eligibility_response import CredentialEligibilityResponse
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
    api_instance = sparkfly_client.CredentialsApi(api_client)
    member_id = 56 # int | The id of the member
    offer_id = 56 # int | The id of the offer

    try:
        # Determine if a member is eligible for an offer
        api_response = api_instance.get_offer_eligibility_for_member(member_id, offer_id)
        print("The response of CredentialsApi->get_offer_eligibility_for_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_offer_eligibility_for_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **int**| The id of the member | 
 **offer_id** | **int**| The id of the offer | 

### Return type

[**CredentialEligibilityResponse**](CredentialEligibilityResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful retrieval of eligibility |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_credential**
> CredentialResponse redeem_credential(credential_id)

Redeem a credential

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.credential_response import CredentialResponse
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
    api_instance = sparkfly_client.CredentialsApi(api_client)
    credential_id = 56 # int | The id of the credential

    try:
        # Redeem a credential
        api_response = api_instance.redeem_credential(credential_id)
        print("The response of CredentialsApi->redeem_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->redeem_credential: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **int**| The id of the credential | 

### Return type

[**CredentialResponse**](CredentialResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful redemption |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Credential was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credential**
> CredentialResponse update_credential(credential_id, credential_input_request=credential_input_request)

Updates a credential

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.credential_input_request import CredentialInputRequest
from sparkfly_client.models.credential_response import CredentialResponse
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
    api_instance = sparkfly_client.CredentialsApi(api_client)
    credential_id = 56 # int | The id of the credential
    credential_input_request = sparkfly_client.CredentialInputRequest() # CredentialInputRequest | Fields of credential to update in system (optional)

    try:
        # Updates a credential
        api_response = api_instance.update_credential(credential_id, credential_input_request=credential_input_request)
        print("The response of CredentialsApi->update_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_credential: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **int**| The id of the credential | 
 **credential_input_request** | [**CredentialInputRequest**](CredentialInputRequest.md)| Fields of credential to update in system | [optional] 

### Return type

[**CredentialResponse**](CredentialResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful update |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**400** | Error parsing request |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Credential was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_credential**
> CredentialResponse void_credential(credential_id)

Void a credential

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.credential_response import CredentialResponse
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
    api_instance = sparkfly_client.CredentialsApi(api_client)
    credential_id = 56 # int | The id of the credential

    try:
        # Void a credential
        api_response = api_instance.void_credential(credential_id)
        print("The response of CredentialsApi->void_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->void_credential: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **int**| The id of the credential | 

### Return type

[**CredentialResponse**](CredentialResponse.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful void |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Etag -  <br>  * Location -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**401** | Unauthorized |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |
**404** | Credential was not found by id |  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * X-Request-Id -  <br>  * X-Runtime -  <br>  * X-Ua-Compatible -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

