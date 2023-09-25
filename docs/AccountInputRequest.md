# AccountInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**AccountInput**](AccountInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.account_input_request import AccountInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInputRequest from a JSON string
account_input_request_instance = AccountInputRequest.from_json(json)
# print the JSON string representation of the object
print AccountInputRequest.to_json()

# convert the object into a dict
account_input_request_dict = account_input_request_instance.to_dict()
# create an instance of AccountInputRequest from a dict
account_input_request_form_dict = account_input_request.from_dict(account_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


