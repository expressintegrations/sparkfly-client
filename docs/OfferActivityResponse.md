# OfferActivityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_activity** | [**OfferActivity**](OfferActivity.md) |  | [optional] 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_activity_response import OfferActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferActivityResponse from a JSON string
offer_activity_response_instance = OfferActivityResponse.from_json(json)
# print the JSON string representation of the object
print OfferActivityResponse.to_json()

# convert the object into a dict
offer_activity_response_dict = offer_activity_response_instance.to_dict()
# create an instance of OfferActivityResponse from a dict
offer_activity_response_form_dict = offer_activity_response.from_dict(offer_activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


