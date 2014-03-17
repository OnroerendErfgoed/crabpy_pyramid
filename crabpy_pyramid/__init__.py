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

def _parse_settings(settings, c):
    args = {}
    if c == 'capakey':
        defaults = {
            'user': None,
            'password': None,
            'wsdl': 'http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL'
        }
    else:
        defaults = {
            'wsdl': 'http://ws.agiv.be/crabws/nodataset.asmx?WSDL'
        }
    args = defaults.copy()

    # set settings
    for short_key_name in ('user', 'password', 'wsdl'):
        key_name = "%s.%s" % (c, short_key_name)
        if key_name in settings:
            args[short_key_name] = settings.get(
                key_name, defaults.get(short_key_name)
            )
    # not set user or password for capakey
    if c == 'capakey':
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
    return args


def _set_caches(settings, gateway, c):
    #create cache
    root = settings.get('root')
    if not os.path.exists(root):
        os.makedirs(root)
    for name in ('permanent', 'long', 'short'):
        gateway.caches[name] = make_region()
        gateway.caches[name].configure_from_config(settings, '%s.%s.' % (c, name))


def _build_capakey(registry):
    capakey = registry.queryUtility(ICapakey)
    if capakey is not None:
        return capakey
    settings = registry.settings
    capakey_settings = _parse_settings(settings, 'capakey')
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
    crab_settings = _parse_settings(settings, 'crab')
    factory = crab_factory(**crab_settings)
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
    config.add_renderer('listjson', json_list_renderer)
    config.add_renderer('itemjson', json_item_renderer)
    config.add_static_view('static', 'static', cache_max_age=3600)
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
    config.include('pyramid_chameleon')
    config.add_route('list_gemeenten', '/capakey/gemeenten')
    config.add_route('get_gemeente', '/capakey/gemeenten/{gemeente_id}')
    config.add_route(
        'list_kadastrale_afdelingen_by_gemeente',
        '/capakey/gemeenten/{gemeente_id}/afdelingen'
    )
    config.add_route('list_kadastrale_afdelingen', '/capakey/afdelingen')
    config.add_route(
        'get_kadastrale_afdeling_by_id',
        '/capakey/afdelingen/{afdeling_id}'
    )
    config.add_route(
        'list_secties_by_afdeling',
        '/capakey/afdelingen/{afdeling_id}/secties'
    )
    config.add_route(   
        'get_sectie_by_id_and_afdeling',
        '/capakey/afdelingen/{afdeling_id}/secties/{sectie_id}'
    )
    config.add_route(
        'list_percelen_by_sectie',
        '/capakey/afdelingen/{afdeling_id}/secties/{sectie_id}/percelen'
    )
    config.add_route(
        'get_perceel_by_sectie_and_id',
        '/capakey/afdelingen/{afdeling_id}/secties/{sectie_id}/percelen/{perceel_id1}/{perceel_id2}'
    )
    config.add_route(
        'get_perceel_by_capakey',
        '/capakey/percelen/{capakey1}/{capakey2}'
    )
    config.add_route('get_perceel_by_percid', '/capakey/percelen/{percid}')
    config.add_route('list_gewesten', '/crab/gewesten')
    config.add_route('get_gewest_by_id', '/crab/gewesten/{gewest_id}')
    config.add_route('list_gemeenten_crab', '/crab/gewesten/{gewest_id}/gemeenten')
    config.add_route('get_gemeente_crab', '/crab/gemeenten/{gemeente_id}')
    config.add_route('list_straten', '/crab/gemeenten/{gemeente_id}/straten')
    config.add_route('get_straat_by_id', '/crab/straten/{straat_id}')
    config.add_route('list_huisnummers', '/crab/straten/{straat_id}/huisnummers')
    config.add_route('get_huisnummer_by_straat_and_label', '/crab/straten/{straat_id}/huisnummers/{huisnummer_label}')
    config.add_route('get_huisnummer_by_id', '/crab/huisnummers/{huisnummer_id}')
    config.add_route('list_percelen', '/crab/huisnummers/{huisnummer_id}/percelen')
    config.add_route('get_perceel_by_id', '/crab/percelen/{perceel_id}')
    config.add_route('list_gebouwen', '/crab/huisnummers/{huisnummer_id}/gebouwen')
    config.add_route('get_gebouw_by_id', '/crab/gebouwen/{gebouw_id}')
    includeme(config)
    config.scan()
    return config.make_wsgi_app()
