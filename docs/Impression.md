# Impression


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**annotations** | **str** |  | [optional] 
**cookie_id** | **str** |  | [optional] 
**offer_xid** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**member_id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**creative_name** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.impression import Impression

# TODO update the JSON string below
json = "{}"
# create an instance of Impression from a JSON string
impression_instance = Impression.from_json(json)
# print the JSON string representation of the object
print Impression.to_json()

# convert the object into a dict
impression_dict = impression_instance.to_dict()
# create an instance of Impression from a dict
impression_form_dict = impression.from_dict(impression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


