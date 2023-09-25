# StoreInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**number** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**primary** | [**Contact**](Contact.md) |  | [optional] 
**secondary** | [**Contact**](Contact.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.store_input import StoreInput

# TODO update the JSON string below
json = "{}"
# create an instance of StoreInput from a JSON string
store_input_instance = StoreInput.from_json(json)
# print the JSON string representation of the object
print StoreInput.to_json()

# convert the object into a dict
store_input_dict = store_input_instance.to_dict()
# create an instance of StoreInput from a dict
store_input_form_dict = store_input.from_dict(store_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


