# OfferStateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state** | [**OfferState**](OfferState.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_state_response import OfferStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateResponse from a JSON string
offer_state_response_instance = OfferStateResponse.from_json(json)
# print the JSON string representation of the object
print OfferStateResponse.to_json()

# convert the object into a dict
offer_state_response_dict = offer_state_response_instance.to_dict()
# create an instance of OfferStateResponse from a dict
offer_state_response_form_dict = offer_state_response.from_dict(offer_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


