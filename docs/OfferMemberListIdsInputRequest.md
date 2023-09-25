# OfferMemberListIdsInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferMemberListIdsInput**](OfferMemberListIdsInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_member_list_ids_input_request import OfferMemberListIdsInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMemberListIdsInputRequest from a JSON string
offer_member_list_ids_input_request_instance = OfferMemberListIdsInputRequest.from_json(json)
# print the JSON string representation of the object
print OfferMemberListIdsInputRequest.to_json()

# convert the object into a dict
offer_member_list_ids_input_request_dict = offer_member_list_ids_input_request_instance.to_dict()
# create an instance of OfferMemberListIdsInputRequest from a dict
offer_member_list_ids_input_request_form_dict = offer_member_list_ids_input_request.from_dict(offer_member_list_ids_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


