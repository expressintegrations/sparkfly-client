# ManufacturerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | [**Manufacturer**](Manufacturer.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.manufacturer_response import ManufacturerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerResponse from a JSON string
manufacturer_response_instance = ManufacturerResponse.from_json(json)
# print the JSON string representation of the object
print ManufacturerResponse.to_json()

# convert the object into a dict
manufacturer_response_dict = manufacturer_response_instance.to_dict()
# create an instance of ManufacturerResponse from a dict
manufacturer_response_form_dict = manufacturer_response.from_dict(manufacturer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


