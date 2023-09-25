# OfferEligibility


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_ids** | **List[int]** |  | [optional] 
**store_list_ids** | **List[int]** |  | [optional] 
**member_list_ids** | **List[int]** |  | [optional] 
**channel_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_eligibility import OfferEligibility

# TODO update the JSON string below
json = "{}"
# create an instance of OfferEligibility from a JSON string
offer_eligibility_instance = OfferEligibility.from_json(json)
# print the JSON string representation of the object
print OfferEligibility.to_json()

# convert the object into a dict
offer_eligibility_dict = offer_eligibility_instance.to_dict()
# create an instance of OfferEligibility from a dict
offer_eligibility_form_dict = offer_eligibility.from_dict(offer_eligibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


