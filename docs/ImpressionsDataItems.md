# ImpressionsDataItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_items** | **List[List[List[str]]]** |  | [optional] 
**series** | [**List[ImpressionsSeriesItems]**](ImpressionsSeriesItems.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.impressions_data_items import ImpressionsDataItems

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionsDataItems from a JSON string
impressions_data_items_instance = ImpressionsDataItems.from_json(json)
# print the JSON string representation of the object
print ImpressionsDataItems.to_json()

# convert the object into a dict
impressions_data_items_dict = impressions_data_items_instance.to_dict()
# create an instance of ImpressionsDataItems from a dict
impressions_data_items_form_dict = impressions_data_items.from_dict(impressions_data_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


