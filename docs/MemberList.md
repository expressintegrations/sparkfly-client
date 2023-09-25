# MemberList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**members** | [**List[MemberResponse]**](MemberResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.member_list import MemberList

# TODO update the JSON string below
json = "{}"
# create an instance of MemberList from a JSON string
member_list_instance = MemberList.from_json(json)
# print the JSON string representation of the object
print MemberList.to_json()

# convert the object into a dict
member_list_dict = member_list_instance.to_dict()
# create an instance of MemberList from a dict
member_list_form_dict = member_list.from_dict(member_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


