# sparkfly-api
# Getting Started
## Overview 
The Sparkfly Platform provides a full lifecycle for promotions and rewards from creation to distribution to settlement. The platform integrates in real-time at the point-of-sale and provides item level discounting and tracking. The capabilities of the Sparkfly Platform are available through the use of the Sparkfly Platform API.
## General API Information
The Sparkfly Platform API is implemented using a RESTful interface that allows access to all functionality of the Sparkfly Platform. Communication with the API is performed using HTTPS on port 443.\\n 
## Request / Response
The Sparkfly Platform API supports the JSON data serialization format. The HTTP Content-Type header is used to specify the request format and the HTTP Accept header or a URI extension is used to specify the response format. Content-Type is required if a transaction includes a request body. Either the Accept Header or URI Extension is required if a transaction includes a response body. The URI Extension will take precedence if a conflicting Accept Header and URI Extension are received.

| Format | Content-Type | Accept-Header | URI Extension
| ------ | ------------ | ------------- | -------------
| JSON | application/json | application/json | .json

### Sample JSON Request with Headers
We use cURL for demonstration purposes, but you can use any client of your choosing.
### Request
```
$ curl -i --header 'X-Auth-Token: 228b236272b6ffc7be0496a5f8186f4767afa3ade292ea1565831892941bb6cd' \\
      --header 'Content-Type: application/json' https://api.sparkfly.com/v1.0/members/1
```
### Response Headers
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
X-Runtime: 0.042759
Content-Length: 153
```
The request would work the same way if we had sent .json at the end of the request URI (/v1.0/members/1.json) instead of sending the \\\"application/json\\\" header.
## Authentication
Authentication is performed against the API by providing a specified Account ID and API key within the HTTP x-headers as X-Auth-Identity and X-Auth-Key. Accounts have particular privileges providing various levels of access to resources within the platform.
### Request
```
$ curl -i --header 'X-Auth-Identity: <SPARKFLY_PROVIDED_ID>' \\
      --header 'X-Auth-Key: <SPARKFLY_PROVIDED_KEY>' \\
      https://api.sparkfly.com/auth
```

### Response Headers
```
HTTP/1.1 204 No Content
X-Auth-Token: ab598e824fd304af32fe34ed4a1af1210ce226ecf05c5f043a4f388d3ab74b12
```
Note how the response headers will contain an X-Auth-Token. All future API operations will only need to pass the received X-Auth-Token for authentication. Tokens will be valid for 24 hours. Applications must be developed in order to re-authenticate if an invalid token is used.
## API Versioning
The API version is required and is indicated in the first element of the URI and will take the form: v[VERSION].  API version numbers will only be incremented when functionality is added that breaks compatibility with previous API versions.

Example: https://api.sparkfly.com/v1.0/
## API Operations
Please see the main section of the documentation for request/response examples of the actions that are possible.
# Sample Implementation
The purpose of this document is to give you a basic overview of some of the core API features. It assumes you already have API credentials and access to the Admin Portal.

## Authentication
The first thing you will want to do is use your provided API credentials to authenticate and get an authentication token. Please see the documentation concerning authentication for more information. In all the requests below, we will need to send our API token in our request headers.

## Members
A typical setup step will be to tell the API about your user database. This way, you can create offers for your members. First let's see if there are any users in the database.

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' https://api-staging.sparkfly.com/v1.0/members.json
```

### Status

```
HTTP/1.1 200 OK
```
### Body
```
{
  \"page\": 1,
  \"per_page\": 50,
  \"total_entries\": 0,
  \"total_pages\": 0,
  \"members\": []
}
```

We can see that there are no members yet. Let's create one.

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
      -XPOST -d '{ \"member\": { \"identifier\": \"unique-member-id\" } }' \\
      https://api-staging.sparkfly.com/v1.0/members.json
```

### Status
```
HTTP/1.1 201 Created
```

### Body
```
{
  \"member\": {
    \"identifier\": \"unique-member-id\",
    \"notification_mode\": \"app\",
    \"id\": 1009,
    \"created_at\": \"2013-01-28T21:44:10Z\",
    \"updated_at\": \"2013-01-28T21:44:10Z\"
  }
}
```

First, we send a POST to /v1.0/members.json to create our new member. The only thing you need to provide is a unique identifier to relate the member back to your system. You can repeat this any number of times until all of your users are loaded. Notice how in the response body, the newly created member has an ID of 1009. We can use that to request a specific member (or any resource) in the system at a later time by using the ID like so:

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
      https://api-staging.sparkfly.com/v1.0/members/1009.json
```

### Status
```
HTTP/1.1 200 OK
```

### Body
```
{
  \"member\": {
    \"identifier\": \"unique-member-id\",
    \"notification_mode\": \"app\",
    \"id\": 1009,
    \"created_at\": \"2013-01-28T21:44:10Z\",
    \"updated_at\": \"2013-01-28T21:44:10Z\"
  }
}
```

If a member is coming from your application, you may also wish to search for them by your internal identifier. You can do that by querying the member search API endpoint: 

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
      https://api-staging.sparkfly.com/v1.0/members/search.json?identifier=unique-member-id
```

### Status
```
HTTP/1.1 200 OK
```

### Body
```
{
  \"member\": {
    \"identifier\": \"unique-member-id\",
    \"notification_mode\": \"app\",
    \"id\": 1009,
    \"created_at\": \"2013-01-28T21:44:10Z\",
    \"updated_at\": \"2013-01-28T21:44:10Z\"
  }
}
```

## Offers
Next we'll want to set up an offer. You can create and configure a offer using the API if desired, but it it usually easier to do this through the Admin Portal. Follow the instructions in the Portal, and by the end of the process you should have at least one Merchant, and an Offer (this is the minimum setup needed to run an offer and generate codes for your members). It is also important to note that a Offer will be run by one or more Channels. A Channel is linked to a offer in a way that allows the system to track where your members are coming from, so that you can view offer statistics and control the number of members that redeem a offer.\\n\\nAssuming we're done setting things up, let's query for our offer and make sure everything is working
```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' https://api-staging.sparkfly.com/v1.0/offers.json
```
### Status
```
HTTP/1.1 200 OK
```

### Body
```
{
  \"page\": 1,
  \"per_page\": 50,
  \"total_entries\": 1,
  \"total_pages\": 1,
  \"offers\": [
    {
      \"offer\": {
        \"id\": 1701,
        \"name\": \"Buy a Burger, Get Free Medium Fries\",
        \"description\": null,
        \"offer_type\": 0,
        \"offer_code\": null,
        \"points_earning_value\": null,
        \"points_required_value\": null,
        \"reward_item_description\": null,
        \"reward_item_value\": null,
        \"terms_and_conditions\": null,
        \"quest_only\": false,
        \"max_amount\": null,
        \"min_spend_amount\": null,
        \"max_redemptions\": null,
        \"max_redemptions_per_member\": null,
        \"max_redemptions_per_member_per_day\": null,
        \"merchant_name\": null,
        \"activates_at\": null,
        \"expires_at\": null,
        \"stop_offering_at\": null,
        \"created_at\": \"2013-01-28T22:25:33Z\",
        \"updated_at\": \"2013-01-28T22:25:33Z\"
      }
    }
  ]
}
```
Great! Now we can see our offer \"Buy a Burger, Get Free Medium Fries\"

## Creating Credentials For Members
After we release our offer, we will want to generate redeemable codes for our members. We do this by creating a record called a Credential. A Credential includes a code which allows a member to redeem a offer at a given location. A typical scenario might go something like this. A member is in your store and is using your Cool Mobile App (Channel ID 456), they click a button that says \"Redeem Now\", and you app triggers a backend query to the Sparkfly Platform to generate a credential like so

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
      -X POST \\
      https://api-staging.sparkfly.com/v1.0/credentials.json?member_id=1009&offer_id=1701&channel_id=456
```

### Status
```
HTTP/1.1 201 Created
```
### Body
```
{
  \"credential\": {
    \"id\": 578,
    \"identifier\": \"3540\",
    \"status\": \"open\",
    \"member_id\": 1009,
    \"offer_id\": 1701,
    \"store_id\": 1,
    \"merchant_id\": 251,
    \"redeemed_at\": null,
    \"voided_at\": null,
    \"offer_name\": \"Buy a Burger, Get Free Medium Fries\",
    \"merchant_name\": \"Q Burger\",
    \"location_address\": null,
    \"code_lifetime\": null
  }
}
```
Congratulations! You now have a Credential that you can display for your user. The key thing to look for here is the identifier field, \"3540\". This code is what can be entered in at the point of sale to trigger a redemption in Sparkfly's system!

Check out the section entitled Credentials In Depth if you run into any problems, or need more information on generating credentials.

## Setting Up a Landing Page
Sparkfly provides a web-based landing page for any offer that you would like to have take advantage of this capability. The landing page provides additional tracking information in the form of Impressions, as well as the option of additional security. The following section explains how to setup an offer to use the landing page via the API.

First, make sure you are authenticated with the API and have at least one created offer.

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
      https://api-staging.sparkfly.com/v1.0/offers.json
```

### Body
```
{
  \"page\": 1,
  \"per_page\": 50,
  \"total_entries\": 0,
  \"total_pages\": 0,
  \"offers\": []
}
```
Since we don't have any offers yet we will create one now. All we need is a name.

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
      -X POST -d '{ \"offer\": { \"name\": \"Test offer\" } }' \\
      https://api-staging.sparkfly.com/v1.0/offers.json
```

### Body

