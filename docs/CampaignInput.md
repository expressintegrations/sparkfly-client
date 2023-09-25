# CampaignInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **int** |  | [optional] 
**code_ref** | **str** |  | [optional] 
**code_count** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**stop_display_at** | **str** |  | [optional] 
**funding_source** | **str** |  | [optional] 
**start_display_at** | **str** |  | [optional] 
**eligible_store_numbers** | **List[int]** |  | [optional] 
**description_template_id** | **str** |  | [optional] 
**generate_reusable_codes** | **bool** |  | [optional] 
**eligible_storelist_numbers** | **List[int]** |  | [optional] 
**landing_page_image_template_id** | **str** |  | [optional] 
**terms_and_conditions_template_id** | **str** |  | [optional] 
**security** | **str** |  | [optional] 
**allow_return_later** | **bool** |  | [optional] 

## Example

```python
from sparkfly_client.models.campaign_input import CampaignInput

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignInput from a JSON string
campaign_input_instance = CampaignInput.from_json(json)
# print the JSON string representation of the object
print CampaignInput.to_json()

# convert the object into a dict
campaign_input_dict = campaign_input_instance.to_dict()
# create an instance of CampaignInput from a dict
campaign_input_form_dict = campaign_input.from_dict(campaign_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


