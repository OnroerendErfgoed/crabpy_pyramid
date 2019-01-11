# -*- coding: utf-8 -*-
"""
Routes for the CAPAKEY views.

.. versionadded:: 0.1.0
"""
import crabpy_pyramid


def includeme(config):
    crabpy_pyramid.add_route(config,
                             'list_gemeenten',
                             '/capakey/gemeenten')
    crabpy_pyramid.add_route(config,
                             'get_gemeente',
                             '/capakey/gemeenten/{gemeente_id}')
    crabpy_pyramid.add_route(config,
                             'list_kadastrale_afdelingen_by_gemeente',
                             '/capakey/gemeenten/{gemeente_id}/afdelingen')
    crabpy_pyramid.add_route(config,
                             'list_kadastrale_afdelingen',
                             '/capakey/afdelingen')
    crabpy_pyramid.add_route(config,
                             'get_kadastrale_afdeling_by_id',
                             '/capakey/afdelingen/{afdeling_id}')
    crabpy_pyramid.add_route(config,
                             'list_secties_by_afdeling',
                             '/capakey/afdelingen/{afdeling_id}/secties')
    crabpy_pyramid.add_route(
        config,
        'get_sectie_by_id_and_afdeling',
        '/capakey/afdelingen/{afdeling_id}/secties/{sectie_id}')
    crabpy_pyramid.add_route(
        config,
        'list_percelen_by_sectie',
        '/capakey/afdelingen/{afdeling_id}/secties/{sectie_id}/percelen')
    crabpy_pyramid.add_route(
        config,
        'get_perceel_by_sectie_and_id',
        '/capakey/afdelingen/{afdeling_id}/secties/{sectie_id}'
        '/percelen/{perceel_id1}/{perceel_id2}')
    crabpy_pyramid.add_route(config,
                             'get_perceel_by_capakey',
                             '/capakey/percelen/{capakey1}/{capakey2}')
    crabpy_pyramid.add_route(config,
                             'get_perceel_by_percid',
                             '/capakey/percelen/{percid}')
