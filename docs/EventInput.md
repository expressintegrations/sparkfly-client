# EventInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.event_input import EventInput

# TODO update the JSON string below
json = "{}"
# create an instance of EventInput from a JSON string
event_input_instance = EventInput.from_json(json)
# print the JSON string representation of the object
print EventInput.to_json()

# convert the object into a dict
event_input_dict = event_input_instance.to_dict()
# create an instance of EventInput from a dict
event_input_form_dict = event_input.from_dict(event_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


