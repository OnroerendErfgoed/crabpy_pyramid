# -*- coding: utf-8 -*-
'''
including all the route information
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
    config.add_route('get_perceel_by_percid', '/capakey/percelen/{percid}')
    config.add_route('list_gewesten', '/crab/gewesten')
    config.add_route('get_gewest_by_id', '/crab/gewesten/{gewest_id}')
    config.add_route('list_gemeenten_crab', '/crab/gewesten/{gewest_id}/gemeenten')
    config.add_route('get_gemeente_crab', '/crab/gemeenten/{gemeente_id}')
    config.add_route('list_straten', '/crab/gemeenten/{gemeente_id}/straten')
    config.add_route('get_straat_by_id', '/crab/straten/{straat_id}')
    config.add_route('get_wegobject', '/crab/wegobjecten/{wegobject_id}')
    config.add_route('list_huisnummers', '/crab/straten/{straat_id}/huisnummers')
    config.add_route('get_huisnummer_by_straat_and_label', '/crab/straten/{straat_id}/huisnummers/{huisnummer_label}')
    config.add_route('get_huisnummer_by_id', '/crab/huisnummers/{huisnummer_id}')
    config.add_route('list_percelen', '/crab/huisnummers/{huisnummer_id}/percelen')
    config.add_route('get_perceel_by_id', '/crab/percelen/{perceel_id1}/{perceel_id2}')
    config.add_route('list_gebouwen', '/crab/huisnummers/{huisnummer_id}/gebouwen')
    config.add_route('get_gebouw_by_id', '/crab/gebouwen/{gebouw_id}')
