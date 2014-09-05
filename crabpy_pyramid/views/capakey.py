# -*- coding: utf-8 -*-
'''
Views for CAPAKEY services.

.. versionadded:: 0.1.0
'''
from pyramid.view import view_config
from crabpy_pyramid.utils import range_return

@view_config(route_name='list_gemeenten', renderer='capakey_listjson', accept='application/json')
def list_gemeenten(request):
    Gateway = request.capakey_gateway()
    gemeenten = Gateway.list_gemeenten(1)
    return range_return(request, gemeenten)


@view_config(route_name='get_gemeente', renderer='capakey_itemjson', accept='application/json')
def get_gemeente_by_niscode(request):
    Gateway = request.capakey_gateway()
    gemeente_id = int(request.matchdict.get('gemeente_id'))
    return Gateway.get_gemeente_by_id(gemeente_id)


@view_config(
    route_name='list_kadastrale_afdelingen_by_gemeente',
    renderer='capakey_listjson', accept='application/json'
)
def list_kadastrale_afdelingen_by_gemeente(request):
    Gateway = request.capakey_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    afdelingen = Gateway.list_kadastrale_afdelingen_by_gemeente(gemeente_id)
    return range_return(request, afdelingen)


@view_config(route_name='list_kadastrale_afdelingen', renderer='capakey_listjson', accept='application/json')
def list_kadastrale_afdelingen(request):
    Gateway = request.capakey_gateway()
    afdelingen = Gateway.list_kadastrale_afdelingen()
    return range_return(request, afdelingen)


@view_config(
    route_name='get_kadastrale_afdeling_by_id',
    renderer='capakey_itemjson', accept='application/json'
)
def get_kadastrale_afdeling_by_id(request):
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    return Gateway.get_kadastrale_afdeling_by_id(afdeling_id)


@view_config(
    route_name='list_secties_by_afdeling',
    renderer='capakey_listjson', accept='application/json'
)
def list_secties_by_afdeling(request):
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    secties = Gateway.list_secties_by_afdeling(afdeling_id)
    return range_return(request, secties)


@view_config(
    route_name='get_sectie_by_id_and_afdeling',
    renderer='capakey_itemjson', accept='application/json'
)
def get_sectie_by_id_and_afdeling(request):
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    sectie_id = request.matchdict.get('sectie_id')
    return Gateway.get_sectie_by_id_and_afdeling(sectie_id, afdeling_id)


@view_config(
    route_name='list_percelen_by_sectie',
    renderer='capakey_listjson', accept='application/json'
)
def list_percelen_by_sectie(request):
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
    Gateway = request.capakey_gateway()
    perceel_id = str(request.matchdict.get('perceel_id1'))+'/'\
        + str(request.matchdict.get('perceel_id2'))
    sectie_id = request.matchdict.get('sectie_id')
    afdeling_id = request.matchdict.get('afdeling_id')
    sectie = Gateway.get_sectie_by_id_and_afdeling(sectie_id, afdeling_id)
    return Gateway.get_perceel_by_id_and_sectie(perceel_id, sectie)


@view_config(
    route_name='get_perceel_by_capakey',
    renderer='capakey_itemjson', accept='application/json'
)
def get_perceel_by_capakey(request):
    Gateway = request.capakey_gateway()
    capakey = str(request.matchdict.get('capakey1'))+'/'\
        + str(request.matchdict.get('capakey2'))
    return Gateway.get_perceel_by_capakey(capakey)


@view_config(
    route_name='get_perceel_by_percid',
    renderer='capakey_itemjson', accept='application/json'
)
def get_perceel_by_percid(request):
    Gateway = request.capakey_gateway()
    percid = request.matchdict.get('percid')
    return Gateway.get_perceel_by_percid(percid)
