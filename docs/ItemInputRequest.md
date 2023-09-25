# ItemInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**ItemInput**](ItemInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.item_input_request import ItemInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ItemInputRequest from a JSON string
item_input_request_instance = ItemInputRequest.from_json(json)
# print the JSON string representation of the object
print ItemInputRequest.to_json()

# convert the object into a dict
item_input_request_dict = item_input_request_instance.to_dict()
# create an instance of ItemInputRequest from a dict
item_input_request_form_dict = item_input_request.from_dict(item_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


