# StoreListInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_list** | [**StoreListInput**](StoreListInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.store_list_input_request import StoreListInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoreListInputRequest from a JSON string
store_list_input_request_instance = StoreListInputRequest.from_json(json)
# print the JSON string representation of the object
print StoreListInputRequest.to_json()

# convert the object into a dict
store_list_input_request_dict = store_list_input_request_instance.to_dict()
# create an instance of StoreListInputRequest from a dict
store_list_input_request_form_dict = store_list_input_request.from_dict(store_list_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


