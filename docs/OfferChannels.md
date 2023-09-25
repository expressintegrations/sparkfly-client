# OfferChannels


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_channels import OfferChannels

# TODO update the JSON string below
json = "{}"
# create an instance of OfferChannels from a JSON string
offer_channels_instance = OfferChannels.from_json(json)
# print the JSON string representation of the object
print OfferChannels.to_json()

# convert the object into a dict
offer_channels_dict = offer_channels_instance.to_dict()
# create an instance of OfferChannels from a dict
offer_channels_form_dict = offer_channels.from_dict(offer_channels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


