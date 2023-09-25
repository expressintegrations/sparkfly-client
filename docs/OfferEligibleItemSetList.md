# OfferEligibleItemSetList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**eligible_item_sets** | [**List[EligibleItemSetResponse]**](EligibleItemSetResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_eligible_item_set_list import OfferEligibleItemSetList

# TODO update the JSON string below
json = "{}"
# create an instance of OfferEligibleItemSetList from a JSON string
offer_eligible_item_set_list_instance = OfferEligibleItemSetList.from_json(json)
# print the JSON string representation of the object
print OfferEligibleItemSetList.to_json()

# convert the object into a dict
offer_eligible_item_set_list_dict = offer_eligible_item_set_list_instance.to_dict()
# create an instance of OfferEligibleItemSetList from a dict
offer_eligible_item_set_list_form_dict = offer_eligible_item_set_list.from_dict(offer_eligible_item_set_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


