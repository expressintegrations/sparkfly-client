# ItemListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**stores** | [**List[ItemResponse]**](ItemResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.item_list_response import ItemListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ItemListResponse from a JSON string
item_list_response_instance = ItemListResponse.from_json(json)
# print the JSON string representation of the object
print ItemListResponse.to_json()

# convert the object into a dict
item_list_response_dict = item_list_response_instance.to_dict()
# create an instance of ItemListResponse from a dict
item_list_response_form_dict = item_list_response.from_dict(item_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


