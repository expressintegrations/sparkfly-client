# ImpressionsReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**ImpressionsReportData1**](ImpressionsReportData1.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.impressions_report import ImpressionsReport

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionsReport from a JSON string
impressions_report_instance = ImpressionsReport.from_json(json)
# print the JSON string representation of the object
print ImpressionsReport.to_json()

# convert the object into a dict
impressions_report_dict = impressions_report_instance.to_dict()
# create an instance of ImpressionsReport from a dict
impressions_report_form_dict = impressions_report.from_dict(impressions_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


