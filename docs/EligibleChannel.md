# EligibleChannel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**xid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**security** | **str** |  | [optional] 
**security_key** | **str** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**sms_keyword** | **str** |  | [optional] 
**allow_return_later** | **bool** |  | [optional] 
**formatting** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.eligible_channel import EligibleChannel

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleChannel from a JSON string
eligible_channel_instance = EligibleChannel.from_json(json)
# print the JSON string representation of the object
print EligibleChannel.to_json()

# convert the object into a dict
eligible_channel_dict = eligible_channel_instance.to_dict()
# create an instance of EligibleChannel from a dict
eligible_channel_form_dict = eligible_channel.from_dict(eligible_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


