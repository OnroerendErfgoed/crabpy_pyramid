from pyramid.config import Configurator

import warnings

from pyramid.settings import asbool

from crabpy.gateway import capakey
from crabpy.gateway.capakey import CapakeyGateway
from crabpy.client import capakey_factory
from zope.interface import Interface

from crabpy_pyramid.utils import (
    json_list_renderer,
    json_item_renderer
)

class ICapakey(Interface):
    pass


def _parse_settings(settings):
    capakey_args = {}
    defaults = {
        'user': None,
        'password': None,
        'wsdl': "http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
    }
    capakey_args = defaults.copy()

    # set settings
    for short_key_name in ('user', 'password', 'wsdl'):
        key_name = "capakey.%s" % short_key_name
        if key_name in settings:
            capakey_args[short_key_name] = settings.get(
                key_name, defaults.get(short_key_name)
            )

    # not set user or password
    for short_key_name in ('user', 'password'):
        if capakey_args[short_key_name] is None:
            warnings.warn(
                '%s was not found in the settings, \
capakey needs this parameter to function properly.' % key_name,
                UserWarning
            )
    return capakey_args

def _build_capakey(registry):
    """
    Build a RawES connection to Elastic Search and add it to the registry.
    """
    ES = registry.queryUtility(ICapakey)
    if ES is not None:
        return ES

    settings = registry.settings
    capakey_args = _parse_settings(settings)
    ES = CapakeyGateway(capakey_factory(**capakey_args))

    registry.registerUtility(ES, ICapakey)
    return registry.queryUtility(ICapakey)

def get_capakey(registry):
    '''
    Get the Capakey connection
    '''
    #argument might be a config or a request
    regis = getattr(registry, 'registry', None)
    if regis is None:
        regis = registry(ICapakey)

    return regis.queryUtility(ICapakey)


def includeme(config):
    config.add_renderer('listjson', json_list_renderer)
    config.add_renderer('itemjson', json_item_renderer)
    config.add_static_view('static', 'static', cache_max_age=3600)
    _build_capakey(config.registry)
    config.add_directive('get_capakey', get_capakey)
    config.add_request_method(get_capakey, 'capakey_gateway')


def main(global_config, **settings):
    '''
     This function returns a Pyramid WSGI application.
    '''
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('list_gemeenten', '/capakey/gemeenten')
    config.add_route('get_gemeente', '/capakey/gemeenten/{gemeente_id}')
    config.add_route('list_kadastrale_afdelingen_by_gemeente', '/capakey/gemeenten/{gemeente_id}/afdelingen')
    config.add_route('list_kadastrale_afdelingen', '/capakey/afdelingen')
    config.add_route('get_kadastrale_afdeling_by_id', '/capakey/afdelingen/{afdeling_id}')
    config.add_route('list_secties_by_afdeling', '/capakey/afdelingen/{afdeling_id}/secties')
    config.add_route('get_sectie_by_id_and_afdeling', '/capakey/afdelingen/{afdeling_id}/secties/{sectie_id}')
    config.add_route('list_percelen_by_sectie', '/capakey/afdelingen/{afdeling_id}/secties/{sectie_id}/percelen')
    config.add_route('get_perceel_by_sectie_and_id', '/capakey/afdelingen/{afdeling_id}/secties/{sectie_id}/percelen/{perceel_id1}/{perceel_id2}')
    config.add_route('get_perceel_by_capakey', '/capakey/percelen/{capakey1}/{capakey2}')
    config.add_route('get_perceel_by_percid', '/capakey/percelen/{percid}')
    includeme(config)
    config.scan()
    return config.make_wsgi_app()
