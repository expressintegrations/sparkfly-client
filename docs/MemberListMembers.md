# MemberListMembers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**member_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.member_list_members import MemberListMembers

# TODO update the JSON string below
json = "{}"
# create an instance of MemberListMembers from a JSON string
member_list_members_instance = MemberListMembers.from_json(json)
# print the JSON string representation of the object
print MemberListMembers.to_json()

# convert the object into a dict
member_list_members_dict = member_list_members_instance.to_dict()
# create an instance of MemberListMembers from a dict
member_list_members_form_dict = member_list_members.from_dict(member_list_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


