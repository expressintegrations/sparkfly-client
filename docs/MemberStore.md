# MemberStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**total_check_ins** | **int** |  | [optional] 
**can_check_in** | **bool** |  | [optional] 

## Example

```python
from sparkfly_client.models.member_store import MemberStore

# TODO update the JSON string below
json = "{}"
# create an instance of MemberStore from a JSON string
member_store_instance = MemberStore.from_json(json)
# print the JSON string representation of the object
print MemberStore.to_json()

# convert the object into a dict
member_store_dict = member_store_instance.to_dict()
# create an instance of MemberStore from a dict
member_store_form_dict = member_store.from_dict(member_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


