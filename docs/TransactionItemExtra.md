# TransactionItemExtra


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**sub_group** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.transaction_item_extra import TransactionItemExtra

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionItemExtra from a JSON string
transaction_item_extra_instance = TransactionItemExtra.from_json(json)
# print the JSON string representation of the object
print TransactionItemExtra.to_json()

# convert the object into a dict
transaction_item_extra_dict = transaction_item_extra_instance.to_dict()
# create an instance of TransactionItemExtra from a dict
transaction_item_extra_form_dict = transaction_item_extra.from_dict(transaction_item_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


