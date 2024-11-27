"""
Functional tests.

.. versionadded:: 0.1.0
"""

import os
import shutil
import unittest
from copy import deepcopy

import responses
from pyramid import testing
from webtest import TestApp

from crabpy_pyramid import main
from tests.fixtures.adressenregister import adres
from tests.fixtures.adressenregister import adressen
from tests.fixtures.adressenregister import perceel
from tests.fixtures.adressenregister import percelen
from tests.fixtures.adressenregister import postinfo_1000
from tests.fixtures.adressenregister import postinfo_1020
from tests.fixtures.adressenregister import postinfos
from tests.fixtures.adressenregister import straat
from tests.fixtures.adressenregister import straten


def as_bool(value):
    """
    Cast a textual value from a config file to a boolean.
    Will convert 'true', 'True', '1', 't', 'T' or 'Yes' to `True`. All other
    values are considered to be `False`.
    """
    return value in ["true", "True", "1", "t", "T", "Yes"]


settings = {
    "crabpy.capakey.cache_config.permanent.backend": "dogpile.cache.dbm",
    "crabpy.capakey.cache_config.permanent.expiration_time": 604800,
    "crabpy.capakey.cache_config.permanent.arguments.filename": os.path.join(
        "/tmp", "capakey_permanent.dbm"
    ),
    "crabpy.capakey.cache_config.long.backend": "dogpile.cache.dbm",
    "crabpy.capakey.cache_config.long.expiration_time": 86400,
    "crabpy.capakey.cache_config.long.arguments.filename": os.path.join(
        "/tmp", "capakey_long.dbm"
    ),
    "crabpy.capakey.cache_config.short.backend": "dogpile.cache.dbm",
    "crabpy.capakey.cache_config.short.expiration_time": 3600,
    "crabpy.capakey.cache_config.short.arguments.filename": os.path.join(
        "/tmp", "capakey_short.dbm"
    ),
    "crabpy.adressenregister.include": True,
    "crabpy.adressenregister.base_url": "https://api.basisregisters.vlaanderen.be",
    "crabpy.adressenregister.api_key": "",
}


def setUpModule():
    shutil.rmtree(os.path.join(os.path.dirname(__file__), "dogpile_data"), True)


class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = main({}, **settings)

    def setUp(self):
        self.testapp = TestApp(self.app)
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()


