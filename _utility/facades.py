from abc import ABC, abstractmethod
from typing import TypeVar, Type

from django_nameko import get_pool

from _utility.nameko import DjangoModels


class ComponentFacade(ABC):
    name: str
    models = DjangoModels()

    @abstractmethod
    def ping(self, service_name):
        pass


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


T = TypeVar('T')


def get_component_facade_object(interface: Type[T]) -> T:
    with get_pool().next() as pool:
        return getattr(pool, interface.name)


