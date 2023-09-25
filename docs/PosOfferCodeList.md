# PosOfferCodeList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**pos_offer_codes** | [**List[PosOfferCodeResponse]**](PosOfferCodeResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.pos_offer_code_list import PosOfferCodeList

# TODO update the JSON string below
json = "{}"
# create an instance of PosOfferCodeList from a JSON string
pos_offer_code_list_instance = PosOfferCodeList.from_json(json)
# print the JSON string representation of the object
print PosOfferCodeList.to_json()

# convert the object into a dict
pos_offer_code_list_dict = pos_offer_code_list_instance.to_dict()
# create an instance of PosOfferCodeList from a dict
pos_offer_code_list_form_dict = pos_offer_code_list.from_dict(pos_offer_code_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


