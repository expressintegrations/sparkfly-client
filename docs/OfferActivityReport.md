# OfferActivityReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**credential_identifier** | **str** |  | [optional] 
**reported_at** | **str** |  | [optional] 
**processed_at** | **str** |  | [optional] 
**business_date** | **str** |  | [optional] 
**type** | **str** | Type value definitions:   * &#39;redeem&#39; - occurs when a previously issued offer is redeemed   * &#39;expire&#39; - occurs when a previously issued offer passes its expiration date and can no longer be used   * &#39;issue&#39; - occurs when an offer is issued.   * &#39;void&#39; - occurs when a previously issued offer is voided.   * &#39;suspend&#39; - occurs when a previously issued offer enters a suspended state.   * &#39;unsuspend&#39; - occurs when a previously issued offer enters an unsuspended state.  | [optional] 
**offer_id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**member** | [**MemberInfo**](MemberInfo.md) |  | [optional] 
**offer_state** | [**OfferStateInfo**](OfferStateInfo.md) |  | [optional] 

## Example

```python
from sparkfly_client.models.offer_activity_report import OfferActivityReport

# TODO update the JSON string below
json = "{}"
# create an instance of OfferActivityReport from a JSON string
offer_activity_report_instance = OfferActivityReport.from_json(json)
# print the JSON string representation of the object
print OfferActivityReport.to_json()

# convert the object into a dict
offer_activity_report_dict = offer_activity_report_instance.to_dict()
# create an instance of OfferActivityReport from a dict
offer_activity_report_form_dict = offer_activity_report.from_dict(offer_activity_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


