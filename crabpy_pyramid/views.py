from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'g'}
        
@view_config(route_name='list_gemeenten', renderer='templates/talissa.pt')
def list_gemeenten(request):
    Gateway = request.capakey_gateway()
    return {'project': Gateway.list_gemeenten()}


@view_config(route_name='get_gemeente_by_id', renderer='templates/talissa.pt')
def get_gemeente_by_id(request):
    Gateway = request.capakey_gateway()
    id = request.matchdict.get('id')
    return {'project': Gateway.get_gemeente_by_id(id)}
