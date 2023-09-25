# PosOfferCodeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos_offer_code** | [**PosOfferCode**](PosOfferCode.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.pos_offer_code_response import PosOfferCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PosOfferCodeResponse from a JSON string
pos_offer_code_response_instance = PosOfferCodeResponse.from_json(json)
# print the JSON string representation of the object
print PosOfferCodeResponse.to_json()

# convert the object into a dict
pos_offer_code_response_dict = pos_offer_code_response_instance.to_dict()
# create an instance of PosOfferCodeResponse from a dict
pos_offer_code_response_form_dict = pos_offer_code_response.from_dict(pos_offer_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


