# -*- coding: utf-8 -*-
'''
Functional tests.

.. versionadded:: 0.1.0
'''
import unittest
import os
import shutil

from pyramid import testing
from webtest import TestApp

from crabpy_pyramid import main


def as_bool(value):
    '''
    Cast a textual value from a config file to a boolean.
    Will convert 'true', 'True', '1', 't', 'T' or 'Yes' to `True`. All other
    values are considered to be `False`.
    '''
    return value in ['true', 'True', '1', 't', 'T', 'Yes']


def run_capakey_integration_tests():
    from testconfig import config
    try:
        return as_bool(config['capakey']['run_integration_tests'])
    except KeyError:  # pragma NO COVER
        return False


def run_crab_integration_tests():
    from testconfig import config
    try:
        return as_bool(config['crab']['run_integration_tests'])
    except KeyError:  # pragma NO COVER
        return False

settings = {
    'crabpy.cache.file.root': os.path.join(os.path.dirname(__file__), 'dogpile_data'),
    'crabpy.capakey.include': True,
    'crabpy.capakey.user': 'vandaeko',
    'crabpy.capakey.password': 'f77737b9-55cc-4c4a-b86a-895d328c88f4',
    'crabpy.capakey.cache_config.permanent.backend': 'dogpile.cache.dbm',
    'crabpy.capakey.cache_config.permanent.expiration_time': 604800,
    'crabpy.capakey.cache_config.permanent.arguments.filename': os.path.join(os.path.dirname(__file__), 'dogpile_data', 'capakey_permanent.dbm'),
    'crabpy.capakey.cache_config.long.backend': 'dogpile.cache.dbm',
    'crabpy.capakey.cache_config.long.expiration_time': 86400,
    'crabpy.capakey.cache_config.long.arguments.filename': os.path.join(os.path.dirname(__file__), 'dogpile_data', 'capakey_long.dbm'),
    'crabpy.capakey.cache_config.short.backend': 'dogpile.cache.dbm',
    'crabpy.capakey.cache_config.short.expiration_time': 3600,
    'crabpy.capakey.cache_config.short.arguments.filename': os.path.join(os.path.dirname(__file__), 'dogpile_data', 'capakey_short.dbm'),
    'crabpy.crab.include': True,
    'crabpy.crab.cache_config.permanent.backend': 'dogpile.cache.dbm',
    'crabpy.crab.cache_config.permanent.expiration_time': 604800,
    'crabpy.crab.cache_config.permanent.arguments.filename': os.path.join(os.path.dirname(__file__), 'dogpile_data', 'crab_permanent.dbm'),
    'crabpy.crab.cache_config.long.backend': 'dogpile.cache.dbm',
    'crabpy.crab.cache_config.long.expiration_time': 86400,
    'crabpy.crab.cache_config.long.arguments.filename': os.path.join(os.path.dirname(__file__), 'dogpile_data', 'crab_long.dbm'),
    'crabpy.crab.cache_config.short.backend': 'dogpile.cache.dbm',
    'crabpy.crab.cache_config.short.expiration_time': 3600,
    'crabpy.crab.cache_config.short.arguments.filename': os.path.join(os.path.dirname(__file__), 'dogpile_data', 'crab_short.dbm'),
}


