from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'g'}
        
@view_config(route_name='list_gemeenten', renderer='templates/talissa.pt')
def list_gemeenten(request):
    Gateway = request.capakey_gateway()
    sort = '%(sort)s' % request.matchdict
    return {'project': Gateway.list_gemeenten(sort)}


@view_config(route_name='get_gemeente_by_niscode', renderer='templates/talissa.pt')
def get_gemeente_by_id(request):
    Gateway = request.capakey_gateway()
    niscode = request.matchdict.get('niscode')
    return {'project': Gateway.get_gemeente_by_id(niscode)}
    
@view_config(route_name='list_kadastrale_afdelingen', renderer='templates/talissa.pt')
def list_kadastrale_afdelingen(request):
    Gateway = request.capakey_gateway()
    gemeente_id = request.matchdict.get('gemeente_id')
    return {'project': Gateway.list_kadastrale_afdelingen_by_gemeente(gemeente_id)}