```
{
  \"offer\": {
    \"id\": 1290,
    \"merchant_id\": null,
    \"manufacturer_id\": null,
    \"name\": \"Test offer\",
    \"description\": null,
    \"offer_type\": 0,
    \"category\": null,
    \"offer_code\": null,
    \"pos_offer_code\": null,
    \"criteria\": {},
    \"points_earning_value\": null,
    \"points_required_value\": null,
    \"reward_item_description\": null,
    \"reward_item_value\": null,
    \"terms_and_conditions\": null,
    \"quest_only\": false,
    \"merchant_name\": null,
    \"external_reward\": null,
    \"is_reward\": false,
    \"locked\": null,
    \"activates_at\": null,
    \"expires_at\": null,
    \"stop_offering_at\": null,
    \"max_amount\": null,
    \"min_spend_amount\": null,
    \"max_redemptions\": null,
    \"max_redemptions_per_member\": null,
    \"max_redemptions_per_member_per_day\": null,
    \"account_id\": 8,
    \"required_item_set_id\": null,
    \"redemption_item_set_id\": null,
    \"required_item_count\": null,
    \"redemption_item_count\": null,
    \"status\": \"pending\",
    \"created_at\": \"2014-02-11T17:44:54Z\",
    \"updated_at\": \"2014-02-11T17:44:54Z\",
    \"offers\": [],
    \"formatting\": {},
    \"passbook_configuration\": null,
    \"landing_page_urls\": [],
    \"channels\": [],
    \"item_sets\": [],
    \"eligibility\": {
      \"merchant_item_set_ids\": [],
      \"manufacturer_item_set_ids\": [],
      \"merchant_ids\": [],
      \"store_list_ids\": [],
      \"member_list_ids\": [],
      \"channel_ids\": []
    }
  },
  \"errors\": {}
}
```

We have created an offer with ID 1290. We also need to approve the offer by sending a PUT request to the approve URL before it will appear correctly on the landing page

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
      -X PUT \\
      https://api-staging.sparkfly.com/v1.0/offers/1290/actions/approve.json
```

Next, make sure you have at least one Channel on which to publish your offer.

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
      https://api-staging.sparkfly.com/v1.0/channels.json
```

If the total_entries field is 0, we will need to create a channel as well. For demonstration purposes, we'll create a landing page for an email campaign. Again, only a name is required here. 

```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
      -X POST -d '{ \\\"channel\\\": { \"name\": \"Email\" } }' \\
      https://api-staging.sparkfly.com/v1.0/channels.json
```
### Body
```
{
  \"channel\": {
    \"id\": 5,
    \"name\": \"Email\",
    \"allow_sms_keyword\": false,
    \"allow_hmac\": false,
    \"conversion_callback_url\": null
  },
  \"errors\": {}
}
```
Now we also have a channel with an ID of 5, meaning we now have at least one offer and one channel. Now we will need to associate the two. To associate the channel to the offer, we will need to POST to the following URL using your offer ID and a body containing an array with your channel ID.
```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
    -X POST -d '{ \"offer\": { \"channel_ids\": [5] } }' \\
    https://api-staging.sparkfly.com/v1.0/offers/1290/channels.json
```
We should get a 201 Created response code and something like:
```
{
  \"offer\": {
    \"channel_ids\": [
      5
    ],
    \"id\": 1290
  }
}
```
Now if we perform a GET request on the offer, we should see that the channel is associated. The section we are interested in is the field called \"channels\" on the offer.
```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
    https://api-staging.sparkfly.com/v1.0/offers/1290.json
```

### Body (some content omitted)
```
{
  \"offer\": {
    \"channels\": [
      {
        \"channel\": {
          \"id\": 5,
          \"xid\": \"Z7nnWs6\",
          \"name\": \"Email\",
          \"security\": null,
          \"security_key\": null,
          \"offer_id\": 1290,
          \"sms_keyword\": null,
          \"allow_return_later\": true
        }
      }
    ]
  }
}
```
In particular, pay attention to the \"xid\" field. This is an identifier that links your offer to your channel, and it will act as the landing page URL. I should now be able to visit the landing page, with the xid as the path, and see my offer. For example, in the staging environment, our landing page would be: https://mp-staging.sparkfly.com/Z7nnWs6

### Note
Landing pages are cached for performance, and are re-cached every hour. If you go to a landing page, and get a 404 or do not see your changes, you may need to wait up to an hour for the page to be updated.

So at this point, we should be able to see a relatively plain offer page. Let's add a banner image to show up at the top of the landing page. To add an image, we will need to update the offer field called \"formatting\" on the offer, by sending a PUT request. Formatting is a nested object which contains a field called \"bg_image\". If we update bg_image, it should show up on the landing page: 
```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
        -X PUT -d '{ \"offer\": { \"formatting\": { \"bg_image\": \"https://my-domain/banner_image.png\" } } }' \\
        https://api-staging.sparkfly.com/v1.0/offers/1290.json
```

We should get a 200 response that shows our bg_image in the response.

The recommended size for a banner image is 1200x600px. You can also set a background color for the header by setting \"bg_color\" in the formatting options, like so:
```
$ curl -i --header 'X-Auth-Token: <YOUR-AUTH_TOKEN>' \\
        -X PUT -d '{ \"offer\": { \"formatting\": { \"bg_image\": \"https://my-domain/banner_image.png\", \"bg_color\": \"#FF00AA\" } } }' \\
        https://api-staging.sparkfly.com/v1.0/offers/1290.json
```
## Other Considerations
For security purposes, the landing page is served over SSL. In order to maintain this security, any image you link to should also be served over https.

If you're testing a landing page from a desktop or laptop computer, the default behavior is to show a static, printable code. If you would like to preview what the landing page will look like on a mobile device, you can attach the parameter printable=false to the landing page URL. For example https://mp-staging.sparkfly.com/TRYstCR?printable=false

# Credentials

## Introduction
Credentials are the backbone of the Sparkfly API. When issued correctly, they allow a member to redeem one or more offers. Sparkfly will properly handle the creation, expiration and redemption of identifiers that can be used to link a member to a purchase at the point of sale.

## Associating Multiple Offers
Credentials can exist that allow for more than one offer to be redeemed at a time. We're assuming you have already authenticated an have a valid auth token at this time (see the authentication section for an example). Below is an example of multiple offers on a credential:

### Associating Multiple Offers
First we can create a new credential for our member with id #123. After that is successful, we can attempt to attach our offers.

#### Request
```
$ curl -i -XPOST --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\
      'https://api.sparkfly.com/v1.0/credentials.json?member_id=123'
```
### First JSON Response

#### Response Body
```
{
  \"error\": \"channel_id is required\"
}
```
Oops! We can see here that the request failed, because we forgot to include a channel_id. If you don't yet have a channel, see the channel API under main to see how to create one. Let's assume we have a working channel, add the ID to the request, and try again.

#### Request
```
$ curl -i -XPOST --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\
      'https://api.sparkfly.com/v1.0/credentials.json?member_id=123&channel_id=456'
```
### Second JSON Response
#### Response Body
```
{
  \"credential\": {
    \"id\": 1009,
    \"account_id\": 5,
    \"created_at\": \"2013-09-16T18:41:13Z\",
    \"updated_at\": \"2013-09-16T18:41:13Z\",
    \"identifier\": null,
    \"member_id\": 123,
    \"store_id\": null,
    \"channel_id\": 456,
    \"offer_ids\": [],
    \"annotations\": {},
    \"code_lifetime\": null,
    \"supports_barcode\": false,
    \"merchant_id\": null,
    \"offer_name\": null,
    \"merchant_name\": null,
    \"location_address\": null,
    \"url\": null
  },
  \"errors\": {}
}
```

Great! Now we get a 201 (Created) response, with associated member and channel IDs. The credential comes back with an ID of 1009. You'll notice that the identifier is \"null\", because there are no associated offers yet (offer_ids is an empty set).

