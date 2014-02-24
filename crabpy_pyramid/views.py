from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'g'}
        
@view_config(route_name='list_gemeenten', renderer='templates/talissa.pt')
def list_gemeenten(request):
    Gateway = request.capakey_gateway()
    return {'project': Gateway.list_gemeenten()}

@view_config(route_name='get_gemeente', renderer='templates/talissa.pt')
def get_gemeente_by_niscode(request):
    Gateway = request.capakey_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    return {'project': Gateway.get_gemeente_by_id(gemeente_id)}
    
@view_config(route_name='list_kadastrale_afdelingen_by_niscode', renderer='templates/talissa.pt')
def list_kadastrale_afdelingen(request):
    Gateway = request.capakey_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    return {'project': Gateway.list_kadastrale_afdelingen_by_gemeente(gemeente_id)}

@view_config(route_name='list_kadastrale_afdelingen', renderer='templates/talissa.pt')
def list_kadastrale_afdelingen(request):
    Gateway = request.capakey_gateway()
    return {'project': Gateway.list_kadastrale_afdelingen()}
    
@view_config(route_name='get_kadastrale_afdeling_by_id', renderer='templates/talissa.pt')
def get_kadastrale_afdeling_by_id(request):
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    return {'project': Gateway.get_kadastrale_afdeling_by_id(afdeling_id)}

@view_config(route_name='list_secties_by_afdeling', renderer='templates/talissa.pt')
def list_secties_by_afdeling(request):
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    return {'project': Gateway.list_secties_by_afdeling(afdeling_id)}
    
@view_config(route_name='get_sectie_by_id_and_afdeling', renderer='templates/talissa.pt')
def get_sectie_by_id_and_afdeling(request):
    Gateway = request.capakey_gateway()
    afdeling_id = request.matchdict.get('afdeling_id')
    sectie_id = request.matchdict.get('sectie_id')
    return {'project': Gateway.get_sectie_by_id_and_afdeling(sectie_id, afdeling_id)}
