# MerchantOfferList


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
from sparkfly_client.models.merchant_offer_list import MerchantOfferList

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOfferList from a JSON string
merchant_offer_list_instance = MerchantOfferList.from_json(json)
# print the JSON string representation of the object
print MerchantOfferList.to_json()

# convert the object into a dict
merchant_offer_list_dict = merchant_offer_list_instance.to_dict()
# create an instance of MerchantOfferList from a dict
merchant_offer_list_form_dict = merchant_offer_list.from_dict(merchant_offer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


