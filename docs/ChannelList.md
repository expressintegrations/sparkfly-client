# ChannelList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**channels** | [**List[ChannelResponse]**](ChannelResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.channel_list import ChannelList

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelList from a JSON string
channel_list_instance = ChannelList.from_json(json)
# print the JSON string representation of the object
print ChannelList.to_json()

# convert the object into a dict
channel_list_dict = channel_list_instance.to_dict()
# create an instance of ChannelList from a dict
channel_list_form_dict = channel_list.from_dict(channel_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


