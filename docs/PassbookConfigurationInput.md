# PassbookConfigurationInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**p12_certificate** | **str** |  | [optional] 
**p12_password** | **str** |  | [optional] 
**team_identifier** | **str** |  | [optional] 
**pass_type_id_name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.passbook_configuration_input import PassbookConfigurationInput

# TODO update the JSON string below
json = "{}"
# create an instance of PassbookConfigurationInput from a JSON string
passbook_configuration_input_instance = PassbookConfigurationInput.from_json(json)
# print the JSON string representation of the object
print PassbookConfigurationInput.to_json()

# convert the object into a dict
passbook_configuration_input_dict = passbook_configuration_input_instance.to_dict()
# create an instance of PassbookConfigurationInput from a dict
passbook_configuration_input_form_dict = passbook_configuration_input.from_dict(passbook_configuration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


