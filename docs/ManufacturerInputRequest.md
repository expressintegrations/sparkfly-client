# ManufacturerInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | [**ManufacturerInput**](ManufacturerInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.manufacturer_input_request import ManufacturerInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerInputRequest from a JSON string
manufacturer_input_request_instance = ManufacturerInputRequest.from_json(json)
# print the JSON string representation of the object
print ManufacturerInputRequest.to_json()

# convert the object into a dict
manufacturer_input_request_dict = manufacturer_input_request_instance.to_dict()
# create an instance of ManufacturerInputRequest from a dict
manufacturer_input_request_form_dict = manufacturer_input_request.from_dict(manufacturer_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


