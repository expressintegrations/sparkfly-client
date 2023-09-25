# ChannelInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**ChannelInput**](ChannelInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.channel_input_request import ChannelInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelInputRequest from a JSON string
channel_input_request_instance = ChannelInputRequest.from_json(json)
# print the JSON string representation of the object
print ChannelInputRequest.to_json()

# convert the object into a dict
channel_input_request_dict = channel_input_request_instance.to_dict()
# create an instance of ChannelInputRequest from a dict
channel_input_request_form_dict = channel_input_request.from_dict(channel_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


