# OfferActivityList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**collection** | [**List[OfferActivityResponse]**](OfferActivityResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_activity_list import OfferActivityList

# TODO update the JSON string below
json = "{}"
# create an instance of OfferActivityList from a JSON string
offer_activity_list_instance = OfferActivityList.from_json(json)
# print the JSON string representation of the object
print OfferActivityList.to_json()

# convert the object into a dict
offer_activity_list_dict = offer_activity_list_instance.to_dict()
# create an instance of OfferActivityList from a dict
offer_activity_list_form_dict = offer_activity_list.from_dict(offer_activity_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


