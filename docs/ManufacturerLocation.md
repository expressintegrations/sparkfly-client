# ManufacturerLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**lat** | **str** |  | [optional] 
**lng** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.manufacturer_location import ManufacturerLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerLocation from a JSON string
manufacturer_location_instance = ManufacturerLocation.from_json(json)
# print the JSON string representation of the object
print ManufacturerLocation.to_json()

# convert the object into a dict
manufacturer_location_dict = manufacturer_location_instance.to_dict()
# create an instance of ManufacturerLocation from a dict
manufacturer_location_form_dict = manufacturer_location.from_dict(manufacturer_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


