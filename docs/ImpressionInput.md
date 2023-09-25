# ImpressionInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie_id** | **str** |  | 
**offer_xid** | **str** |  | 
**annotations** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.impression_input import ImpressionInput

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionInput from a JSON string
impression_input_instance = ImpressionInput.from_json(json)
# print the JSON string representation of the object
print ImpressionInput.to_json()

# convert the object into a dict
impression_input_dict = impression_input_instance.to_dict()
# create an instance of ImpressionInput from a dict
impression_input_form_dict = impression_input.from_dict(impression_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


