# CampaignInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | [**CampaignInput**](CampaignInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.campaign_input_request import CampaignInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignInputRequest from a JSON string
campaign_input_request_instance = CampaignInputRequest.from_json(json)
# print the JSON string representation of the object
print CampaignInputRequest.to_json()

# convert the object into a dict
campaign_input_request_dict = campaign_input_request_instance.to_dict()
# create an instance of CampaignInputRequest from a dict
campaign_input_request_form_dict = campaign_input_request.from_dict(campaign_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


