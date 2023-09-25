# OfferActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**transaction_id** | **int** |  | [optional] 
**credential_id** | **int** |  | [optional] 
**value** | **int** |  | [optional] 
**invoice_id** | **int** |  | [optional] 
**reported_at** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**member_id** | **int** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**activity_type** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**processed_at** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_activity import OfferActivity

# TODO update the JSON string below
json = "{}"
# create an instance of OfferActivity from a JSON string
offer_activity_instance = OfferActivity.from_json(json)
# print the JSON string representation of the object
print OfferActivity.to_json()

# convert the object into a dict
offer_activity_dict = offer_activity_instance.to_dict()
# create an instance of OfferActivity from a dict
offer_activity_form_dict = offer_activity.from_dict(offer_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


