# ItemSetInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_set** | [**ItemSetInput**](ItemSetInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.item_set_input_request import ItemSetInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSetInputRequest from a JSON string
item_set_input_request_instance = ItemSetInputRequest.from_json(json)
# print the JSON string representation of the object
print ItemSetInputRequest.to_json()

# convert the object into a dict
item_set_input_request_dict = item_set_input_request_instance.to_dict()
# create an instance of ItemSetInputRequest from a dict
item_set_input_request_form_dict = item_set_input_request.from_dict(item_set_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


