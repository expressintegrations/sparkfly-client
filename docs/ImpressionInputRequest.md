# ImpressionInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impression** | [**ImpressionInput**](ImpressionInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.impression_input_request import ImpressionInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionInputRequest from a JSON string
impression_input_request_instance = ImpressionInputRequest.from_json(json)
# print the JSON string representation of the object
print ImpressionInputRequest.to_json()

# convert the object into a dict
impression_input_request_dict = impression_input_request_instance.to_dict()
# create an instance of ImpressionInputRequest from a dict
impression_input_request_form_dict = impression_input_request.from_dict(impression_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


