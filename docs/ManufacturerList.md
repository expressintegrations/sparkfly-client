# ManufacturerList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**manufacturers** | [**List[ManufacturerResponse]**](ManufacturerResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.manufacturer_list import ManufacturerList

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerList from a JSON string
manufacturer_list_instance = ManufacturerList.from_json(json)
# print the JSON string representation of the object
print ManufacturerList.to_json()

# convert the object into a dict
manufacturer_list_dict = manufacturer_list_instance.to_dict()
# create an instance of ManufacturerList from a dict
manufacturer_list_form_dict = manufacturer_list.from_dict(manufacturer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


