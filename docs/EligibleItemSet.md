# EligibleItemSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**list_type** | **int** |  | [optional] 
**type_name** | **str** |  | [optional] 
**req_qty** | **int** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**item_set_id** | **int** |  | [optional] 

## Example

```python
from sparkfly_client.models.eligible_item_set import EligibleItemSet

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleItemSet from a JSON string
eligible_item_set_instance = EligibleItemSet.from_json(json)
# print the JSON string representation of the object
print EligibleItemSet.to_json()

# convert the object into a dict
eligible_item_set_dict = eligible_item_set_instance.to_dict()
# create an instance of EligibleItemSet from a dict
eligible_item_set_form_dict = eligible_item_set.from_dict(eligible_item_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


