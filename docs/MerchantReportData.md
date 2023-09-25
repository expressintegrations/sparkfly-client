# MerchantReportData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MerchantReport]**](MerchantReport.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.merchant_report_data import MerchantReportData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantReportData from a JSON string
merchant_report_data_instance = MerchantReportData.from_json(json)
# print the JSON string representation of the object
print MerchantReportData.to_json()

# convert the object into a dict
merchant_report_data_dict = merchant_report_data_instance.to_dict()
# create an instance of MerchantReportData from a dict
merchant_report_data_form_dict = merchant_report_data.from_dict(merchant_report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


