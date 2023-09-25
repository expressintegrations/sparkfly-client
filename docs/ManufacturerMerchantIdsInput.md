# ManufacturerMerchantIdsInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.manufacturer_merchant_ids_input import ManufacturerMerchantIdsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerMerchantIdsInput from a JSON string
manufacturer_merchant_ids_input_instance = ManufacturerMerchantIdsInput.from_json(json)
# print the JSON string representation of the object
print ManufacturerMerchantIdsInput.to_json()

# convert the object into a dict
manufacturer_merchant_ids_input_dict = manufacturer_merchant_ids_input_instance.to_dict()
# create an instance of ManufacturerMerchantIdsInput from a dict
manufacturer_merchant_ids_input_form_dict = manufacturer_merchant_ids_input.from_dict(manufacturer_merchant_ids_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


