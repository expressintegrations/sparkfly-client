# EventList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**events** | [**List[EventResponse]**](EventResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.event_list import EventList

# TODO update the JSON string below
json = "{}"
# create an instance of EventList from a JSON string
event_list_instance = EventList.from_json(json)
# print the JSON string representation of the object
print EventList.to_json()

# convert the object into a dict
event_list_dict = event_list_instance.to_dict()
# create an instance of EventList from a dict
event_list_form_dict = event_list.from_dict(event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


