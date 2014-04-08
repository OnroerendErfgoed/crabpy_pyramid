# -*- coding: utf-8 -*-
'''
Views for capakey services
.. versionadded:: 0.1.0
'''
from pyramid.view import view_config
from .utils import range_return

@view_config(route_name='list_gemeenten', renderer='listjson', accept='application/json')
def list_gemeenten(request):
    Gateway = request.capakey_gateway()
    gemeenten = Gateway.list_gemeenten(1)
    total = len(gemeenten)
    r = range_return(request, total)
    return gemeenten[r[0]: r[1]]


@view_config(route_name='get_gemeente', renderer='itemjson', accept='application/json')
def get_gemeente_by_niscode(request):
    Gateway = request.capakey_gateway()
    gemeente_id = int(request.matchdict.get('gemeente_id'))
    return Gateway.get_gemeente_by_id(gemeente_id)


@view_config(
    route_name='list_kadastrale_afdelingen_by_gemeente',
    renderer='listjson', accept='application/json'
)
def list_kadastrale_afdelingen_by_gemeente(request):
    Gateway = request.capakey_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    afdelingen = Gateway.list_kadastrale_afdelingen_by_gemeente(gemeente_id)
    total = len(afdelingen)
    r = range_return(request, total)
    return afdelingen[r[0]:r[1]]


@view_config(route_name='list_kadastrale_afdelingen', renderer='listjson', accept='application/json')
def list_kadastrale_afdelingen(request):
    Gateway = request.capakey_gateway()
    afdelingen = Gateway.list_kadastrale_afdelingen()
    total = len(afdelingen)
    r = range_return(request, total)
    return afdelingen[r[0]:r[1]]


@view_config(
    route_name='get_kadastrale_afdeling_by_id',
    renderer='itemjson', accept='application/json'
)
def get_kadastrale_afdeling_by_id(request):
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    return Gateway.get_kadastrale_afdeling_by_id(afdeling_id)


@view_config(route_name='list_secties_by_afdeling', renderer='listjson', accept='application/json')
def list_secties_by_afdeling(request):
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    secties = Gateway.list_secties_by_afdeling(afdeling_id)
    total = len(secties)
    r = range_return(request, total)
    return secties[r[0]:r[1]]


@view_config(
    route_name='get_sectie_by_id_and_afdeling',
    renderer='itemjson', accept='application/json'
)
def get_sectie_by_id_and_afdeling(request):
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    sectie_id = request.matchdict.get('sectie_id')
    return Gateway.get_sectie_by_id_and_afdeling(sectie_id, afdeling_id)


@view_config(route_name='list_percelen_by_sectie', renderer='listjson', accept='application/json')
def list_percelen_by_sectie(request):
    Gateway = request.capakey_gateway()
    sectie_id = request.matchdict.get('sectie_id')
    afdeling_id = request.matchdict.get('afdeling_id')
    sectie = Gateway.get_sectie_by_id_and_afdeling(sectie_id, afdeling_id)
    percelen = Gateway.list_percelen_by_sectie(sectie)
    total = len(percelen)
    r = range_return(request, total)
    return percelen[r[0]:r[1]]


@view_config(
    route_name='get_perceel_by_sectie_and_id',
    renderer='itemjson', accept='application/json'
)
def get_perceel_by_sectie_and_id(request):
    Gateway = request.capakey_gateway()
    perceel_id = str(request.matchdict.get('perceel_id1'))+'/'\
        + str(request.matchdict.get('perceel_id2'))
    sectie_id = request.matchdict.get('sectie_id')
    afdeling_id = request.matchdict.get('afdeling_id')
    sectie = Gateway.get_sectie_by_id_and_afdeling(sectie_id, afdeling_id)
    return Gateway.get_perceel_by_id_and_sectie(perceel_id, sectie)


@view_config(route_name='get_perceel_by_capakey', renderer='itemjson', accept='application/json')
def get_perceel_by_capakey(request):
    Gateway = request.capakey_gateway()
    capakey = str(request.matchdict.get('capakey1'))+'/'\
        + str(request.matchdict.get('capakey2'))
    return Gateway.get_perceel_by_capakey(capakey)


@view_config(
    route_name='get_perceel_by_percid',
    renderer='itemjson', accept='application/json'
)
def get_perceel_by_percid(request):
    Gateway = request.capakey_gateway()
    percid = request.matchdict.get('percid')
    return Gateway.get_perceel_by_percid(percid)

''' Views for crab services '''

@view_config(route_name='list_gewesten', renderer='listjson', accept='application/json')
def list_gewesten(request):
    Gateway = request.crab_gateway()
    gewesten = Gateway.list_gewesten()
    total = len(gewesten)
    r = range_return(request, total)
    return gewesten[r[0]: r[1]]

