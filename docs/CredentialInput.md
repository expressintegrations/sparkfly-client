# CredentialInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **int** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**store_id** | **int** |  | [optional] 
**reusable** | **bool** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.credential_input import CredentialInput

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialInput from a JSON string
credential_input_instance = CredentialInput.from_json(json)
# print the JSON string representation of the object
print CredentialInput.to_json()

# convert the object into a dict
credential_input_dict = credential_input_instance.to_dict()
# create an instance of CredentialInput from a dict
credential_input_form_dict = credential_input.from_dict(credential_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


