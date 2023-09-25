# ManufacturerInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**billing_arrangement** | **str** |  | [optional] 
**redemption_identifier_type** | **str** |  | [optional] 
**primary** | [**Contact**](Contact.md) |  | [optional] 
**secondary** | [**Contact**](Contact.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.manufacturer_input import ManufacturerInput

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerInput from a JSON string
manufacturer_input_instance = ManufacturerInput.from_json(json)
# print the JSON string representation of the object
print ManufacturerInput.to_json()

# convert the object into a dict
manufacturer_input_dict = manufacturer_input_instance.to_dict()
# create an instance of ManufacturerInput from a dict
manufacturer_input_form_dict = manufacturer_input.from_dict(manufacturer_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


