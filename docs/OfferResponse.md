# OfferResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**Offer**](Offer.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_response import OfferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponse from a JSON string
offer_response_instance = OfferResponse.from_json(json)
# print the JSON string representation of the object
print OfferResponse.to_json()

# convert the object into a dict
offer_response_dict = offer_response_instance.to_dict()
# create an instance of OfferResponse from a dict
offer_response_form_dict = offer_response.from_dict(offer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


