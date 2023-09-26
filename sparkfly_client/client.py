import functools

from configuration import Configuration
from api_client import ApiClient
from sparkfly_client.exceptions import UnauthorizedException

DEFAULT_HOST = 'https://api.sparkfly.com'


def re_authorize(func, instance):
    """
    :param func: the __call_api function of the ApiClient auto-generated class
    :param instance: an instance of the Client class we can pass to the function, so it can use the authorize function
                     of this class when a 401 is detected initially
    :return: the API Response from __call_api
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except UnauthorizedException:
            getattr(instance, 'authenticate')()
            return func(self, *args, **kwargs)
    return wrapper


class WrappedClient(ApiClient):
    def __init__(
        self,
        configuration: Configuration,
        auth_identity: str = None,
        auth_key: str = None
    ):
        self.auth_identity = auth_identity
        self.auth_key = auth_key
        super().__init__(configuration=configuration)
        if not configuration.api_key.get('X-Auth-Token'):
            self.authenticate()

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        # Here we are decorating the __call_api function of the base client with a re-authorization function
        # if the initial response ever comes back with a 401
        if type(value) not in [bool, type, str, int] and callable(value) and value.__name__ == '__call_api':
            decorator = re_authorize
            return decorator(value, self)

        return value

    def authenticate(self):
        from api.auth_api import AuthApi
        auth = AuthApi(api_client=self)
        auth_response = auth.authenticate_with_http_info(
            x_auth_identity=self.auth_identity,
            x_auth_key=self.auth_key
        )
        self.configuration.api_key['X-Auth-Token'] = auth_response.headers['X-Auth-Token']


class Client:
    def __init__(
        self,
        auth_identity: str = None,
        auth_key: str = None,
        auth_token: str = None,
        host: str = DEFAULT_HOST
    ):
        config = Configuration(
            host=host,
            api_key={
                'X-Auth-Token': auth_token
            }
        )
        self.api_client = WrappedClient(
            configuration=config,
            auth_identity=auth_identity,
            auth_key=auth_key
        )
        if not self.auth_token:
            self.authenticate()

    def authenticate(self):
        self.api_client.authenticate()

    @property
    def auth_token(self):
        return self.api_client.configuration.api_key.get('X-Auth-Token')

    @auth_token.setter
    def auth_token(self, value):
        self.api_client.configuration.api_key['X-Auth-Token'] = value

    @property
    def host(self):
        return self.api_client.configuration.host

    @host.setter
    def host(self, value):
        self.api_client.configuration.host = value

    @property
    def auth(self):
        from api.auth_api import AuthApi
        return AuthApi(api_client=self.api_client)

    @property
    def account(self):
        from api.account_api import AccountApi
        return AccountApi(api_client=self.api_client)

    @property
    def campaigns(self):
        from api.campaigns_api import CampaignsApi
        return CampaignsApi(api_client=self.api_client)

    @property
    def channels(self):
        from api.channels_api import ChannelsApi
        return ChannelsApi(api_client=self.api_client)

    @property
    def counters(self):
        from api.counters_api import CountersApi
        return CountersApi(api_client=self.api_client)

    @property
    def credentials(self):
        from api.credentials_api import CredentialsApi
        return CredentialsApi(api_client=self.api_client)

    @property
    def events(self):
        from api.events_api import EventsApi
        return EventsApi(api_client=self.api_client)

    @property
    def impressions(self):
        from api.impressions_api import ImpressionsApi
        return ImpressionsApi(api_client=self.api_client)

    @property
    def item_sets(self):
        from api.item_sets_api import ItemSetsApi
        return ItemSetsApi(api_client=self.api_client)

    @property
    def items(self):
        from api.items_api import ItemsApi
        return ItemsApi(api_client=self.api_client)

    @property
    def loyalty_points(self):
        from api.loyalty_points_api import LoyaltyPointsApi
        return LoyaltyPointsApi(api_client=self.api_client)

    @property
    def manufacturers(self):
        from api.manufacturers_api import ManufacturersApi
        return ManufacturersApi(api_client=self.api_client)

    @property
    def manufacturers_item_sets(self):
        from api.manufacturers_item_sets_api import ManufacturersItemSetsApi
        return ManufacturersItemSetsApi(api_client=self.api_client)

    @property
    def manufacturers_item_sets_items(self):
        from api.manufacturers_item_sets_items_api import ManufacturersItemSetsItemsApi
        return ManufacturersItemSetsItemsApi(api_client=self.api_client)

    @property
    def manufacturers_items(self):
        from api.manufacturers_items_api import ManufacturersItemsApi
        return ManufacturersItemsApi(api_client=self.api_client)

    @property
    def manufacturers_merchants(self):
        from api.manufacturers_merchants_api import ManufacturersMerchantsApi
        return ManufacturersMerchantsApi(api_client=self.api_client)

    @property
    def member_lists(self):
        from api.member_lists_api import MemberListsApi
        return MemberListsApi(api_client=self.api_client)

    @property
    def member_list_members(self):
        from api.member_lists_members_api import MemberListsMembersApi
        return MemberListsMembersApi(api_client=self.api_client)

    @property
    def member_offers_offer_wallet(self):
        from api.member_offers_offer_wallet_api import MemberOffersOfferWalletApi
        return MemberOffersOfferWalletApi(api_client=self.api_client)

    @property
    def member_privacy(self):
        from api.member_privacy_api import MemberPrivacyApi
        return MemberPrivacyApi(api_client=self.api_client)

    @property
    def members(self):
        from api.members_api import MembersApi
        return MembersApi(api_client=self.api_client)

    @property
    def merchants(self):
        from api.merchants_api import MerchantsApi
        return MerchantsApi(api_client=self.api_client)

    @property
    def merchants_item_sets(self):
        from api.merchants_item_sets_api import MerchantsItemSetsApi
        return MerchantsItemSetsApi(api_client=self.api_client)

    @property
    def merchants_item_sets_items(self):
        from api.merchants_item_sets_items_api import MerchantsItemSetsItemsApi
        return MerchantsItemSetsItemsApi(api_client=self.api_client)

    @property
    def merchants_items(self):
        from api.merchants_items_api import MerchantsItemsApi
        return MerchantsItemsApi(api_client=self.api_client)

    @property
    def merchants_offers(self):
        from api.merchants_offers_api import MerchantsOffersApi
        return MerchantsOffersApi(api_client=self.api_client)

    @property
    def merchants_store_lists(self):
        from api.merchants_store_lists_api import MerchantsStoreListsApi
        return MerchantsStoreListsApi(api_client=self.api_client)

    @property
    def merchants_stores(self):
        from api.merchants_stores_api import MerchantsStoresApi
        return MerchantsStoresApi(api_client=self.api_client)

    @property
    def offer_engine(self):
        from api.offer_engine_api import OfferEngineApi
        return OfferEngineApi(api_client=self.api_client)

    @property
    def offers(self):
        from api.offers_api import OffersApi
        return OffersApi(api_client=self.api_client)

    @property
    def offers_channels(self):
        from api.offers_channels_api import OffersChannelsApi
        return OffersChannelsApi(api_client=self.api_client)

    @property
    def offers_eligible_item_sets(self):
        from api.offers_eligible_item_sets_api import OffersEligibleItemSetsApi
        return OffersEligibleItemSetsApi(api_client=self.api_client)

    @property
    def offers_item_sets(self):
        from api.offers_item_sets_api import OffersItemSetsApi
        return OffersItemSetsApi(api_client=self.api_client)

    @property
    def offers_member_lists(self):
        from api.offers_member_lists_api import OffersMemberListsApi
        return OffersMemberListsApi(api_client=self.api_client)

    @property
    def offers_merchants(self):
        from api.offers_merchants_api import OffersMerchantsApi
        return OffersMerchantsApi(api_client=self.api_client)

    @property
    def offers_passbook_configuration(self):
        from api.offers_passbook_configuration_api import OffersPassbookConfigurationApi
        return OffersPassbookConfigurationApi(api_client=self.api_client)

    @property
    def offers_store_lists(self):
        from api.offers_store_lists_api import OffersStoreListsApi
        return OffersStoreListsApi(api_client=self.api_client)

    @property
    def offers_stores(self):
        from api.offers_stores_api import OffersStoresApi
        return OffersStoresApi(api_client=self.api_client)

    @property
    def pos_offer_codes(self):
        from api.pos_offer_codes_api import POSOfferCodesApi
        return POSOfferCodesApi(api_client=self.api_client)

    @property
    def reports(self):
        from api.reports_api import ReportsApi
        return ReportsApi(api_client=self.api_client)

    @property
    def zidentifiers(self):
        from api.zidentifiers_api import ZidentifiersApi
        return ZidentifiersApi(api_client=self.api_client)
