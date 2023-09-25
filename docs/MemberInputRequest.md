# MemberInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MemberInput**](MemberInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.member_input_request import MemberInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberInputRequest from a JSON string
member_input_request_instance = MemberInputRequest.from_json(json)
# print the JSON string representation of the object
print MemberInputRequest.to_json()

# convert the object into a dict
member_input_request_dict = member_input_request_instance.to_dict()
# create an instance of MemberInputRequest from a dict
member_input_request_form_dict = member_input_request.from_dict(member_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


