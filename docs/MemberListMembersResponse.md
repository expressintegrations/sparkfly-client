# MemberListMembersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_list** | [**MemberListMembers**](MemberListMembers.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.member_list_members_response import MemberListMembersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberListMembersResponse from a JSON string
member_list_members_response_instance = MemberListMembersResponse.from_json(json)
# print the JSON string representation of the object
print MemberListMembersResponse.to_json()

# convert the object into a dict
member_list_members_response_dict = member_list_members_response_instance.to_dict()
# create an instance of MemberListMembersResponse from a dict
member_list_members_response_form_dict = member_list_members_response.from_dict(member_list_members_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


