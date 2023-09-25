# OfferStateList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**offer_states** | [**List[OfferStateResponse]**](OfferStateResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_state_list import OfferStateList

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateList from a JSON string
offer_state_list_instance = OfferStateList.from_json(json)
# print the JSON string representation of the object
print OfferStateList.to_json()

# convert the object into a dict
offer_state_list_dict = offer_state_list_instance.to_dict()
# create an instance of OfferStateList from a dict
offer_state_list_form_dict = offer_state_list.from_dict(offer_state_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