def setUpModule():
    shutil.rmtree(
        os.path.join(os.path.dirname(__file__), 'dogpile_data'),
        True
    )


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
    run_capakey_integration_tests(),
    'No CAPAKEY Integration tests required'
)
class CapakeyFunctionalTests(FunctionalTests):
    def test_list_gemeenten(self):
        res = self.testapp.get('/capakey/gemeenten')
        self.assertEqual('200 OK', res.status)

    def test_get_gemeente_by_id(self):
        res = self.testapp.get('/capakey/gemeenten/11001')
        self.assertEqual('200 OK', res.status)

    def test_get_gemeente_by_unexisting_id(self):
        res = self.testapp.get('/capakey/gemeenten/1100', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_kadastrale_afdelingen_by_gemeente(self):
        res = self.testapp.get('/capakey/gemeenten/11001/afdelingen')
        self.assertEqual('200 OK', res.status)

    def test_list_kadastrale_afdelingen(self):
        res = self.testapp.get('/capakey/afdelingen')
        self.assertEqual('200 OK', res.status)

    def test_get_kadastrale_afdeling_by_id(self):
        res = self.testapp.get('/capakey/afdelingen/11001')
        self.assertEqual('200 OK', res.status)

    def test_get_kadastrale_afdeling_by_unexisting_id(self):
        res = self.testapp.get('/capakey/afdelingen/99999', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_secties_by_afdeling(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties')
        self.assertEqual('200 OK', res.status)

    def test_get_sectie_by_id_and_afdeling(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties/B')
        self.assertEqual('200 OK', res.status)

    def test_get_sectie_by_unexisting_id_and_afdeling(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties/Z', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_percelen_by_sectie(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties/B/percelen')
        self.assertEqual('200 OK', res.status)

    def test_get_perceel_by_sectie_and_id(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties/B/percelen/0001/00S000')
        self.assertEqual('200 OK', res.status)

    def test_get_perceel_by_unexisting_sectie_and_id(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties/B/percelen/0000/00000', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_get_perceel_by_capakey(self):
        res = self.testapp.get('/capakey/percelen/11001B0001/00S000')
        self.assertEqual('200 OK', res.status)

    def test_get_perceel_by_unexisting_capakey(self):
        res = self.testapp.get('/capakey/percelen/00000000000/000000', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_get_perceel_by_percid(self):
        res = self.testapp.get('/capakey/percelen/11001_B_0001_S_000_00')
        self.assertEqual('200 OK', res.status)

    def test_get_perceel_by_unexisting_percid(self):
        res = self.testapp.get('/capakey/percelen/00000_0_0000_0_000_00', status=404)
        self.assertEqual('404 Not Found', res.status)


@unittest.skipUnless(
    run_crab_integration_tests(),
    'No CRAB Integration tests required'
)
class CrabFunctionalTests(FunctionalTests):
    def test_list_gewesten(self):
        res = self.testapp.get('/crab/gewesten')
        self.assertEqual('200 OK', res.status)

    def test_get_gewest_by_id(self):
        res = self.testapp.get('/crab/gewesten/2')
        self.assertEqual('200 OK', res.status)

    def test_get_gewest_by_unexisting_id(self):
        res = self.testapp.get('/crab/gewesten/0', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_provincies(self):
        res = self.testapp.get('/crab/gewesten/2/provincies')
        self.assertEqual('200 OK', res.status)

    def test_get_provincie_by_id(self):
        res = self.testapp.get('/crab/provincies/10000')
        self.assertEqual('200 OK', res.status)

    def test_get_provincie_by_unexisting_id(self):
        res = self.testapp.get('/crab/provincies/00000', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_gemeenten_by_provincie(self):
        res = self.testapp.get('/crab/provincies/10000/gemeenten')
        self.assertEqual('200 OK', res.status)

    def test_list_gemeenten_crab(self):
        res = self.testapp.get('/crab/gewesten/2/gemeenten')
        self.assertEqual('200 OK', res.status)

    def test_get_gemeente_crab_niscode(self):
        res = self.testapp.get('/crab/gemeenten/11001')
        self.assertEqual('200 OK', res.status)

    def test_get_gemeente_crab_unexisting_niscode(self):
        res = self.testapp.get('/crab/gemeenten/00000', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_get_gemeente_crab_id(self):
        res = self.testapp.get('/crab/gemeenten/1')
        self.assertEqual('200 OK', res.status)

    def test_get_gemeente_crab_unexisting_id(self):
        res = self.testapp.get('/crab/gemeenten/0', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_deelgemeenten(self):
        res = self.testapp.get('/crab/gewesten/2/deelgemeenten')
        self.assertEqual('200 OK', res.status)

    def test_list_deelgemeenten_wrong_gewest(self):
        res = self.testapp.get('/crab/gewesten/1/deelgemeenten', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_deelgemeenten_by_gemeente(self):
        res = self.testapp.get('/crab/gemeenten/11001/deelgemeenten')
        self.assertEqual('200 OK', res.status)

    def test_list_deelgemeenten_by_unexisting_gemeente(self):
        res = self.testapp.get('/crab/gemeenten/99999/deelgemeenten', status=404)
        self.assertEqual('404 Not Found', res.status)
        res = self.testapp.get('/crab/gemeenten/9999/deelgemeenten', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_get_deelgemeente_by_id(self):
        res = self.testapp.get('/crab/deelgemeenten/45062A')
        self.assertEqual('200 OK', res.status)

    def test_list_straten(self):
        res = self.testapp.get('/crab/gemeenten/11001/straten')
        self.assertEqual('200 OK', res.status)

    def test_get_straat_by_id(self):
        res = self.testapp.get('/crab/straten/1')
        self.assertEqual('200 OK', res.status)

    def test_get_straat_by_unexisting_id(self):
        res = self.testapp.get('/crab/straten/0', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_huisnummers(self):
        res = self.testapp.get('/crab/straten/1/huisnummers')
        self.assertEqual('200 OK', res.status)

    def test_get_huisnummer_by_straat_and_label(self):
        res = self.testapp.get('/crab/straten/1/huisnummers/3')
        self.assertEqual('200 OK', res.status)

    def test_get_huisnummer_by_unexisting_straat_and_label(self):
        res = self.testapp.get('/crab/straten/1/huisnummers/0', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_get_huisnummer_by_id(self):
        res = self.testapp.get('/crab/huisnummers/1')
        self.assertEqual('200 OK', res.status)

    def test_get_huisnummer_by_unexisting_id(self):
        res = self.testapp.get('/crab/huisnummers/0', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_percelen(self):
        res = self.testapp.get('/crab/huisnummers/1/percelen')
        self.assertEqual('200 OK', res.status)

    def test_get_perceel_by_id(self):
        res = self.testapp.get('/crab/percelen/31433D0011/00T016')
        self.assertEqual('200 OK', res.status)

    def test_get_perceel_by_unexisting_id(self):
        res = self.testapp.get('/crab/percelen/31433D0011/000000', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_huisnummers_by_perceel(self):
        res = self.testapp.get('/crab/percelen/31433D0011/00T016/huisnummers')
        self.assertEqual('200 OK', res.status)

    def test_list_huisnummers_by_unexisting_perceel(self):
        res = self.testapp.get('/crab/percelen/31433D0011/000000/huisnummers', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_gebouwen(self):
        res = self.testapp.get('/crab/huisnummers/1/gebouwen')
        self.assertEqual('200 OK', res.status)

    def test_get_gebouw_by_id(self):
        res = self.testapp.get('/crab/gebouwen/1538575')
        self.assertEqual('200 OK', res.status)

    def test_get_gebouw_by_unexisting_id(self):
        res = self.testapp.get('/crab/gebouwen/99999999', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_get_wegobject(self):
        res = self.testapp.get('/crab/wegobjecten/53694755')
        self.assertEqual('200 OK', res.status)

    def test_get_unexisting_wegobject(self):
        res = self.testapp.get('/crab/wegobjecten/00000000', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_subadressen(self):
        res = self.testapp.get('/crab/huisnummers/129462/subadressen')
        self.assertEqual('200 OK', res.status)

    def test_get_subadressen_by_id(self):
        res = self.testapp.get('/crab/subadressen/1120934')
        self.assertEqual('200 OK', res.status)

    def test_get_subadressen_by_unexisting_id(self):
        res = self.testapp.get('/crab/subadressen/0000000', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_postkantons_by_gemeente(self):
        res = self.testapp.get('/crab/gemeenten/90/postkantons')
        self.assertEqual('200 OK', res.status)

    def test_list_adresposities_by_huisnummer(self):
        res = self.testapp.get('/crab/huisnummers/145/adresposities')
        self.assertEqual('200 OK', res.status)

    def test_list_adresposities_by_subadres(self):
        res = self.testapp.get('/crab/subadressen/145/adresposities')
        self.assertEqual('200 OK', res.status)

    def test_get_adrespositie_by_id(self):
        res = self.testapp.get('/crab/adresposities/137')
        self.assertEqual('200 OK', res.status)

    def test_get_adrespositie_by_unexisting_id(self):
        res = self.testapp.get('/crab/adresposities/0', status=404)
        self.assertEqual('404 Not Found', res.status)

    def test_list_landen(self):
        res = self.testapp.get('/crab/landen')
        self.assertEqual('200 OK', res.status)

    def test_get_land_by_id(self):
        res = self.testapp.get('/crab/landen/BE')
        self.assertEqual('200 OK', res.status)

    def test_get_land_by_unexisting_id(self):
        res = self.testapp.get('/crab/landen/MORDOR', status=404)
        self.assertEqual('404 Not Found', res.status)

@unittest.skipUnless(
    run_crab_integration_tests(),
    'No CRAB Integration tests required'
)
class HttpCachingFunctionalTests(FunctionalTests):
    def test_list_gewesten(self):
        res = self.testapp.get('/crab/gewesten')
        self.assertEqual('200 OK', res.status)
        self.assertIn('ETag', res.headers)

    def test_http_304_res(self):
        res = self.testapp.get('/crab/gewesten')
        self.assertEqual('200 OK', res.status)
        etag = res.headers['Etag']
        res2 = self.testapp.get('/crab/gewesten', headers={'If-None-Match': etag})
        self.assertEqual('304 Not Modified', res2.status)
