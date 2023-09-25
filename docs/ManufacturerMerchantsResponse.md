# ManufacturerMerchantsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | [**ManufacturerMerchants**](ManufacturerMerchants.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.manufacturer_merchants_response import ManufacturerMerchantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerMerchantsResponse from a JSON string
manufacturer_merchants_response_instance = ManufacturerMerchantsResponse.from_json(json)
# print the JSON string representation of the object
print ManufacturerMerchantsResponse.to_json()

# convert the object into a dict
manufacturer_merchants_response_dict = manufacturer_merchants_response_instance.to_dict()
# create an instance of ManufacturerMerchantsResponse from a dict
manufacturer_merchants_response_form_dict = manufacturer_merchants_response.from_dict(manufacturer_merchants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


