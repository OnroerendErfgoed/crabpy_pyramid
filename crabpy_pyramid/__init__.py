from pyramid.config import Configurator

import warnings

from pyramid.settings import asbool


class ICapakey():
    pass

def _parse_settings(settings):
    capakey_args = {}
    defaults = {
        'capakey.user': None,
        'capakey.password': None,
        'capakey.wsdl': "http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
    }
    capakey_args = defaults.copy()

    # set settings
    for key_name in ('capakey.user', 'capakey.password', 'capakey.wsdl'):
        if key_name in settings:
            capakey_args[key_name] = settings.get(key_name, defaults.get(key_name))

    # not set user or password
    for key_name in ('capakey.user', 'capakey.password'):
        if capakey_args[key_name] is None:
            warnings.warn(
                '%s was not found in the settings, \
capakey needs this parameter to function properly.' % key_name,
                UserWarning
            )
    return capakey_args


def get_capakey(registry):
    '''
    Get the Capakey connection
    '''
    #argument might be a config or a request
    regis = getattr(registry, 'registry', None)
    if regis is None:
        regis = registry
    return regis.settings 


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    _parse_settings(config.registry)
    config.add_directive('get_capakey', get_capakey)


def main(global_config, **settings):
    '''
     This function returns a Pyramid WSGI application.
    '''
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('page', '/page')
    includeme(config)
    config.scan()
    return config.make_wsgi_app()
