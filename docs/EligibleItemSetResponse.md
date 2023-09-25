# EligibleItemSetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible_item_set** | [**EligibleItemSet**](EligibleItemSet.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.eligible_item_set_response import EligibleItemSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleItemSetResponse from a JSON string
eligible_item_set_response_instance = EligibleItemSetResponse.from_json(json)
# print the JSON string representation of the object
print EligibleItemSetResponse.to_json()

# convert the object into a dict
eligible_item_set_response_dict = eligible_item_set_response_instance.to_dict()
# create an instance of EligibleItemSetResponse from a dict
eligible_item_set_response_form_dict = eligible_item_set_response.from_dict(eligible_item_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


