# RedemptionList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**credentials** | [**List[CredentialResponse]**](CredentialResponse.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.redemption_list import RedemptionList

# TODO update the JSON string below
json = "{}"
# create an instance of RedemptionList from a JSON string
redemption_list_instance = RedemptionList.from_json(json)
# print the JSON string representation of the object
print RedemptionList.to_json()

# convert the object into a dict
redemption_list_dict = redemption_list_instance.to_dict()
# create an instance of RedemptionList from a dict
redemption_list_form_dict = redemption_list.from_dict(redemption_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


