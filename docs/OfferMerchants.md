# OfferMerchants


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_merchants import OfferMerchants

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMerchants from a JSON string
offer_merchants_instance = OfferMerchants.from_json(json)
# print the JSON string representation of the object
print OfferMerchants.to_json()

# convert the object into a dict
offer_merchants_dict = offer_merchants_instance.to_dict()
# create an instance of OfferMerchants from a dict
offer_merchants_form_dict = offer_merchants.from_dict(offer_merchants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


