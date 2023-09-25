# MemberListInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_list** | [**MemberListInput**](MemberListInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.member_list_input_request import MemberListInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberListInputRequest from a JSON string
member_list_input_request_instance = MemberListInputRequest.from_json(json)
# print the JSON string representation of the object
print MemberListInputRequest.to_json()

# convert the object into a dict
member_list_input_request_dict = member_list_input_request_instance.to_dict()
# create an instance of MemberListInputRequest from a dict
member_list_input_request_form_dict = member_list_input_request.from_dict(member_list_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


