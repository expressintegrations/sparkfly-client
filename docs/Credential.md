# Credential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**member_id** | **int** |  | [optional] 
**store_id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**offer_ids** | **List[int]** |  | [optional] 
**annotations** | **str** |  | [optional] 
**code_lifetime** | **int** |  | [optional] 
**supports_barcode** | **bool** |  | [optional] 
**merchant_id** | **int** |  | [optional] 
**offer_name** | **str** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**location_address** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.credential import Credential

# TODO update the JSON string below
json = "{}"
# create an instance of Credential from a JSON string
credential_instance = Credential.from_json(json)
# print the JSON string representation of the object
print Credential.to_json()

# convert the object into a dict
credential_dict = credential_instance.to_dict()
# create an instance of Credential from a dict
credential_form_dict = credential.from_dict(credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


