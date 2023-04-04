import logging

import pycountry
from crabpy.client import AdressenRegisterClientException
from crabpy.gateway.exception import GatewayResourceNotFoundException
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from crabpy_pyramid.utils import range_return
from crabpy_pyramid.utils import set_http_caching

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
    route_name="adressenregister_get_gewest_by_id",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def get_gewest_by_id(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    gewest_id = int(request.matchdict.get("gewest_id"))
    try:
        return Gateway.get_gewest_by_id(gewest_id)
    except GatewayResourceNotFoundException:
        return HTTPNotFound()


@view_config(
    route_name="adressenregister_list_provincies",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_provincies(request):
    request = set_http_caching(request, "adressenregister", "permanent")
    Gateway = request.adressenregister_gateway()
    gewest_id = int(request.matchdict.get("gewest_id"))
    provincies = Gateway.list_provincies(gewest_id)
    return range_return(request, provincies)


@view_config(
    route_name="adressenregister_get_provincie",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def get_provincie(request):
    request = set_http_caching(request, "adressenregister", "permanent")
    Gateway = request.adressenregister_gateway()
    provincie_id = int(request.matchdict.get("provincie_id"))
    provincie = Gateway.get_provincie_by_id(provincie_id)
    if provincie:
        return provincie
    else:
        return HTTPNotFound()


@view_config(
    route_name="adressenregister_list_deelgemeenten",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_deelgemeenten(request):
    request = set_http_caching(request, "adressenregister", "permanent")
    Gateway = request.adressenregister_gateway()
    gewest_id = int(request.matchdict.get("gewest_id"))
    if gewest_id != 2:
        return HTTPNotFound()
    deelgemeenten = Gateway.list_deelgemeenten(gewest_id)
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
    try:
        gemeente = Gateway.get_gemeente_by_niscode(gemeente_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()
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
    deelgemeente_id = request.matchdict.get("deelgemeente_id")
    try:
        return Gateway.get_deelgemeente_by_id(deelgemeente_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()


@view_config(
    route_name="adressenregister_list_gemeenten_by_provincie",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_gemeenten_by_provincie(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    provincie_id = int(request.matchdict.get("provincie_id"))
    try:
        gemeenten = Gateway.list_gemeenten_by_provincie(provincie_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()
    return range_return(request, gemeenten)


@view_config(
    route_name="list_gemeenten_adressenregister",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_gemeenten_adressenregister(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    gewest_id = request.matchdict.get("gewest_id")
    try:
        gemeenten = Gateway.list_gemeenten(gewest_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()
    return range_return(request, gemeenten)


@view_config(
    route_name="get_gemeente_adressenregister",
    renderer="adresreg_itemjson",
    accept="application/json",
)
def get_gemeente_adressenregister(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    gemeente_id = request.matchdict.get("niscode")
    try:
        return Gateway.get_gemeente_by_niscode(gemeente_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()


@view_config(
    route_name="adressenregister_list_straten",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_straten(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    gemeente_id = request.matchdict.get("niscode")
    try:
        straten = Gateway.list_straten(gemeente_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()
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
    try:
        return Gateway.get_straat_by_id(straat_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()


@view_config(
    route_name="adressenregister_list_adressen",
    renderer="adresreg_listjson",
    accept="application/json",
)
def list_adressen_by_straat(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    straat_id = request.matchdict.get("straat_id")
    try:
        straten = Gateway.list_adressen_with_params(straatnaamObjectId=straat_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()
    return range_return(request, straten)


@view_config(
    route_name="adressenregister_get_adres_by_straat_and_huisnummer",
    renderer="adresreg_listjson",
    accept="application/json",
)
def adressenregister_get_adres_by_straat_huisnummer(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    straat_id = request.matchdict.get("straat_id")
    huisnummer = request.matchdict.get("huisnummer")
    try:
        adressen = Gateway.list_adressen_with_params(
            straatnaamObjectId=straat_id, huisnummer=huisnummer
        )
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()
    return range_return(request, adressen)


@view_config(
    route_name="adressenregister_get_adres_by_straat_and_huisnummer_and_busnummer",
    renderer="adresreg_listjson",
    accept="application/json",
)
def adressenregister_get_adres_by_straat_huisnummer_busnummer(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    straat_id = request.matchdict.get("straat_id")
    huisnummer = request.matchdict.get("huisnummer")
    busnummer = request.matchdict.get("busnummer")
    try:
        adressen = Gateway.list_adressen_with_params(
            straatnaamObjectId=straat_id, huisnummer=huisnummer, busnummer=busnummer
        )
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()
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
    try:
        return Gateway.get_adres_by_id(adres_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()


@view_config(
    route_name="adressenregister_list_percelen_by_adres",
    renderer="adresreg_listjson",
    accept="application/json",
)
def adressenregister_list_percelen_by_adres(request):
    request = set_http_caching(request, "adressenregister", "short")
    Gateway = request.adressenregister_gateway()
    adres_id = request.matchdict.get("adres_id")
    try:
        adressen = Gateway.list_percelen_with_params(adresObjectId=adres_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()
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
    try:
        return Gateway.get_perceel_by_id(perceel_id=perceel_id)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()


@view_config(
    route_name="adressenregister_list_postinfo_by_gemeente",
    renderer="adresreg_listjson",
    accept="application/json",
)
def adressenregister_list_postinfo_by_gemeente(request):
    request = set_http_caching(request, "adressenregister", "long")
    Gateway = request.adressenregister_gateway()
    gemeente_naam = request.matchdict.get("gemeente_naam")
    try:
        adressen = Gateway.get_postinfo_by_gemeentenaam(gemeente_naam)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()
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
    try:
        return Gateway.get_postinfo_by_id(postcode)
    except (GatewayResourceNotFoundException, AdressenRegisterClientException):
        return HTTPNotFound()


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
        return HTTPNotFound()
    return land
