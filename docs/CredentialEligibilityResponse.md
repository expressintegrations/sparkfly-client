# CredentialEligibilityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_eligible** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sparkfly_client.models.credential_eligibility_response import CredentialEligibilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialEligibilityResponse from a JSON string
credential_eligibility_response_instance = CredentialEligibilityResponse.from_json(json)
# print the JSON string representation of the object
print CredentialEligibilityResponse.to_json()

# convert the object into a dict
credential_eligibility_response_dict = credential_eligibility_response_instance.to_dict()
# create an instance of CredentialEligibilityResponse from a dict
credential_eligibility_response_form_dict = credential_eligibility_response.from_dict(credential_eligibility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


