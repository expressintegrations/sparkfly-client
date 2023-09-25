# OfferMerchantsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferMerchants**](OfferMerchants.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_merchants_response import OfferMerchantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMerchantsResponse from a JSON string
offer_merchants_response_instance = OfferMerchantsResponse.from_json(json)
# print the JSON string representation of the object
print OfferMerchantsResponse.to_json()

# convert the object into a dict
offer_merchants_response_dict = offer_merchants_response_instance.to_dict()
# create an instance of OfferMerchantsResponse from a dict
offer_merchants_response_form_dict = offer_merchants_response.from_dict(offer_merchants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


