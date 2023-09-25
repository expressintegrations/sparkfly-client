# sparkfly_client.MemberPrivacyApi

All URIs are relative to *https://api-staging.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_privacy_member_delete_request_post**](MemberPrivacyApi.md#v10_privacy_member_delete_request_post) | **POST** /v1.0/privacy/member/delete_request | Creates a deletion request for a member
[**v10_privacy_member_export_get**](MemberPrivacyApi.md#v10_privacy_member_export_get) | **GET** /v1.0/privacy/member/export | Exports data associated with a member


# **v10_privacy_member_delete_request_post**
> v10_privacy_member_delete_request_post(credential_identifier=credential_identifier, member_identifier=member_identifier)

Creates a deletion request for a member

Looks up and creates a deletion request for the member associated with the provided  `member_identifier` or `credential_identifier` query parameter. For each deletion request, all member offers will first be voided, then after 7 days, or longer if specified in an  Account's preferences, the member will be anonymized. 

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
    api_instance = sparkfly_client.MemberPrivacyApi(api_client)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)
    member_identifier = 'member_identifier_example' # str | The identifier of the member (optional)

    try:
        # Creates a deletion request for a member
        api_instance.v10_privacy_member_delete_request_post(credential_identifier=credential_identifier, member_identifier=member_identifier)
    except Exception as e:
        print("Exception when calling MemberPrivacyApi->v10_privacy_member_delete_request_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_identifier** | **str**| The identifier of the credential | [optional] 
 **member_identifier** | **str**| The identifier of the member | [optional] 

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
**200** | Successfully created a member deletion request |  -  |
**401** | Unauthorized |  -  |
**400** | Bad request |  -  |
**422** | Member could not be located from the member or credential identifiers |  -  |
**500** | Internal issue creating a member deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_privacy_member_export_get**
> MemberExportData v10_privacy_member_export_get(credential_identifier=credential_identifier, member_identifier=member_identifier)

Exports data associated with a member

Looks up and exports data for the member associated with the provided  `member_identifier` or `credential_identifier` query parameter. 

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.member_export_data import MemberExportData
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
    api_instance = sparkfly_client.MemberPrivacyApi(api_client)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)
    member_identifier = 'member_identifier_example' # str | The identifier of the member (optional)

    try:
        # Exports data associated with a member
        api_response = api_instance.v10_privacy_member_export_get(credential_identifier=credential_identifier, member_identifier=member_identifier)
        print("The response of MemberPrivacyApi->v10_privacy_member_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPrivacyApi->v10_privacy_member_export_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_identifier** | **str**| The identifier of the credential | [optional] 
 **member_identifier** | **str**| The identifier of the member | [optional] 

### Return type

[**MemberExportData**](MemberExportData.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully responded with exported data for a member |  -  |
**401** | Unauthorized |  -  |
**400** | Bad request |  -  |
**422** | Member could not be located from the member or credential identifiers |  -  |
**500** | Internal issue exporting member data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

