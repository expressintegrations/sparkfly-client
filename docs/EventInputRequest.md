# EventInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventInput**](EventInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.event_input_request import EventInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventInputRequest from a JSON string
event_input_request_instance = EventInputRequest.from_json(json)
# print the JSON string representation of the object
print EventInputRequest.to_json()

# convert the object into a dict
event_input_request_dict = event_input_request_instance.to_dict()
# create an instance of EventInputRequest from a dict
event_input_request_form_dict = event_input_request.from_dict(event_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


