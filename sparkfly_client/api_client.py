# coding: utf-8

"""
    Sparkfly API

    # Getting Started ## Overview  The Sparkfly Platform provides a full lifecycle for promotions and rewards from creation to distribution to settlement. The platform integrates in real-time at the point-of-sale and provides item level discounting and tracking. The capabilities of the Sparkfly Platform are available through the use of the Sparkfly Platform API. ## General API Information The Sparkfly Platform API is implemented using a RESTful interface that allows access to all functionality of the Sparkfly Platform. Communication with the API is performed using HTTPS on port 443.\\n  ## Request / Response The Sparkfly Platform API supports the JSON data serialization format. The HTTP Content-Type header is used to specify the request format and the HTTP Accept header or a URI extension is used to specify the response format. Content-Type is required if a transaction includes a request body. Either the Accept Header or URI Extension is required if a transaction includes a response body. The URI Extension will take precedence if a conflicting Accept Header and URI Extension are received.  | Format | Content-Type | Accept-Header | URI Extension | ------ | ------------ | ------------- | ------------- | JSON | application/json | application/json | .json  ### Sample JSON Request with Headers We use cURL for demonstration purposes, but you can use any client of your choosing. ### Request ``` $ curl -i --header 'X-Auth-Token: 228b236272b6ffc7be0496a5f8186f4767afa3ade292ea1565831892941bb6cd' \\       --header 'Content-Type: application/json' https://api.sparkfly.com/v1.0/members/1 ``` ### Response Headers ``` HTTP/1.1 200 OK Content-Type: application/json; charset=utf-8 X-Runtime: 0.042759 Content-Length: 153 ``` The request would work the same way if we had sent .json at the end of the request URI (/v1.0/members/1.json) instead of sending the \\\"application/json\\\" header. ## Authentication Authentication is performed against the API by providing a specified Account ID and API key within the HTTP x-headers as X-Auth-Identity and X-Auth-Key. Accounts have particular privileges providing various levels of access to resources within the platform. ### Request ``` $ curl -i --header 'X-Auth-Identity: <SPARKFLY_PROVIDED_ID>' \\       --header 'X-Auth-Key: <SPARKFLY_PROVIDED_KEY>' \\       https://api.sparkfly.com/auth ```  ### Response Headers ``` HTTP/1.1 204 No Content X-Auth-Token: ab598e824fd304af32fe34ed4a1af1210ce226ecf05c5f043a4f388d3ab74b12 ``` Note how the response headers will contain an X-Auth-Token. All future API operations will only need to pass the received X-Auth-Token for authentication. Tokens will be valid for 24 hours. Applications must be developed in order to re-authenticate if an invalid token is used. ## API Versioning The API version is required and is indicated in the first element of the URI and will take the form: v[VERSION].  API version numbers will only be incremented when functionality is added that breaks compatibility with previous API versions.  Example: https://api.sparkfly.com/v1.0/ ## API Operations Please see the main section of the documentation for request/response examples of the actions that are possible. # Sample Implementation The purpose of this document is to give you a basic overview of some of the core API features. It assumes you already have API credentials and access to the Admin Portal.  ## Authentication The first thing you will want to do is use your provided API credentials to authenticate and get an authentication token. Please see the documentation concerning authentication for more information. In all the requests below, we will need to send our API token in our request headers.  ## Members A typical setup step will be to tell the API about your user database. This way, you can create offers for your members. First let's see if there are any users in the database.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' https://api-staging.sparkfly.com/v1.0/members.json ```  ### Status  ``` HTTP/1.1 200 OK ``` ### Body ``` {   \"page\": 1,   \"per_page\": 50,   \"total_entries\": 0,   \"total_pages\": 0,   \"members\": [] } ```  We can see that there are no members yet. Let's create one.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -XPOST -d '{ \"member\": { \"identifier\": \"unique-member-id\" } }' \\       https://api-staging.sparkfly.com/v1.0/members.json ```  ### Status ``` HTTP/1.1 201 Created ```  ### Body ``` {   \"member\": {     \"identifier\": \"unique-member-id\",     \"notification_mode\": \"app\",     \"id\": 1009,     \"created_at\": \"2013-01-28T21:44:10Z\",     \"updated_at\": \"2013-01-28T21:44:10Z\"   } } ```  First, we send a POST to /v1.0/members.json to create our new member. The only thing you need to provide is a unique identifier to relate the member back to your system. You can repeat this any number of times until all of your users are loaded. Notice how in the response body, the newly created member has an ID of 1009. We can use that to request a specific member (or any resource) in the system at a later time by using the ID like so:  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       https://api-staging.sparkfly.com/v1.0/members/1009.json ```  ### Status ``` HTTP/1.1 200 OK ```  ### Body ``` {   \"member\": {     \"identifier\": \"unique-member-id\",     \"notification_mode\": \"app\",     \"id\": 1009,     \"created_at\": \"2013-01-28T21:44:10Z\",     \"updated_at\": \"2013-01-28T21:44:10Z\"   } } ```  If a member is coming from your application, you may also wish to search for them by your internal identifier. You can do that by querying the member search API endpoint:   ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       https://api-staging.sparkfly.com/v1.0/members/search.json?identifier=unique-member-id ```  ### Status ``` HTTP/1.1 200 OK ```  ### Body ``` {   \"member\": {     \"identifier\": \"unique-member-id\",     \"notification_mode\": \"app\",     \"id\": 1009,     \"created_at\": \"2013-01-28T21:44:10Z\",     \"updated_at\": \"2013-01-28T21:44:10Z\"   } } ```  ## Offers Next we'll want to set up an offer. You can create and configure a offer using the API if desired, but it it usually easier to do this through the Admin Portal. Follow the instructions in the Portal, and by the end of the process you should have at least one Merchant, and an Offer (this is the minimum setup needed to run an offer and generate codes for your members). It is also important to note that a Offer will be run by one or more Channels. A Channel is linked to a offer in a way that allows the system to track where your members are coming from, so that you can view offer statistics and control the number of members that redeem a offer.\\n\\nAssuming we're done setting things up, let's query for our offer and make sure everything is working ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' https://api-staging.sparkfly.com/v1.0/offers.json ``` ### Status ``` HTTP/1.1 200 OK ```  ### Body ``` {   \"page\": 1,   \"per_page\": 50,   \"total_entries\": 1,   \"total_pages\": 1,   \"offers\": [     {       \"offer\": {         \"id\": 1701,         \"name\": \"Buy a Burger, Get Free Medium Fries\",         \"description\": null,         \"offer_type\": 0,         \"offer_code\": null,         \"points_earning_value\": null,         \"points_required_value\": null,         \"reward_item_description\": null,         \"reward_item_value\": null,         \"terms_and_conditions\": null,         \"quest_only\": false,         \"max_amount\": null,         \"min_spend_amount\": null,         \"max_redemptions\": null,         \"max_redemptions_per_member\": null,         \"max_redemptions_per_member_per_day\": null,         \"merchant_name\": null,         \"activates_at\": null,         \"expires_at\": null,         \"stop_offering_at\": null,         \"created_at\": \"2013-01-28T22:25:33Z\",         \"updated_at\": \"2013-01-28T22:25:33Z\"       }     }   ] } ``` Great! Now we can see our offer \"Buy a Burger, Get Free Medium Fries\"  ## Creating Credentials For Members After we release our offer, we will want to generate redeemable codes for our members. We do this by creating a record called a Credential. A Credential includes a code which allows a member to redeem a offer at a given location. A typical scenario might go something like this. A member is in your store and is using your Cool Mobile App (Channel ID 456), they click a button that says \"Redeem Now\", and you app triggers a backend query to the Sparkfly Platform to generate a credential like so  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -X POST \\       https://api-staging.sparkfly.com/v1.0/credentials.json?member_id=1009&offer_id=1701&channel_id=456 ```  ### Status ``` HTTP/1.1 201 Created ``` ### Body ``` {   \"credential\": {     \"id\": 578,     \"identifier\": \"3540\",     \"status\": \"open\",     \"member_id\": 1009,     \"offer_id\": 1701,     \"store_id\": 1,     \"merchant_id\": 251,     \"redeemed_at\": null,     \"voided_at\": null,     \"offer_name\": \"Buy a Burger, Get Free Medium Fries\",     \"merchant_name\": \"Q Burger\",     \"location_address\": null,     \"code_lifetime\": null   } } ``` Congratulations! You now have a Credential that you can display for your user. The key thing to look for here is the identifier field, \"3540\". This code is what can be entered in at the point of sale to trigger a redemption in Sparkfly's system!  Check out the section entitled Credentials In Depth if you run into any problems, or need more information on generating credentials.  ## Setting Up a Landing Page Sparkfly provides a web-based landing page for any offer that you would like to have take advantage of this capability. The landing page provides additional tracking information in the form of Impressions, as well as the option of additional security. The following section explains how to setup an offer to use the landing page via the API.  First, make sure you are authenticated with the API and have at least one created offer.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       https://api-staging.sparkfly.com/v1.0/offers.json ```  ### Body ``` {   \"page\": 1,   \"per_page\": 50,   \"total_entries\": 0,   \"total_pages\": 0,   \"offers\": [] } ``` Since we don't have any offers yet we will create one now. All we need is a name.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -X POST -d '{ \"offer\": { \"name\": \"Test offer\" } }' \\       https://api-staging.sparkfly.com/v1.0/offers.json ```  ### Body  ``` {   \"offer\": {     \"id\": 1290,     \"merchant_id\": null,     \"manufacturer_id\": null,     \"name\": \"Test offer\",     \"description\": null,     \"offer_type\": 0,     \"category\": null,     \"offer_code\": null,     \"pos_offer_code\": null,     \"criteria\": {},     \"points_earning_value\": null,     \"points_required_value\": null,     \"reward_item_description\": null,     \"reward_item_value\": null,     \"terms_and_conditions\": null,     \"quest_only\": false,     \"merchant_name\": null,     \"external_reward\": null,     \"is_reward\": false,     \"locked\": null,     \"activates_at\": null,     \"expires_at\": null,     \"stop_offering_at\": null,     \"max_amount\": null,     \"min_spend_amount\": null,     \"max_redemptions\": null,     \"max_redemptions_per_member\": null,     \"max_redemptions_per_member_per_day\": null,     \"account_id\": 8,     \"required_item_set_id\": null,     \"redemption_item_set_id\": null,     \"required_item_count\": null,     \"redemption_item_count\": null,     \"status\": \"pending\",     \"created_at\": \"2014-02-11T17:44:54Z\",     \"updated_at\": \"2014-02-11T17:44:54Z\",     \"offers\": [],     \"formatting\": {},     \"passbook_configuration\": null,     \"landing_page_urls\": [],     \"channels\": [],     \"item_sets\": [],     \"eligibility\": {       \"merchant_item_set_ids\": [],       \"manufacturer_item_set_ids\": [],       \"merchant_ids\": [],       \"store_list_ids\": [],       \"member_list_ids\": [],       \"channel_ids\": []     }   },   \"errors\": {} } ```  We have created an offer with ID 1290. We also need to approve the offer by sending a PUT request to the approve URL before it will appear correctly on the landing page  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -X PUT \\       https://api-staging.sparkfly.com/v1.0/offers/1290/actions/approve.json ```  Next, make sure you have at least one Channel on which to publish your offer.  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       https://api-staging.sparkfly.com/v1.0/channels.json ```  If the total_entries field is 0, we will need to create a channel as well. For demonstration purposes, we'll create a landing page for an email campaign. Again, only a name is required here.   ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\       -X POST -d '{ \\\"channel\\\": { \"name\": \"Email\" } }' \\       https://api-staging.sparkfly.com/v1.0/channels.json ``` ### Body ``` {   \"channel\": {     \"id\": 5,     \"name\": \"Email\",     \"allow_sms_keyword\": false,     \"allow_hmac\": false,     \"conversion_callback_url\": null   },   \"errors\": {} } ``` Now we also have a channel with an ID of 5, meaning we now have at least one offer and one channel. Now we will need to associate the two. To associate the channel to the offer, we will need to POST to the following URL using your offer ID and a body containing an array with your channel ID. ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\     -X POST -d '{ \"offer\": { \"channel_ids\": [5] } }' \\     https://api-staging.sparkfly.com/v1.0/offers/1290/channels.json ``` We should get a 201 Created response code and something like: ``` {   \"offer\": {     \"channel_ids\": [       5     ],     \"id\": 1290   } } ``` Now if we perform a GET request on the offer, we should see that the channel is associated. The section we are interested in is the field called \"channels\" on the offer. ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\     https://api-staging.sparkfly.com/v1.0/offers/1290.json ```  ### Body (some content omitted) ``` {   \"offer\": {     \"channels\": [       {         \"channel\": {           \"id\": 5,           \"xid\": \"Z7nnWs6\",           \"name\": \"Email\",           \"security\": null,           \"security_key\": null,           \"offer_id\": 1290,           \"sms_keyword\": null,           \"allow_return_later\": true         }       }     ]   } } ``` In particular, pay attention to the \"xid\" field. This is an identifier that links your offer to your channel, and it will act as the landing page URL. I should now be able to visit the landing page, with the xid as the path, and see my offer. For example, in the staging environment, our landing page would be: https://mp-staging.sparkfly.com/Z7nnWs6  ### Note Landing pages are cached for performance, and are re-cached every hour. If you go to a landing page, and get a 404 or do not see your changes, you may need to wait up to an hour for the page to be updated.  So at this point, we should be able to see a relatively plain offer page. Let's add a banner image to show up at the top of the landing page. To add an image, we will need to update the offer field called \"formatting\" on the offer, by sending a PUT request. Formatting is a nested object which contains a field called \"bg_image\". If we update bg_image, it should show up on the landing page:  ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\         -X PUT -d '{ \"offer\": { \"formatting\": { \"bg_image\": \"https://my-domain/banner_image.png\" } } }' \\         https://api-staging.sparkfly.com/v1.0/offers/1290.json ```  We should get a 200 response that shows our bg_image in the response.  The recommended size for a banner image is 1200x600px. You can also set a background color for the header by setting \"bg_color\" in the formatting options, like so: ``` $ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\         -X PUT -d '{ \"offer\": { \"formatting\": { \"bg_image\": \"https://my-domain/banner_image.png\", \"bg_color\": \"#FF00AA\" } } }' \\         https://api-staging.sparkfly.com/v1.0/offers/1290.json ``` ## Other Considerations For security purposes, the landing page is served over SSL. In order to maintain this security, any image you link to should also be served over https.  If you're testing a landing page from a desktop or laptop computer, the default behavior is to show a static, printable code. If you would like to preview what the landing page will look like on a mobile device, you can attach the parameter printable=false to the landing page URL. For example https://mp-staging.sparkfly.com/TRYstCR?printable=false  # Credentials  ## Introduction Credentials are the backbone of the Sparkfly API. When issued correctly, they allow a member to redeem one or more offers. Sparkfly will properly handle the creation, expiration and redemption of identifiers that can be used to link a member to a purchase at the point of sale.  ## Associating Multiple Offers Credentials can exist that allow for more than one offer to be redeemed at a time. We're assuming you have already authenticated an have a valid auth token at this time (see the authentication section for an example). Below is an example of multiple offers on a credential:  ### Associating Multiple Offers First we can create a new credential for our member with id #123. After that is successful, we can attempt to attach our offers.  #### Request ``` $ curl -i -XPOST --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\       'https://api.sparkfly.com/v1.0/credentials.json?member_id=123' ``` ### First JSON Response  #### Response Body ``` {   \"error\": \"channel_id is required\" } ``` Oops! We can see here that the request failed, because we forgot to include a channel_id. If you don't yet have a channel, see the channel API under main to see how to create one. Let's assume we have a working channel, add the ID to the request, and try again.  #### Request ``` $ curl -i -XPOST --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\       'https://api.sparkfly.com/v1.0/credentials.json?member_id=123&channel_id=456' ``` ### Second JSON Response #### Response Body ``` {   \"credential\": {     \"id\": 1009,     \"account_id\": 5,     \"created_at\": \"2013-09-16T18:41:13Z\",     \"updated_at\": \"2013-09-16T18:41:13Z\",     \"identifier\": null,     \"member_id\": 123,     \"store_id\": null,     \"channel_id\": 456,     \"offer_ids\": [],     \"annotations\": {},     \"code_lifetime\": null,     \"supports_barcode\": false,     \"merchant_id\": null,     \"offer_name\": null,     \"merchant_name\": null,     \"location_address\": null,     \"url\": null   },   \"errors\": {} } ```  Great! Now we get a 201 (Created) response, with associated member and channel IDs. The credential comes back with an ID of 1009. You'll notice that the identifier is \"null\", because there are no associated offers yet (offer_ids is an empty set).  Next we'll want to associate offers so we can get an identifier generated. We can do this by issuing a PUT request to the newly created credential. The first offer we want to associate has an ID of 1011 ``` $ curl -i -XPUT --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\       'https://api.sparkfly.com/v1.0/credentials/1009.json?channel_id=456&offer_ids=1011' ``` ### Third JSON Response #### Response Body ``` {   \"credential\": {     \"id\": 1009,     \"account_id\": 5,     \"created_at\": \"2013-09-16T18:41:13Z\",     \"updated_at\": \"2013-09-16T18:51:23Z\",     \"identifier\": \"3345\",     \"member_id\": 1,     \"store_id\": null,     \"channel_id\": 456,     \"offer_ids\": [       1011     ],     \"annotations\": {},     \"code_lifetime\": null,     \"supports_barcode\": false,     \"merchant_id\": null,     \"offer_name\": \"First Offer\",     \"merchant_name\": null,     \"location_address\": null,     \"url\": null   },   \"errors\": {} } ``` Once the credential is updated, we should see our offer ID in the offer_ids of the response, as well as our newly generated identifier (3345). At this point, the credential is valid and ready to redeem the single offer, with id 1011. ``` $ curl -i -XPUT --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\         'https://api.sparkfly.com/v1.0/credentials/1009.json?channel_id=456&offer_ids=1011' ``` We can repeat this process to add as many offers as needed like so: ``` $ curl -i -XPUT --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\       'https://api.sparkfly.com/v1.0/credentials/1.json?channel_id=456&offer_ids=1011,1116' ``` Assuming both offers are valid, the JSON response will now show both offer_ids associated with the credential. ## Validations and Errors Validation | Error | Solution -----------|-------|--------- Channel ID is not present | Channel can't be blank and must be associated with your account and offer |  Make sure you send channel_id=<your-channel-id> on every request to create or update a credential. You will also need to make sure that the offers you are associating with the credential are also eligible for that same channel (shows up under the offer's eligibility). Member ID is not present |  Member can't be blank |  Make sure you send member_id=<sparkfly-member-id> on every request to create a credential  Associated offer(s) are not approved |  offer <offer-name> must be approved to generate a credential |  When you request an offer by id, the status should show up as approved. (See the Approve Offer action under Offers). Member is not eligible for offer(s) |  Member must be eligible for offer: <offer-name> |  If you have a member list defined for the offer, make sure the member in question is on that list. Additionally, a member may not be eligible for an offer if you have redemption limits set. That is, an offer may have reached the total number of redemptions allowed as a whole, by channel, per member, or you may have hit the daily limit per member per day as defined on the offer itself. One or more offers is not longer active |  Offer with ID <offer-id> is no longer active |  An offer must have an activates_at datetime field that is before the current date, and an expires_at datetime field that is after the current date. Store is not eligible for offer(s) |  Store must be eligible for offer: <offer-name> |  If you have an eligible store list defined for the offer, make sure the store in question is on that list. Remember, store id is optional, and not needed to create a credential. Credential is locked |  This credential is currently locked for processing. Please try again later. |  You had a member who went through the process of attempting to redeem an offer with this credential. In some cases, there may be a slight delay in processing. If a member attempts to immediately re-use a credential before it can be processed, this error may be returned. This shouldn't ever really be seen, but it is something to be aware of during testing.  Requested offers not found |  Offer not found or not eligible by channel, with id: <one-or-more-requested-ids> |  You are trying to associate one or more offers that either can't be found because the ids are not correct, or the offers are not eligible to be run under the channel id you are requesting. Make sure the offers exist and are eligible to appear on the requested channel. If you see the last message that offers were not found, remember that you need to attach eligible channels with each offer that you run. This can be done in the admin portal under the Publishing Channels section of the offer. If you do not see any channels listed at all, you can enable them when creating a merchant account. You will not be able to generate a credential code without at least one channel attached to your offer. ## Channel Callback When a redemption (conversion) event occurs, it is sometimes desired to get a realtime callback posted to your system for real-time tracking purposes. This can be achieved by specifying a conversion_callback_url on a channel that you control. The Sparkfly system can send data to the conversion_callback_url every time an offer is redeemed.  File | Description -----|------------ credential_id |  The Sparkfly ID of the credential that was redeemed.  xid |  The XID for the offer that was redeemed (XID is a unique GUID for offer and channel)  offer_id |   The offer that was redeemed on this channel  offer_ids |  All offers associated with the redeemed credential  store_id |  The Sparkfly ID for the store where the credential was redeemed  redeemed_at |  When the credential was redeemed  status |  The status of the redeemed credential  sf_uid |  The external identifier of the member who redeemed the credential (for promotions that use Sparkfly's landing page)  sf_ac |  The name of the creative that was viewed to generate the credential (for promotions that use Sparkfly's landing page)  You can substitute any of the above values in your conversion_callback_url by using the %{} notation like so: ``` https://my_server.com/callback/%{credential_id}?time_of_redemption=%{redeemed_at} ```  You would then receive a callback on redemption, with the specific values in place of each %{}.  In addition the the parameters named above, any attributes under the \"conv_ids\" key of the credential's annotations will also be available for selection. See the credential creation documentation for examples of how to set the credential's annotations. Any keys that cannot be resolved will result in blank parameters in the final URL. 

    The version of the OpenAPI document: 1.0.23
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import atexit
import datetime
from dateutil.parser import parse
import json
import mimetypes
from multiprocessing.pool import ThreadPool
import os
import re
import tempfile

from urllib.parse import quote

from sparkfly_client.configuration import Configuration
from sparkfly_client.api_response import ApiResponse
import sparkfly_client.models
from sparkfly_client import rest
from sparkfly_client.exceptions import ApiValueError, ApiException


class ApiClient:
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int, # TODO remove as only py3 is supported?
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }
    _pool = None

    def __init__(self, configuration=None, header_name=None, header_value=None,
                 cookie=None, pool_threads=1) -> None:
        # use default configuration if none is provided
        if configuration is None:
            configuration = Configuration.get_default()
        self.configuration = configuration
        self.pool_threads = pool_threads

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.3/python'
        self.client_side_validation = configuration.client_side_validation

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None
            if hasattr(atexit, 'unregister'):
                atexit.unregister(self.close)

    @property
    def pool(self):
        """Create thread pool on first request
         avoids instantiating unused threadpool for blocking clients.
        """
        if self._pool is None:
            atexit.register(self.close)
            self._pool = ThreadPool(self.pool_threads)
        return self._pool

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value


    _default = None

    @classmethod
    def get_default(cls):
        """Return new instance of ApiClient.

        This method returns newly created, based on default constructor,
        object of ApiClient class or returns a copy of default
        ApiClient.

        :return: The ApiClient object.
        """
        if cls._default is None:
            cls._default = ApiClient()
        return cls._default

    @classmethod
    def set_default(cls, default):
        """Set default instance of ApiClient.

        It stores default ApiClient.

        :param default: object of ApiClient.
        """
        cls._default = default

    def __call_api(
            self, resource_path, method, path_params=None,
            query_params=None, header_params=None, body=None, post_params=None,
            files=None, response_types_map=None, auth_settings=None,
            _return_http_data_only=None, collection_formats=None,
            _preload_content=True, _request_timeout=None, _host=None,
            _request_auth=None):

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)
            post_params.extend(self.files_parameters(files))

        # auth setting
        self.update_params_for_auth(
            header_params, query_params, auth_settings,
            resource_path, method, body,
            request_auth=_request_auth)

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        if _host is None:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            url_query = self.parameters_to_url_query(query_params,
                                                     collection_formats)
            url += "?" + url_query

        try:
            # perform request and return response
            response_data = self.request(
                method, url,
                query_params=query_params,
                headers=header_params,
                post_params=post_params, body=body,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout)
        except ApiException as e:
            if e.body:
                e.body = e.body.decode('utf-8')
            raise e

        self.last_response = response_data

        return_data = None # assuming derialization is not needed
        # data needs deserialization or returns HTTP data (deserialized) only
        if _preload_content or _return_http_data_only:
          response_type = response_types_map.get(str(response_data.status), None)
          if not response_type and isinstance(response_data.status, int) and 100 <= response_data.status <= 599:
              # if not found, look for '1XX', '2XX', etc.
              response_type = response_types_map.get(str(response_data.status)[0] + "XX", None)

          if response_type == "bytearray":
              response_data.data = response_data.data
          else:
              match = None
              content_type = response_data.getheader('content-type')
              if content_type is not None:
                  match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
              encoding = match.group(1) if match else "utf-8"
              response_data.data = response_data.data.decode(encoding)

          # deserialize response data
          if response_type == "bytearray":
              return_data = response_data.data
          elif response_type:
              return_data = self.deserialize(response_data, response_type)
          else:
              return_data = None

        if _return_http_data_only:
            return return_data
        else:
            return ApiResponse(status_code = response_data.status,
                           data = return_data,
                           headers = response_data.getheaders(),
                           raw_data = response_data.data)

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `openapi_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = obj.to_dict()

        return {key: self.sanitize_for_serialization(val)
                for key, val in obj_dict.items()}

    def deserialize(self, response, response_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            return self.__deserialize_file(response)

        # fetch data from response object
        try:
            data = json.loads(response.data)
        except ValueError:
            data = response.data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if isinstance(klass, str):
            if klass.startswith('List['):
                sub_kls = re.match(r'List\[(.*)]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('Dict['):
                sub_kls = re.match(r'Dict\[([^,]*), (.*)]', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in data.items()}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(sparkfly_client.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datetime(data)
        else:
            return self.__deserialize_model(data, klass)

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_types_map=None, auth_settings=None,
                 async_req=None, _return_http_data_only=None,
                 collection_formats=None, _preload_content=True,
                 _request_timeout=None, _host=None, _request_auth=None):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async_req request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_token: dict, optional
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        if not async_req:
            return self.__call_api(resource_path, method,
                                   path_params, query_params, header_params,
                                   body, post_params, files,
                                   response_types_map, auth_settings,
                                   _return_http_data_only, collection_formats,
                                   _preload_content, _request_timeout, _host,
                                   _request_auth)

        return self.pool.apply_async(self.__call_api, (resource_path,
                                                       method, path_params,
                                                       query_params,
                                                       header_params, body,
                                                       post_params, files,
                                                       response_types_map,
                                                       auth_settings,
                                                       _return_http_data_only,
                                                       collection_formats,
                                                       _preload_content,
                                                       _request_timeout,
                                                       _host, _request_auth))

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.get_request(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.head_request(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.options_request(url,
                                            query_params=query_params,
                                            headers=headers,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout)
        elif method == "POST":
            return self.rest_client.post_request(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.put_request(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.patch_request(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.delete_request(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ApiValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def parameters_to_url_query(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: URL query string (e.g. a=Hello%20World&b=123)
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:  # noqa: E501
            if isinstance(v, (int, float)):
                v = str(v)
            if isinstance(v, bool):
                v = str(v).lower()
            if isinstance(v, dict):
                v = json.dumps(v)

            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(quote(str(value)) for value in v)))
            else:
                new_params.append((k, quote(str(v))))

        return "&".join(["=".join(item) for item in new_params])

    def files_parameters(self, files=None):
        """Builds form parameters.

        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if files:
            for k, v in files.items():
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, 'rb') as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = (mimetypes.guess_type(filename)[0] or
                                    'application/octet-stream')
                        params.append(
                            tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        for accept in accepts:
            if re.search('json', accept, re.IGNORECASE):
                return accept

        return accepts[0]

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        for content_type in content_types:
            if re.search('json', content_type, re.IGNORECASE):
                return content_type

        return content_types[0]

    def update_params_for_auth(self, headers, queries, auth_settings,
                               resource_path, method, body,
                               request_auth=None):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param request_auth: if set, the provided settings will
                             override the token in the configuration.
        """
        if not auth_settings:
            return

        if request_auth:
            self._apply_auth_params(headers, queries,
                                    resource_path, method, body,
                                    request_auth)
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                self._apply_auth_params(headers, queries,
                                        resource_path, method, body,
                                        auth_setting)

    def _apply_auth_params(self, headers, queries,
                           resource_path, method, body,
                           auth_setting):
        """Updates the request parameters based on a single auth_setting

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param auth_setting: auth settings for the endpoint
        """
        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['value']
        elif auth_setting['in'] == 'header':
            if auth_setting['type'] != 'http-signature':
                headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise ApiValueError(
                'Authentication token must be in `query` or `header`'
            )

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                                 content_disposition).group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "wb") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return str(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datetime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                )
            )

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        return klass.from_dict(data)
