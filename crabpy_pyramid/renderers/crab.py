# -*- coding: utf-8 -*-
"""
Adapters to help render :mod:`crabpy.gateway.crab` objects to json.

.. versionadded:: 0.1.0
"""
import gettext

import pycountry
from crabpy.gateway import crab
from pyramid.renderers import JSON

json_list_renderer = JSON()
json_item_renderer = JSON()

nederlands = gettext.translation('iso3166', pycountry.LOCALES_DIR, languages=['nl'])
nederlands.install()


def list_gewesten_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Gewest` to json.
    """
    return {
        'id': obj.id,
        'naam': obj.naam
    }


def list_provincie_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Provincie` to json.
    """
    return {
        'niscode': obj.niscode,
        'naam': obj.naam,
        'gewest': {
            'id': obj.gewest.id,
            'naam': obj.gewest.naam
        }
    }


def list_gemeente_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Gemeenten` to json.
    """
    return {
        'id': obj.id,
        'niscode': obj.niscode,
        'naam': obj.naam
    }


def list_deelgemeente_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Deelgemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam
    }


def list_straten_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Straat` to json.
    """
    naam = obj.label
    for name, language in obj.namen:
        if language == 'nl' and name:
            naam = name
            break
    return {
        'id': obj.id,
        'label': obj.label,
        'naam': naam,
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        },
    }


def list_huisnummers_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Huisnummer` to json.
    """
    return {
        'id': obj.id,
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        },
        'label': obj.huisnummer
    }


def list_percelen_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Perceel` to json.
    """
    return {
        'id': obj.id
    }


def list_gebouwen_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Gebouw` to json.
    """
    return {
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
        }
    }


def list_subadres_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Subadres` to json.
    """
    return {
        'id': obj.id,
        'subadres': obj.subadres,
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        }
    }


def list_postkantons_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Postkanton` to json.
    """
    return {
        'id': obj.id
    }


