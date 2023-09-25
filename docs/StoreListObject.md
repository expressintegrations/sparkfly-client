# StoreListObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**merchant_id** | **int** |  | [optional] 
**store_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.store_list_object import StoreListObject

# TODO update the JSON string below
json = "{}"
# create an instance of StoreListObject from a JSON string
store_list_object_instance = StoreListObject.from_json(json)
# print the JSON string representation of the object
print StoreListObject.to_json()

# convert the object into a dict
store_list_object_dict = store_list_object_instance.to_dict()
# create an instance of StoreListObject from a dict
store_list_object_form_dict = store_list_object.from_dict(store_list_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


