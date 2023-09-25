# OfferInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**offer_type** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**offer_code** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**points_earning_value** | **int** |  | [optional] 
**points_required_value** | **int** |  | [optional] 
**reward_item_description** | **str** |  | [optional] 
**reward_item_value** | **int** |  | [optional] 
**terms_and_conditions** | **str** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**external_reward** | **str** |  | [optional] 
**is_reward** | **bool** |  | [optional] 
**activates_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**stop_offering_at** | **datetime** |  | [optional] 
**max_amount** | **int** |  | [optional] 
**min_spend_amount** | **int** |  | [optional] 
**trigger_amount** | **int** |  | [optional] 
**max_redemptions** | **int** |  | [optional] 
**max_redemptions_per_member** | **int** |  | [optional] 
**max_redemptions_per_member_per_day** | **int** |  | [optional] 
**redeem_until_depleted** | **bool** |  | [optional] 
**initial_remaining_value** | **int** |  | [optional] 
**formatting** | [**OfferFormatting**](OfferFormatting.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_input import OfferInput

# TODO update the JSON string below
json = "{}"
# create an instance of OfferInput from a JSON string
offer_input_instance = OfferInput.from_json(json)
# print the JSON string representation of the object
print OfferInput.to_json()

# convert the object into a dict
offer_input_dict = offer_input_instance.to_dict()
# create an instance of OfferInput from a dict
offer_input_form_dict = offer_input.from_dict(offer_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


