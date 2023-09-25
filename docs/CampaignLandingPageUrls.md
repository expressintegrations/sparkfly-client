# CampaignLandingPageUrls


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | **Dict[str, str]** |  | [optional] 
**storelist** | **Dict[str, str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.campaign_landing_page_urls import CampaignLandingPageUrls

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignLandingPageUrls from a JSON string
campaign_landing_page_urls_instance = CampaignLandingPageUrls.from_json(json)
# print the JSON string representation of the object
print CampaignLandingPageUrls.to_json()

# convert the object into a dict
campaign_landing_page_urls_dict = campaign_landing_page_urls_instance.to_dict()
# create an instance of CampaignLandingPageUrls from a dict
campaign_landing_page_urls_form_dict = campaign_landing_page_urls.from_dict(campaign_landing_page_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


