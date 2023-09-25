# Manufacturer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**location** | [**ManufacturerLocation**](ManufacturerLocation.md) |  | [optional] 
**contacts** | [**Contacts**](Contacts.md) |  | [optional] 
**merchant_ids** | **List[int]** |  | [optional] 
**merchants** | [**List[MerchantResponse]**](MerchantResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.manufacturer import Manufacturer

# TODO update the JSON string below
json = "{}"
# create an instance of Manufacturer from a JSON string
manufacturer_instance = Manufacturer.from_json(json)
# print the JSON string representation of the object
print Manufacturer.to_json()

# convert the object into a dict
manufacturer_dict = manufacturer_instance.to_dict()
# create an instance of Manufacturer from a dict
manufacturer_form_dict = manufacturer.from_dict(manufacturer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


