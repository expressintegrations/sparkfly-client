# OfferMerchantIdsInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_merchant_ids_input import OfferMerchantIdsInput

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMerchantIdsInput from a JSON string
offer_merchant_ids_input_instance = OfferMerchantIdsInput.from_json(json)
# print the JSON string representation of the object
print OfferMerchantIdsInput.to_json()

# convert the object into a dict
offer_merchant_ids_input_dict = offer_merchant_ids_input_instance.to_dict()
# create an instance of OfferMerchantIdsInput from a dict
offer_merchant_ids_input_form_dict = offer_merchant_ids_input.from_dict(offer_merchant_ids_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