@unittest.skipUnless(
    as_bool(os.environ.get("CRABPY_INTEGRATION_TESTS", False)),
    "No CAPAKEY Integration tests required",
)
class CapakeyFunctionalTests(FunctionalTests):
    def test_list_gemeenten(self):
        res = self.testapp.get("/capakey/gemeenten")
        self.assertEqual("200 OK", res.status)

    def test_get_gemeente_by_id(self):
        res = self.testapp.get("/capakey/gemeenten/11001")
        self.assertEqual("200 OK", res.status)

    def test_get_gemeente_by_unexisting_id(self):
        res = self.testapp.get("/capakey/gemeenten/1100", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_list_kadastrale_afdelingen_by_gemeente(self):
        res = self.testapp.get("/capakey/gemeenten/11001/afdelingen")
        self.assertEqual("200 OK", res.status)

    def test_list_kadastrale_afdelingen(self):
        res = self.testapp.get("/capakey/afdelingen")
        self.assertEqual("200 OK", res.status)

    def test_get_kadastrale_afdeling_by_id(self):
        res = self.testapp.get("/capakey/afdelingen/11001")
        self.assertEqual("200 OK", res.status)

    def test_get_kadastrale_afdeling_by_unexisting_id(self):
        res = self.testapp.get("/capakey/afdelingen/99999", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_list_secties_by_afdeling(self):
        res = self.testapp.get("/capakey/afdelingen/11001/secties")
        self.assertEqual("200 OK", res.status)

    def test_get_sectie_by_id_and_afdeling(self):
        res = self.testapp.get("/capakey/afdelingen/11001/secties/B")
        self.assertEqual("200 OK", res.status)

    def test_get_sectie_by_unexisting_id_and_afdeling(self):
        res = self.testapp.get("/capakey/afdelingen/11001/secties/Z", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_list_percelen_by_sectie(self):
        res = self.testapp.get("/capakey/afdelingen/11001/secties/B/percelen")
        self.assertEqual("200 OK", res.status)

    def test_get_perceel_by_sectie_and_id(self):
        res = self.testapp.get(
            "/capakey/afdelingen/11001/secties/B/percelen/0001/00S000"
        )
        self.assertEqual("200 OK", res.status)

    def test_get_perceel_by_unexisting_sectie_and_id(self):
        res = self.testapp.get(
            "/capakey/afdelingen/11001/secties/B/percelen/0000/00000", status=404
        )
        self.assertEqual("404 Not Found", res.status)

    def test_get_perceel_by_capakey(self):
        res = self.testapp.get("/capakey/percelen/11001B0001/00S000")
        self.assertEqual("200 OK", res.status)

    def test_get_perceel_by_unexisting_capakey(self):
        res = self.testapp.get("/capakey/percelen/99009X0009/00X000", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_get_perceel_by_percid(self):
        res = self.testapp.get("/capakey/percelen/11001_B_0001_S_000_00")
        self.assertEqual("200 OK", res.status)

    def test_get_perceel_by_unexisting_percid(self):
        res = self.testapp.get("/capakey/percelen/99009_X_0009_X_000_00", status=404)
        self.assertEqual("404 Not Found", res.status)


class AdressenRegisterFunctionalTests(FunctionalTests):
    def test_list_gewesten(self):
        res = self.testapp.get("/adressenregister/gewesten")
        self.assertEqual("200 OK", res.status)
        self.assertCountEqual(
            res.json,
            [
                {"niscode": "4000", "naam": "Brussels Hoofdstedelijk Gewest"},
                {"niscode": "2000", "naam": "Vlaams Gewest"},
                {"niscode": "3000", "naam": "Waals Gewest"},
            ],
        )

    def test_get_gewest_by_niscode(self):
        res = self.testapp.get("/adressenregister/gewesten/2000")
        self.assertEqual("200 OK", res.status)
        self.assertDictEqual(
            res.json,
            {
                "bounding_box": [22279.17, 153050.23, 258873.3, 244022.31],
                "centroid": [138165.09, 189297.53],
                "naam": "Vlaams Gewest",
                "niscode": "2000",
            },
        )

    def test_get_gewest_by_unexisting_id(self):
        res = self.testapp.get("/adressenregister/gewesten/0", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_list_provincies(self):
        res = self.testapp.get("/adressenregister/gewesten/2000/provincies")
        self.assertEqual("200 OK", res.status)
        self.assertEqual(5, len(res.json))

    def test_get_provincie_by_id(self):
        res = self.testapp.get("/adressenregister/provincies/10000")
        self.assertEqual("200 OK", res.status)
        self.assertDictEqual(
            {"gewest": {"niscode": "2000"}, "naam": "Antwerpen", "niscode": "10000"},
            res.json,
        )

    def test_get_provincie_by_unexisting_id(self):
        res = self.testapp.get("/adressenregister/provincies/00000", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_list_deelgemeenten(self):
        res = self.testapp.get("/adressenregister/gewesten/2000/deelgemeenten")
        self.assertEqual("200 OK", res.status)

    def test_list_deelgemeenten_wrong_gewest(self):
        res = self.testapp.get("/adressenregister/gewesten/1/deelgemeenten", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_list_deelgemeenten_by_gemeente(self):
        res = self.testapp.get("/adressenregister/gemeenten/11001/deelgemeenten")
        self.assertEqual("200 OK", res.status)

    def test_list_deelgemeenten_by_unexisting_gemeente(self):
        res = self.testapp.get(
            "/adressenregister/gemeenten/99999/deelgemeenten", status=404
        )
        self.assertEqual("404 Not Found", res.status)
        res = self.testapp.get(
            "/adressenregister/gemeenten/9999/deelgemeenten", status=404
        )
        self.assertEqual("404 Not Found", res.status)

    def test_list_gemeenten_by_provincie(self):
        res = self.testapp.get(
            "/adressenregister/provincies/10000" "/gemeenten?gemeente_status=inGebruik"
        )
        self.assertEqual("200 OK", res.status)
        self.assertEqual(len(res.json), 69)
        self.assertDictEqual(
            {
                "naam": "Aartselaar",
                "niscode": "11001",
                "provincie": {"niscode": "10000"},
                "status": "inGebruik",
            },
            res.json[0],
        )
        res = self.testapp.get(
            "/adressenregister/provincies/10000/gemeenten?gemeente_status=voorgesteld"
        )
        self.assertEqual("200 OK", res.status)
        self.assertEqual(len(res.json), 1)
        self.assertDictEqual(
            {
                "naam": "Beveren-Kruibeke-Zwijndrecht",
                "niscode": "46030",
                "provincie": {"niscode": "10000"},
                "status": "voorgesteld",
            },
            res.json[0],
        )

    def test_list_gemeenten_by_provincie_404(self):
        res = self.testapp.get(
            "/adressenregister/provincies/100000/gemeenten", status=404
        )
        self.assertEqual("404 Not Found", res.status)

    def test_list_gemeenten_adressenregister(self):
        res = self.testapp.get(
            "/adressenregister/gewesten/2000/gemeenten?gemeente_status=inGebruik"
        )
        self.assertEqual("200 OK", res.status)
        self.assertEqual(300, len(res.json))
        res = self.testapp.get(
            "/adressenregister/gewesten/2000/gemeenten?gemeente_status=voorgesteld"
        )
        self.assertEqual("200 OK", res.status)
        self.assertEqual(12, len(res.json))

    def test_list_gemeenten_adressenregister_404(self):
        res = self.testapp.get("/adressenregister/gewesten/20000/gemeenten", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_get_gemeente_adresregister_niscode(self):
        res = self.testapp.get("/adressenregister/gemeenten/11001")
        self.assertEqual("200 OK", res.status)
        self.assertDictEqual(
            {
                "gewest": {"niscode": "2000"},
                "naam": "Aartselaar",
                "niscode": "11001",
                "provincie": {"niscode": "10000"},
            },
            res.json,
        )

    def test_get_gemeente_crab_unexisting_niscode(self):
        res = self.testapp.get("/adressenregister/gemeenten/00000", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_list_straten(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen?nisCode=11001&limit=500",
                json=straten,
                status=200,
            )
            res = self.testapp.get("/adressenregister/gemeenten/11001/straten")
        self.assertCountEqual(
            [
                {
                    "id": "1",
                    "naam": "Acacialaan",
                    "homoniem": None,
                    "status": "inGebruik",
                    "uri": "https://data.vlaanderen.be/id/straatnaam/1",
                },
                {
                    "id": "2",
                    "naam": "Adriaan Sanderslei",
                    "homoniem": None,
                    "status": "inGebruik",
                    "uri": "https://data.vlaanderen.be/id/straatnaam/2",
                },
            ],
            res.json,
        )
        self.assertEqual("200 OK", res.status)

    def test_list_straten_404(self):
        res = self.testapp.get("/adressenregister/gemeenten/110001/straten", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_get_straat_by_id(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                json=straat,
                status=200,
            )
            res = self.testapp.get("/adressenregister/straten/1")
        self.assertEqual("200 OK", res.status)
        self.assertDictEqual(
            {
                "id": "1",
                "naam": "Acacialaan",
                "homoniem": None,
                "status": "inGebruik",
                "uri": "https://data.vlaanderen.be/id/straatnaam/1",
            },
            res.json,
        )

    def test_get_straat_by_unexisting_id(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/0",
                status=404,
            )
            res = self.testapp.get("/adressenregister/straten/0", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_get_adressen_by_straat(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen",
                json=adressen,
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                json={"identificator": {"objectId": 1}},
                status=200,
            )
            res = self.testapp.get("/adressenregister/straten/1/adressen")
        self.assertEqual("200 OK", res.status)
        self.assertEqual(2, len(res.json))

    def test_get_adressen_by_straat_with_params(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen?gemeentenaam=x"
                "&postcode=x&straatnaam=x&homoniemToevoeging=x&huisnummer=x"
                "&busnummer=x&niscode=x&status=x&straatnaamObjectId=1&limit=500",
                json=adressen,
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                json={"identificator": {"objectId": 1}},
                status=200,
            )
            res = self.testapp.get(
                "/adressenregister/straten/1/adressen?gemeentenaam=x"
                "&postcode=x&straatnaam=x&homoniem_toevoeging=x"
                "&huisnummer=x&busnummer=x&niscode=x&status=x"
            )
        self.assertTrue(rsps.assert_all_requests_are_fired)
        self.assertEqual("200 OK", res.status)
        self.assertEqual(2, len(res.json))

    def test_get_adressen_by_straat_404(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                status=404,
            )
            res = self.testapp.get("/adressenregister/straten/1/adressen", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_get_adressen_by_straat_empty(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen",
                json={"adressen": []},
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                json={"identificator": {"objectId": 1}},
                status=200,
            )
            res = self.testapp.get("/adressenregister/straten/1/adressen")
        self.assertEqual("200 OK", res.status)
        self.assertEqual([], res.json)

    def test_get_adres_by_straat_and_huisnummer(self):
        with responses.RequestsMock() as rsps:
            adressen_response = deepcopy(adressen)
            adressen_response["adressen"] = [adressen["adressen"][0]]
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen",
                json=adressen_response,
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                json={"identificator": {"objectId": 1}},
                status=200,
            )
            res = self.testapp.get("/adressenregister/straten/1/huisnummers/4")
        self.assertEqual("200 OK", res.status)
        self.assertCountEqual(
            [
                {
                    "busnummer": "",
                    "huisnummer": "4",
                    "id": "307106",
                    "label": "Acacialaan 4, 2630 Aartselaar",
                    "status": "inGebruik",
                    "uri": "https://data.vlaanderen.be/id/adres/307106",
                }
            ],
            res.json,
        )

    def test_get_adres_by_straat_and_huisnummer_404(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                status=404,
            )
            res = self.testapp.get(
                "/adressenregister/straten/1/huisnummers/4", status=404
            )
        self.assertEqual("404 Not Found", res.status)

    def test_get_adres_by_straat_and_huisnummer_empty(self):
        with responses.RequestsMock() as rsps:
            adressen_response = deepcopy(adressen)
            adressen_response["adressen"] = [adressen["adressen"][0]]
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen",
                json={"adressen": []},
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                json={"identificator": {"objectId": 1}},
                status=200,
            )
            res = self.testapp.get("/adressenregister/straten/1/huisnummers/4")
        self.assertEqual("200 OK", res.status)
        self.assertEqual([], res.json)

    def test_get_adres_by_straat_and_huisnummer_and_busnummer(self):
        with responses.RequestsMock() as rsps:
            adressen_response = deepcopy(adressen)
            adressen_response["adressen"] = [adressen["adressen"][0]]
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen",
                json=adressen_response,
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                json={"identificator": {"objectId": 1}},
                status=200,
            )
            res = self.testapp.get(
                "/adressenregister/straten/1/huisnummers/4/busnummers/1"
            )
        self.assertEqual("200 OK", res.status)
        self.assertCountEqual(
            [
                {
                    "busnummer": "",
                    "huisnummer": "4",
                    "id": "307106",
                    "label": "Acacialaan 4, 2630 Aartselaar",
                    "status": "inGebruik",
                    "uri": "https://data.vlaanderen.be/id/adres/307106",
                },
            ],
            res.json,
        )

    def test_error_other_then_404_400(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen/900746",
                json=adres,
                status=413,
            )
            res = self.testapp.get(
                "/adressenregister/adressen/900746", expect_errors=True
            )
        self.assertEqual(500, res.status_code)
        self.assertIn(
            "Er ging iets fout in de vraag naar adressenregister API.", res.text
        )

    def test_get_adres_by_straat_and_huisnummer_and_busnummer_404(self):
        with responses.RequestsMock() as rsps:
            adressen_response = deepcopy(adressen)
            adressen_response["adressen"] = [adressen["adressen"][0]]
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                json=adressen_response,
                status=404,
            )
            res = self.testapp.get(
                "/adressenregister/straten/1" "/huisnummers/4/busnummers/1", status=404
            )
        self.assertEqual("404 Not Found", res.status)

    def test_get_adres_by_straat_and_huisnummer_and_busnummer_empty(self):
        with responses.RequestsMock() as rsps:
            adressen_response = deepcopy(adressen)
            adressen_response["adressen"] = [adressen["adressen"][0]]
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen",
                json={"adressen": []},
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
                json={"identificator": {"objectId": 1}},
                status=200,
            )
            res = self.testapp.get(
                "/adressenregister/straten/1/huisnummers/4/busnummers/1"
            )
        self.assertEqual("200 OK", res.status)
        self.assertEqual([], res.json)

    def test_get_adres_by_id(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen/900746",
                json=adres,
                status=200,
            )
            res = self.testapp.get("/adressenregister/adressen/900746")
        self.assertEqual("200 OK", res.status)
        self.assertDictEqual(
            {
                "busnummer": "",
                "huisnummer": "50",
                "id": "900746",
                "label": "Sint-Jansvest 50, 9000 Gent",
                "status": "inGebruik",
                "uri": "https://data.vlaanderen.be/id/adres/900746",
            },
            res.json,
        )

    def test_get_adres_by_id_404(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen/900746",
                status=404,
            )
            res = self.testapp.get("/adressenregister/adressen/900746", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_get_percelen_by_adres_id(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/percelen",
                json=percelen,
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen/200001",
                json={"identificator": {"objectId": 1}},
                status=200,
            )
            res = self.testapp.get("/adressenregister/adressen/200001/percelen")
        self.assertEqual("200 OK", res.status)
        self.assertListEqual(
            [
                {
                    "id": "13013C0384-02H003",
                    "status": "gerealiseerd",
                    "uri": "https://data.vlaanderen.be/id/perceel/13013C0384-02H003",
                }
            ],
            res.json,
        )

    def test_get_percelen_by_adres_id_404(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen/200001",
                status=404,
            )
            res = self.testapp.get(
                "/adressenregister/adressen/200001/percelen", status=404
            )
        self.assertEqual("404 Not Found", res.status)

    def test_get_percelen_by_adres_id_empty(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/percelen",
                json={"percelen": []},
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/adressen/200001",
                json={"identificator": {"objectId": 1}},
                status=200,
            )
            res = self.testapp.get("/adressenregister/adressen/200001/percelen")
        self.assertEqual("200 OK", res.status)
        self.assertEqual([], res.json)

    def test_get_perceel_by_id(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/percelen/13013C0384-02H003",
                json=perceel,
                status=200,
            )
            res = self.testapp.get("/adressenregister/percelen/13013C0384-02H003")
        self.assertEqual("200 OK", res.status)
        self.assertDictEqual(
            {
                "adressen": [{"id": "200001"}],
                "id": "13013C0384-02H003",
                "status": "gerealiseerd",
                "uri": "https://data.vlaanderen.be/id/perceel/13013C0384-02H003",
            },
            res.json,
        )

    def test_get_perceel_by_id_parts(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/percelen/13013C0384-02H003",
                json=perceel,
                status=200,
            )
            res = self.testapp.get("/adressenregister/percelen/13013C0384/02H003")
        self.assertEqual("200 OK", res.status)
        self.assertDictEqual(
            {
                "adressen": [{"id": "200001"}],
                "id": "13013C0384-02H003",
                "status": "gerealiseerd",
                "uri": "https://data.vlaanderen.be/id/perceel/13013C0384-02H003",
            },
            res.json,
        )

    def test_get_perceel_by_id_404(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/percelen/13013C0384-02H003",
                status=404,
            )
            res = self.testapp.get(
                "/adressenregister/percelen/13013C0384-02H003", status=404
            )
        self.assertEqual("404 Not Found", res.status)

    def test_adresregister_list_postinfo_by_gemeente_naam(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/postinfo",
                json=postinfos,
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/postinfo/1000",
                json=postinfo_1000,
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/postinfo/1020",
                json=postinfo_1020,
                status=200,
            )
            res = self.testapp.get("/adressenregister/gemeenten/brussel/postinfo")
        self.assertEqual("200 OK", res.status)
        self.assertListEqual(
            [
                {
                    "namen": ["BRUSSEL"],
                    "postcode": "1000",
                    "status": "gerealiseerd",
                    "uri": "https://data.vlaanderen.be/id/postinfo/1000",
                },
                {
                    "namen": ["Laken"],
                    "postcode": "1020",
                    "status": "gerealiseerd",
                    "uri": "https://data.vlaanderen.be/id/postinfo/1020",
                },
            ],
            res.json,
        )

    def test_adresregister_list_postinfo_by_gemeente_niscode(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/postinfo",
                json=postinfos,
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/postinfo/1000",
                json=postinfo_1000,
                status=200,
            )
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/postinfo/1020",
                json=postinfo_1020,
                status=200,
            )
            res = self.testapp.get("/adressenregister/gemeenten/21004/postinfo")
        self.assertEqual("200 OK", res.status)
        self.assertListEqual(
            [
                {
                    "namen": ["BRUSSEL"],
                    "postcode": "1000",
                    "status": "gerealiseerd",
                    "uri": "https://data.vlaanderen.be/id/postinfo/1000",
                },
                {
                    "namen": ["Laken"],
                    "postcode": "1020",
                    "status": "gerealiseerd",
                    "uri": "https://data.vlaanderen.be/id/postinfo/1020",
                },
            ],
            res.json,
        )

    def test_adresregister_list_postinfo_by_gemeente_404(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/postinfo",
                status=404,
            )
            res = self.testapp.get(
                "/adressenregister/gemeenten/brussel/postinfo", status=404
            )
        self.assertEqual("404 Not Found", res.status)

    def test_adresregister_get_postinfo_by_postcode(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/postinfo/1000",
                json=postinfo_1000,
                status=200,
            )

            res = self.testapp.get("/adressenregister/postinfo/1000")
        self.assertEqual("200 OK", res.status)
        self.assertDictEqual(
            {
                "namen": ["BRUSSEL"],
                "postcode": "1000",
                "status": "gerealiseerd",
                "uri": "https://data.vlaanderen.be/id/postinfo/1000",
            },
            res.json,
        )

    def test_adresregister_get_postinfo_by_postcode_404(self):
        with responses.RequestsMock() as rsps:
            rsps.add(
                method=rsps.GET,
                url="https://api.basisregisters.vlaanderen.be/v2/postinfo/1000",
                headers={"accept": "application/json"},
                status=404,
            )
            res = self.testapp.get("/adressenregister/postinfo/1000", status=404)
        self.assertEqual("404 Not Found", res.status)

    def test_get_land_by_id(self):
        res = self.testapp.get("/adressenregister/landen/BE")
        self.assertEqual("200 OK", res.status)
        self.assertEqual("BE", res.json["code"])

    def test_get_land_by_unexisting_id(self):
        res = self.testapp.get("/adressenregister/landen/MORDOR", status=404)
        self.assertEqual("404 Not Found", res.status)
