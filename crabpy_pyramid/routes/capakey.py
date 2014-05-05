# -*- coding: utf-8 -*-
'''
Routes for the CAPAKEY views.

.. versionadded:: 0.1.0
'''
def includeme(config):
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
    config.add_route(
        'get_perceel_by_percid',
        '/capakey/percelen/{percid}'
    )
