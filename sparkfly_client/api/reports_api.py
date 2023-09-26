# coding: utf-8

"""
    Sparkfly API

    # Getting Started ## Overview  The Sparkfly Platform provides a full lifecycle for promotions and rewards from creation to distribution to settlement. The platform integrates in real-time at the point-of-sale and provides item level discounting and tracking. The capabilities of the Sparkfly Platform are available through the use of the Sparkfly Platform API. ## General API Information The Sparkfly Platform API is implemented using a RESTful interface that allows access to all functionality of the Sparkfly Platform. Communication with the API is performed using HTTPS on port 443.\\n  ## Request / Response The Sparkfly Platform API supports the JSON data serialization format. The HTTP Content-Type header is used to specify the request format and the HTTP Accept header or a URI extension is used to specify the response format. Content-Type is required if a transaction includes a request body. Either the Accept Header or URI Extension is required if a transaction includes a response body. The URI Extension will take precedence if a conflicting Accept Header and URI Extension are received.  | Format | Content-Type | Accept-Header | URI Extension | ------ | ------------ | ------------- | ------------- | JSON | application/json | application/json | .json  ### Sample JSON Request with Headers We use cURL for demonstration purposes, but you can use any client of your choosing. ### Request ``` $ curl -i --header 'X-Auth-Token: 228b236272b6ffc7be0496a5f8186f4767afa3ade292ea1565831892941bb6cd' \\       --header 'Content-Type: application/json' https://api.sparkfly.com/v1.0/members/1 ``` ### Response Headers ``` HTTP/1.1 200 OK Content-Type: application/json; charset=utf-8 X-Runtime: 0.042759 Content-Length: 153 ``` The request would work the same way if we had sent .json at the end of the request URI (/v1.0/members/1.json) instead of sending the \\\"application/json\\\" header. ## Authentication Authentication is performed against the API by providing a specified Account ID and API key within the HTTP x-headers as X-Auth-Identity and X-Auth-Key. Accounts have particular privileges providing various levels of access to resources within the platform. ### Request ``` $ curl -i --header 'X-Auth-Identity: <SPARKFLY_PROVIDED_ID>' \\       --header 'X-Auth-Key: <SPARKFLY_PROVIDED_KEY>' \\       https://api.sparkfly.com/auth ```  ### Response Headers ``` HTTP/1.1 204 No Content X-Auth-Token: ab598e824fd304af32fe34ed4a1af1210ce226ecf05c5f043a4f388d3ab74b12 ``` Note how the response headers will contain an X-Auth-Token. All future API operations will only need to pass the received X-Auth-Token for authentication. Tokens will be valid for 24 hours. Applications must be developed in order to re-authenticate if an invalid token is used. ## API Versioning The API version is required and is indicated in the first element of the URI and will take the form: v[VERSION].  API version numbers will only be incremented when functionality is added that breaks compatibility with previous API versions.  Example: https://api.sparkfly.com/v1.0/ ## API Operations Please see the main section of the documentation for request/response examples of the actions that are possible. # Sample Implementation The purpose of this document is to give you a basic overview of some of the core API features. It assumes you already have API credentials and access to the Admin Portal.  ## Authentication The first thing you will want to do is use your provided API credentials to authenticate and get an authentication token. Please see the documentation concerning authentication for more information. In all the requests below, we will need to send our API token in our request headers.  ## Members A typical setup step will be to tell the API about your user database. This way, you can create offers for your members. First let's see if there are any users in the database.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' https://api-staging.sparkfly.com/v1.0/members.json ```  ### Status  ``` HTTP/1.1 200 OK ``` ### Body ``` {   \"page\": 1,   \"per_page\": 50,   \"total_entries\": 0,   \"total_pages\": 0,   \"members\": [] } ```  We can see that there are no members yet. Let's create one.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -XPOST -d '{ \"member\": { \"identifier\": \"unique-member-id\" } }' \\       https://api-staging.sparkfly.com/v1.0/members.json ```  ### Status ``` HTTP/1.1 201 Created ```  ### Body ``` {   \"member\": {     \"identifier\": \"unique-member-id\",     \"notification_mode\": \"app\",     \"id\": 1009,     \"created_at\": \"2013-01-28T21:44:10Z\",     \"updated_at\": \"2013-01-28T21:44:10Z\"   } } ```  First, we send a POST to /v1.0/members.json to create our new member. The only thing you need to provide is a unique identifier to relate the member back to your system. You can repeat this any number of times until all of your users are loaded. Notice how in the response body, the newly created member has an ID of 1009. We can use that to request a specific member (or any resource) in the system at a later time by using the ID like so:  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       https://api-staging.sparkfly.com/v1.0/members/1009.json ```  ### Status ``` HTTP/1.1 200 OK ```  ### Body ``` {   \"member\": {     \"identifier\": \"unique-member-id\",     \"notification_mode\": \"app\",     \"id\": 1009,     \"created_at\": \"2013-01-28T21:44:10Z\",     \"updated_at\": \"2013-01-28T21:44:10Z\"   } } ```  If a member is coming from your application, you may also wish to search for them by your internal identifier. You can do that by querying the member search API endpoint:   ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       https://api-staging.sparkfly.com/v1.0/members/search.json?identifier=unique-member-id ```  ### Status ``` HTTP/1.1 200 OK ```  ### Body ``` {   \"member\": {     \"identifier\": \"unique-member-id\",     \"notification_mode\": \"app\",     \"id\": 1009,     \"created_at\": \"2013-01-28T21:44:10Z\",     \"updated_at\": \"2013-01-28T21:44:10Z\"   } } ```  ## Offers Next we'll want to set up an offer. You can create and configure a offer using the API if desired, but it it usually easier to do this through the Admin Portal. Follow the instructions in the Portal, and by the end of the process you should have at least one Merchant, and an Offer (this is the minimum setup needed to run an offer and generate codes for your members). It is also important to note that a Offer will be run by one or more Channels. A Channel is linked to a offer in a way that allows the system to track where your members are coming from, so that you can view offer statistics and control the number of members that redeem a offer.\\n\\nAssuming we're done setting things up, let's query for our offer and make sure everything is working ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' https://api-staging.sparkfly.com/v1.0/offers.json ``` ### Status ``` HTTP/1.1 200 OK ```  ### Body ``` {   \"page\": 1,   \"per_page\": 50,   \"total_entries\": 1,   \"total_pages\": 1,   \"offers\": [     {       \"offer\": {         \"id\": 1701,         \"name\": \"Buy a Burger, Get Free Medium Fries\",         \"description\": null,         \"offer_type\": 0,         \"offer_code\": null,         \"points_earning_value\": null,         \"points_required_value\": null,         \"reward_item_description\": null,         \"reward_item_value\": null,         \"terms_and_conditions\": null,         \"quest_only\": false,         \"max_amount\": null,         \"min_spend_amount\": null,         \"max_redemptions\": null,         \"max_redemptions_per_member\": null,         \"max_redemptions_per_member_per_day\": null,         \"merchant_name\": null,         \"activates_at\": null,         \"expires_at\": null,         \"stop_offering_at\": null,         \"created_at\": \"2013-01-28T22:25:33Z\",         \"updated_at\": \"2013-01-28T22:25:33Z\"       }     }   ] } ``` Great! Now we can see our offer \"Buy a Burger, Get Free Medium Fries\"  ## Creating Credentials For Members After we release our offer, we will want to generate redeemable codes for our members. We do this by creating a record called a Credential. A Credential includes a code which allows a member to redeem a offer at a given location. A typical scenario might go something like this. A member is in your store and is using your Cool Mobile App (Channel ID 456), they click a button that says \"Redeem Now\", and you app triggers a backend query to the Sparkfly Platform to generate a credential like so  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -X POST \\       https://api-staging.sparkfly.com/v1.0/credentials.json?member_id=1009&offer_id=1701&channel_id=456 ```  ### Status ``` HTTP/1.1 201 Created ``` ### Body ``` {   \"credential\": {     \"id\": 578,     \"identifier\": \"3540\",     \"status\": \"open\",     \"member_id\": 1009,     \"offer_id\": 1701,     \"store_id\": 1,     \"merchant_id\": 251,     \"redeemed_at\": null,     \"voided_at\": null,     \"offer_name\": \"Buy a Burger, Get Free Medium Fries\",     \"merchant_name\": \"Q Burger\",     \"location_address\": null,     \"code_lifetime\": null   } } ``` Congratulations! You now have a Credential that you can display for your user. The key thing to look for here is the identifier field, \"3540\". This code is what can be entered in at the point of sale to trigger a redemption in Sparkfly's system!  Check out the section entitled Credentials In Depth if you run into any problems, or need more information on generating credentials.  ## Setting Up a Landing Page Sparkfly provides a web-based landing page for any offer that you would like to have take advantage of this capability. The landing page provides additional tracking information in the form of Impressions, as well as the option of additional security. The following section explains how to setup an offer to use the landing page via the API.  First, make sure you are authenticated with the API and have at least one created offer.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       https://api-staging.sparkfly.com/v1.0/offers.json ```  ### Body ``` {   \"page\": 1,   \"per_page\": 50,   \"total_entries\": 0,   \"total_pages\": 0,   \"offers\": [] } ``` Since we don't have any offers yet we will create one now. All we need is a name.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -X POST -d '{ \"offer\": { \"name\": \"Test offer\" } }' \\       https://api-staging.sparkfly.com/v1.0/offers.json ```  ### Body  ``` {   \"offer\": {     \"id\": 1290,     \"merchant_id\": null,     \"manufacturer_id\": null,     \"name\": \"Test offer\",     \"description\": null,     \"offer_type\": 0,     \"category\": null,     \"offer_code\": null,     \"pos_offer_code\": null,     \"criteria\": {},     \"points_earning_value\": null,     \"points_required_value\": null,     \"reward_item_description\": null,     \"reward_item_value\": null,     \"terms_and_conditions\": null,     \"quest_only\": false,     \"merchant_name\": null,     \"external_reward\": null,     \"is_reward\": false,     \"locked\": null,     \"activates_at\": null,     \"expires_at\": null,     \"stop_offering_at\": null,     \"max_amount\": null,     \"min_spend_amount\": null,     \"max_redemptions\": null,     \"max_redemptions_per_member\": null,     \"max_redemptions_per_member_per_day\": null,     \"account_id\": 8,     \"required_item_set_id\": null,     \"redemption_item_set_id\": null,     \"required_item_count\": null,     \"redemption_item_count\": null,     \"status\": \"pending\",     \"created_at\": \"2014-02-11T17:44:54Z\",     \"updated_at\": \"2014-02-11T17:44:54Z\",     \"offers\": [],     \"formatting\": {},     \"passbook_configuration\": null,     \"landing_page_urls\": [],     \"channels\": [],     \"item_sets\": [],     \"eligibility\": {       \"merchant_item_set_ids\": [],       \"manufacturer_item_set_ids\": [],       \"merchant_ids\": [],       \"store_list_ids\": [],       \"member_list_ids\": [],       \"channel_ids\": []     }   },   \"errors\": {} } ```  We have created an offer with ID 1290. We also need to approve the offer by sending a PUT request to the approve URL before it will appear correctly on the landing page  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -X PUT \\       https://api-staging.sparkfly.com/v1.0/offers/1290/actions/approve.json ```  Next, make sure you have at least one Channel on which to publish your offer.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       https://api-staging.sparkfly.com/v1.0/channels.json ```  If the total_entries field is 0, we will need to create a channel as well. For demonstration purposes, we'll create a landing page for an email campaign. Again, only a name is required here.   ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -X POST -d '{ \\\"channel\\\": { \"name\": \"Email\" } }' \\       https://api-staging.sparkfly.com/v1.0/channels.json ``` ### Body ``` {   \"channel\": {     \"id\": 5,     \"name\": \"Email\",     \"allow_sms_keyword\": false,     \"allow_hmac\": false,     \"conversion_callback_url\": null   },   \"errors\": {} } ``` Now we also have a channel with an ID of 5, meaning we now have at least one offer and one channel. Now we will need to associate the two. To associate the channel to the offer, we will need to POST to the following URL using your offer ID and a body containing an array with your channel ID. ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\     -X POST -d '{ \"offer\": { \"channel_ids\": [5] } }' \\     https://api-staging.sparkfly.com/v1.0/offers/1290/channels.json ``` We should get a 201 Created response code and something like: ``` {   \"offer\": {     \"channel_ids\": [       5     ],     \"id\": 1290   } } ``` Now if we perform a GET request on the offer, we should see that the channel is associated. The section we are interested in is the field called \"channels\" on the offer. ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\     https://api-staging.sparkfly.com/v1.0/offers/1290.json ```  ### Body (some content omitted) ``` {   \"offer\": {     \"channels\": [       {         \"channel\": {           \"id\": 5,           \"xid\": \"Z7nnWs6\",           \"name\": \"Email\",           \"security\": null,           \"security_key\": null,           \"offer_id\": 1290,           \"sms_keyword\": null,           \"allow_return_later\": true         }       }     ]   } } ``` In particular, pay attention to the \"xid\" field. This is an identifier that links your offer to your channel, and it will act as the landing page URL. I should now be able to visit the landing page, with the xid as the path, and see my offer. For example, in the staging environment, our landing page would be: https://mp-staging.sparkfly.com/Z7nnWs6  ### Note Landing pages are cached for performance, and are re-cached every hour. If you go to a landing page, and get a 404 or do not see your changes, you may need to wait up to an hour for the page to be updated.  So at this point, we should be able to see a relatively plain offer page. Let's add a banner image to show up at the top of the landing page. To add an image, we will need to update the offer field called \"formatting\" on the offer, by sending a PUT request. Formatting is a nested object which contains a field called \"bg_image\". If we update bg_image, it should show up on the landing page:  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\         -X PUT -d '{ \"offer\": { \"formatting\": { \"bg_image\": \"https://my-domain/banner_image.png\" } } }' \\         https://api-staging.sparkfly.com/v1.0/offers/1290.json ```  We should get a 200 response that shows our bg_image in the response.  The recommended size for a banner image is 1200x600px. You can also set a background color for the header by setting \"bg_color\" in the formatting options, like so: ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\         -X PUT -d '{ \"offer\": { \"formatting\": { \"bg_image\": \"https://my-domain/banner_image.png\", \"bg_color\": \"#FF00AA\" } } }' \\         https://api-staging.sparkfly.com/v1.0/offers/1290.json ``` ## Other Considerations For security purposes, the landing page is served over SSL. In order to maintain this security, any image you link to should also be served over https.  If you're testing a landing page from a desktop or laptop computer, the default behavior is to show a static, printable code. If you would like to preview what the landing page will look like on a mobile device, you can attach the parameter printable=false to the landing page URL. For example https://mp-staging.sparkfly.com/TRYstCR?printable=false  # Credentials  ## Introduction Credentials are the backbone of the Sparkfly API. When issued correctly, they allow a member to redeem one or more offers. Sparkfly will properly handle the creation, expiration and redemption of identifiers that can be used to link a member to a purchase at the point of sale.  ## Associating Multiple Offers Credentials can exist that allow for more than one offer to be redeemed at a time. We're assuming you have already authenticated an have a valid auth token at this time (see the authentication section for an example). Below is an example of multiple offers on a credential:  ### Associating Multiple Offers First we can create a new credential for our member with id #123. After that is successful, we can attempt to attach our offers.  #### Request ``` $ curl -i -XPOST --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\       'https://api.sparkfly.com/v1.0/credentials.json?member_id=123' ``` ### First JSON Response  #### Response Body ``` {   \"error\": \"channel_id is required\" } ``` Oops! We can see here that the request failed, because we forgot to include a channel_id. If you don't yet have a channel, see the channel API under main to see how to create one. Let's assume we have a working channel, add the ID to the request, and try again.  #### Request ``` $ curl -i -XPOST --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\       'https://api.sparkfly.com/v1.0/credentials.json?member_id=123&channel_id=456' ``` ### Second JSON Response #### Response Body ``` {   \"credential\": {     \"id\": 1009,     \"account_id\": 5,     \"created_at\": \"2013-09-16T18:41:13Z\",     \"updated_at\": \"2013-09-16T18:41:13Z\",     \"identifier\": null,     \"member_id\": 123,     \"store_id\": null,     \"channel_id\": 456,     \"offer_ids\": [],     \"annotations\": {},     \"code_lifetime\": null,     \"supports_barcode\": false,     \"merchant_id\": null,     \"offer_name\": null,     \"merchant_name\": null,     \"location_address\": null,     \"url\": null   },   \"errors\": {} } ```  Great! Now we get a 201 (Created) response, with associated member and channel IDs. The credential comes back with an ID of 1009. You'll notice that the identifier is \"null\", because there are no associated offers yet (offer_ids is an empty set).  Next we'll want to associate offers so we can get an identifier generated. We can do this by issuing a PUT request to the newly created credential. The first offer we want to associate has an ID of 1011 ``` $ curl -i -XPUT --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\       'https://api.sparkfly.com/v1.0/credentials/1009.json?channel_id=456&offer_ids=1011' ``` ### Third JSON Response #### Response Body ``` {   \"credential\": {     \"id\": 1009,     \"account_id\": 5,     \"created_at\": \"2013-09-16T18:41:13Z\",     \"updated_at\": \"2013-09-16T18:51:23Z\",     \"identifier\": \"3345\",     \"member_id\": 1,     \"store_id\": null,     \"channel_id\": 456,     \"offer_ids\": [       1011     ],     \"annotations\": {},     \"code_lifetime\": null,     \"supports_barcode\": false,     \"merchant_id\": null,     \"offer_name\": \"First Offer\",     \"merchant_name\": null,     \"location_address\": null,     \"url\": null   },   \"errors\": {} } ``` Once the credential is updated, we should see our offer ID in the offer_ids of the response, as well as our newly generated identifier (3345). At this point, the credential is valid and ready to redeem the single offer, with id 1011. ``` $ curl -i -XPUT --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\         'https://api.sparkfly.com/v1.0/credentials/1009.json?channel_id=456&offer_ids=1011' ``` We can repeat this process to add as many offers as needed like so: ``` $ curl -i -XPUT --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\       'https://api.sparkfly.com/v1.0/credentials/1.json?channel_id=456&offer_ids=1011,1116' ``` Assuming both offers are valid, the JSON response will now show both offer_ids associated with the credential. ## Validations and Errors Validation | Error | Solution -----------|-------|--------- Channel ID is not present | Channel can't be blank and must be associated with your account and offer |  Make sure you send channel_id=<your-channel-id> on every request to create or update a credential. You will also need to make sure that the offers you are associating with the credential are also eligible for that same channel (shows up under the offer's eligibility). Member ID is not present |  Member can't be blank |  Make sure you send member_id=<sparkfly-member-id> on every request to create a credential  Associated offer(s) are not approved |  offer <offer-name> must be approved to generate a credential |  When you request an offer by id, the status should show up as approved. (See the Approve Offer action under Offers). Member is not eligible for offer(s) |  Member must be eligible for offer: <offer-name> |  If you have a member list defined for the offer, make sure the member in question is on that list. Additionally, a member may not be eligible for an offer if you have redemption limits set. That is, an offer may have reached the total number of redemptions allowed as a whole, by channel, per member, or you may have hit the daily limit per member per day as defined on the offer itself. One or more offers is not longer active |  Offer with ID <offer-id> is no longer active |  An offer must have an activates_at datetime field that is before the current date, and an expires_at datetime field that is after the current date. Store is not eligible for offer(s) |  Store must be eligible for offer: <offer-name> |  If you have an eligible store list defined for the offer, make sure the store in question is on that list. Remember, store id is optional, and not needed to create a credential. Credential is locked |  This credential is currently locked for processing. Please try again later. |  You had a member who went through the process of attempting to redeem an offer with this credential. In some cases, there may be a slight delay in processing. If a member attempts to immediately re-use a credential before it can be processed, this error may be returned. This shouldn't ever really be seen, but it is something to be aware of during testing.  Requested offers not found |  Offer not found or not eligible by channel, with id: <one-or-more-requested-ids> |  You are trying to associate one or more offers that either can't be found because the ids are not correct, or the offers are not eligible to be run under the channel id you are requesting. Make sure the offers exist and are eligible to appear on the requested channel. If you see the last message that offers were not found, remember that you need to attach eligible channels with each offer that you run. This can be done in the admin portal under the Publishing Channels section of the offer. If you do not see any channels listed at all, you can enable them when creating a merchant account. You will not be able to generate a credential code without at least one channel attached to your offer. ## Channel Callback When a redemption (conversion) event occurs, it is sometimes desired to get a realtime callback posted to your system for real-time tracking purposes. This can be achieved by specifying a conversion_callback_url on a channel that you control. The Sparkfly system can send data to the conversion_callback_url every time an offer is redeemed.  File | Description -----|------------ credential_id |  The Sparkfly ID of the credential that was redeemed.  xid |  The XID for the offer that was redeemed (XID is a unique GUID for offer and channel)  offer_id |   The offer that was redeemed on this channel  offer_ids |  All offers associated with the redeemed credential  store_id |  The Sparkfly ID for the store where the credential was redeemed  redeemed_at |  When the credential was redeemed  status |  The status of the redeemed credential  sf_uid |  The external identifier of the member who redeemed the credential (for promotions that use Sparkfly's landing page)  sf_ac |  The name of the creative that was viewed to generate the credential (for promotions that use Sparkfly's landing page)  You can substitute any of the above values in your conversion_callback_url by using the %{} notation like so: ``` https://my_server.com/callback/%{credential_id}?time_of_redemption=%{redeemed_at} ```  You would then receive a callback on redemption, with the specific values in place of each %{}.  In addition the the parameters named above, any attributes under the \"conv_ids\" key of the credential's annotations will also be available for selection. See the credential creation documentation for examples of how to set the credential's annotations. Any keys that cannot be resolved will result in blank parameters in the final URL. 

    The version of the OpenAPI document: 1.0.23
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from datetime import date, datetime

from pydantic import Field, StrictInt, StrictStr

from typing import List, Optional

from sparkfly_client.models.account_level_merchant_report import AccountLevelMerchantReport
from sparkfly_client.models.impressions_report_data import ImpressionsReportData
from sparkfly_client.models.merchant_report_data import MerchantReportData
from sparkfly_client.models.offer_activity_report import OfferActivityReport
from sparkfly_client.models.redemption_list1 import RedemptionList1

from sparkfly_client.api_client import ApiClient
from sparkfly_client.api_response import ApiResponse
from sparkfly_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ReportsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_all_merchant_data(self, var_from : Annotated[StrictInt, Field(..., description="The first reported datetime to gather data from. Must be paired with the \"to\" parameter.")], to : Annotated[StrictInt, Field(..., description="The last reported datetime to gather data from. Must be paired with the \"from\" parameter.")], **kwargs) -> AccountLevelMerchantReport:  # noqa: E501
        """Generates a report of full Merchant data in a given timeframe for a all Merchants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_merchant_data(var_from, to, async_req=True)
        >>> result = thread.get()

        :param var_from: The first reported datetime to gather data from. Must be paired with the \"to\" parameter. (required)
        :type var_from: int
        :param to: The last reported datetime to gather data from. Must be paired with the \"from\" parameter. (required)
        :type to: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccountLevelMerchantReport
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_all_merchant_data_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_all_merchant_data_with_http_info(var_from, to, **kwargs)  # noqa: E501

    @validate_arguments
    def get_all_merchant_data_with_http_info(self, var_from : Annotated[StrictInt, Field(..., description="The first reported datetime to gather data from. Must be paired with the \"to\" parameter.")], to : Annotated[StrictInt, Field(..., description="The last reported datetime to gather data from. Must be paired with the \"from\" parameter.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Generates a report of full Merchant data in a given timeframe for a all Merchants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_merchant_data_with_http_info(var_from, to, async_req=True)
        >>> result = thread.get()

        :param var_from: The first reported datetime to gather data from. Must be paired with the \"to\" parameter. (required)
        :type var_from: int
        :param to: The last reported datetime to gather data from. Must be paired with the \"from\" parameter. (required)
        :type to: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AccountLevelMerchantReport, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'var_from',
            'to'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_merchant_data" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('var_from') is not None:  # noqa: E501
            _query_params.append(('from', _params['var_from']))

        if _params.get('to') is not None:  # noqa: E501
            _query_params.append(('to', _params['to']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Auth-Token']  # noqa: E501

        _response_types_map = {
            '200': "AccountLevelMerchantReport",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/v1.0/reports/account_level', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_merchant_data(self, merchant_id : Annotated[StrictInt, Field(..., description="The id of the merchant")], var_from : Annotated[StrictInt, Field(..., description="The first reported datetime to gather data from. Must be paired with the \"to\" parameter.")], to : Annotated[StrictInt, Field(..., description="The last reported datetime to gather data from. Must be paired with the \"from\" parameter.")], **kwargs) -> MerchantReportData:  # noqa: E501
        """Generates a report of full Merchant data in a given timeframe for a single Merchant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_merchant_data(merchant_id, var_from, to, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The id of the merchant (required)
        :type merchant_id: int
        :param var_from: The first reported datetime to gather data from. Must be paired with the \"to\" parameter. (required)
        :type var_from: int
        :param to: The last reported datetime to gather data from. Must be paired with the \"from\" parameter. (required)
        :type to: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MerchantReportData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_merchant_data_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_merchant_data_with_http_info(merchant_id, var_from, to, **kwargs)  # noqa: E501

    @validate_arguments
    def get_merchant_data_with_http_info(self, merchant_id : Annotated[StrictInt, Field(..., description="The id of the merchant")], var_from : Annotated[StrictInt, Field(..., description="The first reported datetime to gather data from. Must be paired with the \"to\" parameter.")], to : Annotated[StrictInt, Field(..., description="The last reported datetime to gather data from. Must be paired with the \"from\" parameter.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Generates a report of full Merchant data in a given timeframe for a single Merchant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_merchant_data_with_http_info(merchant_id, var_from, to, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The id of the merchant (required)
        :type merchant_id: int
        :param var_from: The first reported datetime to gather data from. Must be paired with the \"to\" parameter. (required)
        :type var_from: int
        :param to: The last reported datetime to gather data from. Must be paired with the \"from\" parameter. (required)
        :type to: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MerchantReportData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'merchant_id',
            'var_from',
            'to'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_merchant_data" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['merchant_id']:
            _path_params['merchant_id'] = _params['merchant_id']


        # process the query parameters
        _query_params = []
        if _params.get('var_from') is not None:  # noqa: E501
            _query_params.append(('from', _params['var_from']))

        if _params.get('to') is not None:  # noqa: E501
            _query_params.append(('to', _params['to']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Auth-Token']  # noqa: E501

        _response_types_map = {
            '200': "MerchantReportData",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/v1.0/merchants/{merchant_id}/reports/full', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_merchant_impressions(self, merchant_id : Annotated[StrictInt, Field(..., description="The id of the merchant")], var_from : Annotated[StrictInt, Field(..., description="The first reported datetime to gather data from. Must be paired with the \"to\" parameter.")], to : Annotated[StrictInt, Field(..., description="The last reported datetime to gather data from. Must be paired with the \"from\" parameter.")], **kwargs) -> ImpressionsReportData:  # noqa: E501
        """Get Unique Impressions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_merchant_impressions(merchant_id, var_from, to, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The id of the merchant (required)
        :type merchant_id: int
        :param var_from: The first reported datetime to gather data from. Must be paired with the \"to\" parameter. (required)
        :type var_from: int
        :param to: The last reported datetime to gather data from. Must be paired with the \"from\" parameter. (required)
        :type to: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ImpressionsReportData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_merchant_impressions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_merchant_impressions_with_http_info(merchant_id, var_from, to, **kwargs)  # noqa: E501

    @validate_arguments
    def get_merchant_impressions_with_http_info(self, merchant_id : Annotated[StrictInt, Field(..., description="The id of the merchant")], var_from : Annotated[StrictInt, Field(..., description="The first reported datetime to gather data from. Must be paired with the \"to\" parameter.")], to : Annotated[StrictInt, Field(..., description="The last reported datetime to gather data from. Must be paired with the \"from\" parameter.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Unique Impressions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_merchant_impressions_with_http_info(merchant_id, var_from, to, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The id of the merchant (required)
        :type merchant_id: int
        :param var_from: The first reported datetime to gather data from. Must be paired with the \"to\" parameter. (required)
        :type var_from: int
        :param to: The last reported datetime to gather data from. Must be paired with the \"from\" parameter. (required)
        :type to: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ImpressionsReportData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'merchant_id',
            'var_from',
            'to'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_merchant_impressions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['merchant_id']:
            _path_params['merchant_id'] = _params['merchant_id']


        # process the query parameters
        _query_params = []
        if _params.get('var_from') is not None:  # noqa: E501
            _query_params.append(('from', _params['var_from']))

        if _params.get('to') is not None:  # noqa: E501
            _query_params.append(('to', _params['to']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Auth-Token']  # noqa: E501

        _response_types_map = {
            '200': "ImpressionsReportData",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/v1.0/merchants/{merchant_id}/reports/impressions', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_offer_activity(self, from_reported_datetime : Annotated[Optional[datetime], Field(description="The first reported datetime to gather data from. Must be paired with the \"to_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, to_reported_datetime : Annotated[Optional[datetime], Field(description="The last reported datetime to gather data from. Must be paired with the \"from_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, from_processed_datetime : Annotated[Optional[datetime], Field(description="The first processed datetime to gather data from. Must be paired with the \"to_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, to_processed_datetime : Annotated[Optional[datetime], Field(description="The last reported datetime to gather data from. Must be paired with the \"from_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, from_business_date : Annotated[Optional[date], Field(description="The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, to_business_date : Annotated[Optional[date], Field(description="The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, channel_id : Annotated[Optional[StrictInt], Field(description="The id of the channel. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\"")] = None, channel_name : Annotated[Optional[StrictStr], Field(description="The name of the channel. If no channel_id is provided, the program will try to find the id by the channel name. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\"")] = None, offer_id : Annotated[Optional[StrictInt], Field(description="The id of the offer. This is an optional filter.")] = None, type : Annotated[Optional[StrictStr], Field(description="The type of the offer. This is an optional filter.")] = None, campaign_xid : Annotated[Optional[StrictStr], Field(description="The id of the campaign. This is an optional filter.")] = None, credential_identifier : Annotated[Optional[StrictInt], Field(description="The identifier of the credential. This is an optional filter.")] = None, **kwargs) -> List[OfferActivityReport]:  # noqa: E501
        """Generates a report of all offer activity in a given timeframe  # noqa: E501

        Given a timeframe of less than 30 consecutive days, this will generate a report of  all offer activities for your account. Three types of dates are accepted: reported,  processed, and business date, but only one will be used. If more than one date set  is given, it will prioritize the dates in the order given before. Some filters can  also be applied to narrow down the reports given.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_offer_activity(from_reported_datetime, to_reported_datetime, from_processed_datetime, to_processed_datetime, from_business_date, to_business_date, channel_id, channel_name, offer_id, type, campaign_xid, credential_identifier, async_req=True)
        >>> result = thread.get()

        :param from_reported_datetime: The first reported datetime to gather data from. Must be paired with the \"to_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type from_reported_datetime: datetime
        :param to_reported_datetime: The last reported datetime to gather data from. Must be paired with the \"from_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type to_reported_datetime: datetime
        :param from_processed_datetime: The first processed datetime to gather data from. Must be paired with the \"to_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type from_processed_datetime: datetime
        :param to_processed_datetime: The last reported datetime to gather data from. Must be paired with the \"from_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type to_processed_datetime: datetime
        :param from_business_date: The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type from_business_date: date
        :param to_business_date: The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type to_business_date: date
        :param channel_id: The id of the channel. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\"
        :type channel_id: int
        :param channel_name: The name of the channel. If no channel_id is provided, the program will try to find the id by the channel name. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\"
        :type channel_name: str
        :param offer_id: The id of the offer. This is an optional filter.
        :type offer_id: int
        :param type: The type of the offer. This is an optional filter.
        :type type: str
        :param campaign_xid: The id of the campaign. This is an optional filter.
        :type campaign_xid: str
        :param credential_identifier: The identifier of the credential. This is an optional filter.
        :type credential_identifier: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[OfferActivityReport]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_offer_activity_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_offer_activity_with_http_info(from_reported_datetime, to_reported_datetime, from_processed_datetime, to_processed_datetime, from_business_date, to_business_date, channel_id, channel_name, offer_id, type, campaign_xid, credential_identifier, **kwargs)  # noqa: E501

    @validate_arguments
    def get_offer_activity_with_http_info(self, from_reported_datetime : Annotated[Optional[datetime], Field(description="The first reported datetime to gather data from. Must be paired with the \"to_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, to_reported_datetime : Annotated[Optional[datetime], Field(description="The last reported datetime to gather data from. Must be paired with the \"from_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, from_processed_datetime : Annotated[Optional[datetime], Field(description="The first processed datetime to gather data from. Must be paired with the \"to_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, to_processed_datetime : Annotated[Optional[datetime], Field(description="The last reported datetime to gather data from. Must be paired with the \"from_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, from_business_date : Annotated[Optional[date], Field(description="The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, to_business_date : Annotated[Optional[date], Field(description="The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.")] = None, channel_id : Annotated[Optional[StrictInt], Field(description="The id of the channel. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\"")] = None, channel_name : Annotated[Optional[StrictStr], Field(description="The name of the channel. If no channel_id is provided, the program will try to find the id by the channel name. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\"")] = None, offer_id : Annotated[Optional[StrictInt], Field(description="The id of the offer. This is an optional filter.")] = None, type : Annotated[Optional[StrictStr], Field(description="The type of the offer. This is an optional filter.")] = None, campaign_xid : Annotated[Optional[StrictStr], Field(description="The id of the campaign. This is an optional filter.")] = None, credential_identifier : Annotated[Optional[StrictInt], Field(description="The identifier of the credential. This is an optional filter.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Generates a report of all offer activity in a given timeframe  # noqa: E501

        Given a timeframe of less than 30 consecutive days, this will generate a report of  all offer activities for your account. Three types of dates are accepted: reported,  processed, and business date, but only one will be used. If more than one date set  is given, it will prioritize the dates in the order given before. Some filters can  also be applied to narrow down the reports given.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_offer_activity_with_http_info(from_reported_datetime, to_reported_datetime, from_processed_datetime, to_processed_datetime, from_business_date, to_business_date, channel_id, channel_name, offer_id, type, campaign_xid, credential_identifier, async_req=True)
        >>> result = thread.get()

        :param from_reported_datetime: The first reported datetime to gather data from. Must be paired with the \"to_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type from_reported_datetime: datetime
        :param to_reported_datetime: The last reported datetime to gather data from. Must be paired with the \"from_reported_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type to_reported_datetime: datetime
        :param from_processed_datetime: The first processed datetime to gather data from. Must be paired with the \"to_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type from_processed_datetime: datetime
        :param to_processed_datetime: The last reported datetime to gather data from. Must be paired with the \"from_processed_datetime\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type to_processed_datetime: datetime
        :param from_business_date: The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type from_business_date: date
        :param to_business_date: The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request. The duration between the \"from\" and \"to\" dates must not exceed 1 day.
        :type to_business_date: date
        :param channel_id: The id of the channel. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\"
        :type channel_id: int
        :param channel_name: The name of the channel. If no channel_id is provided, the program will try to find the id by the channel name. If both channel_id AND channel_name are missing, the request will return a \"400 - Bad Request\"
        :type channel_name: str
        :param offer_id: The id of the offer. This is an optional filter.
        :type offer_id: int
        :param type: The type of the offer. This is an optional filter.
        :type type: str
        :param campaign_xid: The id of the campaign. This is an optional filter.
        :type campaign_xid: str
        :param credential_identifier: The identifier of the credential. This is an optional filter.
        :type credential_identifier: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[OfferActivityReport], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'from_reported_datetime',
            'to_reported_datetime',
            'from_processed_datetime',
            'to_processed_datetime',
            'from_business_date',
            'to_business_date',
            'channel_id',
            'channel_name',
            'offer_id',
            'type',
            'campaign_xid',
            'credential_identifier'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_offer_activity" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('from_reported_datetime') is not None:  # noqa: E501
            if isinstance(_params['from_reported_datetime'], datetime):
                _query_params.append(('from_reported_datetime', _params['from_reported_datetime'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('from_reported_datetime', _params['from_reported_datetime']))

        if _params.get('to_reported_datetime') is not None:  # noqa: E501
            if isinstance(_params['to_reported_datetime'], datetime):
                _query_params.append(('to_reported_datetime', _params['to_reported_datetime'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('to_reported_datetime', _params['to_reported_datetime']))

        if _params.get('from_processed_datetime') is not None:  # noqa: E501
            if isinstance(_params['from_processed_datetime'], datetime):
                _query_params.append(('from_processed_datetime', _params['from_processed_datetime'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('from_processed_datetime', _params['from_processed_datetime']))

        if _params.get('to_processed_datetime') is not None:  # noqa: E501
            if isinstance(_params['to_processed_datetime'], datetime):
                _query_params.append(('to_processed_datetime', _params['to_processed_datetime'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('to_processed_datetime', _params['to_processed_datetime']))

        if _params.get('from_business_date') is not None:  # noqa: E501
            if isinstance(_params['from_business_date'], date):
                _query_params.append(('from_business_date', _params['from_business_date'].strftime(self.api_client.configuration.date_format)))
            else:
                _query_params.append(('from_business_date', _params['from_business_date']))

        if _params.get('to_business_date') is not None:  # noqa: E501
            if isinstance(_params['to_business_date'], date):
                _query_params.append(('to_business_date', _params['to_business_date'].strftime(self.api_client.configuration.date_format)))
            else:
                _query_params.append(('to_business_date', _params['to_business_date']))

        if _params.get('channel_id') is not None:  # noqa: E501
            _query_params.append(('channel_id', _params['channel_id']))

        if _params.get('channel_name') is not None:  # noqa: E501
            _query_params.append(('channel_name', _params['channel_name']))

        if _params.get('offer_id') is not None:  # noqa: E501
            _query_params.append(('offer_id', _params['offer_id']))

        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type']))

        if _params.get('campaign_xid') is not None:  # noqa: E501
            _query_params.append(('campaign_xid', _params['campaign_xid']))

        if _params.get('credential_identifier') is not None:  # noqa: E501
            _query_params.append(('credential_identifier', _params['credential_identifier']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Auth-Token']  # noqa: E501

        _response_types_map = {
            '200': "List[OfferActivityReport]",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/v1.0/reports/offer_activity', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_offer_redemptions(self, from_business_date : Annotated[Optional[datetime], Field(description="The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request.")] = None, to_business_date : Annotated[Optional[datetime], Field(description="The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request.")] = None, from_redemption_datetime : Annotated[Optional[datetime], Field(description="The first redemption datetime to gather data from. Must be paired with the \"to_redemption_datetime\" parameter. One pair of dates must be provided in the request.")] = None, to_redemption_datetime : Annotated[Optional[datetime], Field(description="The last redemption datetime to gather data from. Must be paired with the \"from_redemption_datetime\" parameter. One pair of dates must be provided in the request.")] = None, bi_storelist : Annotated[Optional[StrictInt], Field(description="The ID of the Store List. Filters the redemptions using the Stores from the given Store List. If not given, ALL Store Lists and the corresponding Stores will be used to filter the results.")] = None, **kwargs) -> RedemptionList1:  # noqa: E501
        """Generates a report of all offer redemptions for a given timeframe and store list  # noqa: E501

        Given a timeframe, this will generate a report of all offer activities for your account.  Two types of dates are accepted: business date and redemption date, but only one can be used.  If more than one date set is given, an error will be returned. Some filters can  also be applied to narrow down the reports given.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_offer_redemptions(from_business_date, to_business_date, from_redemption_datetime, to_redemption_datetime, bi_storelist, async_req=True)
        >>> result = thread.get()

        :param from_business_date: The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request.
        :type from_business_date: datetime
        :param to_business_date: The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request.
        :type to_business_date: datetime
        :param from_redemption_datetime: The first redemption datetime to gather data from. Must be paired with the \"to_redemption_datetime\" parameter. One pair of dates must be provided in the request.
        :type from_redemption_datetime: datetime
        :param to_redemption_datetime: The last redemption datetime to gather data from. Must be paired with the \"from_redemption_datetime\" parameter. One pair of dates must be provided in the request.
        :type to_redemption_datetime: datetime
        :param bi_storelist: The ID of the Store List. Filters the redemptions using the Stores from the given Store List. If not given, ALL Store Lists and the corresponding Stores will be used to filter the results.
        :type bi_storelist: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RedemptionList1
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_offer_redemptions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_offer_redemptions_with_http_info(from_business_date, to_business_date, from_redemption_datetime, to_redemption_datetime, bi_storelist, **kwargs)  # noqa: E501

    @validate_arguments
    def get_offer_redemptions_with_http_info(self, from_business_date : Annotated[Optional[datetime], Field(description="The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request.")] = None, to_business_date : Annotated[Optional[datetime], Field(description="The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request.")] = None, from_redemption_datetime : Annotated[Optional[datetime], Field(description="The first redemption datetime to gather data from. Must be paired with the \"to_redemption_datetime\" parameter. One pair of dates must be provided in the request.")] = None, to_redemption_datetime : Annotated[Optional[datetime], Field(description="The last redemption datetime to gather data from. Must be paired with the \"from_redemption_datetime\" parameter. One pair of dates must be provided in the request.")] = None, bi_storelist : Annotated[Optional[StrictInt], Field(description="The ID of the Store List. Filters the redemptions using the Stores from the given Store List. If not given, ALL Store Lists and the corresponding Stores will be used to filter the results.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Generates a report of all offer redemptions for a given timeframe and store list  # noqa: E501

        Given a timeframe, this will generate a report of all offer activities for your account.  Two types of dates are accepted: business date and redemption date, but only one can be used.  If more than one date set is given, an error will be returned. Some filters can  also be applied to narrow down the reports given.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_offer_redemptions_with_http_info(from_business_date, to_business_date, from_redemption_datetime, to_redemption_datetime, bi_storelist, async_req=True)
        >>> result = thread.get()

        :param from_business_date: The first business date to gather data from. Must be paired with the \"to_business_date\" parameter. One pair of dates must be provided in the request.
        :type from_business_date: datetime
        :param to_business_date: The last business date to gather data from. Must be paired with the \"from_business_date\" parameter. One pair of dates must be provided in the request.
        :type to_business_date: datetime
        :param from_redemption_datetime: The first redemption datetime to gather data from. Must be paired with the \"to_redemption_datetime\" parameter. One pair of dates must be provided in the request.
        :type from_redemption_datetime: datetime
        :param to_redemption_datetime: The last redemption datetime to gather data from. Must be paired with the \"from_redemption_datetime\" parameter. One pair of dates must be provided in the request.
        :type to_redemption_datetime: datetime
        :param bi_storelist: The ID of the Store List. Filters the redemptions using the Stores from the given Store List. If not given, ALL Store Lists and the corresponding Stores will be used to filter the results.
        :type bi_storelist: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(RedemptionList1, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'from_business_date',
            'to_business_date',
            'from_redemption_datetime',
            'to_redemption_datetime',
            'bi_storelist'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_offer_redemptions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('from_business_date') is not None:  # noqa: E501
            if isinstance(_params['from_business_date'], datetime):
                _query_params.append(('from_business_date', _params['from_business_date'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('from_business_date', _params['from_business_date']))

        if _params.get('to_business_date') is not None:  # noqa: E501
            if isinstance(_params['to_business_date'], datetime):
                _query_params.append(('to_business_date', _params['to_business_date'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('to_business_date', _params['to_business_date']))

        if _params.get('from_redemption_datetime') is not None:  # noqa: E501
            if isinstance(_params['from_redemption_datetime'], datetime):
                _query_params.append(('from_redemption_datetime', _params['from_redemption_datetime'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('from_redemption_datetime', _params['from_redemption_datetime']))

        if _params.get('to_redemption_datetime') is not None:  # noqa: E501
            if isinstance(_params['to_redemption_datetime'], datetime):
                _query_params.append(('to_redemption_datetime', _params['to_redemption_datetime'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('to_redemption_datetime', _params['to_redemption_datetime']))

        if _params.get('bi_storelist') is not None:  # noqa: E501
            _query_params.append(('bi_storelist', _params['bi_storelist']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Auth-Token']  # noqa: E501

        _response_types_map = {
            '200': "RedemptionList1",
            '400': None,
            '422': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/v1.0/reports/redemptions', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
