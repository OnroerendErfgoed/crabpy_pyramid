"""
The capakey component for crabpy pyramid.

Known settings:
crabpy.capakey.cache_config.*
"""

import functools
import logging
from dataclasses import dataclass
from typing import Any
from typing import Mapping

from crabpy.gateway.capakey import CapakeyRestGateway
from pyramid.config import Configurator
from pyramid.registry import Registry
from pyramid.request import Request
from zope.interface import Interface

from crabpy_pyramid.renderers.capakey import json_item_renderer
from crabpy_pyramid.renderers.capakey import json_list_renderer


LOG = logging.getLogger(__name__)


class ICapakey(Interface):
    pass


@dataclass
class ParsedSettings:
    cache_config: dict[str, str] | None


def includeme(config: Configurator):
    LOG.info("Adding capakey to the application.")
    add_renderers(config)
    build_capakey(config)
    add_routes(config)
    add_views(config)


def parse_settings(settings: Mapping[str, Any]) -> ParsedSettings:
    # cache configuration
    prefix = "crabpy.capakey.cache_config."
    cutoff = len(prefix)
    cache_config = {}
    for key, value in settings.items():
        if key.startswith(prefix):
            cache_config[key[cutoff:]] = value

    LOG.debug(f"{ParsedSettings=}")
    return ParsedSettings(cache_config=cache_config or None)


def add_views(config: Configurator):
    config.scan("crabpy_pyramid.views.capakey")


def add_routes(config: Configurator):
    config.include("crabpy_pyramid.routes.capakey")


def add_renderers(config: Configurator):
    config.add_renderer("capakey_listjson", json_list_renderer)
    config.add_renderer("capakey_itemjson", json_item_renderer)


@functools.singledispatch
def get_capakey(arg) -> CapakeyRestGateway:
    raise NotImplementedError(f"Invalid argument {arg}. Pass a request or registry.")


@get_capakey.register
def _(registry: Registry) -> CapakeyRestGateway:
    return registry.queryUtility(ICapakey)


@get_capakey.register
def _(request: Request) -> CapakeyRestGateway:
    return request.registry.queryUtility(ICapakey)


def build_capakey(config: Configurator) -> CapakeyRestGateway:
    """
    Create an capakey Gateway and set it up for pyramid usage.

    This method does 3 things:
    - Create the gateway
    - Register it as a utility in the registry under `ICapakey`
    - Add a request method `capakey_gateway`
    """
    registry: Registry = config.registry  # type: ignore
    capakey = get_capakey(registry)
    if capakey is not None:
        return capakey

    # Start building
    parsed_settings = parse_settings(registry.settings)
    kwargs = {}
    if parsed_settings.cache_config:
        kwargs["cache_config"] = parsed_settings.cache_config

    gateway = CapakeyRestGateway(**kwargs)

    registry.registerUtility(gateway, ICapakey)
    config.add_request_method(get_capakey, "capakey_gateway")
    return gateway