@view_config(route_name='get_gewest_by_id', renderer='itemjson', accept='application/json')
def get_gewest_by_id(request):
    Gateway = request.crab_gateway()
    gewest_id = int(request.matchdict.get('gewest_id'))
    return Gateway.get_gewest_by_id(gewest_id)
    
@view_config(route_name='list_gemeenten_crab', renderer='listjson', accept='application/json')
def list_gemeenten_crab(request):
    Gateway = request.crab_gateway()
    gewest_id = request.matchdict.get('gewest_id')
    gemeenten = Gateway.list_gemeenten(gewest_id)
    total = len(gemeenten)
    r = range_return(request, total)
    return gemeenten[r[0]: r[1]]

@view_config(route_name='get_gemeente_crab', renderer='itemjson', accept='application/json')
def get_gemeente_crab(request):
    Gateway = request.crab_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    if len(gemeente_id) == 5:
        return Gateway.get_gemeente_by_niscode(gemeente_id)
    else:
        return Gateway.get_gemeente_by_id(gemeente_id)
    

@view_config(route_name='list_straten', renderer='listjson', accept='application/json')
def list_straten(request):
    Gateway = request.crab_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    if len(gemeente_id)==5:
        gemeente_id = Gateway.get_gemeente_by_niscode(gemeente_id)
    straten = Gateway.list_straten(gemeente_id)
    total = len(straten)
    r = range_return(request, total)
    return straten[r[0]: r[1]]
    

@view_config(route_name='get_straat_by_id', renderer='itemjson', accept='application/json')
def get_straat_by_id(request):
    Gateway = request.crab_gateway()
    straat_id = request.matchdict.get('straat_id')
    return Gateway.get_straat_by_id(straat_id)

@view_config(route_name='list_huisnummers', renderer='listjson', accept='application/json')
def list_huisnummers(request):
    Gateway = request.crab_gateway()
    straat_id = request.matchdict.get('straat_id')
    huisnummers = Gateway.list_huisnummers_by_straat(straat_id)
    total = len(huisnummers)
    r = range_return(request, total)
    return huisnummers[r[0]: r[1]]

@view_config(route_name='get_huisnummer_by_straat_and_label', renderer='itemjson', accept='application/json')
def get_huisnummer_by_straat_and_label(request):
    Gateway = request.crab_gateway()
    straat_id = request.matchdict.get('straat_id')
    huisnummer = request.matchdict.get('huisnummer_label')
    return Gateway.get_huisnummer_by_nummer_and_straat(huisnummer, straat_id)
    
    
@view_config(route_name='get_huisnummer_by_id', renderer='itemjson', accept='application/json')
def get_huisnummer_by_id(request):
    Gateway = request.crab_gateway()
    huisnummer_id = request.matchdict.get('huisnummer_id')
    return Gateway.get_huisnummer_by_id(huisnummer_id)

@view_config(route_name='list_percelen', renderer='listjson', accept='application/json')
def list_percelen(request):
    Gateway = request.crab_gateway()
    huisnummer_id = request.matchdict.get('huisnummer_id')
    percelen = Gateway.list_percelen_by_huisnummer(huisnummer_id)
    total = len(percelen)
    r = range_return(request, total)
    return percelen[r[0]: r[1]]

@view_config(route_name='get_perceel_by_id', renderer='itemjson', accept='application/json')
def get_perceel_by_id(request):
    Gateway = request.crab_gateway()
    perceel_id = request.matchdict.get('perceel_id1')+'/'+request.matchdict.get('perceel_id2')
    return Gateway.get_perceel_by_id(perceel_id)

@view_config(route_name='list_gebouwen', renderer='listjson', accept='application/json')
def list_gebouwen(request):
    Gateway = request.crab_gateway()
    huisnummer_id = request.matchdict.get('huisnummer_id')
    gebouwen = Gateway.list_gebouwen_by_huisnummer(huisnummer_id)
    total = len(gebouwen)
    r = range_return(request, total)
    return gebouwen[r[0]: r[1]]

@view_config(route_name='get_gebouw_by_id', renderer='itemjson', accept='application/json')
def get_gebouw_by_id(request):
    Gateway = request.crab_gateway()
    gebouw_id = request.matchdict.get('gebouw_id')
    return Gateway.get_gebouw_by_id(gebouw_id)
    
@view_config(route_name='get_wegobject', renderer='itemjson', accept='application/json')
def get_wegobject(request):
    Gateway = request.crab_gateway()
    wegobject_id = request.matchdict.get('wegobject_id')
    return Gateway.get_wegobject_by_id(wegobject_id)
