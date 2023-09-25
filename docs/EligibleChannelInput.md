# EligibleChannelInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security** | **str** |  | [optional] 
**sms_keyword** | **str** |  | [optional] 
**allow_return_later** | **bool** |  | [optional] 

## Example

```python
from sparkfly_client.models.eligible_channel_input import EligibleChannelInput

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleChannelInput from a JSON string
eligible_channel_input_instance = EligibleChannelInput.from_json(json)
# print the JSON string representation of the object
print EligibleChannelInput.to_json()

# convert the object into a dict
eligible_channel_input_dict = eligible_channel_input_instance.to_dict()
# create an instance of EligibleChannelInput from a dict
eligible_channel_input_form_dict = eligible_channel_input.from_dict(eligible_channel_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


