# MerchantList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**merchants** | [**List[MerchantResponse]**](MerchantResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.merchant_list import MerchantList

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantList from a JSON string
merchant_list_instance = MerchantList.from_json(json)
# print the JSON string representation of the object
print MerchantList.to_json()

# convert the object into a dict
merchant_list_dict = merchant_list_instance.to_dict()
# create an instance of MerchantList from a dict
merchant_list_form_dict = merchant_list.from_dict(merchant_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


