# CredentialResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**Credential**](Credential.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.credential_response import CredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialResponse from a JSON string
credential_response_instance = CredentialResponse.from_json(json)
# print the JSON string representation of the object
print CredentialResponse.to_json()

# convert the object into a dict
credential_response_dict = credential_response_instance.to_dict()
# create an instance of CredentialResponse from a dict
credential_response_form_dict = credential_response.from_dict(credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


