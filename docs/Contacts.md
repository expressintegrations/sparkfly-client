# Contacts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | [**Contact**](Contact.md) |  | [optional] 
**secondary** | [**Contact**](Contact.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.contacts import Contacts

# TODO update the JSON string below
json = "{}"
# create an instance of Contacts from a JSON string
contacts_instance = Contacts.from_json(json)
# print the JSON string representation of the object
print Contacts.to_json()

# convert the object into a dict
contacts_dict = contacts_instance.to_dict()
# create an instance of Contacts from a dict
contacts_form_dict = contacts.from_dict(contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


