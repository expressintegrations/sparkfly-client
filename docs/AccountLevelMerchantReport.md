# AccountLevelMerchantReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MerchantReport]**](MerchantReport.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.account_level_merchant_report import AccountLevelMerchantReport

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLevelMerchantReport from a JSON string
account_level_merchant_report_instance = AccountLevelMerchantReport.from_json(json)
# print the JSON string representation of the object
print AccountLevelMerchantReport.to_json()

# convert the object into a dict
account_level_merchant_report_dict = account_level_merchant_report_instance.to_dict()
# create an instance of AccountLevelMerchantReport from a dict
account_level_merchant_report_form_dict = account_level_merchant_report.from_dict(account_level_merchant_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


