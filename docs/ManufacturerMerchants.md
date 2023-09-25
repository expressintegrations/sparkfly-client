# ManufacturerMerchants


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**merchant_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.manufacturer_merchants import ManufacturerMerchants

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerMerchants from a JSON string
manufacturer_merchants_instance = ManufacturerMerchants.from_json(json)
# print the JSON string representation of the object
print ManufacturerMerchants.to_json()

# convert the object into a dict
manufacturer_merchants_dict = manufacturer_merchants_instance.to_dict()
# create an instance of ManufacturerMerchants from a dict
manufacturer_merchants_form_dict = manufacturer_merchants.from_dict(manufacturer_merchants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


