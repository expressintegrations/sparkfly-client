# StoreListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**stores** | [**List[StoreResponse]**](StoreResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.store_list_response import StoreListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StoreListResponse from a JSON string
store_list_response_instance = StoreListResponse.from_json(json)
# print the JSON string representation of the object
print StoreListResponse.to_json()

# convert the object into a dict
store_list_response_dict = store_list_response_instance.to_dict()
# create an instance of StoreListResponse from a dict
store_list_response_form_dict = store_list_response.from_dict(store_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


