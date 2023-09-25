# MemberExportData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**ExportMember**](ExportMember.md) |  | [optional] 
**credentials** | [**List[ExportCredential]**](ExportCredential.md) |  | [optional] 
**offer_activities** | [**List[OfferActivity]**](OfferActivity.md) |  | [optional] 
**transactions** | [**List[Transaction]**](Transaction.md) |  | [optional] 
**impressions** | [**List[Impression]**](Impression.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.member_export_data import MemberExportData

# TODO update the JSON string below
json = "{}"
# create an instance of MemberExportData from a JSON string
member_export_data_instance = MemberExportData.from_json(json)
# print the JSON string representation of the object
print MemberExportData.to_json()

# convert the object into a dict
member_export_data_dict = member_export_data_instance.to_dict()
# create an instance of MemberExportData from a dict
member_export_data_form_dict = member_export_data.from_dict(member_export_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


