# StoreListObjectResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_list** | [**StoreListObject**](StoreListObject.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.store_list_object_response import StoreListObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StoreListObjectResponse from a JSON string
store_list_object_response_instance = StoreListObjectResponse.from_json(json)
# print the JSON string representation of the object
print StoreListObjectResponse.to_json()

# convert the object into a dict
store_list_object_response_dict = store_list_object_response_instance.to_dict()
# create an instance of StoreListObjectResponse from a dict
store_list_object_response_form_dict = store_list_object_response.from_dict(store_list_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


