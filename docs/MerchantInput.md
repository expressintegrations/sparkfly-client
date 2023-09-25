# MerchantInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**logo** | **str** | Logo URL | [optional] 
**is_active** | **bool** | Set merchant to active | [optional] 
**billing_arrangement** | **str** | Billing arrangement settings | [optional] 
**supports_barcode** | **bool** | Whether or not a merchant can scan optical barcodes to redeem offers | [optional] 
**redemption_identifier_type** | **int** | Redemption identifier | [optional] 
**primary** | [**Contact**](Contact.md) |  | [optional] 
**secondary** | [**Contact**](Contact.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.merchant_input import MerchantInput

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantInput from a JSON string
merchant_input_instance = MerchantInput.from_json(json)
# print the JSON string representation of the object
print MerchantInput.to_json()

# convert the object into a dict
merchant_input_dict = merchant_input_instance.to_dict()
# create an instance of MerchantInput from a dict
merchant_input_form_dict = merchant_input.from_dict(merchant_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


