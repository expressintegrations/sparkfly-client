# MemberInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**notification_mode** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.member_input import MemberInput

# TODO update the JSON string below
json = "{}"
# create an instance of MemberInput from a JSON string
member_input_instance = MemberInput.from_json(json)
# print the JSON string representation of the object
print MemberInput.to_json()

# convert the object into a dict
member_input_dict = member_input_instance.to_dict()
# create an instance of MemberInput from a dict
member_input_form_dict = member_input.from_dict(member_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


