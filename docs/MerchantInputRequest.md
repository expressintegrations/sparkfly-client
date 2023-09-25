# MerchantInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant** | [**MerchantInput**](MerchantInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.merchant_input_request import MerchantInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantInputRequest from a JSON string
merchant_input_request_instance = MerchantInputRequest.from_json(json)
# print the JSON string representation of the object
print MerchantInputRequest.to_json()

# convert the object into a dict
merchant_input_request_dict = merchant_input_request_instance.to_dict()
# create an instance of MerchantInputRequest from a dict
merchant_input_request_form_dict = merchant_input_request.from_dict(merchant_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


