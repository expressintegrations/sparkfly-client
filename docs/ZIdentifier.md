# ZIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**zid** | **str** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**member_id** | **int** |  | [optional] 
**member_identifier** | **str** |  | [optional] 
**offer_xid** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.z_identifier import ZIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ZIdentifier from a JSON string
z_identifier_instance = ZIdentifier.from_json(json)
# print the JSON string representation of the object
print ZIdentifier.to_json()

# convert the object into a dict
z_identifier_dict = z_identifier_instance.to_dict()
# create an instance of ZIdentifier from a dict
z_identifier_form_dict = z_identifier.from_dict(z_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


