# OfferStateInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state** | [**OfferStateInput**](OfferStateInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_state_input_request import OfferStateInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateInputRequest from a JSON string
offer_state_input_request_instance = OfferStateInputRequest.from_json(json)
# print the JSON string representation of the object
print OfferStateInputRequest.to_json()

# convert the object into a dict
offer_state_input_request_dict = offer_state_input_request_instance.to_dict()
# create an instance of OfferStateInputRequest from a dict
offer_state_input_request_form_dict = offer_state_input_request.from_dict(offer_state_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


