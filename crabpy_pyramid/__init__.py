import logging
import os
from collections.abc import Sequence

from crabpy.client import AdressenRegisterClient
from crabpy.gateway.adressenregister import Gateway
from crabpy.gateway.capakey import CapakeyRestGateway
from pyramid.config import Configurator
from pyramid.settings import asbool
from zope.interface import Interface

from crabpy_pyramid.renderers.adressenregister import (
    json_item_renderer as adresreg_json_item_renderer,
)
from crabpy_pyramid.renderers.adressenregister import (
    json_list_renderer as adresreg_json_list_renderer,
)
from crabpy_pyramid.renderers.capakey import (
    json_item_renderer as capakey_json_item_renderer,
)
from crabpy_pyramid.renderers.capakey import (
    json_list_renderer as capakey_json_list_renderer,
)

log = logging.getLogger(__name__)
GENERATE_ETAG_ROUTE_NAMES = set()


class ICapakey(Interface):
    pass


class IAdressenregister(Interface):
    pass


def _parse_settings(settings):
    defaults = {
        "capakey.include": False,
        "adressenregister.include": True,
        "adressenregister.base_url": "https://api.basisregisters.vlaanderen.be",
        "adressenregister.api_key": None,
        "cache.file.root": "/tmp/dogpile_data",
    }
    args = defaults.copy()
    if "crabpy.adressenregister.api_key" not in settings:
        log.warning(
            "No adressenregister.api_key set in settings. "
            "The api might stop working after reaching the limit of x requests per day."
        )

    # booelean settings
    for short_key_name in (
        "capakey.include",
        "adressenregister.include",
    ):
        key_name = "crabpy.%s" % short_key_name
        if key_name in settings:
            args[short_key_name] = asbool(
                settings.get(key_name, defaults.get(short_key_name))
            )

    # string setting
    for short_key_name in (
        "proxy.http",
        "proxy.https",
        "cache.file.root",
        "adressenregister.base_url",
        "adressenregister.api_key",
    ):
        key_name = "crabpy.%s" % short_key_name
        if key_name in settings:
            args[short_key_name] = settings.get(key_name)

    # cache configuration
    for short_key_name in (
        "capakey.cache_config",
        "adressenregister.cache_config",
    ):
        key_name = "crabpy.%s." % short_key_name
        cache_config = {}
        for skey in settings.keys():
            if skey.startswith(key_name):
                cache_config[skey[len(key_name) :]] = settings.get(skey)
        if cache_config:
            args[short_key_name] = cache_config

    log.debug(settings)
    log.debug(args)
    return args


def _filter_settings(settings, prefix):
    """
    Filter all settings to only return settings that start with a certain
    prefix.

    :param dict settings: A settings dictionary.
    :param str prefix: A prefix.
    """
    ret = {}
    for skey in settings.keys():
        if skey.startswith(prefix):
            key = skey[len(prefix) :]
            ret[key] = settings[skey]
    return ret


def _build_capakey(registry, settings):
    capakey = registry.queryUtility(ICapakey)
    if capakey is not None:
        return capakey
    if "cache_config" in settings:
        cache_config = settings["cache_config"]
        del settings["cache_config"]
    else:
        cache_config = {}
    gateway = CapakeyRestGateway(cache_config=cache_config)

    registry.registerUtility(gateway, ICapakey)
    return registry.queryUtility(ICapakey)


def _build_adressenregister(registry, settings):
    adressenregister = registry.queryUtility(IAdressenregister)
    if adressenregister is not None:
        return adressenregister
    if "cache_config" in settings:
        cache_config = settings["cache_config"]
        del settings["cache_config"]
    else:
        cache_config = None
    gateway = Gateway(
        client=AdressenRegisterClient(settings["base_url"], settings["api_key"]),
        cache_settings=cache_config,
    )

    registry.registerUtility(gateway, IAdressenregister)
    return registry.queryUtility(IAdressenregister)


def get_capakey(registry):
    """
    Get the Capakey Gateway

    :rtype: :class:`crabpy.gateway.capakey.CapakeyRestGateway`
    """
    # argument might be a config or a request
    regis = getattr(registry, "registry", None)
    if regis is None:
        regis = registry

    return regis.queryUtility(ICapakey)


def get_adressenregister(registry):
    """
    Get the Adresssenregister Gateway

    :rtype: :class:`crabpy.gateway.adressenregister.Gateway`
    # argument might be a config or a request
    """
    # argument might be a config or a request
    regis = getattr(registry, "registry", None)
    if regis is None:
        regis = registry

    return regis.queryUtility(IAdressenregister)


