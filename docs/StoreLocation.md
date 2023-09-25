# StoreLocation


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
from sparkfly_client.models.store_location import StoreLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StoreLocation from a JSON string
store_location_instance = StoreLocation.from_json(json)
# print the JSON string representation of the object
print StoreLocation.to_json()

# convert the object into a dict
store_location_dict = store_location_instance.to_dict()
# create an instance of StoreLocation from a dict
store_location_form_dict = store_location.from_dict(store_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


