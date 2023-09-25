# OfferStateInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_state_info import OfferStateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateInfo from a JSON string
offer_state_info_instance = OfferStateInfo.from_json(json)
# print the JSON string representation of the object
print OfferStateInfo.to_json()

# convert the object into a dict
offer_state_info_dict = offer_state_info_instance.to_dict()
# create an instance of OfferStateInfo from a dict
offer_state_info_form_dict = offer_state_info.from_dict(offer_state_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


