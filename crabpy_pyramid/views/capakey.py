# -*- coding: utf-8 -*-
"""
Views for CAPAKEY services.

.. versionadded:: 0.1.0
"""
from pyramid.view import view_config
from crabpy_pyramid.utils import range_return, set_http_caching

from crabpy.gateway.exception import GatewayResourceNotFoundException

from pyramid.httpexceptions import HTTPNotFound


@view_config(route_name='list_gemeenten', renderer='capakey_listjson', accept='application/json')
def list_gemeenten(request):
    request = set_http_caching(request, 'capakey', 'permanent')
    Gateway = request.capakey_gateway()
    sort = request.params.get('sort', 1)
    gemeenten = Gateway.list_gemeenten(sort)
    return range_return(request, gemeenten)


@view_config(route_name='get_gemeente', renderer='capakey_itemjson', accept='application/json')
def get_gemeente_by_niscode(request):
    request = set_http_caching(request, 'capakey', 'long')
    Gateway = request.capakey_gateway()
    gemeente_id = int(request.matchdict.get('gemeente_id'))
    try:
        return Gateway.get_gemeente_by_id(gemeente_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()


@view_config(
    route_name='list_kadastrale_afdelingen_by_gemeente',
    renderer='capakey_listjson', accept='application/json'
)
def list_kadastrale_afdelingen_by_gemeente(request):
    request = set_http_caching(request, 'capakey', 'permanent')
    Gateway = request.capakey_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    sort = request.params.get('sort', 1)
    afdelingen = Gateway.list_kadastrale_afdelingen_by_gemeente(gemeente_id, sort)
    return range_return(request, afdelingen)


@view_config(route_name='list_kadastrale_afdelingen', renderer='capakey_listjson', accept='application/json')
def list_kadastrale_afdelingen(request):
    request = set_http_caching(request, 'capakey', 'permanent')
    Gateway = request.capakey_gateway()
    afdelingen = Gateway.list_kadastrale_afdelingen()
    return range_return(request, afdelingen)


@view_config(
    route_name='get_kadastrale_afdeling_by_id',
    renderer='capakey_itemjson', accept='application/json'
)
def get_kadastrale_afdeling_by_id(request):
    request = set_http_caching(request, 'capakey', 'long')
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    try:
        return Gateway.get_kadastrale_afdeling_by_id(afdeling_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()


@view_config(
    route_name='list_secties_by_afdeling',
    renderer='capakey_listjson', accept='application/json'
)
def list_secties_by_afdeling(request):
    request = set_http_caching(request, 'capakey', 'long')
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    secties = Gateway.list_secties_by_afdeling(afdeling_id)
    return range_return(request, secties)


@view_config(
    route_name='get_sectie_by_id_and_afdeling',
    renderer='capakey_itemjson', accept='application/json'
)
def get_sectie_by_id_and_afdeling(request):
    request = set_http_caching(request, 'capakey', 'long')
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    sectie_id = request.matchdict.get('sectie_id')
    try:
        return Gateway.get_sectie_by_id_and_afdeling(sectie_id, afdeling_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()


@view_config(
    route_name='list_percelen_by_sectie',
    renderer='capakey_listjson', accept='application/json'
)
def list_percelen_by_sectie(request):
    request = set_http_caching(request, 'capakey', 'short')
    Gateway = request.capakey_gateway()
    sectie_id = request.matchdict.get('sectie_id')
    afdeling_id = request.matchdict.get('afdeling_id')
    sectie = Gateway.get_sectie_by_id_and_afdeling(sectie_id, afdeling_id)
    percelen = Gateway.list_percelen_by_sectie(sectie)
    return range_return(request, percelen)


@view_config(
    route_name='get_perceel_by_sectie_and_id',
    renderer='capakey_itemjson', accept='application/json'
)
def get_perceel_by_sectie_and_id(request):
    request = set_http_caching(request, 'capakey', 'short')
    Gateway = request.capakey_gateway()
    perceel_id = str(request.matchdict.get('perceel_id1')) + '/' \
                 + str(request.matchdict.get('perceel_id2'))
    sectie_id = request.matchdict.get('sectie_id')
    afdeling_id = request.matchdict.get('afdeling_id')
    sectie = Gateway.get_sectie_by_id_and_afdeling(sectie_id, afdeling_id)
    try:
        return Gateway.get_perceel_by_id_and_sectie(perceel_id, sectie)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()


@view_config(
    route_name='get_perceel_by_capakey',
    renderer='capakey_itemjson', accept='application/json'
)
def get_perceel_by_capakey(request):
    request = set_http_caching(request, 'capakey', 'short')
    Gateway = request.capakey_gateway()
    capakey = str(request.matchdict.get('capakey1')) + '/' \
              + str(request.matchdict.get('capakey2'))
    try:
        return Gateway.get_perceel_by_capakey(capakey)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()


@view_config(
    route_name='get_perceel_by_percid',
    renderer='capakey_itemjson', accept='application/json'
)
def get_perceel_by_percid(request):
    request = set_http_caching(request, 'capakey', 'short')
    Gateway = request.capakey_gateway()
    percid = request.matchdict.get('percid')
    try:
        return Gateway.get_perceel_by_percid(percid)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()
