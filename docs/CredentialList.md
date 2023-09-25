# CredentialList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**credentials** | [**List[CredentialResponse]**](CredentialResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.credential_list import CredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialList from a JSON string
credential_list_instance = CredentialList.from_json(json)
# print the JSON string representation of the object
print CredentialList.to_json()

# convert the object into a dict
credential_list_dict = credential_list_instance.to_dict()
# create an instance of CredentialList from a dict
credential_list_form_dict = credential_list.from_dict(credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


