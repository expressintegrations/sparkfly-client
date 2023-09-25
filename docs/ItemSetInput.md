# ItemSetInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**merchant_id** | **int** |  | [optional] 
**manufacturer_id** | **int** |  | [optional] 
**item_ids** | **List[int]** |  | [optional] 
**set_type** | **int** |  | [optional] 

## Example

```python
from sparkfly_client.models.item_set_input import ItemSetInput

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSetInput from a JSON string
item_set_input_instance = ItemSetInput.from_json(json)
# print the JSON string representation of the object
print ItemSetInput.to_json()

# convert the object into a dict
item_set_input_dict = item_set_input_instance.to_dict()
# create an instance of ItemSetInput from a dict
item_set_input_form_dict = item_set_input.from_dict(item_set_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


