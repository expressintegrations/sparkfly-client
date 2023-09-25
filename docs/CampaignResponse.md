# CampaignResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | [**Campaign**](Campaign.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.campaign_response import CampaignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignResponse from a JSON string
campaign_response_instance = CampaignResponse.from_json(json)
# print the JSON string representation of the object
print CampaignResponse.to_json()

# convert the object into a dict
campaign_response_dict = campaign_response_instance.to_dict()
# create an instance of CampaignResponse from a dict
campaign_response_form_dict = campaign_response.from_dict(campaign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


