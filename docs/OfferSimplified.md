# OfferSimplified


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**manufacturer_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**offer_type** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**offer_code** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**criteria** | **str** |  | [optional] 
**points_earning_value** | **str** |  | [optional] 
**points_required_value** | **str** |  | [optional] 
**reward_item_description** | **str** |  | [optional] 
**reward_item_value** | **str** |  | [optional] 
**terms_and_conditions** | **str** |  | [optional] 
**quest_only** | **bool** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**external_reward** | **str** |  | [optional] 
**is_reward** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**activates_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**stop_offering_at** | **datetime** |  | [optional] 
**max_amount** | **str** |  | [optional] 
**min_spend_amount** | **str** |  | [optional] 
**max_redemptions** | **str** |  | [optional] 
**max_redemptions_per_member** | **str** |  | [optional] 
**max_redemptions_per_member_per_day** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_simplified import OfferSimplified

# TODO update the JSON string below
json = "{}"
# create an instance of OfferSimplified from a JSON string
offer_simplified_instance = OfferSimplified.from_json(json)
# print the JSON string representation of the object
print OfferSimplified.to_json()

# convert the object into a dict
offer_simplified_dict = offer_simplified_instance.to_dict()
# create an instance of OfferSimplified from a dict
offer_simplified_form_dict = offer_simplified.from_dict(offer_simplified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


