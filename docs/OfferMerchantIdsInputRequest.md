# OfferMerchantIdsInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferMerchantIdsInput**](OfferMerchantIdsInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_merchant_ids_input_request import OfferMerchantIdsInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMerchantIdsInputRequest from a JSON string
offer_merchant_ids_input_request_instance = OfferMerchantIdsInputRequest.from_json(json)
# print the JSON string representation of the object
print OfferMerchantIdsInputRequest.to_json()

# convert the object into a dict
offer_merchant_ids_input_request_dict = offer_merchant_ids_input_request_instance.to_dict()
# create an instance of OfferMerchantIdsInputRequest from a dict
offer_merchant_ids_input_request_form_dict = offer_merchant_ids_input_request.from_dict(offer_merchant_ids_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


