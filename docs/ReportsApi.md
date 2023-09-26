# sparkfly_client.ReportsApi

All URIs are relative to *https://api.sparkfly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_merchant_data**](ReportsApi.md#get_all_merchant_data) | **GET** /v1.0/reports/account_level | Generates a report of full Merchant data in a given timeframe for a all Merchants
[**get_merchant_data**](ReportsApi.md#get_merchant_data) | **GET** /v1.0/merchants/{merchant_id}/reports/full | Generates a report of full Merchant data in a given timeframe for a single Merchant
[**get_merchant_impressions**](ReportsApi.md#get_merchant_impressions) | **GET** /v1.0/merchants/{merchant_id}/reports/impressions | Get Unique Impressions
[**get_offer_activity**](ReportsApi.md#get_offer_activity) | **GET** /v1.0/reports/offer_activity | Generates a report of all offer activity in a given timeframe
[**get_offer_redemptions**](ReportsApi.md#get_offer_redemptions) | **GET** /v1.0/reports/redemptions | Generates a report of all offer redemptions for a given timeframe and store list


# **get_all_merchant_data**
> AccountLevelMerchantReport get_all_merchant_data(var_from, to)

Generates a report of full Merchant data in a given timeframe for a all Merchants

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.account_level_merchant_report import AccountLevelMerchantReport
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
    api_instance = sparkfly_client.ReportsApi(api_client)
    var_from = 1455197824 # int | The first reported datetime to gather data from. Must be paired with the \"to\" parameter.
    to = 1455629824 # int | The last reported datetime to gather data from. Must be paired with the \"from\" parameter.

    try:
        # Generates a report of full Merchant data in a given timeframe for a all Merchants
        api_response = api_instance.get_all_merchant_data(var_from, to)
        print("The response of ReportsApi->get_all_merchant_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_all_merchant_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**| The first reported datetime to gather data from. Must be paired with the \&quot;to\&quot; parameter. | 
 **to** | **int**| The last reported datetime to gather data from. Must be paired with the \&quot;from\&quot; parameter. | 

### Return type

[**AccountLevelMerchantReport**](AccountLevelMerchantReport.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully sent the query to the database to retrieve the merchant data |  -  |
**400** | Bad request |  -  |
**500** | Internal issue connecting to the database |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant_data**
> MerchantReportData get_merchant_data(merchant_id, var_from, to)

Generates a report of full Merchant data in a given timeframe for a single Merchant

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.merchant_report_data import MerchantReportData
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
    api_instance = sparkfly_client.ReportsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    var_from = 1455197824 # int | The first reported datetime to gather data from. Must be paired with the \"to\" parameter.
    to = 1455629824 # int | The last reported datetime to gather data from. Must be paired with the \"from\" parameter.

    try:
        # Generates a report of full Merchant data in a given timeframe for a single Merchant
        api_response = api_instance.get_merchant_data(merchant_id, var_from, to)
        print("The response of ReportsApi->get_merchant_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_merchant_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **var_from** | **int**| The first reported datetime to gather data from. Must be paired with the \&quot;to\&quot; parameter. | 
 **to** | **int**| The last reported datetime to gather data from. Must be paired with the \&quot;from\&quot; parameter. | 

### Return type

[**MerchantReportData**](MerchantReportData.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully sent the query to the database to retrieve the merchant data |  -  |
**400** | Bad request |  -  |
**500** | Internal issue connecting to the database |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant_impressions**
> ImpressionsReportData get_merchant_impressions(merchant_id, var_from, to)

Get Unique Impressions

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.impressions_report_data import ImpressionsReportData
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
    api_instance = sparkfly_client.ReportsApi(api_client)
    merchant_id = 56 # int | The id of the merchant
    var_from = 1455197824 # int | The first reported datetime to gather data from. Must be paired with the \"to\" parameter.
    to = 1455629824 # int | The last reported datetime to gather data from. Must be paired with the \"from\" parameter.

    try:
        # Get Unique Impressions
        api_response = api_instance.get_merchant_impressions(merchant_id, var_from, to)
        print("The response of ReportsApi->get_merchant_impressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_merchant_impressions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The id of the merchant | 
 **var_from** | **int**| The first reported datetime to gather data from. Must be paired with the \&quot;to\&quot; parameter. | 
 **to** | **int**| The last reported datetime to gather data from. Must be paired with the \&quot;from\&quot; parameter. | 

### Return type

[**ImpressionsReportData**](ImpressionsReportData.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully sent the query to the database to retrieve the merchant data |  -  |
**400** | Bad request |  -  |
**500** | Internal issue connecting to the database |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_activity**
> List[OfferActivityReport] get_offer_activity(from_reported_datetime=from_reported_datetime, to_reported_datetime=to_reported_datetime, from_processed_datetime=from_processed_datetime, to_processed_datetime=to_processed_datetime, from_business_date=from_business_date, to_business_date=to_business_date, channel_id=channel_id, channel_name=channel_name, offer_id=offer_id, type=type, campaign_xid=campaign_xid, credential_identifier=credential_identifier)

Generates a report of all offer activity in a given timeframe

Given a timeframe of less than 30 consecutive days, this will generate a report of  all offer activities for your account. Three types of dates are accepted: reported,  processed, and business date, but only one will be used. If more than one date set  is given, it will prioritize the dates in the order given before. Some filters can  also be applied to narrow down the reports given. 

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.offer_activity_report import OfferActivityReport
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
    api_instance = sparkfly_client.ReportsApi(api_client)
    from_reported_datetime = '2017-07-21T17:32:28Z' # datetime | The first reported datetime to gather data from. Must be paired with the \"to_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day. (optional)
    to_reported_datetime = '2017-07-21T17:32:28Z' # datetime | The last reported datetime to gather data from. Must be paired with the \"from_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day. (optional)
    from_processed_datetime = '2017-07-21T17:32:28Z' # datetime | The first processed datetime to gather data from. Must be paired with the \"to_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day. (optional)
    to_processed_datetime = '2017-07-21T17:32:28Z' # datetime | The last reported datetime to gather data from. Must be paired with the \"from_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day. (optional)
    from_business_date = 'Sun Apr 11 20:00:00 EDT 2010' # date | The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day. (optional)
    to_business_date = 'Sun Apr 11 20:00:00 EDT 2010' # date | The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day. (optional)
    channel_id = 56 # int | The id of the channel. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\" (optional)
    channel_name = 'channel_name_example' # str | The name of the channel. If no channel_id is provided, the program will try to find the id by the channel name. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\" (optional)
    offer_id = 56 # int | The id of the offer. This is an optional filter. (optional)
    type = 'type_example' # str | The type of the offer. This is an optional filter. (optional)
    campaign_xid = 'campaign_xid_example' # str | The id of the campaign. This is an optional filter. (optional)
    credential_identifier = 56 # int | The identifier of the credential. This is an optional filter. (optional)

    try:
        # Generates a report of all offer activity in a given timeframe
        api_response = api_instance.get_offer_activity(from_reported_datetime=from_reported_datetime, to_reported_datetime=to_reported_datetime, from_processed_datetime=from_processed_datetime, to_processed_datetime=to_processed_datetime, from_business_date=from_business_date, to_business_date=to_business_date, channel_id=channel_id, channel_name=channel_name, offer_id=offer_id, type=type, campaign_xid=campaign_xid, credential_identifier=credential_identifier)
        print("The response of ReportsApi->get_offer_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_offer_activity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_reported_datetime** | **datetime**| The first reported datetime to gather data from. Must be paired with the \&quot;to_reported_datetime\&quot; parameter. One pair of dates must be provided in the request. The duration between the \&quot;from\&quot; and \&quot;to\&quot; dates must not exceed 1 day. | [optional] 
 **to_reported_datetime** | **datetime**| The last reported datetime to gather data from. Must be paired with the \&quot;from_reported_datetime\&quot; parameter. One pair of dates must be provided in the request. The duration between the \&quot;from\&quot; and \&quot;to\&quot; dates must not exceed 1 day. | [optional] 
 **from_processed_datetime** | **datetime**| The first processed datetime to gather data from. Must be paired with the \&quot;to_processed_datetime\&quot; parameter. One pair of dates must be provided in the request. The duration between the \&quot;from\&quot; and \&quot;to\&quot; dates must not exceed 1 day. | [optional] 
 **to_processed_datetime** | **datetime**| The last reported datetime to gather data from. Must be paired with the \&quot;from_processed_datetime\&quot; parameter. One pair of dates must be provided in the request. The duration between the \&quot;from\&quot; and \&quot;to\&quot; dates must not exceed 1 day. | [optional] 
 **from_business_date** | **date**| The first business date to gather data from. Must be paired with the \&quot;to_business_date\&quot; parameter. One pair of dates must be provided in the request. The duration between the \&quot;from\&quot; and \&quot;to\&quot; dates must not exceed 1 day. | [optional] 
 **to_business_date** | **date**| The last business date to gather data from. Must be paired with the \&quot;from_business_date\&quot; parameter. One pair of dates must be provided in the request. The duration between the \&quot;from\&quot; and \&quot;to\&quot; dates must not exceed 1 day. | [optional] 
 **channel_id** | **int**| The id of the channel. If both channel_id AND channel_name are missing, the request will return a \&quot;400 - Bad Request\&quot; | [optional] 
 **channel_name** | **str**| The name of the channel. If no channel_id is provided, the program will try to find the id by the channel name. If both channel_id AND channel_name are missing, the request will return a \&quot;400 - Bad Request\&quot; | [optional] 
 **offer_id** | **int**| The id of the offer. This is an optional filter. | [optional] 
 **type** | **str**| The type of the offer. This is an optional filter. | [optional] 
 **campaign_xid** | **str**| The id of the campaign. This is an optional filter. | [optional] 
 **credential_identifier** | **int**| The identifier of the credential. This is an optional filter. | [optional] 

### Return type

[**List[OfferActivityReport]**](OfferActivityReport.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully sent the query to the database to retrieve the offer activities. The output will be streamed as the activities are received from the database and processed. If there is an error as the output is being streamed, it will cut off at that report and it will need to be re-run. The 200 status will remain regardless. |  -  |
**400** | Bad request |  -  |
**500** | Internal issue connecting to the database |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_redemptions**
> RedemptionList1 get_offer_redemptions(from_business_date=from_business_date, to_business_date=to_business_date, from_redemption_datetime=from_redemption_datetime, to_redemption_datetime=to_redemption_datetime, bi_storelist=bi_storelist)

Generates a report of all offer redemptions for a given timeframe and store list

Given a timeframe, this will generate a report of all offer activities for your account.  Two types of dates are accepted: business date and redemption date, but only one can be used.  If more than one date set is given, an error will be returned. Some filters can  also be applied to narrow down the reports given.  

### Example

* Api Key Authentication (X-Auth-Token):
```python
import time
import os
import sparkfly_client
from sparkfly_client.models.redemption_list1 import RedemptionList1
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
    api_instance = sparkfly_client.ReportsApi(api_client)
    from_business_date = '2013-10-20T19:20:30+01:00' # datetime | The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request. (optional)
    to_business_date = '2013-10-20T19:20:30+01:00' # datetime | The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request. (optional)
    from_redemption_datetime = '2017-07-01T17:32:28Z' # datetime | The first redemption datetime to gather data from. Must be paired with the \"to_redemption_datetime\" parameter. One pair of dates must be provided in the request. (optional)
    to_redemption_datetime = '2017-07-31T17:32:28Z' # datetime | The last redemption datetime to gather data from. Must be paired with the \"from_redemption_datetime\" parameter. One pair of dates must be provided in the request. (optional)
    bi_storelist = 56 # int | The ID of the Store List. Filters the redemptions using the Stores from the given Store List. If not given, ALL Store Lists and the corresponding Stores will be used to filter the results. (optional)

    try:
        # Generates a report of all offer redemptions for a given timeframe and store list
        api_response = api_instance.get_offer_redemptions(from_business_date=from_business_date, to_business_date=to_business_date, from_redemption_datetime=from_redemption_datetime, to_redemption_datetime=to_redemption_datetime, bi_storelist=bi_storelist)
        print("The response of ReportsApi->get_offer_redemptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_offer_redemptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_business_date** | **datetime**| The first business date to gather data from. Must be paired with the \&quot;to_business_date\&quot; parameter. One pair of dates must be provided in the request. | [optional] 
 **to_business_date** | **datetime**| The last business date to gather data from. Must be paired with the \&quot;from_business_date\&quot; parameter. One pair of dates must be provided in the request. | [optional] 
 **from_redemption_datetime** | **datetime**| The first redemption datetime to gather data from. Must be paired with the \&quot;to_redemption_datetime\&quot; parameter. One pair of dates must be provided in the request. | [optional] 
 **to_redemption_datetime** | **datetime**| The last redemption datetime to gather data from. Must be paired with the \&quot;from_redemption_datetime\&quot; parameter. One pair of dates must be provided in the request. | [optional] 
 **bi_storelist** | **int**| The ID of the Store List. Filters the redemptions using the Stores from the given Store List. If not given, ALL Store Lists and the corresponding Stores will be used to filter the results. | [optional] 

### Return type

[**RedemptionList1**](RedemptionList1.md)

### Authorization

[X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully sent the query to the database to retrieve the redemptions. |  -  |
**400** | Bad request |  -  |
**422** | The request was unable to be followed due to semantic errors. |  -  |
**500** | Internal issue connecting to the database |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

