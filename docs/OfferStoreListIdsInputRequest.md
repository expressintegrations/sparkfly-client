# OfferStoreListIdsInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferStoreListIdsInput**](OfferStoreListIdsInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_store_list_ids_input_request import OfferStoreListIdsInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStoreListIdsInputRequest from a JSON string
offer_store_list_ids_input_request_instance = OfferStoreListIdsInputRequest.from_json(json)
# print the JSON string representation of the object
print OfferStoreListIdsInputRequest.to_json()

# convert the object into a dict
offer_store_list_ids_input_request_dict = offer_store_list_ids_input_request_instance.to_dict()
# create an instance of OfferStoreListIdsInputRequest from a dict
offer_store_list_ids_input_request_form_dict = offer_store_list_ids_input_request.from_dict(offer_store_list_ids_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


