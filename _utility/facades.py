from abc import ABC

from django_nameko import get_pool
from nameko.rpc import rpc

from _utility.nameko import DjangoModels


class ComponentFacade(ABC):
    name: str
    models = DjangoModels()

    @rpc
    def ping(self, service_name):
        print(f'ping from {service_name}')
        return 'pong'

    @classmethod
    def get_instance(cls):
        with get_pool().next() as pool:
            return getattr(pool, cls.name)


class AccountsFacade(ComponentFacade, ABC):
    name = 'accounts'


class ChannelManagementFacade(ComponentFacade, ABC):
    name = 'channel_management'


class ChannelsFacade(ComponentFacade, ABC):
    name = 'channels'


class FinancialFacade(ComponentFacade, ABC):
    name = 'financial'


class SubscribeFacade(ComponentFacade, ABC):
    name = 'subscribe'

