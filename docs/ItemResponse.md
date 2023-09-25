# ItemResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**Item**](Item.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.item_response import ItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ItemResponse from a JSON string
item_response_instance = ItemResponse.from_json(json)
# print the JSON string representation of the object
print ItemResponse.to_json()

# convert the object into a dict
item_response_dict = item_response_instance.to_dict()
# create an instance of ItemResponse from a dict
item_response_form_dict = item_response.from_dict(item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


