import logging
import re

import pycountry
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from crabpy_pyramid.utils import range_return
from crabpy_pyramid.utils import set_http_caching
from crabpy_pyramid.views.utils import extract_valid_params
from crabpy_pyramid.views.utils import handle_gateway_response


log = logging.getLogger(__name__)


@view_config(
    route_name="adressenregister_list_gewesten",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_gewesten(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    gewesten = Gateway.list_gewesten()
    return range_return(request, gewesten)


@view_config(
    route_name="adressenregister_get_gewest_by_niscode",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def get_gewest_by_niscode(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    gewest_niscode = request.matchdict.get("gewest_niscode")
    return handle_gateway_response(Gateway.get_gewest_by_niscode, gewest_niscode)


@view_config(
    route_name="adressenregister_list_provincies",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_provincies(request):
    request = set_http_caching(request, "adressenregister", "permanent")
    Gateway = request.adressenregister_gateway()
    gewest_niscode = request.matchdict.get("gewest_niscode")
    handle_gateway_response(Gateway.get_gewest_by_niscode, gewest_niscode)
    provincies = handle_gateway_response(Gateway.list_provincies, gewest_niscode)
    return range_return(request, provincies)


@view_config(
    route_name="adressenregister_get_provincie",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def get_provincie(request):
    request = set_http_caching(request, "adressenregister", "permanent")
    Gateway = request.adressenregister_gateway()
    provincie_niscode = request.matchdict.get("provincie_niscode")

    return handle_gateway_response(Gateway.get_provincie_by_niscode, provincie_niscode)


@view_config(
    route_name="adressenregister_list_deelgemeenten",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_deelgemeenten(request):
    request = set_http_caching(request, "adressenregister", "permanent")
    Gateway = request.adressenregister_gateway()
    gewest_niscode = request.matchdict.get("gewest_niscode")
    if gewest_niscode != "2000":
        raise HTTPNotFound()
    deelgemeenten = handle_gateway_response(Gateway.list_deelgemeenten, gewest_niscode)

    return range_return(request, deelgemeenten)


@view_config(
    route_name="adressenregister_list_deelgemeenten_by_gemeente",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_deelgemeenten_by_gemeente(request):
    request = set_http_caching(request, "adressenregister", "permanent")
    Gateway = request.adressenregister_gateway()
    gemeente_id = request.matchdict.get("niscode")
    gemeente = handle_gateway_response(Gateway.get_gemeente_by_niscode, gemeente_id)
    deelgemeenten = Gateway.list_deelgemeenten_by_gemeente(gemeente)

    return range_return(request, deelgemeenten)


@view_config(
    route_name="adressenregister_get_deelgemeente_by_id",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def get_deelgemeente_by_id(request):
    request = set_http_caching(request, "adressenregister", "permanent")
    Gateway = request.adressenregister_gateway()
    deelgemeente_niscode = request.matchdict.get("deelgemeente_niscode")

    return handle_gateway_response(Gateway.get_deelgemeente_by_id, deelgemeente_niscode)


@view_config(
    route_name="adressenregister_list_gemeenten_by_provincie",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_gemeenten_by_provincie(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    provincie_id = request.matchdict.get("provincie_niscode")
    kwargs = extract_valid_params(Gateway.list_gemeenten_by_provincie, request)
    provincie = handle_gateway_response(Gateway.get_provincie_by_niscode, provincie_id)
    gemeenten = handle_gateway_response(
        Gateway.list_gemeenten_by_provincie, provincie, **kwargs
    )

    return range_return(request, gemeenten)


@view_config(
    route_name="list_gemeenten_adressenregister",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_gemeenten_adressenregister(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    method = Gateway.list_gemeenten
    gewest_niscode = request.matchdict.get("gewest_niscode")
    handle_gateway_response(Gateway.get_gewest_by_niscode, gewest_niscode)
    kwargs = extract_valid_params(method, request)
    kwargs["gewest_niscode"] = gewest_niscode
    gemeenten = handle_gateway_response(method, **kwargs)

    return range_return(request, gemeenten)


@view_config(
    route_name="get_gemeente_adressenregister",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def get_gemeente_adressenregister(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    gemeente_niscode = request.matchdict.get("niscode")

    return handle_gateway_response(Gateway.get_gemeente_by_niscode, gemeente_niscode)


@view_config(
    route_name="adressenregister_list_straten",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_straten(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    method = Gateway.list_straten
    gemeente_niscode = request.matchdict.get("niscode")
    gemeente = handle_gateway_response(
        Gateway.get_gemeente_by_niscode, gemeente_niscode
    )
    kwargs = extract_valid_params(method, request)
    kwargs["gemeente"] = gemeente
    straten = handle_gateway_response(method, **kwargs)

    return range_return(request, straten)


@view_config(
    route_name="adressenregister_get_straat_by_id",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def get_straat_by_id(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    straat_id = request.matchdict.get("straat_id")

    return handle_gateway_response(Gateway.get_straat_by_id, straat_id)


@view_config(
    route_name="adressenregister_list_adressen",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_adressen_by_straat(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    method = Gateway.list_adressen_with_params
    straat_id = request.matchdict.get("straat_id")
    handle_gateway_response(Gateway.get_straat_by_id, straat_id)
    kwargs = extract_valid_params(method, request)
    kwargs["straatnaamObjectId"] = straat_id
    straten = handle_gateway_response(method, **kwargs)

    return range_return(request, straten)


@view_config(
    route_name="adressenregister_get_adres_by_straat_and_huisnummer",
    renderer="adresreg_listjson",
    accept="application/json",
)
def adressenregister_get_adres_by_straat_huisnummer(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    method = Gateway.list_adressen_with_params
    straat_id = request.matchdict.get("straat_id")
    handle_gateway_response(Gateway.get_straat_by_id, straat_id)
    kwargs = extract_valid_params(method, request)
    kwargs["straatnaamObjectId"] = straat_id
    kwargs["huisnummer"] = request.matchdict.get("huisnummer")
    adressen = handle_gateway_response(method, **kwargs)

    return range_return(request, adressen)


@view_config(
    route_name="adressenregister_get_adres_by_straat_and_huisnummer_and_busnummer",
    renderer="adresreg_listjson",
    accept="application/json",
)
def adressenregister_get_adres_by_straat_huisnummer_busnummer(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    method = Gateway.list_adressen_with_params
    straat_id = request.matchdict.get("straat_id")
    handle_gateway_response(Gateway.get_straat_by_id, straat_id)
    kwargs = extract_valid_params(method, request)
    kwargs["straatnaamObjectId"] = straat_id
    kwargs["huisnummer"] = request.matchdict.get("huisnummer")
    kwargs["busnummer"] = request.matchdict.get("busnummer")
    adressen = handle_gateway_response(method, **kwargs)
    return range_return(request, adressen)


@view_config(
    route_name="adressenregister_get_adres_by_id",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def adressenregister_get_adres_by_id(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    adres_id = request.matchdict.get("adres_id")

    return handle_gateway_response(Gateway.get_adres_by_id, adres_id)


@view_config(
    route_name="adressenregister_list_percelen_by_adres",
    renderer="adresreg_listjson",
    accept="application/json",
)
def adressenregister_list_percelen_by_adres(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    method = Gateway.list_percelen_with_params
    adres_id = request.matchdict.get("adres_id")
    handle_gateway_response(Gateway.get_adres_by_id, adres_id)
    kwargs = extract_valid_params(method, request)
    kwargs["adresObjectId"] = adres_id
    adressen = handle_gateway_response(method, **kwargs)

    return range_return(request, adressen)


@view_config(
    route_name="adressenregister_get_perceel_by_id",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def adressenregister_get_perceel_by_id(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    perceel_id = request.matchdict.get("perceel_id")
    return handle_gateway_response(Gateway.get_perceel_by_id, perceel_id=perceel_id)


@view_config(
    route_name="adressenregister_get_perceel_by_id_parts",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def adressenregister_get_perceel_by_id_parts(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    perceel_id = (
        f'{request.matchdict.get("perceel_id_part1")}'
        f'-{request.matchdict.get("perceel_id_part2")}'
    )
    return handle_gateway_response(Gateway.get_perceel_by_id, perceel_id=perceel_id)


@view_config(
    route_name="adressenregister_list_postinfo_by_gemeente",
    renderer="adresreg_listjson",
    accept="application/json",
)
def adressenregister_list_postinfo_by_gemeente(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    gemeente_param = request.matchdict.get("gemeente_naam_niscode")
    niscode_pattern = re.compile(r"^\d{5}$")
    if niscode_pattern.match(gemeente_param):
        gemeente = handle_gateway_response(
            Gateway.get_gemeente_by_niscode, gemeente_param
        )
        gemeente_param = gemeente.naam()
    adressen = handle_gateway_response(
        Gateway.get_postinfo_by_gemeentenaam, gemeente_param
    )

    return range_return(request, adressen)


@view_config(
    route_name="adressenregister_get_postinfo_by_postcode",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def adressenregister_get_postinfo_by_postcode(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    postcode = request.matchdict.get("postcode")

    return handle_gateway_response(Gateway.get_postinfo_by_id, postcode)


@view_config(
    route_name="adressenregister_list_landen",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_landen(request):
    set_http_caching(request, "adressenregister", "permanent")
    return list(pycountry.countries)


@view_config(
    route_name="adressenregister_get_land_by_id",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def get_land_by_id(request):
    request = set_http_caching(request, "adressenregister", "permanent")
    land_id = request.matchdict.get("land_id")
    land = pycountry.countries.get(alpha_2=land_id)
    if land is None:
        raise HTTPNotFound()
    return land
