# MerchantStoreListStoresResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**store_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.merchant_store_list_stores_response import MerchantStoreListStoresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantStoreListStoresResponse from a JSON string
merchant_store_list_stores_response_instance = MerchantStoreListStoresResponse.from_json(json)
# print the JSON string representation of the object
print MerchantStoreListStoresResponse.to_json()

# convert the object into a dict
merchant_store_list_stores_response_dict = merchant_store_list_stores_response_instance.to_dict()
# create an instance of MerchantStoreListStoresResponse from a dict
merchant_store_list_stores_response_form_dict = merchant_store_list_stores_response.from_dict(merchant_store_list_stores_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


