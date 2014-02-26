from pyramid.view import view_config
from .utils import range_return


@view_config(route_name='list_gemeenten', renderer='listjson', accept='application/json')
def list_gemeenten(request):
    Gateway = request.capakey_gateway()
    gemeenten = Gateway.list_gemeenten(1)
    r = range_return(request)
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
    r = range_return(request)
    return afdelingen[r[0]:r[1]]


@view_config(route_name='list_kadastrale_afdelingen', renderer='listjson', accept='application/json')
def list_kadastrale_afdelingen(request):
    Gateway = request.capakey_gateway()
    afdelingen = Gateway.list_kadastrale_afdelingen()
    r = range_return(request)
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
    r = range_return(request)
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
    r = range_return(request)
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
