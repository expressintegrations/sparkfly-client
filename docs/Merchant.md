# Merchant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**account_id** | **int** |  | [optional] 
**billing_arrangement** | **str** |  | [optional] 
**supports_barcode** | **bool** |  | [optional] 
**redemption_identifier_type** | **int** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**channels** | [**List[Channel]**](Channel.md) |  | [optional] 
**contacts** | [**Contacts**](Contacts.md) |  | [optional] 
**linked_by_channel** | **bool** |  | [optional] 

## Example

```python
from sparkfly_client.models.merchant import Merchant

# TODO update the JSON string below
json = "{}"
# create an instance of Merchant from a JSON string
merchant_instance = Merchant.from_json(json)
# print the JSON string representation of the object
print Merchant.to_json()

# convert the object into a dict
merchant_dict = merchant_instance.to_dict()
# create an instance of Merchant from a dict
merchant_form_dict = merchant.from_dict(merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


