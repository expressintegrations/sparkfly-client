# MemberListMemberIdsInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.member_list_member_ids_input import MemberListMemberIdsInput

# TODO update the JSON string below
json = "{}"
# create an instance of MemberListMemberIdsInput from a JSON string
member_list_member_ids_input_instance = MemberListMemberIdsInput.from_json(json)
# print the JSON string representation of the object
print MemberListMemberIdsInput.to_json()

# convert the object into a dict
member_list_member_ids_input_dict = member_list_member_ids_input_instance.to_dict()
# create an instance of MemberListMemberIdsInput from a dict
member_list_member_ids_input_form_dict = member_list_member_ids_input.from_dict(member_list_member_ids_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


