# ZIdentifierResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | [**ZIdentifier**](ZIdentifier.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.z_identifier_response import ZIdentifierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ZIdentifierResponse from a JSON string
z_identifier_response_instance = ZIdentifierResponse.from_json(json)
# print the JSON string representation of the object
print ZIdentifierResponse.to_json()

# convert the object into a dict
z_identifier_response_dict = z_identifier_response_instance.to_dict()
# create an instance of ZIdentifierResponse from a dict
z_identifier_response_form_dict = z_identifier_response.from_dict(z_identifier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


