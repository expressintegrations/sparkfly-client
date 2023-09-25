# CampaignSimplified


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** |  | [optional] 
**campaign_name** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.campaign_simplified import CampaignSimplified

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignSimplified from a JSON string
campaign_simplified_instance = CampaignSimplified.from_json(json)
# print the JSON string representation of the object
print CampaignSimplified.to_json()

# convert the object into a dict
campaign_simplified_dict = campaign_simplified_instance.to_dict()
# create an instance of CampaignSimplified from a dict
campaign_simplified_form_dict = campaign_simplified.from_dict(campaign_simplified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


