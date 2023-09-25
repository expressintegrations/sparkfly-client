# MemberListObjectResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_list** | [**MemberListObject**](MemberListObject.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.member_list_object_response import MemberListObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberListObjectResponse from a JSON string
member_list_object_response_instance = MemberListObjectResponse.from_json(json)
# print the JSON string representation of the object
print MemberListObjectResponse.to_json()

# convert the object into a dict
member_list_object_response_dict = member_list_object_response_instance.to_dict()
# create an instance of MemberListObjectResponse from a dict
member_list_object_response_form_dict = member_list_object_response.from_dict(member_list_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


