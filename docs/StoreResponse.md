# StoreResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | [**Store**](Store.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.store_response import StoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StoreResponse from a JSON string
store_response_instance = StoreResponse.from_json(json)
# print the JSON string representation of the object
print StoreResponse.to_json()

# convert the object into a dict
store_response_dict = store_response_instance.to_dict()
# create an instance of StoreResponse from a dict
store_response_form_dict = store_response.from_dict(store_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


