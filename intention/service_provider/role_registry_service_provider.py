from ..role.role_registry import RoleRegistry
from ..role.service_provider import service_provider
from ..role.role_regsitry_global import role_registry_global
from .service_provider import ServiceProvider


# This provider might seem a bit redundant, considering that role registry is
# a part of DI container itself, but I didn't want to make exceptions for it
@service_provider(provides=RoleRegistry)
class RoleRegistryServiceProvider(ServiceProvider[RoleRegistry]):
    def provide(self) -> RoleRegistry:
        return role_registry_global
