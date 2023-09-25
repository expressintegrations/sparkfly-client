# Redemption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**pos_transaction_id** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**operator_id** | **str** |  | [optional] 
**member_id** | **int** |  | [optional] 
**credential_identifier** | **str** |  | [optional] 
**store_name** | **str** |  | [optional] 
**store_number** | **str** |  | [optional] 
**store_id** | **int** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**offer_name** | **str** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**purchase_amount** | **int** |  | [optional] 
**value** | **int** |  | [optional] 
**transaction_items** | [**List[TransactionItem]**](TransactionItem.md) |  | [optional] 
**business_date** | **str** |  | [optional] 
**redemption_datetime** | **str** |  | [optional] 
**customer_identifier** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**campaign_name** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.redemption import Redemption

# TODO update the JSON string below
json = "{}"
# create an instance of Redemption from a JSON string
redemption_instance = Redemption.from_json(json)
# print the JSON string representation of the object
print Redemption.to_json()

# convert the object into a dict
redemption_dict = redemption_instance.to_dict()
# create an instance of Redemption from a dict
redemption_form_dict = redemption.from_dict(redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