Next we'll want to associate offers so we can get an identifier generated. We can do this by issuing a PUT request to the newly created credential. The first offer we want to associate has an ID of 1011
```
$ curl -i -XPUT --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\
      'https://api.sparkfly.com/v1.0/credentials/1009.json?channel_id=456&offer_ids=1011'
```
### Third JSON Response
#### Response Body
```
{
  \"credential\": {
    \"id\": 1009,
    \"account_id\": 5,
    \"created_at\": \"2013-09-16T18:41:13Z\",
    \"updated_at\": \"2013-09-16T18:51:23Z\",
    \"identifier\": \"3345\",
    \"member_id\": 1,
    \"store_id\": null,
    \"channel_id\": 456,
    \"offer_ids\": [
      1011
    ],
    \"annotations\": {},
    \"code_lifetime\": null,
    \"supports_barcode\": false,
    \"merchant_id\": null,
    \"offer_name\": \"First Offer\",
    \"merchant_name\": null,
    \"location_address\": null,
    \"url\": null
  },
  \"errors\": {}
}
```
Once the credential is updated, we should see our offer ID in the offer_ids of the response, as well as our newly generated identifier (3345). At this point, the credential is valid and ready to redeem the single offer, with id 1011.
```
$ curl -i -XPUT --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\
        'https://api.sparkfly.com/v1.0/credentials/1009.json?channel_id=456&offer_ids=1011'
```
We can repeat this process to add as many offers as needed like so:
```
$ curl -i -XPUT --header 'X-Auth-Token: d47bfec9446fbe92ee9f7a7da3d1ab973ec0802c28b15f6d9a95ada41937b07d' \\
      'https://api.sparkfly.com/v1.0/credentials/1.json?channel_id=456&offer_ids=1011,1116'
```
Assuming both offers are valid, the JSON response will now show both offer_ids associated with the credential.
## Validations and Errors
Validation | Error | Solution
-----------|-------|---------
Channel ID is not present | Channel can't be blank and must be associated with your account and offer |  Make sure you send channel_id=<your-channel-id> on every request to create or update a credential. You will also need to make sure that the offers you are associating with the credential are also eligible for that same channel (shows up under the offer's eligibility).
Member ID is not present |  Member can't be blank |  Make sure you send member_id=<sparkfly-member-id> on every request to create a credential 
Associated offer(s) are not approved |  offer <offer-name> must be approved to generate a credential |  When you request an offer by id, the status should show up as approved. (See the Approve Offer action under Offers).
Member is not eligible for offer(s) |  Member must be eligible for offer: <offer-name> |  If you have a member list defined for the offer, make sure the member in question is on that list. Additionally, a member may not be eligible for an offer if you have redemption limits set. That is, an offer may have reached the total number of redemptions allowed as a whole, by channel, per member, or you may have hit the daily limit per member per day as defined on the offer itself.
One or more offers is not longer active |  Offer with ID <offer-id> is no longer active |  An offer must have an activates_at datetime field that is before the current date, and an expires_at datetime field that is after the current date.
Store is not eligible for offer(s) |  Store must be eligible for offer: <offer-name> |  If you have an eligible store list defined for the offer, make sure the store in question is on that list. Remember, store id is optional, and not needed to create a credential.
Credential is locked |  This credential is currently locked for processing. Please try again later. |  You had a member who went through the process of attempting to redeem an offer with this credential. In some cases, there may be a slight delay in processing. If a member attempts to immediately re-use a credential before it can be processed, this error may be returned. This shouldn't ever really be seen, but it is something to be aware of during testing. 
Requested offers not found |  Offer not found or not eligible by channel, with id: <one-or-more-requested-ids> |  You are trying to associate one or more offers that either can't be found because the ids are not correct, or the offers are not eligible to be run under the channel id you are requesting. Make sure the offers exist and are eligible to appear on the requested channel.
If you see the last message that offers were not found, remember that you need to attach eligible channels with each offer that you run. This can be done in the admin portal under the Publishing Channels section of the offer. If you do not see any channels listed at all, you can enable them when creating a merchant account. You will not be able to generate a credential code without at least one channel attached to your offer.
## Channel Callback
When a redemption (conversion) event occurs, it is sometimes desired to get a realtime callback posted to your system for real-time tracking purposes. This can be achieved by specifying a conversion_callback_url on a channel that you control. The Sparkfly system can send data to the conversion_callback_url every time an offer is redeemed. 
File | Description
-----|------------
credential_id |  The Sparkfly ID of the credential that was redeemed. 
xid |  The XID for the offer that was redeemed (XID is a unique GUID for offer and channel) 
offer_id |   The offer that was redeemed on this channel 
offer_ids |  All offers associated with the redeemed credential 
store_id |  The Sparkfly ID for the store where the credential was redeemed 
redeemed_at |  When the credential was redeemed 
status |  The status of the redeemed credential 
sf_uid |  The external identifier of the member who redeemed the credential (for promotions that use Sparkfly's landing page) 
sf_ac |  The name of the creative that was viewed to generate the credential (for promotions that use Sparkfly's landing page)

You can substitute any of the above values in your conversion_callback_url by using the %{} notation like so:
```
https://my_server.com/callback/%{credential_id}?time_of_redemption=%{redeemed_at}
```

You would then receive a callback on redemption, with the specific values in place of each %{}.

In addition the the parameters named above, any attributes under the \"conv_ids\" key of the credential's annotations will also be available for selection. See the credential creation documentation for examples of how to set the credential's annotations. Any keys that cannot be resolved will result in blank parameters in the final URL.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.23
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/expressintegrations/sparkfly-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/expressintegrations/sparkfly-client.git`)

Then import the package:
```python
import sparkfly_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sparkfly_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import sparkfly_client
from sparkfly_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_client.Configuration(
    host = "https://api-staging.sparkfly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Auth-Token
configuration.api_key['X-Auth-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'


# Enter a context with an instance of the API client
with sparkfly_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_client.AccountApi(api_client)

    try:
        # Disable Callbacks
        api_instance.v10_account_callbacks_disable_put()
    except ApiException as e:
        print("Exception when calling AccountApi->v10_account_callbacks_disable_put: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api-staging.sparkfly.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**v10_account_callbacks_disable_put**](docs/AccountApi.md#v10_account_callbacks_disable_put) | **PUT** /v1.0/account/callbacks/disable | Disable Callbacks
*AccountApi* | [**v10_account_callbacks_enable_put**](docs/AccountApi.md#v10_account_callbacks_enable_put) | **PUT** /v1.0/account/callbacks/enable | Enable Callbacks
*AccountApi* | [**v10_account_get**](docs/AccountApi.md#v10_account_get) | **GET** /v1.0/account | View Account
*AccountApi* | [**v10_account_put**](docs/AccountApi.md#v10_account_put) | **PUT** /v1.0/account | Update Account
*AuthApi* | [**auth_get**](docs/AuthApi.md#auth_get) | **GET** /auth | authenticate and receive auth token
*CampaignsApi* | [**v10_campaigns_campaign_id_delete**](docs/CampaignsApi.md#v10_campaigns_campaign_id_delete) | **DELETE** /v1.0/campaigns/:campaign_id | Delete the campaign
*CampaignsApi* | [**v10_campaigns_campaign_id_get**](docs/CampaignsApi.md#v10_campaigns_campaign_id_get) | **GET** /v1.0/campaigns/:campaign_id | Retrieve Campaign
*CampaignsApi* | [**v10_campaigns_campaign_id_put**](docs/CampaignsApi.md#v10_campaigns_campaign_id_put) | **PUT** /v1.0/campaigns/:campaign_id | Update Campaign
*CampaignsApi* | [**v10_campaigns_get**](docs/CampaignsApi.md#v10_campaigns_get) | **GET** /v1.0/campaigns | Get campaign by external ID
*CampaignsApi* | [**v10_campaigns_post**](docs/CampaignsApi.md#v10_campaigns_post) | **POST** /v1.0/campaigns | Create a new campaign
*CampaignsApi* | [**v10_campaigns_search_get**](docs/CampaignsApi.md#v10_campaigns_search_get) | **GET** /v1.0/campaigns/search | Get active reward program campaigns
*ChannelsApi* | [**v10_channels_channel_id_delete**](docs/ChannelsApi.md#v10_channels_channel_id_delete) | **DELETE** /v1.0/channels/:channel_id | Delete channel by ID
*ChannelsApi* | [**v10_channels_channel_id_get**](docs/ChannelsApi.md#v10_channels_channel_id_get) | **GET** /v1.0/channels/:channel_id | Get channel by ID
*ChannelsApi* | [**v10_channels_channel_id_put**](docs/ChannelsApi.md#v10_channels_channel_id_put) | **PUT** /v1.0/channels/:channel_id | Update channel by ID
*ChannelsApi* | [**v10_channels_get**](docs/ChannelsApi.md#v10_channels_get) | **GET** /v1.0/channels | Get channels
*ChannelsApi* | [**v10_channels_post**](docs/ChannelsApi.md#v10_channels_post) | **POST** /v1.0/channels | Create a channel
*CountersApi* | [**v10_counters_counter_id_delete**](docs/CountersApi.md#v10_counters_counter_id_delete) | **DELETE** /v1.0/counters/:counter_id | Delete counter by ID
*CountersApi* | [**v10_counters_counter_id_get**](docs/CountersApi.md#v10_counters_counter_id_get) | **GET** /v1.0/counters/:counter_id | Get counter by ID
*CountersApi* | [**v10_counters_counter_id_put**](docs/CountersApi.md#v10_counters_counter_id_put) | **PUT** /v1.0/counters/:counter_id | Update counter by ID
*CountersApi* | [**v10_counters_get**](docs/CountersApi.md#v10_counters_get) | **GET** /v1.0/counters | Get counters
*CountersApi* | [**v10_counters_post**](docs/CountersApi.md#v10_counters_post) | **POST** /v1.0/counters | Create a counter
*CredentialsApi* | [**v10_credentials_credential_id_delete**](docs/CredentialsApi.md#v10_credentials_credential_id_delete) | **DELETE** /v1.0/credentials/:credential_id | Delete Credential
*CredentialsApi* | [**v10_credentials_credential_id_get**](docs/CredentialsApi.md#v10_credentials_credential_id_get) | **GET** /v1.0/credentials/:credential_id | Get Credential
*CredentialsApi* | [**v10_credentials_credential_id_put**](docs/CredentialsApi.md#v10_credentials_credential_id_put) | **PUT** /v1.0/credentials/:credential_id | Updates a credential
*CredentialsApi* | [**v10_credentials_credential_id_redeem_put**](docs/CredentialsApi.md#v10_credentials_credential_id_redeem_put) | **PUT** /v1.0/credentials/:credential_id/redeem | Redeem a credential
*CredentialsApi* | [**v10_credentials_credential_id_void_put**](docs/CredentialsApi.md#v10_credentials_credential_id_void_put) | **PUT** /v1.0/credentials/:credential_id/void | Void a credential
*CredentialsApi* | [**v10_credentials_eligible_get**](docs/CredentialsApi.md#v10_credentials_eligible_get) | **GET** /v1.0/credentials/eligible | Determine if a member is eligible for an offer
*CredentialsApi* | [**v10_credentials_get**](docs/CredentialsApi.md#v10_credentials_get) | **GET** /v1.0/credentials | List Credentials
*CredentialsApi* | [**v10_credentials_post**](docs/CredentialsApi.md#v10_credentials_post) | **POST** /v1.0/credentials | Creates a credential
*EventsApi* | [**v10_events_event_id_delete**](docs/EventsApi.md#v10_events_event_id_delete) | **DELETE** /v1.0/events/:event_id | Delete the event
*EventsApi* | [**v10_events_event_id_get**](docs/EventsApi.md#v10_events_event_id_get) | **GET** /v1.0/events/:event_id | Get event by ID
*EventsApi* | [**v10_events_event_id_put**](docs/EventsApi.md#v10_events_event_id_put) | **PUT** /v1.0/events/:event_id | Change the name of an event
*EventsApi* | [**v10_events_get**](docs/EventsApi.md#v10_events_get) | **GET** /v1.0/events | get all events
*EventsApi* | [**v10_events_post**](docs/EventsApi.md#v10_events_post) | **POST** /v1.0/events | Creates an event
*ImpressionsApi* | [**v10_impressions_get**](docs/ImpressionsApi.md#v10_impressions_get) | **GET** /v1.0/impressions | Get all impressions
*ImpressionsApi* | [**v10_impressions_impression_id_delete**](docs/ImpressionsApi.md#v10_impressions_impression_id_delete) | **DELETE** /v1.0/impressions/:impression_id | Delete the impression
*ImpressionsApi* | [**v10_impressions_post**](docs/ImpressionsApi.md#v10_impressions_post) | **POST** /v1.0/impressions | Creates an impression
*ItemSetsApi* | [**v10_item_sets_get**](docs/ItemSetsApi.md#v10_item_sets_get) | **GET** /v1.0/item_sets | Get all item sets
*ItemSetsApi* | [**v10_item_sets_item_set_id_delete**](docs/ItemSetsApi.md#v10_item_sets_item_set_id_delete) | **DELETE** /v1.0/item_sets/:item_set_id | Delete item set by ID
*ItemSetsApi* | [**v10_item_sets_item_set_id_get**](docs/ItemSetsApi.md#v10_item_sets_item_set_id_get) | **GET** /v1.0/item_sets/:item_set_id | Get item set by ID
*ItemSetsApi* | [**v10_item_sets_item_set_id_items_get**](docs/ItemSetsApi.md#v10_item_sets_item_set_id_items_get) | **GET** /v1.0/item_sets/:item_set_id/items | Get items for item set
*ItemSetsApi* | [**v10_item_sets_item_set_id_put**](docs/ItemSetsApi.md#v10_item_sets_item_set_id_put) | **PUT** /v1.0/item_sets/:item_set_id | Update item set by ID
*ItemSetsApi* | [**v10_item_sets_post**](docs/ItemSetsApi.md#v10_item_sets_post) | **POST** /v1.0/item_sets | Create an item set
*ItemsApi* | [**v10_items_get**](docs/ItemsApi.md#v10_items_get) | **GET** /v1.0/items | Get all items
*ItemsApi* | [**v10_items_item_id_delete**](docs/ItemsApi.md#v10_items_item_id_delete) | **DELETE** /v1.0/items/:item_id | Delete item by ID
*ItemsApi* | [**v10_items_item_id_get**](docs/ItemsApi.md#v10_items_item_id_get) | **GET** /v1.0/items/:item_id | Get item by ID
*ItemsApi* | [**v10_items_item_id_put**](docs/ItemsApi.md#v10_items_item_id_put) | **PUT** /v1.0/items/:item_id | Update item by ID
*ItemsApi* | [**v10_items_post**](docs/ItemsApi.md#v10_items_post) | **POST** /v1.0/items | Create an item
*LoyaltyPointsApi* | [**v10_points_card_status_get**](docs/LoyaltyPointsApi.md#v10_points_card_status_get) | **GET** /v1.0/points/card_status | Check Card Status
*LoyaltyPointsApi* | [**v10_points_transfer_post**](docs/LoyaltyPointsApi.md#v10_points_transfer_post) | **POST** /v1.0/points/transfer | Transfer Loyalty Points
*ManufacturersApi* | [**v10_manufacturers_get**](docs/ManufacturersApi.md#v10_manufacturers_get) | **GET** /v1.0/manufacturers | Get all manufacturers
*ManufacturersApi* | [**v10_manufacturers_manufacturer_id_delete**](docs/ManufacturersApi.md#v10_manufacturers_manufacturer_id_delete) | **DELETE** /v1.0/manufacturers/:manufacturer_id | Delete manufacturer by ID
*ManufacturersApi* | [**v10_manufacturers_manufacturer_id_get**](docs/ManufacturersApi.md#v10_manufacturers_manufacturer_id_get) | **GET** /v1.0/manufacturers/:manufacturer_id | Get manufacturer by ID
*ManufacturersApi* | [**v10_manufacturers_manufacturer_id_put**](docs/ManufacturersApi.md#v10_manufacturers_manufacturer_id_put) | **PUT** /v1.0/manufacturers/:manufacturer_id | Update manufacturer by ID
*ManufacturersApi* | [**v10_manufacturers_post**](docs/ManufacturersApi.md#v10_manufacturers_post) | **POST** /v1.0/manufacturers | Create a manufacturer
*ManufacturersItemSetsApi* | [**v10_manufacturers_manufacturer_id_item_sets_get**](docs/ManufacturersItemSetsApi.md#v10_manufacturers_manufacturer_id_item_sets_get) | **GET** /v1.0/manufacturers/:manufacturer_id/item_sets | Get all item sets for manufacturer
*ManufacturersItemSetsApi* | [**v10_manufacturers_manufacturer_id_item_sets_item_set_id_delete**](docs/ManufacturersItemSetsApi.md#v10_manufacturers_manufacturer_id_item_sets_item_set_id_delete) | **DELETE** /v1.0/manufacturers/:manufacturer_id/item_sets/:item_set_id | Delete item set by ID for manufacturer
*ManufacturersItemSetsApi* | [**v10_manufacturers_manufacturer_id_item_sets_item_set_id_get**](docs/ManufacturersItemSetsApi.md#v10_manufacturers_manufacturer_id_item_sets_item_set_id_get) | **GET** /v1.0/manufacturers/:manufacturer_id/item_sets/:item_set_id | Get item set by ID for manufacturer
*ManufacturersItemSetsApi* | [**v10_manufacturers_manufacturer_id_item_sets_item_set_id_put**](docs/ManufacturersItemSetsApi.md#v10_manufacturers_manufacturer_id_item_sets_item_set_id_put) | **PUT** /v1.0/manufacturers/:manufacturer_id/item_sets/:item_set_id | Update item set by ID for manufacturer
*ManufacturersItemSetsApi* | [**v10_manufacturers_manufacturer_id_item_sets_post**](docs/ManufacturersItemSetsApi.md#v10_manufacturers_manufacturer_id_item_sets_post) | **POST** /v1.0/manufacturers/:manufacturer_id/item_sets | Create an item set for manufacturer
*ManufacturersItemSetsItemsApi* | [**v10_manufacturers_manufacturer_id_item_sets_item_set_id_items_get**](docs/ManufacturersItemSetsItemsApi.md#v10_manufacturers_manufacturer_id_item_sets_item_set_id_items_get) | **GET** /v1.0/manufacturers/:manufacturer_id/item_sets/:item_set_id/items | Get items for item set for manufacturer
*ManufacturersItemsApi* | [**v10_manufacturers_manufacturer_id_items_get**](docs/ManufacturersItemsApi.md#v10_manufacturers_manufacturer_id_items_get) | **GET** /v1.0/manufacturers/:manufacturer_id/items | Get all items for manufacturer
*ManufacturersItemsApi* | [**v10_manufacturers_manufacturer_id_items_item_id_delete**](docs/ManufacturersItemsApi.md#v10_manufacturers_manufacturer_id_items_item_id_delete) | **DELETE** /v1.0/manufacturers/:manufacturer_id/items/:item_id | Delete item by ID for manufacturer
*ManufacturersItemsApi* | [**v10_manufacturers_manufacturer_id_items_item_id_get**](docs/ManufacturersItemsApi.md#v10_manufacturers_manufacturer_id_items_item_id_get) | **GET** /v1.0/manufacturers/:manufacturer_id/items/:item_id | Get item by ID for manufacturer
*ManufacturersItemsApi* | [**v10_manufacturers_manufacturer_id_items_item_id_put**](docs/ManufacturersItemsApi.md#v10_manufacturers_manufacturer_id_items_item_id_put) | **PUT** /v1.0/manufacturers/:manufacturer_id/items/:item_id | Update item by ID for manufacturer
*ManufacturersItemsApi* | [**v10_manufacturers_manufacturer_id_items_post**](docs/ManufacturersItemsApi.md#v10_manufacturers_manufacturer_id_items_post) | **POST** /v1.0/manufacturers/:manufacturer_id/items | Create an item for manufacturer
*ManufacturersMerchantsApi* | [**v10_manufacturers_manufacturer_id_merchants_delete**](docs/ManufacturersMerchantsApi.md#v10_manufacturers_manufacturer_id_merchants_delete) | **DELETE** /v1.0/manufacturers/:manufacturer_id/merchants | Remove an eligible merchant for manufacturer
*ManufacturersMerchantsApi* | [**v10_manufacturers_manufacturer_id_merchants_get**](docs/ManufacturersMerchantsApi.md#v10_manufacturers_manufacturer_id_merchants_get) | **GET** /v1.0/manufacturers/:manufacturer_id/merchants | Get all merchants for manufacturer
*ManufacturersMerchantsApi* | [**v10_manufacturers_manufacturer_id_merchants_post**](docs/ManufacturersMerchantsApi.md#v10_manufacturers_manufacturer_id_merchants_post) | **POST** /v1.0/manufacturers/:manufacturer_id/merchants | Add an eligible merchant for manufacturer
*ManufacturersMerchantsApi* | [**v10_manufacturers_manufacturer_id_merchants_put**](docs/ManufacturersMerchantsApi.md#v10_manufacturers_manufacturer_id_merchants_put) | **PUT** /v1.0/manufacturers/:manufacturer_id/merchants | Add an eligible merchant for manufacturer
*MemberListsApi* | [**v10_member_lists_get**](docs/MemberListsApi.md#v10_member_lists_get) | **GET** /v1.0/member_lists | Get all member lists
*MemberListsApi* | [**v10_member_lists_member_list_id_delete**](docs/MemberListsApi.md#v10_member_lists_member_list_id_delete) | **DELETE** /v1.0/member_lists/:member_list_id | Delete Member List by ID
*MemberListsApi* | [**v10_member_lists_member_list_id_get**](docs/MemberListsApi.md#v10_member_lists_member_list_id_get) | **GET** /v1.0/member_lists/:member_list_id | Get member list by ID
*MemberListsApi* | [**v10_member_lists_member_list_id_put**](docs/MemberListsApi.md#v10_member_lists_member_list_id_put) | **PUT** /v1.0/member_lists/:member_list_id | Update Member List by ID
*MemberListsApi* | [**v10_member_lists_post**](docs/MemberListsApi.md#v10_member_lists_post) | **POST** /v1.0/member_lists | Create a member list
*MemberListsMembersApi* | [**v10_member_lists_member_list_id_members_delete**](docs/MemberListsMembersApi.md#v10_member_lists_member_list_id_members_delete) | **DELETE** /v1.0/member_lists/:member_list_id/members | Remove an eligible member for member_list
*MemberListsMembersApi* | [**v10_member_lists_member_list_id_members_get**](docs/MemberListsMembersApi.md#v10_member_lists_member_list_id_members_get) | **GET** /v1.0/member_lists/:member_list_id/members | Get all Members for Member List
*MemberListsMembersApi* | [**v10_member_lists_member_list_id_members_post**](docs/MemberListsMembersApi.md#v10_member_lists_member_list_id_members_post) | **POST** /v1.0/member_lists/:member_list_id/members | Set eligible members for Member List
*MemberListsMembersApi* | [**v10_member_lists_member_list_id_members_put**](docs/MemberListsMembersApi.md#v10_member_lists_member_list_id_members_put) | **PUT** /v1.0/member_lists/:member_list_id/members | Add eligible members for Member List
*MemberOffersOfferWalletApi* | [**v10_members_member_id_offer_states_get**](docs/MemberOffersOfferWalletApi.md#v10_members_member_id_offer_states_get) | **GET** /v1.0/members/:member_id/offer_states | Get the entire list of Offer States for a Member
*MemberOffersOfferWalletApi* | [**v10_members_member_id_offer_states_offer_state_id_get**](docs/MemberOffersOfferWalletApi.md#v10_members_member_id_offer_states_offer_state_id_get) | **GET** /v1.0/members/:member_id/offer_states/:offer_state_id | Get an individual Offer State for a Member
*MemberOffersOfferWalletApi* | [**v10_members_member_id_offer_states_offer_state_id_put**](docs/MemberOffersOfferWalletApi.md#v10_members_member_id_offer_states_offer_state_id_put) | **PUT** /v1.0/members/:member_id/offer_states/:offer_state_id | Update an individual Offer State for a Member - in order to change the availability
*MemberOffersOfferWalletApi* | [**v10_members_member_id_offer_states_offer_state_id_void_post**](docs/MemberOffersOfferWalletApi.md#v10_members_member_id_offer_states_offer_state_id_void_post) | **POST** /v1.0/members/:member_id/offer_states/:offer_state_id/void | Voids an individual Offer State for a Member by Member ID
*MemberOffersOfferWalletApi* | [**v10_members_member_id_offer_states_post**](docs/MemberOffersOfferWalletApi.md#v10_members_member_id_offer_states_post) | **POST** /v1.0/members/:member_id/offer_states | Create a new Member Offer State and provide optional activation and expiration dates
*MemberOffersOfferWalletApi* | [**v10_members_offer_states_get**](docs/MemberOffersOfferWalletApi.md#v10_members_offer_states_get) | **GET** /v1.0/members/offer_states | Retrieve Offer States
*MemberOffersOfferWalletApi* | [**v10_members_offer_states_offer_state_id_void_post**](docs/MemberOffersOfferWalletApi.md#v10_members_offer_states_offer_state_id_void_post) | **POST** /v1.0/members/offer_states/:offer_state_id/void | Voids an individual Offer State for a Member by Member Identifier
*MemberPrivacyApi* | [**v10_privacy_member_delete_request_post**](docs/MemberPrivacyApi.md#v10_privacy_member_delete_request_post) | **POST** /v1.0/privacy/member/delete_request | Creates a deletion request for a member
*MemberPrivacyApi* | [**v10_privacy_member_export_get**](docs/MemberPrivacyApi.md#v10_privacy_member_export_get) | **GET** /v1.0/privacy/member/export | Exports data associated with a member
*MembersApi* | [**v10_members_get**](docs/MembersApi.md#v10_members_get) | **GET** /v1.0/members | List members
*MembersApi* | [**v10_members_member_id_delete**](docs/MembersApi.md#v10_members_member_id_delete) | **DELETE** /v1.0/members/:member_id | Delete the member
*MembersApi* | [**v10_members_member_id_get**](docs/MembersApi.md#v10_members_member_id_get) | **GET** /v1.0/members/:member_id | Retrieve Member
*MembersApi* | [**v10_members_member_id_put**](docs/MembersApi.md#v10_members_member_id_put) | **PUT** /v1.0/members/:member_id | Update Member
*MembersApi* | [**v10_members_post**](docs/MembersApi.md#v10_members_post) | **POST** /v1.0/members | Creates a member
*MembersApi* | [**v10_members_search_get**](docs/MembersApi.md#v10_members_search_get) | **GET** /v1.0/members/search | Search for Member by Identifier
*MerchantsApi* | [**v10_merchants_get**](docs/MerchantsApi.md#v10_merchants_get) | **GET** /v1.0/merchants | Get all merchants
*MerchantsApi* | [**v10_merchants_merchant_id_delete**](docs/MerchantsApi.md#v10_merchants_merchant_id_delete) | **DELETE** /v1.0/merchants/:merchant_id | Delete merchant by ID
*MerchantsApi* | [**v10_merchants_merchant_id_get**](docs/MerchantsApi.md#v10_merchants_merchant_id_get) | **GET** /v1.0/merchants/:merchant_id | Get merchant by ID
*MerchantsApi* | [**v10_merchants_merchant_id_put**](docs/MerchantsApi.md#v10_merchants_merchant_id_put) | **PUT** /v1.0/merchants/:merchant_id | Update merchant by ID
*MerchantsApi* | [**v10_merchants_post**](docs/MerchantsApi.md#v10_merchants_post) | **POST** /v1.0/merchants | Create a merchant
*MerchantsItemSetsApi* | [**v10_merchants_merchant_id_item_sets_get**](docs/MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_get) | **GET** /v1.0/merchants/:merchant_id/item_sets | Get all item sets for merchant
*MerchantsItemSetsApi* | [**v10_merchants_merchant_id_item_sets_item_set_id_delete**](docs/MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_item_set_id_delete) | **DELETE** /v1.0/merchants/:merchant_id/item_sets/:item_set_id | Delete item set by ID for merchant
*MerchantsItemSetsApi* | [**v10_merchants_merchant_id_item_sets_item_set_id_get**](docs/MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_item_set_id_get) | **GET** /v1.0/merchants/:merchant_id/item_sets/:item_set_id | Get item set by ID for merchant
*MerchantsItemSetsApi* | [**v10_merchants_merchant_id_item_sets_item_set_id_put**](docs/MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_item_set_id_put) | **PUT** /v1.0/merchants/:merchant_id/item_sets/:item_set_id | Update item set by ID for merchant
*MerchantsItemSetsApi* | [**v10_merchants_merchant_id_item_sets_post**](docs/MerchantsItemSetsApi.md#v10_merchants_merchant_id_item_sets_post) | **POST** /v1.0/merchants/:merchant_id/item_sets | Create an item set for merchant
*MerchantsItemSetsItemsApi* | [**v10_merchants_merchant_id_item_sets_item_set_id_items_get**](docs/MerchantsItemSetsItemsApi.md#v10_merchants_merchant_id_item_sets_item_set_id_items_get) | **GET** /v1.0/merchants/:merchant_id/item_sets/:item_set_id/items | Get items for item set for merchant
*MerchantsItemsApi* | [**v10_merchants_merchant_id_items_get**](docs/MerchantsItemsApi.md#v10_merchants_merchant_id_items_get) | **GET** /v1.0/merchants/:merchant_id/items | Get all items for merchant
*MerchantsItemsApi* | [**v10_merchants_merchant_id_items_item_id_delete**](docs/MerchantsItemsApi.md#v10_merchants_merchant_id_items_item_id_delete) | **DELETE** /v1.0/merchants/:merchant_id/items/:item_id | Delete item by ID for merchant
*MerchantsItemsApi* | [**v10_merchants_merchant_id_items_item_id_get**](docs/MerchantsItemsApi.md#v10_merchants_merchant_id_items_item_id_get) | **GET** /v1.0/merchants/:merchant_id/items/:item_id | Get item by ID for merchant
*MerchantsItemsApi* | [**v10_merchants_merchant_id_items_item_id_put**](docs/MerchantsItemsApi.md#v10_merchants_merchant_id_items_item_id_put) | **PUT** /v1.0/merchants/:merchant_id/items/:item_id | Update item by ID for merchant
*MerchantsItemsApi* | [**v10_merchants_merchant_id_items_post**](docs/MerchantsItemsApi.md#v10_merchants_merchant_id_items_post) | **POST** /v1.0/merchants/:merchant_id/items | Create an item for merchant
*MerchantsOffersApi* | [**v10_merchants_merchant_id_offers_get**](docs/MerchantsOffersApi.md#v10_merchants_merchant_id_offers_get) | **GET** /v1.0/merchants/:merchant_id/offers | List offers for merchant
*MerchantsStoreListsApi* | [**v10_merchants_merchant_id_store_lists_get**](docs/MerchantsStoreListsApi.md#v10_merchants_merchant_id_store_lists_get) | **GET** /v1.0/merchants/:merchant_id/store_lists | Get all Store Lists for merchant
*MerchantsStoreListsApi* | [**v10_merchants_merchant_id_store_lists_post**](docs/MerchantsStoreListsApi.md#v10_merchants_merchant_id_store_lists_post) | **POST** /v1.0/merchants/:merchant_id/store_lists | Create an Store List for merchant
*MerchantsStoreListsApi* | [**v10_merchants_merchant_id_store_lists_store_list_id_delete**](docs/MerchantsStoreListsApi.md#v10_merchants_merchant_id_store_lists_store_list_id_delete) | **DELETE** /v1.0/merchants/:merchant_id/store_lists/:store_list_id | Delete Store List by ID for merchant
*MerchantsStoreListsApi* | [**v10_merchants_merchant_id_store_lists_store_list_id_get**](docs/MerchantsStoreListsApi.md#v10_merchants_merchant_id_store_lists_store_list_id_get) | **GET** /v1.0/merchants/:merchant_id/store_lists/:store_list_id | Get Store List by ID for merchant
*MerchantsStoreListsApi* | [**v10_merchants_merchant_id_store_lists_store_list_id_put**](docs/MerchantsStoreListsApi.md#v10_merchants_merchant_id_store_lists_store_list_id_put) | **PUT** /v1.0/merchants/:merchant_id/store_lists/:store_list_id | Update Store List by ID for merchant
*MerchantsStoreListsApi* | [**v10_merchants_merchant_id_store_lists_store_list_id_stores_get**](docs/MerchantsStoreListsApi.md#v10_merchants_merchant_id_store_lists_store_list_id_stores_get) | **GET** /v1.0/merchants/:merchant_id/store_lists/:store_list_id/stores | Get all Stores for Store List (detailed)
*MerchantsStoreListsApi* | [**v10_merchants_store_lists_store_list_id_stores_delete**](docs/MerchantsStoreListsApi.md#v10_merchants_store_lists_store_list_id_stores_delete) | **DELETE** /v1.0/merchants/store_lists/:store_list_id/stores | Remove an eligible Store for store_list
*MerchantsStoreListsApi* | [**v10_merchants_store_lists_store_list_id_stores_get**](docs/MerchantsStoreListsApi.md#v10_merchants_store_lists_store_list_id_stores_get) | **GET** /v1.0/merchants/store_lists/:store_list_id/stores | Get all Stores for Store List
*MerchantsStoreListsApi* | [**v10_merchants_store_lists_store_list_id_stores_post**](docs/MerchantsStoreListsApi.md#v10_merchants_store_lists_store_list_id_stores_post) | **POST** /v1.0/merchants/store_lists/:store_list_id/stores | Set eligible Stores for Store List
*MerchantsStoreListsApi* | [**v10_merchants_store_lists_store_list_id_stores_put**](docs/MerchantsStoreListsApi.md#v10_merchants_store_lists_store_list_id_stores_put) | **PUT** /v1.0/merchants/store_lists/:store_list_id/stores | Add eligible Stores for Store List
*MerchantsStoresApi* | [**v10_merchants_merchant_id_stores_get**](docs/MerchantsStoresApi.md#v10_merchants_merchant_id_stores_get) | **GET** /v1.0/merchants/:merchant_id/stores | Get all Stores for merchant
*MerchantsStoresApi* | [**v10_merchants_merchant_id_stores_post**](docs/MerchantsStoresApi.md#v10_merchants_merchant_id_stores_post) | **POST** /v1.0/merchants/:merchant_id/stores | Create an Store for merchant
*MerchantsStoresApi* | [**v10_merchants_merchant_id_stores_store_id_delete**](docs/MerchantsStoresApi.md#v10_merchants_merchant_id_stores_store_id_delete) | **DELETE** /v1.0/merchants/:merchant_id/stores/:store_id | Delete Store by ID for merchant
*MerchantsStoresApi* | [**v10_merchants_merchant_id_stores_store_id_get**](docs/MerchantsStoresApi.md#v10_merchants_merchant_id_stores_store_id_get) | **GET** /v1.0/merchants/:merchant_id/stores/:store_id | Get Store by ID for merchant
*MerchantsStoresApi* | [**v10_merchants_merchant_id_stores_store_id_offers_get**](docs/MerchantsStoresApi.md#v10_merchants_merchant_id_stores_store_id_offers_get) | **GET** /v1.0/merchants/:merchant_id/stores/:store_id/offers | List Offer IDs for Merchant and Store
*MerchantsStoresApi* | [**v10_merchants_merchant_id_stores_store_id_put**](docs/MerchantsStoresApi.md#v10_merchants_merchant_id_stores_store_id_put) | **PUT** /v1.0/merchants/:merchant_id/stores/:store_id | Update Store by ID for merchant
*MerchantsStoresApi* | [**v10_merchants_stores_index_get**](docs/MerchantsStoresApi.md#v10_merchants_stores_index_get) | **GET** /v1.0/merchants/stores/index | Get and Filter Stores WITH Active Offers (stores/index)
*MerchantsStoresApi* | [**v10_merchants_stores_nearby_index_get**](docs/MerchantsStoresApi.md#v10_merchants_stores_nearby_index_get) | **GET** /v1.0/merchants/stores/nearby/index | Get and Filter Stores WITH Active Offers (stores/nearby/index)
*MerchantsStoresApi* | [**v10_merchants_stores_nearby_lat_lng_index_get**](docs/MerchantsStoresApi.md#v10_merchants_stores_nearby_lat_lng_index_get) | **GET** /v1.0/merchants/stores/nearby/:lat/:lng/index | Get and Filter Stores WITH Active Offers (stores/nearby/:lat/:lng/index)
*MerchantsStoresApi* | [**v10_merchants_stores_store_id_get**](docs/MerchantsStoresApi.md#v10_merchants_stores_store_id_get) | **GET** /v1.0/merchants/stores/:store_id | Get Store by ID (without merchant)
*OfferEngineApi* | [**v10_activities_offers_get**](docs/OfferEngineApi.md#v10_activities_offers_get) | **GET** /v1.0/activities/offers | Retrieve Offer Activities for Member
*OfferEngineApi* | [**v10_members_member_id_activities_redemptions_get**](docs/OfferEngineApi.md#v10_members_member_id_activities_redemptions_get) | **GET** /v1.0/members/:member_id/activities/redemptions | Retrieve Redeemed Redemptions for Member
*OfferEngineApi* | [**v10_members_member_id_stores_store_id_activities_redemptions_get**](docs/OfferEngineApi.md#v10_members_member_id_stores_store_id_activities_redemptions_get) | **GET** /v1.0/members/:member_id/stores/:store_id/activities/redemptions | Retrieve Redeemed Redemptions for Member for Store
*OfferEngineApi* | [**v10_members_member_id_stores_store_id_check_incheck_in_latlatcheck_in_lnglng_post**](docs/OfferEngineApi.md#v10_members_member_id_stores_store_id_check_incheck_in_latlatcheck_in_lnglng_post) | **POST** /v1.0/members/:member_id/stores/:store_id/check-in?check_in[lat]&#x3D;:lat&amp;check_in[lng]&#x3D;:lng | Check-In Member to Store
*OfferEngineApi* | [**v10_members_member_id_stores_store_id_get**](docs/OfferEngineApi.md#v10_members_member_id_stores_store_id_get) | **GET** /v1.0/members/:member_id/stores/:store_id | Retrieve Store for Member
*OffersApi* | [**v10_offers_get**](docs/OffersApi.md#v10_offers_get) | **GET** /v1.0/offers | List offers
*OffersApi* | [**v10_offers_offer_id_delete**](docs/OffersApi.md#v10_offers_offer_id_delete) | **DELETE** /v1.0/offers/:offer_id | Delete the offer
*OffersApi* | [**v10_offers_offer_id_get**](docs/OffersApi.md#v10_offers_offer_id_get) | **GET** /v1.0/offers/:offer_id | Retrieve Offer
*OffersApi* | [**v10_offers_offer_id_put**](docs/OffersApi.md#v10_offers_offer_id_put) | **PUT** /v1.0/offers/:offer_id | Update Offer
*OffersApi* | [**v10_offers_post**](docs/OffersApi.md#v10_offers_post) | **POST** /v1.0/offers | Creates an offer
*OffersChannelsApi* | [**v10_offers_offer_id_channels_channel_id_get**](docs/OffersChannelsApi.md#v10_offers_offer_id_channels_channel_id_get) | **GET** /v1.0/offers/:offer_id/channels/:channel_id | Eligible Channel Show
*OffersChannelsApi* | [**v10_offers_offer_id_channels_channel_id_put**](docs/OffersChannelsApi.md#v10_offers_offer_id_channels_channel_id_put) | **PUT** /v1.0/offers/:offer_id/channels/:channel_id | Eligible Channel Update
*OffersChannelsApi* | [**v10_offers_offer_id_channels_delete**](docs/OffersChannelsApi.md#v10_offers_offer_id_channels_delete) | **DELETE** /v1.0/offers/:offer_id/channels | Remove eligible Channels from offer
*OffersChannelsApi* | [**v10_offers_offer_id_channels_get**](docs/OffersChannelsApi.md#v10_offers_offer_id_channels_get) | **GET** /v1.0/offers/:offer_id/channels | Eligible Channels List
*OffersChannelsApi* | [**v10_offers_offer_id_channels_post**](docs/OffersChannelsApi.md#v10_offers_offer_id_channels_post) | **POST** /v1.0/offers/:offer_id/channels | Set eligible Channels for offer
*OffersChannelsApi* | [**v10_offers_offer_id_channels_put**](docs/OffersChannelsApi.md#v10_offers_offer_id_channels_put) | **PUT** /v1.0/offers/:offer_id/channels | Add eligible Channels for offer
*OffersEligibleItemSetsApi* | [**v10_offers_offer_id_eligible_item_sets_get**](docs/OffersEligibleItemSetsApi.md#v10_offers_offer_id_eligible_item_sets_get) | **GET** /v1.0/offers/:offer_id/eligible_item_sets | Eligible Item Sets List
*OffersItemSetsApi* | [**v10_offers_offer_id_eligible_item_sets_eligible_item_set_id_delete**](docs/OffersItemSetsApi.md#v10_offers_offer_id_eligible_item_sets_eligible_item_set_id_delete) | **DELETE** /v1.0/offers/:offer_id/eligible_item_sets/:eligible_item_set_id | Remove eligible Item Set from offer
*OffersItemSetsApi* | [**v10_offers_offer_id_eligible_item_sets_eligible_item_set_id_get**](docs/OffersItemSetsApi.md#v10_offers_offer_id_eligible_item_sets_eligible_item_set_id_get) | **GET** /v1.0/offers/:offer_id/eligible_item_sets/:eligible_item_set_id | Retrieve eligible Item Set for offer
*OffersItemSetsApi* | [**v10_offers_offer_id_eligible_item_sets_eligible_item_set_id_put**](docs/OffersItemSetsApi.md#v10_offers_offer_id_eligible_item_sets_eligible_item_set_id_put) | **PUT** /v1.0/offers/:offer_id/eligible_item_sets/:eligible_item_set_id | Update eligible Item Set for offer
*OffersItemSetsApi* | [**v10_offers_offer_id_eligible_item_sets_post**](docs/OffersItemSetsApi.md#v10_offers_offer_id_eligible_item_sets_post) | **POST** /v1.0/offers/:offer_id/eligible_item_sets | Eligible Item Set for Offer - Create
*OffersMemberListsApi* | [**v10_offers_offer_id_member_lists_delete**](docs/OffersMemberListsApi.md#v10_offers_offer_id_member_lists_delete) | **DELETE** /v1.0/offers/:offer_id/member_lists | Remove eligible Member Lists from offer
*OffersMemberListsApi* | [**v10_offers_offer_id_member_lists_get**](docs/OffersMemberListsApi.md#v10_offers_offer_id_member_lists_get) | **GET** /v1.0/offers/:offer_id/member_lists | Eligible Member Lists List
*OffersMemberListsApi* | [**v10_offers_offer_id_member_lists_post**](docs/OffersMemberListsApi.md#v10_offers_offer_id_member_lists_post) | **POST** /v1.0/offers/:offer_id/member_lists | Set eligible Member Lists for offer
*OffersMemberListsApi* | [**v10_offers_offer_id_member_lists_put**](docs/OffersMemberListsApi.md#v10_offers_offer_id_member_lists_put) | **PUT** /v1.0/offers/:offer_id/member_lists | Add eligible Member Lists for offer
*OffersMerchantsApi* | [**v10_offers_offer_id_merchants_delete**](docs/OffersMerchantsApi.md#v10_offers_offer_id_merchants_delete) | **DELETE** /v1.0/offers/:offer_id/merchants | Remove eligible Merchants from offer
*OffersMerchantsApi* | [**v10_offers_offer_id_merchants_get**](docs/OffersMerchantsApi.md#v10_offers_offer_id_merchants_get) | **GET** /v1.0/offers/:offer_id/merchants | Eligible Merchants List
*OffersMerchantsApi* | [**v10_offers_offer_id_merchants_post**](docs/OffersMerchantsApi.md#v10_offers_offer_id_merchants_post) | **POST** /v1.0/offers/:offer_id/merchants | Set eligible Merchants for offer
*OffersMerchantsApi* | [**v10_offers_offer_id_merchants_put**](docs/OffersMerchantsApi.md#v10_offers_offer_id_merchants_put) | **PUT** /v1.0/offers/:offer_id/merchants | Add eligible Merchants for offer
*OffersPassbookConfigurationApi* | [**v10_offers_offer_id_passbook_configuration_delete**](docs/OffersPassbookConfigurationApi.md#v10_offers_offer_id_passbook_configuration_delete) | **DELETE** /v1.0/offers/:offer_id/passbook_configuration | Passbook Configuration Delete for Offer
*OffersPassbookConfigurationApi* | [**v10_offers_offer_id_passbook_configuration_get**](docs/OffersPassbookConfigurationApi.md#v10_offers_offer_id_passbook_configuration_get) | **GET** /v1.0/offers/:offer_id/passbook_configuration | Get Passbook Configuration for Offer
*OffersPassbookConfigurationApi* | [**v10_offers_offer_id_passbook_configuration_post**](docs/OffersPassbookConfigurationApi.md#v10_offers_offer_id_passbook_configuration_post) | **POST** /v1.0/offers/:offer_id/passbook_configuration | Passbook Configuration Create
*OffersPassbookConfigurationApi* | [**v10_offers_offer_id_passbook_configuration_put**](docs/OffersPassbookConfigurationApi.md#v10_offers_offer_id_passbook_configuration_put) | **PUT** /v1.0/offers/:offer_id/passbook_configuration | Update Passbook Configuration for Offer
*OffersStoreListsApi* | [**v10_offers_offer_id_store_lists_delete**](docs/OffersStoreListsApi.md#v10_offers_offer_id_store_lists_delete) | **DELETE** /v1.0/offers/:offer_id/store_lists | Remove eligible Store Lists from offer
*OffersStoreListsApi* | [**v10_offers_offer_id_store_lists_get**](docs/OffersStoreListsApi.md#v10_offers_offer_id_store_lists_get) | **GET** /v1.0/offers/:offer_id/store_lists | Eligible Store Lists List
*OffersStoreListsApi* | [**v10_offers_offer_id_store_lists_post**](docs/OffersStoreListsApi.md#v10_offers_offer_id_store_lists_post) | **POST** /v1.0/offers/:offer_id/store_lists | Set eligible Store Lists for offer
*OffersStoreListsApi* | [**v10_offers_offer_id_store_lists_put**](docs/OffersStoreListsApi.md#v10_offers_offer_id_store_lists_put) | **PUT** /v1.0/offers/:offer_id/store_lists | Add eligible Store Lists for offer
*OffersStoresApi* | [**v10_offers_offer_id_stores_get**](docs/OffersStoresApi.md#v10_offers_offer_id_stores_get) | **GET** /v1.0/offers/:offer_id/stores | Get nearby Stores for Offer
*POSOfferCodesApi* | [**v10_pos_offer_codes_get**](docs/POSOfferCodesApi.md#v10_pos_offer_codes_get) | **GET** /v1.0/pos_offer_codes | List POS Offer Codes
*POSOfferCodesApi* | [**v10_pos_offer_codes_pos_offer_code_id_get**](docs/POSOfferCodesApi.md#v10_pos_offer_codes_pos_offer_code_id_get) | **GET** /v1.0/pos_offer_codes/:pos_offer_code_id | Get POS Offer Code
*ReportsApi* | [**v10_merchants_merchant_id_reports_full_get**](docs/ReportsApi.md#v10_merchants_merchant_id_reports_full_get) | **GET** /v1.0/merchants/:merchant_id/reports/full | Generates a report of full Merchant data in a given timeframe for a single Merchant
*ReportsApi* | [**v10_merchants_merchant_id_reports_impressions_get**](docs/ReportsApi.md#v10_merchants_merchant_id_reports_impressions_get) | **GET** /v1.0/merchants/:merchant_id/reports/impressions | Get Unique Impressions
*ReportsApi* | [**v10_reports_account_level_get**](docs/ReportsApi.md#v10_reports_account_level_get) | **GET** /v1.0/reports/account_level | Generates a report of full Merchant data in a given timeframe for a all Merchants
*ReportsApi* | [**v10_reports_offer_activity_get**](docs/ReportsApi.md#v10_reports_offer_activity_get) | **GET** /v1.0/reports/offer_activity | Generates a report of all offer activity in a given timeframe
*ReportsApi* | [**v10_reports_redemptions_get**](docs/ReportsApi.md#v10_reports_redemptions_get) | **GET** /v1.0/reports/redemptions | Generates a report of all offer redemptions for a given timeframe and store list
*ZidentifiersApi* | [**v10_members_member_id_offers_offer_id_zidentifiers_get**](docs/ZidentifiersApi.md#v10_members_member_id_offers_offer_id_zidentifiers_get) | **GET** /v1.0/members/:member_id/offers/:offer_id/zidentifiers | Create an identifier linking Offer, Member, Channel
*ZidentifiersApi* | [**v10_members_zidentifiers_zid_get**](docs/ZidentifiersApi.md#v10_members_zidentifiers_zid_get) | **GET** /v1.0/members/zidentifiers/:zid | Get Zidentifier


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountCallbacks](docs/AccountCallbacks.md)
 - [AccountInput](docs/AccountInput.md)
 - [AccountInputRequest](docs/AccountInputRequest.md)
 - [AccountLevelMerchantReport](docs/AccountLevelMerchantReport.md)
 - [AccountResponse](docs/AccountResponse.md)
 - [BadRequestObject](docs/BadRequestObject.md)
 - [Campaign](docs/Campaign.md)
 - [CampaignInput](docs/CampaignInput.md)
 - [CampaignInputRequest](docs/CampaignInputRequest.md)
 - [CampaignLandingPageUrls](docs/CampaignLandingPageUrls.md)
 - [CampaignResponse](docs/CampaignResponse.md)
 - [CampaignSimplified](docs/CampaignSimplified.md)
 - [Channel](docs/Channel.md)
 - [ChannelInput](docs/ChannelInput.md)
 - [ChannelInputRequest](docs/ChannelInputRequest.md)
 - [ChannelList](docs/ChannelList.md)
 - [ChannelResponse](docs/ChannelResponse.md)
 - [Contact](docs/Contact.md)
 - [Contacts](docs/Contacts.md)
 - [Counter](docs/Counter.md)
 - [CounterInput](docs/CounterInput.md)
 - [CounterInputRequest](docs/CounterInputRequest.md)
 - [CounterList](docs/CounterList.md)
 - [CounterResponse](docs/CounterResponse.md)
 - [Credential](docs/Credential.md)
 - [CredentialEligibilityResponse](docs/CredentialEligibilityResponse.md)
 - [CredentialInput](docs/CredentialInput.md)
 - [CredentialInputRequest](docs/CredentialInputRequest.md)
 - [CredentialList](docs/CredentialList.md)
 - [CredentialResponse](docs/CredentialResponse.md)
 - [EligibleChannel](docs/EligibleChannel.md)
 - [EligibleChannelInput](docs/EligibleChannelInput.md)
 - [EligibleChannelInputRequest](docs/EligibleChannelInputRequest.md)
 - [EligibleChannelResponse](docs/EligibleChannelResponse.md)
 - [EligibleItemSet](docs/EligibleItemSet.md)
 - [EligibleItemSetInput](docs/EligibleItemSetInput.md)
 - [EligibleItemSetInputRequest](docs/EligibleItemSetInputRequest.md)
 - [EligibleItemSetResponse](docs/EligibleItemSetResponse.md)
 - [Event](docs/Event.md)
 - [EventInput](docs/EventInput.md)
 - [EventInputRequest](docs/EventInputRequest.md)
 - [EventList](docs/EventList.md)
 - [EventResponse](docs/EventResponse.md)
 - [ExportCredential](docs/ExportCredential.md)
 - [ExportMember](docs/ExportMember.md)
 - [Impression](docs/Impression.md)
 - [ImpressionInput](docs/ImpressionInput.md)
 - [ImpressionInputRequest](docs/ImpressionInputRequest.md)
 - [ImpressionList](docs/ImpressionList.md)
 - [ImpressionResponse](docs/ImpressionResponse.md)
 - [ImpressionsDataItems](docs/ImpressionsDataItems.md)
 - [ImpressionsReport](docs/ImpressionsReport.md)
 - [ImpressionsReportData](docs/ImpressionsReportData.md)
 - [ImpressionsReportData1](docs/ImpressionsReportData1.md)
 - [ImpressionsSeriesItems](docs/ImpressionsSeriesItems.md)
 - [Item](docs/Item.md)
 - [ItemInput](docs/ItemInput.md)
 - [ItemInputRequest](docs/ItemInputRequest.md)
 - [ItemListResponse](docs/ItemListResponse.md)
 - [ItemResponse](docs/ItemResponse.md)
 - [ItemSet](docs/ItemSet.md)
 - [ItemSetInput](docs/ItemSetInput.md)
 - [ItemSetInputRequest](docs/ItemSetInputRequest.md)
 - [ItemSetList](docs/ItemSetList.md)
 - [ItemSetResponse](docs/ItemSetResponse.md)
 - [Location](docs/Location.md)
 - [Manufacturer](docs/Manufacturer.md)
 - [ManufacturerInput](docs/ManufacturerInput.md)
 - [ManufacturerInputRequest](docs/ManufacturerInputRequest.md)
 - [ManufacturerItemSetList](docs/ManufacturerItemSetList.md)
 - [ManufacturerList](docs/ManufacturerList.md)
 - [ManufacturerLocation](docs/ManufacturerLocation.md)
 - [ManufacturerMerchantIdsInput](docs/ManufacturerMerchantIdsInput.md)
 - [ManufacturerMerchantIdsInputRequest](docs/ManufacturerMerchantIdsInputRequest.md)
 - [ManufacturerMerchants](docs/ManufacturerMerchants.md)
 - [ManufacturerMerchantsResponse](docs/ManufacturerMerchantsResponse.md)
 - [ManufacturerResponse](docs/ManufacturerResponse.md)
 - [Member](docs/Member.md)
 - [MemberExportData](docs/MemberExportData.md)
 - [MemberInfo](docs/MemberInfo.md)
 - [MemberInput](docs/MemberInput.md)
 - [MemberInputRequest](docs/MemberInputRequest.md)
 - [MemberList](docs/MemberList.md)
 - [MemberListInput](docs/MemberListInput.md)
 - [MemberListInputRequest](docs/MemberListInputRequest.md)
 - [MemberListList](docs/MemberListList.md)
 - [MemberListMemberIdsInput](docs/MemberListMemberIdsInput.md)
 - [MemberListMemberIdsInputRequest](docs/MemberListMemberIdsInputRequest.md)
 - [MemberListMembers](docs/MemberListMembers.md)
 - [MemberListMembersResponse](docs/MemberListMembersResponse.md)
 - [MemberListObject](docs/MemberListObject.md)
 - [MemberListObjectResponse](docs/MemberListObjectResponse.md)
 - [MemberResponse](docs/MemberResponse.md)
 - [MemberStore](docs/MemberStore.md)
 - [MemberStoreResponse](docs/MemberStoreResponse.md)
 - [Merchant](docs/Merchant.md)
 - [MerchantInput](docs/MerchantInput.md)
 - [MerchantInputRequest](docs/MerchantInputRequest.md)
 - [MerchantItemSetList](docs/MerchantItemSetList.md)
 - [MerchantList](docs/MerchantList.md)
 - [MerchantOfferList](docs/MerchantOfferList.md)
 - [MerchantReport](docs/MerchantReport.md)
 - [MerchantReportData](docs/MerchantReportData.md)
 - [MerchantResponse](docs/MerchantResponse.md)
 - [MerchantStoreListList](docs/MerchantStoreListList.md)
 - [MerchantStoreListStoreIdsInputRequest](docs/MerchantStoreListStoreIdsInputRequest.md)
 - [MerchantStoreListStoresList](docs/MerchantStoreListStoresList.md)
 - [MerchantStoreListStoresResponse](docs/MerchantStoreListStoresResponse.md)
 - [MerchantStoreOfferIdList](docs/MerchantStoreOfferIdList.md)
 - [Offer](docs/Offer.md)
 - [OfferActivity](docs/OfferActivity.md)
 - [OfferActivityList](docs/OfferActivityList.md)
 - [OfferActivityReport](docs/OfferActivityReport.md)
 - [OfferActivityResponse](docs/OfferActivityResponse.md)
 - [OfferChannelIdsInput](docs/OfferChannelIdsInput.md)
 - [OfferChannelIdsInputRequest](docs/OfferChannelIdsInputRequest.md)
 - [OfferChannels](docs/OfferChannels.md)
 - [OfferChannelsResponse](docs/OfferChannelsResponse.md)
 - [OfferEligibility](docs/OfferEligibility.md)
 - [OfferEligibleItemSetList](docs/OfferEligibleItemSetList.md)
 - [OfferFormatting](docs/OfferFormatting.md)
 - [OfferInput](docs/OfferInput.md)
 - [OfferInputRequest](docs/OfferInputRequest.md)
 - [OfferList](docs/OfferList.md)
 - [OfferMemberListIdsInput](docs/OfferMemberListIdsInput.md)
 - [OfferMemberListIdsInputRequest](docs/OfferMemberListIdsInputRequest.md)
 - [OfferMemberLists](docs/OfferMemberLists.md)
 - [OfferMemberListsResponse](docs/OfferMemberListsResponse.md)
 - [OfferMerchantIdsInput](docs/OfferMerchantIdsInput.md)
 - [OfferMerchantIdsInputRequest](docs/OfferMerchantIdsInputRequest.md)
 - [OfferMerchants](docs/OfferMerchants.md)
 - [OfferMerchantsResponse](docs/OfferMerchantsResponse.md)
 - [OfferResponse](docs/OfferResponse.md)
 - [OfferSimplified](docs/OfferSimplified.md)
 - [OfferSimplifiedResponse](docs/OfferSimplifiedResponse.md)
 - [OfferState](docs/OfferState.md)
 - [OfferStateInfo](docs/OfferStateInfo.md)
 - [OfferStateInput](docs/OfferStateInput.md)
 - [OfferStateInputRequest](docs/OfferStateInputRequest.md)
 - [OfferStateList](docs/OfferStateList.md)
 - [OfferStateResponse](docs/OfferStateResponse.md)
 - [OfferStoreListIdsInput](docs/OfferStoreListIdsInput.md)
 - [OfferStoreListIdsInputRequest](docs/OfferStoreListIdsInputRequest.md)
 - [OfferStoreLists](docs/OfferStoreLists.md)
 - [OfferStoreListsResponse](docs/OfferStoreListsResponse.md)
 - [PassbookConfiguration](docs/PassbookConfiguration.md)
 - [PassbookConfigurationInput](docs/PassbookConfigurationInput.md)
 - [PassbookConfigurationInputRequest](docs/PassbookConfigurationInputRequest.md)
 - [PassbookConfigurationResponse](docs/PassbookConfigurationResponse.md)
 - [PointsCardStatus](docs/PointsCardStatus.md)
 - [PosOfferCode](docs/PosOfferCode.md)
 - [PosOfferCodeList](docs/PosOfferCodeList.md)
 - [PosOfferCodeResponse](docs/PosOfferCodeResponse.md)
 - [Redemption](docs/Redemption.md)
 - [RedemptionList](docs/RedemptionList.md)
 - [RedemptionList1](docs/RedemptionList1.md)
 - [ReportData](docs/ReportData.md)
 - [Store](docs/Store.md)
 - [StoreInput](docs/StoreInput.md)
 - [StoreInputRequest](docs/StoreInputRequest.md)
 - [StoreListInput](docs/StoreListInput.md)
 - [StoreListInputRequest](docs/StoreListInputRequest.md)
 - [StoreListObject](docs/StoreListObject.md)
 - [StoreListObjectResponse](docs/StoreListObjectResponse.md)
 - [StoreListResponse](docs/StoreListResponse.md)
 - [StoreListStoreIdsInput](docs/StoreListStoreIdsInput.md)
 - [StoreLocation](docs/StoreLocation.md)
 - [StoreNearby](docs/StoreNearby.md)
 - [StoreResponse](docs/StoreResponse.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionItem](docs/TransactionItem.md)
 - [TransactionItemExtra](docs/TransactionItemExtra.md)
 - [ZIdentifier](docs/ZIdentifier.md)
 - [ZIdentifierResponse](docs/ZIdentifierResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="X-Auth-Token"></a>
### X-Auth-Token

- **Type**: API key
- **API key parameter name**: X-Auth-Token
- **Location**: HTTP header


## Author




