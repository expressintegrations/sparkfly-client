# ChannelInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**allow_sms_keyword** | **bool** |  | [optional] 
**allow_hmac** | **bool** |  | [optional] 
**conversion_callback_url** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.channel_input import ChannelInput

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelInput from a JSON string
channel_input_instance = ChannelInput.from_json(json)
# print the JSON string representation of the object
print ChannelInput.to_json()

# convert the object into a dict
channel_input_dict = channel_input_instance.to_dict()
# create an instance of ChannelInput from a dict
channel_input_form_dict = channel_input.from_dict(channel_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


