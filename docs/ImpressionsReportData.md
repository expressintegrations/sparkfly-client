# ImpressionsReportData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ImpressionsReport]**](ImpressionsReport.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.impressions_report_data import ImpressionsReportData

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionsReportData from a JSON string
impressions_report_data_instance = ImpressionsReportData.from_json(json)
# print the JSON string representation of the object
print ImpressionsReportData.to_json()

# convert the object into a dict
impressions_report_data_dict = impressions_report_data_instance.to_dict()
# create an instance of ImpressionsReportData from a dict
impressions_report_data_form_dict = impressions_report_data.from_dict(impressions_report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


