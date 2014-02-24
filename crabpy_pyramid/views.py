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
    
@view_config(route_name='list_kadastrale_afdelingen', renderer='templates/talissa.pt')
def list_kadastrale_afdelingen(request):
    Gateway = request.capakey_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    return {'project': Gateway.list_kadastrale_afdelingen_by_gemeente(gemeente_id)}
