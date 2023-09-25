# EligibleChannelResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible_channel** | [**EligibleChannel**](EligibleChannel.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.eligible_channel_response import EligibleChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleChannelResponse from a JSON string
eligible_channel_response_instance = EligibleChannelResponse.from_json(json)
# print the JSON string representation of the object
print EligibleChannelResponse.to_json()

# convert the object into a dict
eligible_channel_response_dict = eligible_channel_response_instance.to_dict()
# create an instance of EligibleChannelResponse from a dict
eligible_channel_response_form_dict = eligible_channel_response.from_dict(eligible_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


