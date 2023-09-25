# ItemSetList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**item_sets** | [**List[ItemSetResponse]**](ItemSetResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.item_set_list import ItemSetList

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSetList from a JSON string
item_set_list_instance = ItemSetList.from_json(json)
# print the JSON string representation of the object
print ItemSetList.to_json()

# convert the object into a dict
item_set_list_dict = item_set_list_instance.to_dict()
# create an instance of ItemSetList from a dict
item_set_list_form_dict = item_set_list.from_dict(item_set_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


