# EligibleItemSetInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_set_id** | **int** |  | [optional] 
**list_type** | **int** |  | [optional] 
**req_qty** | **int** |  | [optional] 

## Example

```python
from sparkfly_client.models.eligible_item_set_input import EligibleItemSetInput

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleItemSetInput from a JSON string
eligible_item_set_input_instance = EligibleItemSetInput.from_json(json)
# print the JSON string representation of the object
print EligibleItemSetInput.to_json()

# convert the object into a dict
eligible_item_set_input_dict = eligible_item_set_input_instance.to_dict()
# create an instance of EligibleItemSetInput from a dict
eligible_item_set_input_form_dict = eligible_item_set_input.from_dict(eligible_item_set_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


