# OfferStoreListsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferStoreLists**](OfferStoreLists.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_store_lists_response import OfferStoreListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStoreListsResponse from a JSON string
offer_store_lists_response_instance = OfferStoreListsResponse.from_json(json)
# print the JSON string representation of the object
print OfferStoreListsResponse.to_json()

# convert the object into a dict
offer_store_lists_response_dict = offer_store_lists_response_instance.to_dict()
# create an instance of OfferStoreListsResponse from a dict
offer_store_lists_response_form_dict = offer_store_lists_response.from_dict(offer_store_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


