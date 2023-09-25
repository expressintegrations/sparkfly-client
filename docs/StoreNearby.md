# StoreNearby


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **str** |  | [optional] 
**lng** | **str** |  | [optional] 
**distance** | **int** |  | [optional] 

## Example

```python
from sparkfly_client.models.store_nearby import StoreNearby

# TODO update the JSON string below
json = "{}"
# create an instance of StoreNearby from a JSON string
store_nearby_instance = StoreNearby.from_json(json)
# print the JSON string representation of the object
print StoreNearby.to_json()

# convert the object into a dict
store_nearby_dict = store_nearby_instance.to_dict()
# create an instance of StoreNearby from a dict
store_nearby_form_dict = store_nearby.from_dict(store_nearby_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


