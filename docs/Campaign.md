# Campaign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**xid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code_ref** | **str** |  | [optional] 
**code_count** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**online_offer_code** | **str** |  | [optional] 
**activation_date** | **datetime** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**start_display_at** | **datetime** |  | [optional] 
**stop_display_at** | **str** |  | [optional] 
**funding_source** | **str** |  | [optional] 
**eligible_channel_tags** | **str** |  | [optional] 
**eligible_store_ids** | **List[int]** |  | [optional] 
**eligible_store_numbers** | **List[str]** |  | [optional] 
**eligible_storelist_ids** | **List[int]** |  | [optional] 
**eligible_storelist_numbers** | **List[str]** |  | [optional] 
**landing_page_image_template_id** | **str** |  | [optional] 
**description_template_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**terms_and_conditions_template_id** | **str** |  | [optional] 
**terms_and_conditions** | **str** |  | [optional] 
**security** | **str** |  | [optional] 
**landing_page_urls** | [**CampaignLandingPageUrls**](CampaignLandingPageUrls.md) |  | [optional] 
**allow_return_later** | **bool** |  | [optional] 
**redemption_identifier_type** | **int** |  | [optional] 
**member_required** | **bool** |  | [optional] 
**max_redemptions_per_member** | **str** |  | [optional] 
**dynamic_expiration** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.campaign import Campaign

# TODO update the JSON string below
json = "{}"
# create an instance of Campaign from a JSON string
campaign_instance = Campaign.from_json(json)
# print the JSON string representation of the object
print Campaign.to_json()

# convert the object into a dict
campaign_dict = campaign_instance.to_dict()
# create an instance of Campaign from a dict
campaign_form_dict = campaign.from_dict(campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


