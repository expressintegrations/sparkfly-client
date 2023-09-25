# CounterList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**counters** | [**List[CounterResponse]**](CounterResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.counter_list import CounterList

# TODO update the JSON string below
json = "{}"
# create an instance of CounterList from a JSON string
counter_list_instance = CounterList.from_json(json)
# print the JSON string representation of the object
print CounterList.to_json()

# convert the object into a dict
counter_list_dict = counter_list_instance.to_dict()
# create an instance of CounterList from a dict
counter_list_form_dict = counter_list.from_dict(counter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


