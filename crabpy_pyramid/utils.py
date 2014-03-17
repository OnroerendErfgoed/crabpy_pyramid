from pyramid.renderers import JSON
from crabpy.gateway import capakey, crab

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
    OR :class `crabpy.gateway.crab.Gemeenten` to json.
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
    
def list_gewesten_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.crab.Gewest` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam
    }

def list_straten_adapter(obj, request):
    '''
    Adapter for rendering a list of 
    :class: `crabpy.gateway.crab.Straat` to json.
    '''
    return {
        'id': obj.id,
        'label': obj.label,
        'status': obj.status
    }
    
def list_huisnummers_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.crab.Huisnummer` to json.
    '''
    return {
        'id':obj.id,
        'status':obj.status,
        'label':obj.huisnummer
    }

def list_percelen_adapter(obj, request):
    '''
    Adapter for rendering a list of 
    :class: `crabpy.gateway.crab.Perceel` to json.
    '''
    return {
        'id':obj.id
    }

def list_gebouwen_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.crab.Gebouw` to json.
    '''
    return{
        'id': obj.id,
        'aard': obj.aard,
        'status': obj.status
    }

json_list_renderer.add_adapter(capakey.Gemeente, list_gemeente_adapter)
json_list_renderer.add_adapter(crab.Gemeente, list_gemeente_adapter)
json_list_renderer.add_adapter(capakey.Afdeling, list_afdeling_adapter)
json_list_renderer.add_adapter(capakey.Sectie, list_sectie_adapter)
json_list_renderer.add_adapter(capakey.Perceel, list_perceel_adapter)
json_list_renderer.add_adapter(crab.Gewest, list_gewesten_adapter)
json_list_renderer.add_adapter(crab.Straat, list_straten_adapter)
json_list_renderer.add_adapter(crab.Huisnummer, list_huisnummers_adapter)
json_list_renderer.add_adapter(crab.Perceel, list_percelen_adapter)
json_list_renderer.add_adapter(crab.Gebouw, list_gebouwen_adapter)

json_item_renderer = JSON()


def item_gemeente_adapter(obj, request):
    '''
    Adapter for rendering an object of
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
    Adapter for rendering an object of
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
    Adapter for rendering an object of
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
    Adapter for rendering an object of
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


def item_gewest_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.crab.Gewest` to json.
    '''
    return {
        'id': obj.id,
        'namen': obj._namen,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }
    
def item_gemeente_crab_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.crab.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box,
        'metadata': obj.metadata
    }

def item_straat_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.crab.Straat` to json.
    '''
    return {
        'id': obj.id,
        'label': obj.label,
        'namen': obj.namen,
        'status': obj.status,
        'taal': obj.taal,
        'metadata': obj.metadata
    }

def item_huisnummer_adapter(obj, request):
    '''
    Adapter for rendering an object of 
    :class: `crabpy.gateway.crab.Huisnummer` to json.
    '''
    return {
        'id': obj.id,
        'huisnummer': obj.huisnummer,
        'status': obj.status,
        'metadata': obj.metadata
    } 

def item_perceel_crab_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.crab.Perceel` to json.
    '''
    return {
        'id': obj.id,
        'centroid': obj.centroid,
        'metadata': obj.metadata
    }

def item_gebouw_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.crab.Gebouw` to json.
    '''
    return {
        'id': obj.id,
        'aard': obj.aard,
        'status': obj.status,
        'geometriemethode': obj.methode,
        'geometrie': obj.geometrie,
        'metadata': obj.metadata
    }

json_item_renderer.add_adapter(capakey.Gemeente, item_gemeente_adapter)
json_item_renderer.add_adapter(capakey.Afdeling, item_afdeling_adapter)
json_item_renderer.add_adapter(capakey.Sectie, item_sectie_adapter)
json_item_renderer.add_adapter(capakey.Perceel, item_perceel_adapter)
json_item_renderer.add_adapter(crab.Gewest, item_gewest_adapter)
json_item_renderer.add_adapter(crab.Gemeente, item_gemeente_crab_adapter)
json_item_renderer.add_adapter(crab.Straat, item_straat_adapter)
json_item_renderer.add_adapter(crab.Huisnummer, item_huisnummer_adapter)
json_item_renderer.add_adapter(crab.Perceel, item_perceel_crab_adapter)
json_item_renderer.add_adapter(crab.Gebouw, item_gebouw_adapter)
