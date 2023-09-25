# CounterInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter** | [**CounterInput**](CounterInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.counter_input_request import CounterInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CounterInputRequest from a JSON string
counter_input_request_instance = CounterInputRequest.from_json(json)
# print the JSON string representation of the object
print CounterInputRequest.to_json()

# convert the object into a dict
counter_input_request_dict = counter_input_request_instance.to_dict()
# create an instance of CounterInputRequest from a dict
counter_input_request_form_dict = counter_input_request.from_dict(counter_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


