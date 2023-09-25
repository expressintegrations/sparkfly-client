# PosOfferCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.pos_offer_code import PosOfferCode

# TODO update the JSON string below
json = "{}"
# create an instance of PosOfferCode from a JSON string
pos_offer_code_instance = PosOfferCode.from_json(json)
# print the JSON string representation of the object
print PosOfferCode.to_json()

# convert the object into a dict
pos_offer_code_dict = pos_offer_code_instance.to_dict()
# create an instance of PosOfferCode from a dict
pos_offer_code_form_dict = pos_offer_code.from_dict(pos_offer_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


