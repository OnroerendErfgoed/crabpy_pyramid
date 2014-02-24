from pyramid.config import Configurator

import warnings

from pyramid.settings import asbool

from crabpy.gateway import capakey
from crabpy.gateway.capakey import CapakeyGateway
from crabpy.client import capakey_factory
from zope.interface import Interface

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
    config.add_route('list_gemeenten', '/list_gemeenten/{sort}')
    config.add_route('get_gemeente_by_id', '/get_gemeente_by_id/{id}')
    includeme(config)
    config.scan()
    return config.make_wsgi_app()
