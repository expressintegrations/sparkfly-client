# OfferState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state_id** | **int** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**member_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**value** | **int** |  | [optional] 
**offer_name** | **str** |  | [optional] 
**offer_description** | **str** |  | [optional] 
**offer_terms_and_conditions** | **str** |  | [optional] 
**offer_web_image_url** | **str** |  | [optional] 
**offer_web_thumb_url** | **str** |  | [optional] 
**offer_mobile_image_url** | **str** |  | [optional] 
**offer_mobile_thumb_url** | **str** |  | [optional] 
**credential_identifier** | **str** |  | [optional] 
**offer_value_required** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**is_reward** | **bool** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 
**activates_at** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**transferable** | **bool** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_state import OfferState

# TODO update the JSON string below
json = "{}"
# create an instance of OfferState from a JSON string
offer_state_instance = OfferState.from_json(json)
# print the JSON string representation of the object
print OfferState.to_json()

# convert the object into a dict
offer_state_dict = offer_state_instance.to_dict()
# create an instance of OfferState from a dict
offer_state_form_dict = offer_state.from_dict(offer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


