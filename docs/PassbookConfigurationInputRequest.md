# PassbookConfigurationInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passbook_configuration** | [**PassbookConfigurationInput**](PassbookConfigurationInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.passbook_configuration_input_request import PassbookConfigurationInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PassbookConfigurationInputRequest from a JSON string
passbook_configuration_input_request_instance = PassbookConfigurationInputRequest.from_json(json)
# print the JSON string representation of the object
print PassbookConfigurationInputRequest.to_json()

# convert the object into a dict
passbook_configuration_input_request_dict = passbook_configuration_input_request_instance.to_dict()
# create an instance of PassbookConfigurationInputRequest from a dict
passbook_configuration_input_request_form_dict = passbook_configuration_input_request.from_dict(passbook_configuration_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


