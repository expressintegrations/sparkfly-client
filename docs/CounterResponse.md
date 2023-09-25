# CounterResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter** | [**Counter**](Counter.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.counter_response import CounterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CounterResponse from a JSON string
counter_response_instance = CounterResponse.from_json(json)
# print the JSON string representation of the object
print CounterResponse.to_json()

# convert the object into a dict
counter_response_dict = counter_response_instance.to_dict()
# create an instance of CounterResponse from a dict
counter_response_form_dict = counter_response.from_dict(counter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


