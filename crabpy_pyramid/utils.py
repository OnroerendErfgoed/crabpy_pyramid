# -*- coding: utf-8 -*-
'''
Adapters to translate objects into json And range handling.
.. versionadded:: 0.1.0
'''
from pyramid.renderers import JSON
from crabpy.gateway import capakey, crab
import re

json_list_renderer = JSON()

def range_header(range):
    match = re.match('^items=([0-9]+)-([0-9]+)$', range)
    if match:
        start = int(match.group(1))
        einde = int(match.group(2))
        if einde < start:
            einde = start
        return {
        'start': start,
        'einde': einde,
        'aantal': einde - start + 1
        }
    else:
        return False
    
def range_return(request, total):
    range = False
    if ('Range' in request.headers):
        range = request.headers['Range']
        range = range_header(range)
        start = range['start']
        einde = range['einde']
        request.response.headers['Content-Range'] = 'items %d-%d/%d' % (start, einde, total)
    elif ('X-Range' in request.headers):
        range = request.headers['X-Range']
        range = range_header(range)
        start = range['start']
        einde = range['einde']
        request.response.headers['X-Content-Range'] = 'items %d-%d/%d' % (start, einde, total)
    else:
        start = int(request.params.get('start', 0))
        aantal = int(request.params.get('aantal', 10))
        einde = start + aantal
    return (start, einde)


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
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        },
    }
    
def list_huisnummers_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.crab.Huisnummer` to json.
    '''
    return {
        'id':obj.id,
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        },
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
        'aard': {
            'id': obj.aard.id,
            'naam': obj.aard.naam,
            'definitie': obj.aard.definitie
        },
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        },
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
        'metadata': {
            'begin_tijd': obj.metadata.begin_tijd,
            'begin_datum': obj.metadata.begin_datum,
            'begin_bewerking': {
                'id': obj.metadata.begin_bewerking.id,
                'naam': obj.metadata.begin_bewerking.naam,
                'definitie': obj.metadata.begin_bewerking.definitie
            },
            'begin_organisatie': {
                'id': obj.metadata.begin_organisatie.id,
                'naam': obj.metadata.begin_organisatie.naam,
                'definitie': obj.metadata.begin_organisatie.definitie
            }
        }
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
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        },
        'taal': {
            'id': obj.taal.id,
            'naam': obj.taal.naam,
            'definitie': obj.taal.definitie
        },
        'metadata': {
            'begin_tijd': obj.metadata.begin_tijd,
            'begin_datum': obj.metadata.begin_datum,
            'begin_bewerking': {
                'id': obj.metadata.begin_bewerking.id,
                'naam': obj.metadata.begin_bewerking.naam,
                'definitie': obj.metadata.begin_bewerking.definitie
            },
            'begin_organisatie': {
                'id': obj.metadata.begin_organisatie.id,
                'naam': obj.metadata.begin_organisatie.naam,
                'definitie': obj.metadata.begin_organisatie.definitie
            }
        }
    }

def item_huisnummer_adapter(obj, request):
    '''
    Adapter for rendering an object of 
    :class: `crabpy.gateway.crab.Huisnummer` to json.
    '''
    return {
        'id': obj.id,
        'huisnummer': obj.huisnummer,
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        },
        'metadata': {
            'begin_tijd': obj.metadata.begin_tijd,
            'begin_datum': obj.metadata.begin_datum,
            'begin_bewerking': {
                'id': obj.metadata.begin_bewerking.id,
                'naam': obj.metadata.begin_bewerking.naam,
                'definitie': obj.metadata.begin_bewerking.definitie
            },
            'begin_organisatie': {
                'id': obj.metadata.begin_organisatie.id,
                'naam': obj.metadata.begin_organisatie.naam,
                'definitie': obj.metadata.begin_organisatie.definitie
            }
        }
    } 

def item_perceel_crab_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.crab.Perceel` to json.
    '''
    return {
        'id': obj.id,
        'centroid': obj.centroid,
        'metadata': {
            'begin_tijd': obj.metadata.begin_tijd,
            'begin_datum': obj.metadata.begin_datum,
            'begin_bewerking': {
                'id': obj.metadata.begin_bewerking.id,
                'naam': obj.metadata.begin_bewerking.naam,
                'definitie': obj.metadata.begin_bewerking.definitie
            },
            'begin_organisatie': {
                'id': obj.metadata.begin_organisatie.id,
                'naam': obj.metadata.begin_organisatie.naam,
                'definitie': obj.metadata.begin_organisatie.definitie
            }
        }
    }

def item_gebouw_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.crab.Gebouw` to json.
    '''
    return {
        'id': obj.id,
        'aard': {
            'id': obj.aard.id,
            'naam': obj.aard.naam,
            'definitie': obj.aard. definitie
        },
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        },
        'geometriemethode': {
            'id': obj.methode.id,
            'naam': obj.methode.naam,
            'definitie': obj.methode.definitie
        },
        'geometrie': obj.geometrie,
        'metadata': {
            'begin_tijd': obj.metadata.begin_tijd,
            'begin_datum': obj.metadata.begin_datum,
            'begin_bewerking': {
                'id': obj.metadata.begin_bewerking.id,
                'naam': obj.metadata.begin_bewerking.naam,
                'definitie': obj.metadata.begin_bewerking.definitie
            },
            'begin_organisatie': {
                'id': obj.metadata.begin_organisatie.id,
                'naam': obj.metadata.begin_organisatie.naam,
                'definitie': obj.metadata.begin_organisatie.definitie
            }
        }
    }
    
def item_wegobject_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.Wegobject` to json.
    '''
    return {
        'id': obj.id,
        'aard': {
            'id': obj.aard.id,
            'naam': obj.aard.naam,
            'definitie': obj.aard.definitie
        },
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box,
        'metadata': {
            'begin_tijd': obj.metadata.begin_tijd,
            'begin_datum': obj.metadata.begin_datum,
            'begin_bewerking': {
                'id': obj.metadata.begin_bewerking.id,
                'naam': obj.metadata.begin_bewerking.naam,
                'definitie': obj.metadata.begin_bewerking.definitie
            },
            'begin_organisatie': {
                'id': obj.metadata.begin_organisatie.id,
                'naam': obj.metadata.begin_organisatie.naam,
                'definitie': obj.metadata.begin_organisatie.definitie
            }
        }
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
json_item_renderer.add_adapter(crab.Wegobject, item_wegobject_adapter)
