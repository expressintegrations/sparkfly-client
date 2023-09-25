# MemberListList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**member_lists** | [**List[MemberListObjectResponse]**](MemberListObjectResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.member_list_list import MemberListList

# TODO update the JSON string below
json = "{}"
# create an instance of MemberListList from a JSON string
member_list_list_instance = MemberListList.from_json(json)
# print the JSON string representation of the object
print MemberListList.to_json()

# convert the object into a dict
member_list_list_dict = member_list_list_instance.to_dict()
# create an instance of MemberListList from a dict
member_list_list_form_dict = member_list_list.from_dict(member_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


