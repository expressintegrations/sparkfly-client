# Store


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**phone** | **str** |  | [optional] 
**location** | [**StoreLocation**](StoreLocation.md) |  | [optional] 
**contacts** | [**Contacts**](Contacts.md) |  | [optional] 
**merchant_id** | **int** |  | [optional] 
**nearby** | [**StoreNearby**](StoreNearby.md) |  | [optional] 
**icon_url** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.store import Store

# TODO update the JSON string below
json = "{}"
# create an instance of Store from a JSON string
store_instance = Store.from_json(json)
# print the JSON string representation of the object
print Store.to_json()

# convert the object into a dict
store_dict = store_instance.to_dict()
# create an instance of Store from a dict
store_form_dict = store.from_dict(store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


