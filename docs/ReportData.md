# ReportData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**pos_transaction_id** | **str** |  | [optional] 
**operator_id** | **str** |  | [optional] 
**merchant_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**member_id** | **int** |  | [optional] 
**credential_identifier** | **str** |  | [optional] 
**credential_id** | **int** |  | [optional] 
**store_id** | **int** |  | [optional] 
**store_name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**offer_group** | **str** |  | [optional] 
**offer_group_id** | **int** |  | [optional] 
**offer_name** | **str** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**channel_group_id** | **int** |  | [optional] 
**channel_group_name** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**purchase_amount** | **int** |  | [optional] 
**value** | **int** |  | [optional] 
**items** | **List[str]** |  | [optional] 
**transaction_items** | [**List[TransactionItem]**](TransactionItem.md) |  | [optional] 
**item_groups** | [**List[Item]**](Item.md) |  | [optional] 
**redeemed_items** | [**List[Item]**](Item.md) |  | [optional] 
**impression_ids** | **List[int]** |  | [optional] 
**business_date** | **datetime** |  | [optional] 
**redemption_datetime** | **datetime** |  | [optional] 
**impression_datetime** | **str** |  | [optional] 
**creative** | **str** |  | [optional] 
**redemption_type** | **str** |  | [optional] 
**customer_identifier** | **str** |  | [optional] 
**time_period** | **str** |  | [optional] 
**day_period** | **str** |  | [optional] 
**customer_age** | **str** |  | [optional] 
**customer_frequency** | **str** |  | [optional] 
**customer_gender** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**campaign_name** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**store_number** | **str** |  | [optional] 
**offer_activity_id** | **int** |  | [optional] 
**qualifying_items** | **str** |  | [optional] 
**external_offer_instance_id** | **str** |  | [optional] 
**offer_state_id** | **str** |  | [optional] 
**loyalty_id** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.report_data import ReportData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportData from a JSON string
report_data_instance = ReportData.from_json(json)
# print the JSON string representation of the object
print ReportData.to_json()

# convert the object into a dict
report_data_dict = report_data_instance.to_dict()
# create an instance of ReportData from a dict
report_data_form_dict = report_data.from_dict(report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


