# StoreInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | [**StoreInput**](StoreInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.store_input_request import StoreInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoreInputRequest from a JSON string
store_input_request_instance = StoreInputRequest.from_json(json)
# print the JSON string representation of the object
print StoreInputRequest.to_json()

# convert the object into a dict
store_input_request_dict = store_input_request_instance.to_dict()
# create an instance of StoreInputRequest from a dict
store_input_request_form_dict = store_input_request.from_dict(store_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


