# Offer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**manufacturer_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_template_id** | **str** |  | [optional] 
**offer_type** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**offer_code** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**criteria** | **object** |  | [optional] 
**points_earning_value** | **int** |  | [optional] 
**points_required_value** | **int** |  | [optional] 
**reward_item_description** | **str** |  | [optional] 
**reward_item_value** | **int** |  | [optional] 
**terms_and_conditions** | **str** |  | [optional] 
**terms_and_conditions_template_id** | **str** |  | [optional] 
**quest_only** | **str** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**external_reward** | **str** |  | [optional] 
**is_reward** | **bool** |  | [optional] 
**locked** | **str** |  | [optional] 
**activates_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**stop_offering_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**max_amount** | **int** |  | [optional] 
**min_spend_amount** | **int** |  | [optional] 
**trigger_amount** | **int** |  | [optional] 
**max_redemptions** | **int** |  | [optional] 
**max_redemptions_per_member** | **int** |  | [optional] 
**max_redemptions_per_member_per_day** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**initial_value_mode** | **str** |  | [optional] 
**availability** | **str** |  | [optional] 
**offer_value_text** | **str** |  | [optional] 
**offer_value_text_es** | **str** |  | [optional] 
**formatting** | [**OfferFormatting**](OfferFormatting.md) |  | [optional] 
**eligibility** | [**OfferEligibility**](OfferEligibility.md) |  | [optional] 
**redeem_until_depleted** | **bool** |  | [optional] 
**initial_remaining_value** | **int** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer import Offer

# TODO update the JSON string below
json = "{}"
# create an instance of Offer from a JSON string
offer_instance = Offer.from_json(json)
# print the JSON string representation of the object
print Offer.to_json()

# convert the object into a dict
offer_dict = offer_instance.to_dict()
# create an instance of Offer from a dict
offer_form_dict = offer.from_dict(offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


