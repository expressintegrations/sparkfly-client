# OfferList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**offers** | [**List[OfferSimplifiedResponse]**](OfferSimplifiedResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_list import OfferList

# TODO update the JSON string below
json = "{}"
# create an instance of OfferList from a JSON string
offer_list_instance = OfferList.from_json(json)
# print the JSON string representation of the object
print OfferList.to_json()

# convert the object into a dict
offer_list_dict = offer_list_instance.to_dict()
# create an instance of OfferList from a dict
offer_list_form_dict = offer_list.from_dict(offer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


