# OfferChannelsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferChannels**](OfferChannels.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_channels_response import OfferChannelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferChannelsResponse from a JSON string
offer_channels_response_instance = OfferChannelsResponse.from_json(json)
# print the JSON string representation of the object
print OfferChannelsResponse.to_json()

# convert the object into a dict
offer_channels_response_dict = offer_channels_response_instance.to_dict()
# create an instance of OfferChannelsResponse from a dict
offer_channels_response_form_dict = offer_channels_response.from_dict(offer_channels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


