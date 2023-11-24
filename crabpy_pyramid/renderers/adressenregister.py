import pycountry
from crabpy.gateway import adressenregister
from pyramid.renderers import JSON

json_list_renderer = JSON()
json_item_renderer = JSON()


def list_gewesten_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adressenregister.Gewest` to json.
    """
    return {"naam": obj.naam, "niscode": obj.niscode}


def list_provincie_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adressenregister.Provincie` to json.
    """
    return {
        "niscode": obj.niscode,
        "naam": obj.naam,
        "gewest": {
            "niscode": obj.gewest_niscode,
        },
    }


def list_deelgemeente_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adressenregister.Deelgemeente` to json.
    """
    return {
        "niscode": obj.id,
        "naam": obj.naam,
        "gemeente": {"niscode": obj.gemeente_niscode},
    }


def list_gemeente_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adressenregister.Gemeenten` to json.
    """
    return {
        "niscode": obj.niscode,
        "naam": obj.naam(),
        "provincie": {"niscode": obj.provincie_niscode},
    }


def list_straten_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adresregister.Straat` to json.
    """
    return {
        "id": obj.id,
        "naam": obj.naam(),
        "homoniem": obj.homoniem(),
        "status": obj.status,
        "uri": obj.uri,
    }


def list_adressen_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adresregister.Adres` to json.
    """
    return {
        "id": obj.id,
        "uri": obj.uri,
        "label": obj.label,
        "huisnummer": obj.huisnummer,
        "busnummer": obj.busnummer,
        "status": obj.status,
    }


def list_percelen_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adressenregister.Perceel` to json.
    """
    return {"id": obj.id, "uri": obj.uri, "status": obj.status}


def list_postinfo_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adressenregister.Postinfo` to json.
    """
    return {
        "postcode": obj.id,
        "uri": obj.uri,
        "status": obj.status,
        "namen": obj.namen(),
    }


def list_landen_adapter(obj, request):
    """
    Adapter for rendering a list of landen to json.
    """
    return {"code": obj.alpha_2, "naam": _(obj.name)}


json_list_renderer.add_adapter(adressenregister.Gewest, list_gewesten_adapter)
json_list_renderer.add_adapter(adressenregister.Provincie, list_provincie_adapter)
json_list_renderer.add_adapter(adressenregister.Deelgemeente, list_deelgemeente_adapter)
json_list_renderer.add_adapter(adressenregister.Gemeente, list_gemeente_adapter)
json_list_renderer.add_adapter(adressenregister.Straat, list_straten_adapter)
json_list_renderer.add_adapter(adressenregister.Adres, list_adressen_adapter)
json_list_renderer.add_adapter(adressenregister.Perceel, list_percelen_adapter)
json_list_renderer.add_adapter(adressenregister.Postinfo, list_postinfo_adapter)
json_list_renderer.add_adapter(pycountry.db.Data, list_landen_adapter)


def item_gewest_adapter(obj, request):
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.adressenregister.Gewest` to json.
    """
    return {
        "niscode": obj.niscode,
        "naam": obj.naam,
        "centroid": obj.centroid,
        "bounding_box": obj.bounding_box,
    }


def item_provincie_adapter(obj, request):
    """
    Adapter for rendering a object of
    :class:`crabpy.gateway.adressenregister.Provincie` to json.
    """
    return {
        "niscode": obj.niscode,
        "naam": obj.naam,
        "gewest": {
            "niscode": obj.gewest_niscode,
        },
    }


def item_gemeente_adapter(obj, request):
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.adressenregister.Gemeente` to json.
    """
    return {
        "niscode": obj.niscode,
        "naam": obj.naam(),
        "provincie": {"niscode": obj.provincie_niscode},
        "gewest": {"niscode": obj.gewest.niscode},
    }


def item_deelgemeente_adapter(obj, request):
    """
    Adapter for rendering a object of
    :class:`crabpy.gateway.adressenregister.Deelgemeente` to json.
    """
    return {
        "niscode": obj.id,
        "naam": obj.naam,
        "gemeente": {"niscode": obj.gemeente.niscode, "naam": obj.gemeente.naam()},
    }


def item_straat_adapter(obj, request):
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.adressenregister.Straat` to json.
    """
    return {
        "id": obj.id,
        "naam": obj.naam(
            include_homoniem=True if request.params.get("include_homoniem") else False
        ),
        "homoniem": obj.homoniem(),
        "status": obj.status,
        "uri": obj.uri,
    }


def item_adres_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adresregister.Adres` to json.
    """
    return {
        "id": obj.id,
        "uri": obj.uri,
        "label": obj.label,
        "huisnummer": obj.huisnummer,
        "busnummer": obj.busnummer,
        "status": obj.status,
    }


def item_perceel_adapter(obj, request):
    """
    Adapter for rendering an object of
    :class:`crabpy.gateway.adressenregister.Perceel` to json.
    """
    return {
        "id": obj.id,
        "uri": obj.uri,
        "status": obj.status,
        "adressen": [{"id": adres.id} for adres in obj.adressen],
    }


def item_land_adapter(obj, request):
    """
    Adapter for rendering an item of
    :class: `pycountry.db.Data` to json.
    """
    return {
        "code": obj.alpha_2,
        "alpha2": obj.alpha_2,
        "alpha3": obj.alpha_3,
        "naam": obj.name,
    }


def list_postinfo_adapter(obj, request):
    """
    Adapter for rendering a list of
    :class:`crabpy.gateway.adressenregister.Postinfo` to json.
    """
    return {
        "postcode": obj.id,
        "uri": obj.uri,
        "status": obj.status,
        "namen": obj.namen(),
    }


json_item_renderer.add_adapter(adressenregister.Gewest, item_gewest_adapter)
json_item_renderer.add_adapter(adressenregister.Provincie, item_provincie_adapter)
json_item_renderer.add_adapter(adressenregister.Deelgemeente, item_deelgemeente_adapter)
json_item_renderer.add_adapter(adressenregister.Gemeente, item_gemeente_adapter)
json_item_renderer.add_adapter(adressenregister.Straat, item_straat_adapter)
json_item_renderer.add_adapter(adressenregister.Perceel, item_perceel_adapter)
json_item_renderer.add_adapter(adressenregister.Adres, item_adres_adapter)
json_item_renderer.add_adapter(adressenregister.Postinfo, list_postinfo_adapter)
json_item_renderer.add_adapter(pycountry.db.Data, item_land_adapter)
