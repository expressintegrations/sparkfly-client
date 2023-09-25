# BadRequestObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.bad_request_object import BadRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestObject from a JSON string
bad_request_object_instance = BadRequestObject.from_json(json)
# print the JSON string representation of the object
print BadRequestObject.to_json()

# convert the object into a dict
bad_request_object_dict = bad_request_object_instance.to_dict()
# create an instance of BadRequestObject from a dict
bad_request_object_form_dict = bad_request_object.from_dict(bad_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