def list_adresposities_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.crab.Adrespositie` to json.
    """
    return {
        'id': obj.id,
        'herkomst': {
            'id': obj.herkomst.id,
            'naam': obj.herkomst.naam,
            'definitie': obj.herkomst.definitie
        }
    }


def list_landen_adapter(obj, request):
    """
    Adapter for rendering a list of landen to json.
    """
    return {
        'id': obj.alpha_2,
        'naam': _(obj.name)
    }


json_list_renderer.add_adapter(crab.Gewest, list_gewesten_adapter)
json_list_renderer.add_adapter(crab.Provincie, list_provincie_adapter)
json_list_renderer.add_adapter(crab.Gemeente, list_gemeente_adapter)
json_list_renderer.add_adapter(crab.Deelgemeente, list_deelgemeente_adapter)
json_list_renderer.add_adapter(crab.Straat, list_straten_adapter)
json_list_renderer.add_adapter(crab.Huisnummer, list_huisnummers_adapter)
json_list_renderer.add_adapter(crab.Perceel, list_percelen_adapter)
json_list_renderer.add_adapter(crab.Gebouw, list_gebouwen_adapter)
json_list_renderer.add_adapter(crab.Subadres, list_subadres_adapter)
json_list_renderer.add_adapter(crab.Postkanton, list_postkantons_adapter)
json_list_renderer.add_adapter(crab.Adrespositie, list_adresposities_adapter)
json_list_renderer.add_adapter(pycountry.db.Data, list_landen_adapter)


def item_gewest_adapter(obj, request):
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.crab.Gewest` to json.
    """
    return {
        'id': obj.id,
        'namen': obj._namen,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }


def item_provincie_adapter(obj, request):
    """
    Adapter for rendering a object of
    :class:`crabpy.gateway.crab.Provincie` to json.
    """
    return {
        'niscode': obj.niscode,
        'naam': obj.naam,
        'gewest': {
            'id': obj.gewest.id,
            'naam': obj.gewest.naam
        }
    }


def item_gemeente_adapter(obj, request):
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.crab.Gemeente` to json.
    """
    return {
        'id': obj.id,
        'niscode': obj.niscode,
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


def item_deelgemeente_adapter(obj, request):
    """
    Adapter for rendering a object of
    :class:`crabpy.gateway.crab.Deelgemeente` to json.
    """
    return {
        'id': obj.id,
        'naam': obj.naam,
        'gemeente': {
            'id': obj.gemeente.id,
            'naam': obj.gemeente.naam
        }
    }


def item_straat_adapter(obj, request):
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.crab.Straat` to json.
    """
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
        },
        'bounding_box': obj.bounding_box
    }


def item_huisnummer_adapter(obj, request):
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.crab.Huisnummer` to json.
    """
    return {
        'id': obj.id,
        'huisnummer': obj.huisnummer,
        'postadres': obj.postadres,
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
        },
        'bounding_box': obj.bounding_box
    }


def item_perceel_crab_adapter(obj, request):
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.crab.Perceel` to json.
    """
    return {
        'id': obj.id,
        'centroid': obj.centroid,
        'postadressen': obj.postadressen,
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
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.crab.Gebouw` to json.
    """
    return {
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
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.Wegobject` to json.
    """
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


def item_subadres_adapter(obj, request):
    """
    Adapter for rendering an item of
    :class:`crabpy.gateway.Subadres` to json.
    """
    return {
        'id': obj.id,
        'subadres': obj.subadres,
        'postadres': obj.postadres,
        'status': {
            'id': obj.status.id,
            'naam': obj.status.naam,
            'definitie': obj.status.definitie
        },
        'aard': {
            'id': obj.aard.id,
            'naam': obj.aard.naam,
            'definitie': obj.aard.definitie
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


def item_adrespositie_adapter(obj, request):
    """
    Adapter for rendering an item of
    :class:`crabpy.gateway.Adrespositie` to json.
    """
    return {
        'id': obj.id,
        'herkomst': {
            'id': obj.herkomst.id,
            'naam': obj.herkomst.naam,
            'definitie': obj.herkomst.definitie
        },
        'geometrie': obj.geometrie,
        'aard': {
            'id': obj.aard.id,
            'naam': obj.aard.naam,
            'definitie': obj.aard.definitie
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


def item_land_adapter(obj, request):
    """
    Adapter for rendering an item of
    :class: `pycountry.db.Data` to json.
    """
    return {
        'id': obj.alpha_2,
        'alpha2': obj.alpha_2,
        'alpha3': obj.alpha_3,
        'naam': _(obj.name)
    }


def item_postkanton_adapter(obj, request):
    """
    Adapter for rendering an item of
    :class: `pycountry.db.Data` to json.
    """
    return {
        'postcode': obj.id,
    }


json_item_renderer.add_adapter(crab.Gewest, item_gewest_adapter)
json_item_renderer.add_adapter(crab.Provincie, item_provincie_adapter)
json_item_renderer.add_adapter(crab.Gemeente, item_gemeente_adapter)
json_item_renderer.add_adapter(crab.Deelgemeente, item_deelgemeente_adapter)
json_item_renderer.add_adapter(crab.Straat, item_straat_adapter)
json_item_renderer.add_adapter(crab.Huisnummer, item_huisnummer_adapter)
json_item_renderer.add_adapter(crab.Perceel, item_perceel_crab_adapter)
json_item_renderer.add_adapter(crab.Gebouw, item_gebouw_adapter)
json_item_renderer.add_adapter(crab.Wegobject, item_wegobject_adapter)
json_item_renderer.add_adapter(crab.Subadres, item_subadres_adapter)
json_item_renderer.add_adapter(crab.Adrespositie, item_adrespositie_adapter)
json_item_renderer.add_adapter(pycountry.db.Data, item_land_adapter)
json_item_renderer.add_adapter(crab.Postkanton, item_postkanton_adapter)
