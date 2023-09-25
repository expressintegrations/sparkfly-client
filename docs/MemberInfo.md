# MemberInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.member_info import MemberInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MemberInfo from a JSON string
member_info_instance = MemberInfo.from_json(json)
# print the JSON string representation of the object
print MemberInfo.to_json()

# convert the object into a dict
member_info_dict = member_info_instance.to_dict()
# create an instance of MemberInfo from a dict
member_info_form_dict = member_info.from_dict(member_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


