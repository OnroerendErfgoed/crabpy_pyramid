# -*- coding: utf-8 -*-
'''
Routes for the CRAB views.

.. versionadded:: 0.1.0
'''
def includeme(config):
    config.add_route('list_gewesten', '/crab/gewesten')
    config.add_route('get_gewest_by_id', '/crab/gewesten/{gewest_id}')
    config.add_route('list_provincies', '/crab/gewesten/{gewest_id}/provincies')
    config.add_route('get_provincie', '/crab/provincies/{provincie_id}')
    config.add_route('list_gemeenten_by_provincie', '/crab/provincies/{provincie_id}/gemeenten')
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
    config.add_route('list_subadressen', '/crab/huisnummers/{huisnummer_id}/subadressen')
    config.add_route('get_subadres_by_id', '/crab/subadressen/{subadres_id}')
    config.add_route('list_postkantons_by_gemeente', '/crab/gemeenten/{gemeente_id}/postkantons')
