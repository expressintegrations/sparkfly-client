# ItemSetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_set** | [**ItemSet**](ItemSet.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.item_set_response import ItemSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSetResponse from a JSON string
item_set_response_instance = ItemSetResponse.from_json(json)
# print the JSON string representation of the object
print ItemSetResponse.to_json()

# convert the object into a dict
item_set_response_dict = item_set_response_instance.to_dict()
# create an instance of ItemSetResponse from a dict
item_set_response_form_dict = item_set_response.from_dict(item_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


