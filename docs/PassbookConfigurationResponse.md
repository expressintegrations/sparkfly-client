# PassbookConfigurationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passbook_configuration** | [**PassbookConfiguration**](PassbookConfiguration.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.passbook_configuration_response import PassbookConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PassbookConfigurationResponse from a JSON string
passbook_configuration_response_instance = PassbookConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print PassbookConfigurationResponse.to_json()

# convert the object into a dict
passbook_configuration_response_dict = passbook_configuration_response_instance.to_dict()
# create an instance of PassbookConfigurationResponse from a dict
passbook_configuration_response_form_dict = passbook_configuration_response.from_dict(passbook_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


