# EligibleChannelInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible_channel** | [**EligibleChannelInput**](EligibleChannelInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.eligible_channel_input_request import EligibleChannelInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleChannelInputRequest from a JSON string
eligible_channel_input_request_instance = EligibleChannelInputRequest.from_json(json)
# print the JSON string representation of the object
print EligibleChannelInputRequest.to_json()

# convert the object into a dict
eligible_channel_input_request_dict = eligible_channel_input_request_instance.to_dict()
# create an instance of EligibleChannelInputRequest from a dict
eligible_channel_input_request_form_dict = eligible_channel_input_request.from_dict(eligible_channel_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


