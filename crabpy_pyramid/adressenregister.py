"""
The adressenregister component for crabpy pyramid.

Known settings:
crabpy.adressenregister.include
crabpy.adressenregister.base_url
crabpy.adressenregister.api_key
crabpy.adressenregister.cache_config.*
"""

import functools
import logging
from dataclasses import dataclass
from typing import Any
from typing import Mapping

from crabpy.client import AdressenRegisterClient
from crabpy.gateway.adressenregister import Gateway
from pyramid.config import Configurator
from pyramid.registry import Registry
from pyramid.request import Request
from zope.interface import Interface

from crabpy_pyramid.renderers.adressenregister import json_item_renderer
from crabpy_pyramid.renderers.adressenregister import json_list_renderer


LOG = logging.getLogger(__name__)


class IAdressenregister(Interface):
    pass


@dataclass
class ParsedSettings:
    settings: dict[str, str]
    cache_config: dict[str, str] | None


def includeme(config: Configurator):
    LOG.info("Adding adressenregister to the application.")
    add_renderers(config)
    build_adressenregister(config)
    add_routes(config)
    add_views(config)


def parse_settings(settings: Mapping[str, Any]) -> ParsedSettings:
    parsed_settings = {  # defaults
        "base_url": "https://api.basisregisters.vlaanderen.be",
        "api_key": None,
    }

    # remove the `crabpy.adressenregister.` prefix from known settings
    for short_key_name in ("base_url", "api_key"):
        key_name = f"crabpy.adressenregister.{short_key_name}"
        if key_name in settings:
            parsed_settings[short_key_name] = settings.get(key_name)

    # cache configuration
    prefix = "crabpy.adressenregister.cache_config."
    cutoff = len(prefix)
    cache_config = {}
    for key, value in settings.items():
        if key.startswith(prefix):
            cache_config[key[cutoff:]] = value

    LOG.debug(f"{ParsedSettings=}")
    if "api_key" not in parsed_settings:
        LOG.warning(
            "No adressenregister api_key set in settings. "
            "The api might stop working after reaching the limit of x requests per day."
        )
    return ParsedSettings(settings=parsed_settings, cache_config=cache_config or None)


def build_adressenregister(config: Configurator) -> Gateway:
    """
    Create an adressenregister Gateway and set it up for pyramid usage.

    This method does 3 things:
    - Create the gateway
    - Register it as a utility in the registry under `IAdressenregister`
    - Add a request method `adressenregister_gateway`
    """
    registry: Registry = config.registry  # type: ignore
    adressenregister = registry.queryUtility(IAdressenregister)
    if adressenregister is not None:
        return adressenregister

    # Start building
    settings = registry.settings
    parsed_settings = parse_settings(registry.settings)
    settings = parsed_settings.settings
    client = AdressenRegisterClient(settings["base_url"], settings["api_key"])
    gateway = Gateway(client=client, cache_settings=parsed_settings.cache_config)

    registry.registerUtility(gateway, IAdressenregister)
    config.add_request_method(get_adressenregister, "adressenregister_gateway")
    return gateway


@functools.singledispatch
def get_adressenregister(arg) -> Gateway:
    raise NotImplementedError(f"Invalid argument {arg}. Pass a request or registry.")


@get_adressenregister.register
def _(registry: Registry) -> Gateway:
    return registry.queryUtility(IAdressenregister)


@get_adressenregister.register
def _(request: Request) -> Gateway:
    return request.registry.queryUtility(IAdressenregister)


def add_views(config: Configurator):
    config.scan("crabpy_pyramid.views.adressenregister")
    config.scan("crabpy_pyramid.views.exceptions")


def add_routes(config: Configurator):
    config.include("crabpy_pyramid.routes.adressenregister")


def add_renderers(config: Configurator):
    config.add_renderer("adresreg_listjson", json_list_renderer)
    config.add_renderer("adresreg_itemjson", json_item_renderer)
