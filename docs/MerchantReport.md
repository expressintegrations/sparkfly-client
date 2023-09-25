# MerchantReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReportData]**](ReportData.md) |  | [optional] 
**total_redemptions** | **int** |  | [optional] 
**total_purchase_amount** | **float** |  | [optional] 
**average_purchase** | **float** |  | [optional] 
**average_items_per_transaction** | **float** |  | [optional] 
**redemptions_by_date** | **Dict[str, str]** |  | [optional] 
**redemptions_by_location** | **Dict[str, int]** |  | [optional] 
**total_purchase_amount_by_location** | **Dict[str, float]** |  | [optional] 
**redemptions_by_merchant** | **Dict[str, int]** |  | [optional] 
**total_purchase_amount_by_merchant** | **Dict[str, float]** |  | [optional] 
**redemptions_by_offer** | **Dict[str, Dict[str, int]]** |  | [optional] 
**average_items_per_transaction_per_location** | **Dict[str, float]** |  | [optional] 
**average_purchase_by_location** | **Dict[str, float]** |  | [optional] 
**number_of_items** | **int** |  | [optional] 
**item_counts** | **Dict[str, List[int]]** |  | [optional] 
**customers_by_period** | **Dict[str, int]** |  | [optional] 
**customer_frequency** | **Dict[str, int]** |  | [optional] 
**customer_age_groups** | **Dict[str, int]** |  | [optional] 
**customer_genders** | **Dict[str, int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.merchant_report import MerchantReport

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantReport from a JSON string
merchant_report_instance = MerchantReport.from_json(json)
# print the JSON string representation of the object
print MerchantReport.to_json()

# convert the object into a dict
merchant_report_dict = merchant_report_instance.to_dict()
# create an instance of MerchantReport from a dict
merchant_report_form_dict = merchant_report.from_dict(merchant_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