def _get_proxy_settings(settings):
    base_settings = {}
    http = settings.get("proxy.http", None)
    https = settings.get("proxy.https", None)
    if http or https:
        base_settings["proxy"] = {}
        if "proxy.http" in settings:
            base_settings["proxy"]["http"] = settings["proxy.http"]
            log.info("HTTP proxy: %s" % base_settings["proxy"]["http"])
        if "proxy.https" in settings:
            base_settings["proxy"]["https"] = settings["proxy.https"]
            log.info("HTTPS proxy: %s" % base_settings["proxy"]["https"])
    return base_settings


def add_route(config, name, pattern, *args, **kwargs):
    """
    Adds a pyramid route to the config. All args and kwargs will be
    passed on to config.add_route.

    This exists so the default behaviour of including crabpy will still be to
    cache all crabpy routes.
    """
    config.add_route(name, pattern, *args, **kwargs)
    GENERATE_ETAG_ROUTE_NAMES.add(name)


def conditional_http_tween_factory(handler, registry):
    """
    Tween that adds ETag headers and tells Pyramid to enable
    conditional responses where appropriate.
    """
    settings = registry.settings if hasattr(registry, "settings") else {}
    if "generate_etag_for.list" in settings:
        route_names = settings.get("generate_etag_for.list").split()
        GENERATE_ETAG_ROUTE_NAMES.update(route_names)

    def conditional_http_tween(request):
        response = handler(request)
        if request.matched_route is None:
            return response

        if request.matched_route.name in GENERATE_ETAG_ROUTE_NAMES:

            # If the Last-Modified header has been set, we want to enable the
            # conditional response processing.
            if response.last_modified is not None:
                response.conditional_response = True

            # We want to only enable the conditional machinery if either we
            # were given an explicit ETag header by the view or we have a
            # buffered response and can generate the ETag header ourself.
            if response.etag is not None:
                response.conditional_response = True
            elif (
                isinstance(response.app_iter, Sequence) and len(response.app_iter) == 1
            ) and response.body is not None:
                response.conditional_response = True
                response.md5_etag()

        return response

    return conditional_http_tween


def includeme(config):
    """
    Include `crabpy_pyramid` in this `Pyramid` application.

    :param pyramid.config.Configurator config: A Pyramid configurator.
    """

    settings = _parse_settings(config.registry.settings)
    base_settings = _get_proxy_settings(settings)

    # http caching tween
    if not settings.get("etag_tween_disabled", False):
        config.add_tween("crabpy_pyramid.conditional_http_tween_factory")

    # create cache
    root = settings.get("cache.file.root", "/tmp/dogpile_data")
    if not os.path.exists(root):
        os.makedirs(root)

    capakey_settings = dict(_filter_settings(settings, "capakey."), **base_settings)
    if "include" in capakey_settings:
        log.info(
            "The 'capakey.include' setting is deprecated. Capakey will "
            "always be included."
        )
    log.info("Adding CAPAKEY Gateway.")
    config.add_renderer("capakey_listjson", capakey_json_list_renderer)
    config.add_renderer("capakey_itemjson", capakey_json_item_renderer)
    _build_capakey(config.registry, capakey_settings)
    config.add_request_method(get_capakey, "capakey_gateway")
    config.add_directive("get_capakey", get_capakey)
    config.include("crabpy_pyramid.routes.capakey")
    config.scan("crabpy_pyramid.views.capakey")

    # adressenregister wordt afgekort tot adresreg
    adresreg_settings = dict(
        _filter_settings(settings, "adressenregister."), **base_settings
    )

    if adresreg_settings["include"]:
        log.info("Adding adressen register Gateway.")
        del adresreg_settings["include"]
        config.add_renderer("adresreg_listjson", adresreg_json_list_renderer)
        config.add_renderer("adresreg_itemjson", adresreg_json_item_renderer)
        _build_adressenregister(config.registry, adresreg_settings)
        config.add_directive("get_adressenregister", get_adressenregister)
        config.add_request_method(get_adressenregister, "adressenregister_gateway")
        config.include("crabpy_pyramid.routes.adressenregister")
        config.scan("crabpy_pyramid.views.adressenregister")
        config.scan("crabpy_pyramid.views.exceptions")


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    includeme(config)
    return config.make_wsgi_app()
