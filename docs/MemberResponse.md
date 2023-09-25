# MemberResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**Member**](Member.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.member_response import MemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberResponse from a JSON string
member_response_instance = MemberResponse.from_json(json)
# print the JSON string representation of the object
print MemberResponse.to_json()

# convert the object into a dict
member_response_dict = member_response_instance.to_dict()
# create an instance of MemberResponse from a dict
member_response_form_dict = member_response.from_dict(member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


