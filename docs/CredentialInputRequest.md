# CredentialInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**CredentialInput**](CredentialInput.md) |  | [optional] 
**printable** | **bool** |  | [optional] 

## Example

```python
from sparkfly_client.models.credential_input_request import CredentialInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialInputRequest from a JSON string
credential_input_request_instance = CredentialInputRequest.from_json(json)
# print the JSON string representation of the object
print CredentialInputRequest.to_json()

# convert the object into a dict
credential_input_request_dict = credential_input_request_instance.to_dict()
# create an instance of CredentialInputRequest from a dict
credential_input_request_form_dict = credential_input_request.from_dict(credential_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


