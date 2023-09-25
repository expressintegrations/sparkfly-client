# OfferSimplifiedResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferSimplified**](OfferSimplified.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_simplified_response import OfferSimplifiedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferSimplifiedResponse from a JSON string
offer_simplified_response_instance = OfferSimplifiedResponse.from_json(json)
# print the JSON string representation of the object
print OfferSimplifiedResponse.to_json()

# convert the object into a dict
offer_simplified_response_dict = offer_simplified_response_instance.to_dict()
# create an instance of OfferSimplifiedResponse from a dict
offer_simplified_response_form_dict = offer_simplified_response.from_dict(offer_simplified_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


