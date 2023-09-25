# Transaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**member_id** | **int** |  | [optional] 
**store_id** | **int** |  | [optional] 
**terminal_id** | **int** |  | [optional] 
**serviced_device_id** | **str** |  | [optional] 
**operator_id** | **str** |  | [optional] 
**purchased_amount** | **int** |  | [optional] 
**nr_items** | **int** |  | [optional] 
**transaction_identifier** | **str** |  | [optional] 
**source_id** | **int** |  | [optional] 
**credential_id** | **int** |  | [optional] 
**occurred_at** | **str** |  | [optional] 
**reported_at** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**receipt_id** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**business_date** | **str** |  | [optional] 
**num_guests** | **int** |  | [optional] 
**till_id** | **str** |  | [optional] 
**total_due** | **int** |  | [optional] 
**total_discount** | **int** |  | [optional] 
**total_service** | **int** |  | [optional] 
**total_tax** | **int** |  | [optional] 
**total_paid** | **int** |  | [optional] 
**translator_id** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print Transaction.to_json()

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_form_dict = transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


