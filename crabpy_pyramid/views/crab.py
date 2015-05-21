# -*- coding: utf-8 -*-
'''
Views for CRAB services

.. versionadded:: 0.1.0
'''
from pyramid.view import view_config
from crabpy_pyramid.utils import range_return
import pycountry

from crabpy.gateway.exception import GatewayResourceNotFoundException

from pyramid.httpexceptions import HTTPNotFound

@view_config(
    route_name='list_gewesten',
    renderer='crab_listjson', accept='application/json'
)
def list_gewesten(request):
    Gateway = request.crab_gateway()
    gewesten = Gateway.list_gewesten()
    return range_return(request, gewesten)

@view_config(
    route_name='get_gewest_by_id',
    renderer='crab_itemjson', accept='application/json'
)
def get_gewest_by_id(request):
    Gateway = request.crab_gateway()
    gewest_id = int(request.matchdict.get('gewest_id'))
    try:
        return Gateway.get_gewest_by_id(gewest_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()

@view_config(
    route_name='list_provincies',
    renderer='crab_listjson', accept='application/json'
)
def list_provincies(request):
    Gateway = request.crab_gateway()
    gewest_id = int(request.matchdict.get('gewest_id'))
    provincies = Gateway.list_provincies(gewest_id)
    return range_return(request, provincies)

@view_config(
    route_name='get_provincie',
    renderer='crab_itemjson', accept='application/json'
)
def get_provincie(request):
    Gateway = request.crab_gateway()
    provincie_id = int(request.matchdict.get('provincie_id'))
    try:
        return Gateway.get_provincie_by_id(provincie_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()

@view_config(
    route_name='list_gemeenten_by_provincie',
    renderer='crab_listjson', accept='application/json'
)
def list_gemeenten_by_provincie(request):
    Gateway = request.crab_gateway()
    provincie_id = int(request.matchdict.get('provincie_id'))
    gemeenten = Gateway.list_gemeenten_by_provincie(provincie_id)
    return range_return(request, gemeenten)

@view_config(
    route_name='list_gemeenten_crab',
    renderer='crab_listjson', accept='application/json'
)
def list_gemeenten_crab(request):
    Gateway = request.crab_gateway()
    sort = request.params.get('sort', 'niscode')
    sort_map = {'id': 1, 'naam': 2, 'niscode': 6}
    sort = sort_map.get(sort, 6)
    gewest_id = request.matchdict.get('gewest_id')
    gemeenten = Gateway.list_gemeenten(gewest_id, sort)
    return range_return(request, gemeenten)

@view_config(
    route_name='get_gemeente_crab',
    renderer='crab_itemjson', accept='application/json'
)
def get_gemeente_crab(request):
    Gateway = request.crab_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    if len(gemeente_id) == 5:
        try:
            return Gateway.get_gemeente_by_niscode(gemeente_id)
        except GatewayResourceNotFoundException:
            return HTTPNotFound()
    else:
        try:
            return Gateway.get_gemeente_by_id(gemeente_id)
        except GatewayResourceNotFoundException:
            return HTTPNotFound()

@view_config(
    route_name='list_straten',
    renderer='crab_listjson', accept='application/json'
)
def list_straten(request):
    Gateway = request.crab_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    if len(gemeente_id)==5:
        gemeente_id = Gateway.get_gemeente_by_niscode(gemeente_id)
    straten = Gateway.list_straten(gemeente_id)
    return range_return(request, straten)

@view_config(
    route_name='get_straat_by_id',
    renderer='crab_itemjson', accept='application/json'
)
def get_straat_by_id(request):
    Gateway = request.crab_gateway()
    straat_id = request.matchdict.get('straat_id')
    try:
        return Gateway.get_straat_by_id(straat_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()

@view_config(
    route_name='list_huisnummers',
    renderer='crab_listjson', accept='application/json'
)
def list_huisnummers(request):
    Gateway = request.crab_gateway()
    straat_id = request.matchdict.get('straat_id')
    huisnummers = Gateway.list_huisnummers_by_straat(straat_id)
    return range_return(request, huisnummers)

@view_config(
    route_name='get_huisnummer_by_straat_and_label',
    renderer='crab_itemjson', accept='application/json'
)
def get_huisnummer_by_straat_and_label(request):
    Gateway = request.crab_gateway()
    straat_id = request.matchdict.get('straat_id')
    huisnummer = request.matchdict.get('huisnummer_label')
    try:
        return Gateway.get_huisnummer_by_nummer_and_straat(huisnummer, straat_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()


@view_config(
    route_name='get_huisnummer_by_id',
    renderer='crab_itemjson', accept='application/json'
)
def get_huisnummer_by_id(request):
    Gateway = request.crab_gateway()
    huisnummer_id = request.matchdict.get('huisnummer_id')
    try:
        return Gateway.get_huisnummer_by_id(huisnummer_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()

@view_config(
    route_name='list_percelen',
    renderer='crab_listjson', accept='application/json'
)
def list_percelen(request):
    Gateway = request.crab_gateway()
    huisnummer_id = request.matchdict.get('huisnummer_id')
    percelen = Gateway.list_percelen_by_huisnummer(huisnummer_id)
    return range_return(request, percelen)

@view_config(
    route_name='get_perceel_by_id',
    renderer='crab_itemjson', accept='application/json'
)
def get_perceel_by_id(request):
    Gateway = request.crab_gateway()
    perceel_id = request.matchdict.get('perceel_id1')+'/'+request.matchdict.get('perceel_id2')
    try:
        return Gateway.get_perceel_by_id(perceel_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()

@view_config(
    route_name='list_gebouwen',
    renderer='crab_listjson', accept='application/json'
)
def list_gebouwen(request):
    Gateway = request.crab_gateway()
    huisnummer_id = request.matchdict.get('huisnummer_id')
    gebouwen = Gateway.list_gebouwen_by_huisnummer(huisnummer_id)
    return range_return(request, gebouwen)

@view_config(
    route_name='get_gebouw_by_id',
    renderer='crab_itemjson', accept='application/json'
)
def get_gebouw_by_id(request):
    Gateway = request.crab_gateway()
    gebouw_id = request.matchdict.get('gebouw_id')
    try:
        return Gateway.get_gebouw_by_id(gebouw_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()

@view_config(
    route_name='get_wegobject',
    renderer='crab_itemjson', accept='application/json'
)
def get_wegobject(request):
    Gateway = request.crab_gateway()
    wegobject_id = request.matchdict.get('wegobject_id')
    try:
        return Gateway.get_wegobject_by_id(wegobject_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()

@view_config(
    route_name='list_subadressen',
    renderer='crab_listjson', accept='application/json'
)
def list_subadressen(request):
    Gateway = request.crab_gateway()
    huisnummer_id = request.matchdict.get('huisnummer_id')
    subadressen = Gateway.list_subadressen_by_huisnummer(huisnummer_id)
    return range_return(request, subadressen)

@view_config(
    route_name='get_subadres_by_id',
    renderer='crab_itemjson', accept='application/json'
)
def get_subadres_by_id(request):
    Gateway = request.crab_gateway()
    subadres_id = request.matchdict.get('subadres_id')
    try:
        return Gateway.get_subadres_by_id(subadres_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()


@view_config(
    route_name='list_postkantons_by_gemeente',
    renderer='crab_listjson', accept='application/json'
)
def list_postkantons_by_gemeente(request):
    Gateway = request.crab_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    postkantons = Gateway.list_postkantons_by_gemeente(gemeente_id)
    return range_return(request, postkantons)


@view_config(
    route_name='list_adresposities_by_huisnummer',
    renderer='crab_listjson', accept='application/json'
)
def list_adresposities_by_huisnummer(request):
    Gateway = request.crab_gateway()
    huisnummer_id = request.matchdict.get('huisnummer_id')
    adresposities = Gateway.list_adresposities_by_huisnummer(huisnummer_id)
    return range_return(request, adresposities)


@view_config(
    route_name='list_adresposities_by_subadres',
    renderer='crab_listjson', accept='application/json'
)
def list_adresposities_by_subadres(request):
    Gateway = request.crab_gateway()
    subadres_id = request.matchdict.get('subadres_id')
    adresposities = Gateway.list_adresposities_by_subadres(subadres_id)
    return range_return(request, adresposities)


@view_config(
    route_name='get_adrespositie_by_id',
    renderer='crab_itemjson', accept='application/json'
)
def get_adrespositie_by_id(request):
    Gateway = request.crab_gateway()
    adrespositie_id = request.matchdict.get('adrespositie_id')
    try:
        return Gateway.get_adrespositie_by_id(adrespositie_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()


@view_config(
    route_name='list_landen',
    renderer='crab_listjson', accept='application/json'
)
def list_landen(request):
    return list(pycountry.countries)

@view_config(
    route_name='get_land_by_id',
    renderer='crab_itemjson', accept='application/json'
)
def get_land_by_id(request):
    land_id = request.matchdict.get('land_id')
    try:
        land = pycountry.countries.get(alpha2=land_id)
    except KeyError:
        return HTTPNotFound()
    return land
