# EligibleItemSetInputRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible_item_set** | [**EligibleItemSetInput**](EligibleItemSetInput.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.eligible_item_set_input_request import EligibleItemSetInputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleItemSetInputRequest from a JSON string
eligible_item_set_input_request_instance = EligibleItemSetInputRequest.from_json(json)
# print the JSON string representation of the object
print EligibleItemSetInputRequest.to_json()

# convert the object into a dict
eligible_item_set_input_request_dict = eligible_item_set_input_request_instance.to_dict()
# create an instance of EligibleItemSetInputRequest from a dict
eligible_item_set_input_request_form_dict = eligible_item_set_input_request.from_dict(eligible_item_set_input_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


