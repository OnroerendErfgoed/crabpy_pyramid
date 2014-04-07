from pyramid.config import Configurator
import os
import warnings
from dogpile.cache import make_region

from crabpy.gateway.capakey import CapakeyGateway
from crabpy.gateway.crab import CrabGateway
from crabpy.client import capakey_factory, crab_factory
from zope.interface import Interface

from crabpy_pyramid.utils import (
    json_list_renderer,
    json_item_renderer
)


class ICapakey(Interface):
    pass


class ICrab(Interface):
    pass

def _parse_settings(settings):
    args = {}
    defaults = {
        'user': None,
        'password': None
    }
    args = defaults.copy()

    # set settings
    for short_key_name in ('user', 'password'):
        key_name = "capakey.%s" % (short_key_name)
        if key_name in settings:
            args[short_key_name] = settings.get(
                key_name, defaults.get(short_key_name)
            )
    # not set user or password
    for short_key_name in ('user', 'password'):
        if (
            (not short_key_name in args) or
            args[short_key_name] is None
        ):
            warnings.warn(
                '%s was not found in the settings, \
    capakey needs this parameter to function properly.' % short_key_name,
                UserWarning
            )
    # set proxy
    args['proxy'] = get_proxy(settings)
    
    
    return args


def _set_caches(settings, gateway, c):
    #create cache
    root = settings.get('root')
    if not os.path.exists(root):
        os.makedirs(root)
    for name in ('permanent', 'long', 'short'):
        gateway.caches[name] = make_region(key_mangler=str)
        gateway.caches[name].configure_from_config(settings, '%s.%s.' % (c, name))

def get_proxy(settings):
    args = {}
    for short_key_name in ('http', 'https'):
        key_name = "proxy.%s" % (short_key_name)
        if key_name in settings:
            args[short_key_name] = settings.get(key_name)
    return args

def _build_capakey(registry):
    capakey = registry.queryUtility(ICapakey)
    if capakey is not None:
        return capakey
    settings = registry.settings
    capakey_settings = _parse_settings(settings)
    factory = capakey_factory(**capakey_settings)
    gateway = CapakeyGateway(factory)
    _set_caches(settings, gateway, 'capakey')

    registry.registerUtility(gateway, ICapakey)
    return registry.queryUtility(ICapakey)


def _build_crab(registry):
    crab = registry.queryUtility(ICrab)
    if crab is not None:
        return crab
    settings = registry.settings
    proxy = {}
    proxy['proxy'] = get_proxy(settings)
    factory = crab_factory(**proxy)
    gateway = CrabGateway(factory)
    _set_caches(settings, gateway, 'crab')
    
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
    
    # including routes
    config.include('crabpy_pyramid.routes')
    
    config.add_renderer('listjson', json_list_renderer)
    config.add_renderer('itemjson', json_item_renderer)
    _build_capakey(config.registry)
    _build_crab(config.registry)
    config.add_directive('get_capakey', get_capakey)
    config.add_directive('get_crab', get_crab)
    config.add_request_method(get_capakey, 'capakey_gateway')
    config.add_request_method(get_crab, 'crab_gateway')


def main(global_config, **settings):
    '''
     This function returns a Pyramid WSGI application.
    '''
    config = Configurator(settings=settings)
    
    includeme(config)
    config.scan()
    return config.make_wsgi_app()
