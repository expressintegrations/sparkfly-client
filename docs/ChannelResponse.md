# ChannelResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**Channel**](Channel.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.channel_response import ChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelResponse from a JSON string
channel_response_instance = ChannelResponse.from_json(json)
# print the JSON string representation of the object
print ChannelResponse.to_json()

# convert the object into a dict
channel_response_dict = channel_response_instance.to_dict()
# create an instance of ChannelResponse from a dict
channel_response_form_dict = channel_response.from_dict(channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


