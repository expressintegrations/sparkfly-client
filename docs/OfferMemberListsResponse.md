# OfferMemberListsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferMemberLists**](OfferMemberLists.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_member_lists_response import OfferMemberListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMemberListsResponse from a JSON string
offer_member_lists_response_instance = OfferMemberListsResponse.from_json(json)
# print the JSON string representation of the object
print OfferMemberListsResponse.to_json()

# convert the object into a dict
offer_member_lists_response_dict = offer_member_lists_response_instance.to_dict()
# create an instance of OfferMemberListsResponse from a dict
offer_member_lists_response_form_dict = offer_member_lists_response.from_dict(offer_member_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


