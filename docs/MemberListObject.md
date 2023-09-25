# MemberListObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**member_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.member_list_object import MemberListObject

# TODO update the JSON string below
json = "{}"
# create an instance of MemberListObject from a JSON string
member_list_object_instance = MemberListObject.from_json(json)
# print the JSON string representation of the object
print MemberListObject.to_json()

# convert the object into a dict
member_list_object_dict = member_list_object_instance.to_dict()
# create an instance of MemberListObject from a dict
member_list_object_form_dict = member_list_object.from_dict(member_list_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


