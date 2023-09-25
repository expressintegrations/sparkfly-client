# OfferFormatting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bg_color** | **str** |  | [optional] 
**bg_image** | **str** |  | [optional] 
**custom_credential_content** | **str** |  | [optional] 
**in_store_only** | **bool** |  | [optional] 
**extra_content** | **str** |  | [optional] 
**highest_value_to_customer** | **bool** |  | [optional] 
**instructions** | **str** |  | [optional] 
**mobile_thumb_url** | **str** |  | [optional] 
**mobile_url** | **str** |  | [optional] 
**multiple_offers_can_be_combined_on_an_order** | **bool** |  | [optional] 
**no_printable** | **bool** |  | [optional] 
**online_offer_code** | **str** |  | [optional] 
**reduces_taxable_amount** | **bool** |  | [optional] 
**short_name** | **str** |  | [optional] 
**text_message** | **str** |  | [optional] 
**web_thumb_url** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_formatting import OfferFormatting

# TODO update the JSON string below
json = "{}"
# create an instance of OfferFormatting from a JSON string
offer_formatting_instance = OfferFormatting.from_json(json)
# print the JSON string representation of the object
print OfferFormatting.to_json()

# convert the object into a dict
offer_formatting_dict = offer_formatting_instance.to_dict()
# create an instance of OfferFormatting from a dict
offer_formatting_form_dict = offer_formatting.from_dict(offer_formatting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


