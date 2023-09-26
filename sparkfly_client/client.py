from configuration import Configuration
from api_client import ApiClient
from sparkfly_client import ApiException

DEFAULT_HOST = 'https://api.sparkfly.com'


class Client:
    def __init__(
        self,
        auth_token: str = None,
        auth_identity: str = None,
        auth_key: str = None,
        host: str = DEFAULT_HOST
    ):
        self.config = Configuration(
            host=host,
            api_key={
                'X-Auth-Token': auth_token
            }
        )
        self.auth_identity = auth_identity
        self.auth_key = auth_key
        self.api_client = ApiClient(configuration=self.config)
        if not self.auth_token:
            self.authenticate()

    def authenticate(self):
        auth_response = self.auth.authenticate_with_http_info(
            x_auth_identity=self.auth_identity,
            x_auth_key=self.auth_key
        )
        if 'X-Auth-Token' not in auth_response.headers:
            raise ApiException(reason="Unable to authenticate with the provided auth identity and auth key")
        self.auth_token = auth_response.headers['X-Auth-Token']

    @property
    def auth_token(self):
        return self.config.api_key.get('X-Auth-Token')

    @auth_token.setter
    def auth_token(self, value):
        self.config.api_key['X-Auth-Token'] = value
        self.api_client.configuration = self.config

    @property
    def host(self):
        return self.config.host

    @host.setter
    def host(self, value):
        self.config.host = value
        self.api_client.configuration = self.config

    @property
    def auth(self):
        from api.auth_api import AuthApi
        return AuthApi(self.api_client)

    @property
    def account(self):
        from api.account_api import AccountApi
        return AccountApi(self.api_client)

    @property
    def campaigns(self):
        from api.campaigns_api import CampaignsApi
        return CampaignsApi(self.api_client)

    @property
    def channels(self):
        from api.channels_api import ChannelsApi
        return ChannelsApi(self.api_client)

    @property
    def counters(self):
        from api.counters_api import CountersApi
        return CountersApi(self.api_client)

    @property
    def credentials(self):
        from api.credentials_api import CredentialsApi
        return CredentialsApi(self.api_client)

    @property
    def events(self):
        from api.events_api import EventsApi
        return EventsApi(self.api_client)

    @property
    def impressions(self):
        from api.impressions_api import ImpressionsApi
        return ImpressionsApi(self.api_client)

    @property
    def item_sets(self):
        from api.item_sets_api import ItemSetsApi
        return ItemSetsApi(self.api_client)

    @property
    def items(self):
        from api.items_api import ItemsApi
        return ItemsApi(self.api_client)

    @property
    def loyalty_points(self):
        from api.loyalty_points_api import LoyaltyPointsApi
        return LoyaltyPointsApi(self.api_client)

    @property
    def manufacturers(self):
        from api.manufacturers_api import ManufacturersApi
        return ManufacturersApi(self.api_client)

    @property
    def manufacturers_item_sets(self):
        from api.manufacturers_item_sets_api import ManufacturersItemSetsApi
        return ManufacturersItemSetsApi(self.api_client)

    @property
    def manufacturers_item_sets_items(self):
        from api.manufacturers_item_sets_items_api import ManufacturersItemSetsItemsApi
        return ManufacturersItemSetsItemsApi(self.api_client)

    @property
    def manufacturers_items(self):
        from api.manufacturers_items_api import ManufacturersItemsApi
        return ManufacturersItemsApi(self.api_client)

    @property
    def manufacturers_merchants(self):
        from api.manufacturers_merchants_api import ManufacturersMerchantsApi
        return ManufacturersMerchantsApi(self.api_client)

    @property
    def member_lists(self):
        from api.member_lists_api import MemberListsApi
        return MemberListsApi(self.api_client)

    @property
    def member_list_members(self):
        from api.member_lists_members_api import MemberListsMembersApi
        return MemberListsMembersApi(self.api_client)

    @property
    def member_offers_offer_wallet(self):
        from api.member_offers_offer_wallet_api import MemberOffersOfferWalletApi
        return MemberOffersOfferWalletApi(self.api_client)

    @property
    def member_privacy(self):
        from api.member_privacy_api import MemberPrivacyApi
        return MemberPrivacyApi(self.api_client)

    @property
    def members(self):
        from api.members_api import MembersApi
        return MembersApi(self.api_client)

    @property
    def merchants(self):
        from api.merchants_api import MerchantsApi
        return MerchantsApi(self.api_client)

    @property
    def merchants_item_sets(self):
        from api.merchants_item_sets_api import MerchantsItemSetsApi
        return MerchantsItemSetsApi(self.api_client)

    @property
    def merchants_item_sets_items(self):
        from api.merchants_item_sets_items_api import MerchantsItemSetsItemsApi
        return MerchantsItemSetsItemsApi(self.api_client)

    @property
    def merchants_items(self):
        from api.merchants_items_api import MerchantsItemsApi
        return MerchantsItemsApi(self.api_client)

    @property
    def merchants_offers(self):
        from api.merchants_offers_api import MerchantsOffersApi
        return MerchantsOffersApi(self.api_client)

    @property
    def merchants_store_lists(self):
        from api.merchants_store_lists_api import MerchantsStoreListsApi
        return MerchantsStoreListsApi(self.api_client)

    @property
    def merchants_stores(self):
        from api.merchants_stores_api import MerchantsStoresApi
        return MerchantsStoresApi(self.api_client)

    @property
    def offer_engine(self):
        from api.offer_engine_api import OfferEngineApi
        return OfferEngineApi(self.api_client)

    @property
    def offers(self):
        from api.offers_api import OffersApi
        return OffersApi(self.api_client)

    @property
    def offers_channels(self):
        from api.offers_channels_api import OffersChannelsApi
        return OffersChannelsApi(self.api_client)

    @property
    def offers_eligible_item_sets(self):
        from api.offers_eligible_item_sets_api import OffersEligibleItemSetsApi
        return OffersEligibleItemSetsApi(self.api_client)

    @property
    def offers_item_sets(self):
        from api.offers_item_sets_api import OffersItemSetsApi
        return OffersItemSetsApi(self.api_client)

    @property
    def offers_member_lists(self):
        from api.offers_member_lists_api import OffersMemberListsApi
        return OffersMemberListsApi(self.api_client)

    @property
    def offers_merchants(self):
        from api.offers_merchants_api import OffersMerchantsApi
        return OffersMerchantsApi(self.api_client)

    @property
    def offers_passbook_configuration(self):
        from api.offers_passbook_configuration_api import OffersPassbookConfigurationApi
        return OffersPassbookConfigurationApi(self.api_client)

    @property
    def offers_store_lists(self):
        from api.offers_store_lists_api import OffersStoreListsApi
        return OffersStoreListsApi(self.api_client)

    @property
    def offers_stores(self):
        from api.offers_stores_api import OffersStoresApi
        return OffersStoresApi(self.api_client)

    @property
    def pos_offer_codes(self):
        from api.pos_offer_codes_api import POSOfferCodesApi
        return POSOfferCodesApi(self.api_client)

    @property
    def reports(self):
        from api.reports_api import ReportsApi
        return ReportsApi(self.api_client)

    @property
    def zidentifiers(self):
        from api.zidentifiers_api import ZidentifiersApi
        return ZidentifiersApi(self.api_client)
