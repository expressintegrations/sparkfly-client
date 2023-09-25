# ImpressionList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**impressions** | [**List[ImpressionResponse]**](ImpressionResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.impression_list import ImpressionList

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionList from a JSON string
impression_list_instance = ImpressionList.from_json(json)
# print the JSON string representation of the object
print ImpressionList.to_json()

# convert the object into a dict
impression_list_dict = impression_list_instance.to_dict()
# create an instance of ImpressionList from a dict
impression_list_form_dict = impression_list.from_dict(impression_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


