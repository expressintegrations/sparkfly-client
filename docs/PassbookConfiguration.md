# PassbookConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**p12_certificate** | **str** |  | [optional] 
**p12_password** | **str** |  | [optional] 
**pass_type_id_name** | **str** |  | [optional] 
**serial_number** | **int** |  | [optional] 
**team_identifier** | **str** |  | [optional] 
**bg_color** | **str** |  | [optional] 
**fg_color** | **str** |  | [optional] 
**label_color** | **str** |  | [optional] 
**bg_image** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.passbook_configuration import PassbookConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PassbookConfiguration from a JSON string
passbook_configuration_instance = PassbookConfiguration.from_json(json)
# print the JSON string representation of the object
print PassbookConfiguration.to_json()

# convert the object into a dict
passbook_configuration_dict = passbook_configuration_instance.to_dict()
# create an instance of PassbookConfiguration from a dict
passbook_configuration_form_dict = passbook_configuration.from_dict(passbook_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


