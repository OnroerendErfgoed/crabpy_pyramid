from pyramid.config import Configurator
import os
import warnings
from dogpile.cache import make_region

from crabpy.gateway.capakey import CapakeyGateway
from crabpy.gateway.crab import CrabGateway
from crabpy.client import capakey_factory, crab_factory
from zope.interface import Interface

from crabpy_pyramid.renderers.capakey import (
    json_list_renderer as capakey_json_list_renderer,
    json_item_renderer as capakey_json_item_renderer
)

from crabpy_pyramid.renderers.crab import (
    json_list_renderer as crab_json_list_renderer,
    json_item_renderer as crab_json_item_renderer
)

from pyramid.settings import asbool


class ICapakey(Interface):
    pass


class ICrab(Interface):
    pass

def _parse_settings(settings):
    args = {}
    defaults = {
        'capakey.include' : False,
        'crab.include' : True,
        'capakey.user': None,
        'capakey.password': None,
        'cache.file.root': '/tmp/dogpile_data'
    }
    args = defaults.copy()

    # booelean settings
    for short_key_name in ('capakey.include', 'crab.include'):
        key_name = "crabpy.%s" % (short_key_name)
        if key_name in settings:
            args[short_key_name] = asbool(settings.get(
                key_name, defaults.get(short_key_name)
            ))

    # set settings
    for short_key_name in ('capakey.user', 'capakey.password'):
        key_name = "crabpy.%s" % (short_key_name)
        if key_name in settings:
            args[short_key_name] = settings.get(
                key_name, defaults.get(short_key_name)
            )
    # not set user or password
    for short_key_name in ('capakey.user', 'capakey.password'):
        if (
            (not short_key_name in args) or
            args[short_key_name] is None
        ):
            warnings.warn(
                '%s was not found in the settings, \
    capakey needs this parameter to function properly.' % short_key_name,
                UserWarning
            )
    # string setting
    for short_key_name in ('proxy.http', 'proxy.https', 'cache.file.root'):
        key_name = "crabpy.%s" % (short_key_name)
        if key_name in settings:
            args[short_key_name] = settings.get(key_name)

    # cache configuration
    for short_key_name in ('crab.cache_config', 'capakey.cache_config'):
        key_name = "crabpy.%s." % (short_key_name)
        cache_config = {}
        for skey in settings.keys():
            if skey.startswith(key_name):
                cache_config[skey[len(key_name):]] = settings.get(skey)
        if cache_config:
            args[short_key_name] = cache_config
    
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
            key = skey[len(prefix):]
            ret[key] = settings[skey]
    return ret

def _build_capakey(registry, settings):
    capakey = registry.queryUtility(ICapakey)
    if capakey is not None:
        return capakey
    if 'cache_config' in settings:
        cache_config = settings['cache_config']
        del settings['cache_config']
    else:
        cache_config = {}
    print settings
    factory = capakey_factory(**settings)
    gateway = CapakeyGateway(factory, cache_config=cache_config)

    registry.registerUtility(gateway, ICapakey)
    return registry.queryUtility(ICapakey)


def _build_crab(registry, settings):
    crab = registry.queryUtility(ICrab)
    if crab is not None:
        return crab
    if 'cache_config' in settings:
        cache_config = settings['cache_config']
        del settings['cache_config']
    else:
        cache_config = {}
    print settings
    factory = crab_factory(**settings)
    gateway = CrabGateway(factory, cache_config=cache_config)
    
    registry.registerUtility(gateway, ICrab)
    return registry.queryUtility(ICapakey)


def get_capakey(registry):
    '''
    Get the Capakey Gateway
    '''
    #argument might be a config or a request
    regis = getattr(registry, 'registry', None)
    if regis is None:
        regis = registry

    return regis.queryUtility(ICapakey)
    
def get_crab(registry):
    '''
    Get the Crab Gateway
    '''
    #argument might be a config or a request
    regis = getattr(registry, 'registry', None)
    if regis is None:
        regis = registry
        
    return regis.queryUtility(ICrab)


def includeme(config):


    settings = _parse_settings(config.registry.settings)

    # create cache
    root = settings.get('cache.file.root', '/tmp/dogpile_data')
    if not os.path.exists(root):
        os.makedirs(root)

    capakey_settings = _filter_settings(settings, 'capakey.')
    if capakey_settings['include']:
        del capakey_settings['include']
        config.add_renderer('capakey_listjson', capakey_json_list_renderer)
        config.add_renderer('capakey_itemjson', capakey_json_item_renderer)
        _build_capakey(config.registry, capakey_settings)
        config.add_request_method(get_capakey, 'capakey_gateway')
        config.add_directive('get_capakey', get_capakey)
        config.include('crabpy_pyramid.routes.capakey')
        config.scan('crabpy_pyramid.views.capakey')
    
    crab_settings = _filter_settings(settings, 'crab.')
    if crab_settings['include']:
        del crab_settings['include']
        config.add_renderer('crab_listjson', crab_json_list_renderer)
        config.add_renderer('crab_itemjson', crab_json_item_renderer)
        _build_crab(config.registry, crab_settings)
        config.add_directive('get_crab', get_crab)
        config.add_request_method(get_crab, 'crab_gateway')
        config.include('crabpy_pyramid.routes.crab')
        config.scan('crabpy_pyramid.views.crab')


def main(global_config, **settings):
    '''
     This function returns a Pyramid WSGI application.
    '''
    config = Configurator(settings=settings)
    
    includeme(config)
    return config.make_wsgi_app()
