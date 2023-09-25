# OfferChannelIdsInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferChannelIdsInput**](OfferChannelIdsInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_channel_ids_input_request import OfferChannelIdsInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OfferChannelIdsInputRequest from a JSON string
offer_channel_ids_input_request_instance = OfferChannelIdsInputRequest.from_json(json)
# print the JSON string representation of the object
print OfferChannelIdsInputRequest.to_json()

# convert the object into a dict
offer_channel_ids_input_request_dict = offer_channel_ids_input_request_instance.to_dict()
# create an instance of OfferChannelIdsInputRequest from a dict
offer_channel_ids_input_request_form_dict = offer_channel_ids_input_request.from_dict(offer_channel_ids_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


