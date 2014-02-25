from pyramid.renderers import JSON
from crabpy.gateway import capakey

json_list_renderer = JSON()


def range_return(request):
    start = int(request.params.get('start', 0))
    aantal = int(request.params.get('aantal', 10))
    end = start + aantal
    return (start, end)


def list_gemeente_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam
    }


def list_afdeling_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam,
        'gemeente': obj.gemeente
    }


def list_sectie_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'afdeling': obj.afdeling
    }


def list_perceel_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'sectie': obj.sectie,
        'capakey': obj.capakey,
        'percid': obj.percid
    }

json_list_renderer.add_adapter(capakey.Gemeente, list_gemeente_adapter)
json_list_renderer.add_adapter(capakey.Afdeling, list_afdeling_adapter)
json_list_renderer.add_adapter(capakey.Sectie, list_sectie_adapter)
json_list_renderer.add_adapter(capakey.Perceel, list_perceel_adapter)

json_item_renderer = JSON()


def item_gemeente_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }


def item_afdeling_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam,
        'gemeente': obj.gemeente,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }


def item_sectie_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'afdeling': obj.afdeling,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }


def item_perceel_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'sectie': obj.sectie,
        'capakey': obj.capakey,
        'percid': obj.percid,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }


json_item_renderer.add_adapter(capakey.Gemeente, item_gemeente_adapter)
json_item_renderer.add_adapter(capakey.Afdeling, item_afdeling_adapter)
json_item_renderer.add_adapter(capakey.Sectie, item_sectie_adapter)
json_item_renderer.add_adapter(capakey.Perceel, item_perceel_adapter)
