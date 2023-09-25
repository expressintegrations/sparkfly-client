# MerchantStoreListList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**store_lists** | [**List[StoreListObjectResponse]**](StoreListObjectResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.merchant_store_list_list import MerchantStoreListList

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantStoreListList from a JSON string
merchant_store_list_list_instance = MerchantStoreListList.from_json(json)
# print the JSON string representation of the object
print MerchantStoreListList.to_json()

# convert the object into a dict
merchant_store_list_list_dict = merchant_store_list_list_instance.to_dict()
# create an instance of MerchantStoreListList from a dict
merchant_store_list_list_form_dict = merchant_store_list_list.from_dict(merchant_store_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


