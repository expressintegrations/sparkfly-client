# OfferStateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activates_at** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_state_input import OfferStateInput

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateInput from a JSON string
offer_state_input_instance = OfferStateInput.from_json(json)
# print the JSON string representation of the object
print OfferStateInput.to_json()

# convert the object into a dict
offer_state_input_dict = offer_state_input_instance.to_dict()
# create an instance of OfferStateInput from a dict
offer_state_input_form_dict = offer_state_input.from_dict(offer_state_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


