from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


class ICapakey():
    pass


def _parse_settings(settings):
    capakey_args={}
    defaults={
        'user' = None,
        'password' = None,
        'wsdl' = "http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
    }
    capakey_args = defaults.copy()
    
    # set settings
    for short_key_name in ('user', 'password', 'wsdl'):
        key_name='capakey.%s' % (short_key_name)
        if key_name in settings:
            capakey_args[key_name] = \
                settings.get(key_name, defaults.get(short_key_name))
                
    # not set user or password
    for short_key_name in ('user', 'password'):
        key_name='capakey.%s' % (short_key_name)
        if key_name == None:
            warnings.warn(
                '%s was not found in the settings, \
                    capakey needs this parameter to function properly.',
                UserWarning 
            )


def _build_capakey(registry):
    '''
    Build a Capakey connection to Elasticsearch and add it to the registry.
    '''
    ES = registry.queryUtility(ICapakey)
    if ES is not None:
        return ES
    settings = registry.settings
    capakey_args = _parse_settings(settings)
    ES = capakey.Elastic(**capakey_args)
    registry.register.Utility(ES, ICapakey)
    return registry.queryUtility(ICapakey)


def _get_capakey(registry):
    '''
    Get the Capakey connection
    '''
    #argument might be a config or a request
    regis = getattr(registry, 'registry', None)
    if regis is None:
        regis = registry
    return regis.queryUtility(ICapakey)
    

def includeme(config):
    _build_capakey(config.registry)
    config.add_directive('get_capakey',get_capakey)






























def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
