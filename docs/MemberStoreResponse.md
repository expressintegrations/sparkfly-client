# MemberStoreResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | [**MemberStore**](MemberStore.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.member_store_response import MemberStoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberStoreResponse from a JSON string
member_store_response_instance = MemberStoreResponse.from_json(json)
# print the JSON string representation of the object
print MemberStoreResponse.to_json()

# convert the object into a dict
member_store_response_dict = member_store_response_instance.to_dict()
# create an instance of MemberStoreResponse from a dict
member_store_response_form_dict = member_store_response.from_dict(member_store_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


