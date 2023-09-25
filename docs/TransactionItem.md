# TransactionItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**item_code** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**ext_price** | **int** |  | [optional] 
**transaction_type** | **int** |  | [optional] 
**extra_data** | [**TransactionItemExtra**](TransactionItemExtra.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.transaction_item import TransactionItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionItem from a JSON string
transaction_item_instance = TransactionItem.from_json(json)
# print the JSON string representation of the object
print TransactionItem.to_json()

# convert the object into a dict
transaction_item_dict = transaction_item_instance.to_dict()
# create an instance of TransactionItem from a dict
transaction_item_form_dict = transaction_item.from_dict(transaction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


