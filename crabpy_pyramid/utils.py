from pyramid.renderers import JSON

from crabpy.gateway.capakey import(
    Gemeente,
    Afdeling,
    Sectie,
    Perceel
)
json_renderer = JSON()

def gemeente_adapter(obj, request):
    '''
    Adapter for rendering a :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam
    }
    
def afdeling_adapter(obj, request):
    '''
    Adapter for rendering a :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam,
        'gemeente': obj.gemeente
    }
    
def sectie_adapter(obj, request):
    '''
    Adapter for rendering a :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'afdeling': obj.afdeling
    }
    
def perceel_adapter(obj,request):
    '''
    Adapter for rendering a :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'sectie': obj.sectie,
        'capakey': obj.capakey,
        'percid': obj.percid
    }
    
json_renderer.add_adapter(Gemeente, gemeente_adapter)
json_renderer.add_adapter(Afdeling, afdeling_adapter)
json_renderer.add_adadpter(Sectie, sectie_adapter)
json_renderer.add_adapter(Perceel, perceel_adapter)
