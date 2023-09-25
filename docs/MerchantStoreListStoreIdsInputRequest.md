# MerchantStoreListStoreIdsInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_list** | [**StoreListStoreIdsInput**](StoreListStoreIdsInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.merchant_store_list_store_ids_input_request import MerchantStoreListStoreIdsInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantStoreListStoreIdsInputRequest from a JSON string
merchant_store_list_store_ids_input_request_instance = MerchantStoreListStoreIdsInputRequest.from_json(json)
# print the JSON string representation of the object
print MerchantStoreListStoreIdsInputRequest.to_json()

# convert the object into a dict
merchant_store_list_store_ids_input_request_dict = merchant_store_list_store_ids_input_request_instance.to_dict()
# create an instance of MerchantStoreListStoreIdsInputRequest from a dict
merchant_store_list_store_ids_input_request_form_dict = merchant_store_list_store_ids_input_request.from_dict(merchant_store_list_store_ids_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


