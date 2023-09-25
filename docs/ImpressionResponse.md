# ImpressionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impression** | [**Impression**](Impression.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.impression_response import ImpressionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionResponse from a JSON string
impression_response_instance = ImpressionResponse.from_json(json)
# print the JSON string representation of the object
print ImpressionResponse.to_json()

# convert the object into a dict
impression_response_dict = impression_response_instance.to_dict()
# create an instance of ImpressionResponse from a dict
impression_response_form_dict = impression_response.from_dict(impression_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


