# -*- coding: utf-8 -*-
'''
Functional tests.
.. versionadded:: 0.1.0
'''
import unittest
import json
import os

from paste.deploy.loadwsgi import appconfig

from pyramid import testing
from webtest import TestApp

from crabpy_pyramid import main

def run_capakey_integration_tests():
    from testconfig import config
    from crabpy.tests import as_bool
    try:
        return as_bool(config['capakey']['run_integration_tests'])
    except KeyError:  # pragma NO COVER
        return False

settings = {
    'capakey.user': 'USEr',
    'capakey.password': 'PSWD',
    'root': './dogpile_data/',
    'capakey.permanent.backend': 'dogpile.cache.dbm',
    'capakey.permanent.expiration_time': 604800,
    'capakey.permanent.arguments.filename': 'dogpile_data/capakey_permanent.dbm',
    'capakey.long.backend': 'dogpile.cache.dbm',
    'capakey.long.expiration_time': 86400,
    'capakey.long.arguments.filename': 'dogpile_data/capakey_long.dbm',
    'capakey.short.backend': 'dogpile.cache.dbm',
    'capakey.short.expiration_time': 3600,
    'capakey.short.arguments.filename': 'dogpile_data/capakey_short.dbm',
    'crab.permanent.backend': 'dogpile.cache.dbm',
    'crab.permanent.expiration_time': 604800,
    'crab.permanent.arguments.filename': 'dogpile_data/crab_permanent.dbm',
    'crab.long.backend': 'dogpile.cache.dbm',
    'crab.long.expiration_time': 86400,
    'crab.long.arguments.filename': 'dogpile_data/crab_long.dbm',
    'crab.short.backend': 'dogpile.cache.dbm',
    'crab.short.expiration_time': 3600,
    'crab.short.arguments.filename': 'dogpile_data/crab_short.dbm'
}


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
    
    def test_list_kadastrale_afdelingen_by_gemeente(self):
        res = self.testapp.get('/capakey/gemeenten/11001/afdelingen')
        self.assertEqual('200 OK', res.status)
        
    def test_list_secties_by_afdeling(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties')
        self.assertEqual('200 OK', res.status)
        
    def test_get_sectie_by_id_and_afdeling(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties/B')
        self.assertEqual('200 OK', res.status)

    def test_list_percelen_by_sectie(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties/B/percelen')
        self.assertEqual('200 OK', res.status)

    def test_get_perceel_by_sectie_and_id(self):
        res = self.testapp.get('/capakey/afdelingen/11001/secties/B/percelen/0001/00S000')
        self.assertEqual('200 OK', res.status)

    def test_get_perceel_by_capakey(self):
        res = self.testapp.get('/capakey/percelen/11001B0001/00S000')
        self.assertEqual('200 OK', res.status)

    def test_get_perceel_by_percid(self):
        res = self.testapp.get('/capakey/percelen/11001_B_0001_S_000_00')
        self.assertEqual('200 OK', res.status)  
        
class CrabFunctionalTests(FunctionalTests):
    def test_list_gewesten(self):
        res = self.testapp.get('/crab/gewesten')
        self.assertEqual('200 OK', res.status)
        
    def test_get_gewest_by_id(self):
        res = self.testapp.get('/crab/gewesten/2')
        self.assertEqual('200 OK', res.status)
        
    def test_list_gemeenten_crab(self):
        res = self.testapp.get('/crab/gewesten/2/gemeenten')
        self.assertEqual('200 OK', res.status)
        
    def test_get_gemeente_crab_niscode(self):
        res = self.testapp.get('/crab/gemeenten/11001')
        self.assertEqual('200 OK', res.status)
        
    def test_get_gemeente_crab_id(self):
        res = self.testapp.get('/crab/gemeenten/1')
        self.assertEqual('200 OK', res.status)

    def test_list_straten(self):
        res = self.testapp.get('/crab/gemeenten/11001/straten')
        self.assertEqual('200 OK', res.status)
        
    def test_get_straat_by_id(self):
        res = self.testapp.get('/crab/straten/1')
        self.assertEqual('200 OK', res.status)
        
    def test_list_huisnummers(self):
        res = self.testapp.get('/crab/straten/1/huisnummers')
        self.assertEqual('200 OK', res.status)
        
    def test_get_huisnummer_by_straat_and_label(self):
        res = self.testapp.get('/crab/straten/1/huisnummers/3')
        self.assertEqual('200 OK', res.status)
    
    def test_get_huisnummer_by_id(self):
        res = self.testapp.get('/crab/huisnummers/1')
        self.assertEqual('200 OK', res.status)
        
    def test_list_percelen(self):
        res = self.testapp.get('/crab/huisnummers/1/percelen')
        self.assertEqual('200 OK', res.status)
        
    def test_get_perceel_by_id(self):
        res = self.testapp.get('/crab/percelen/31433D0011/00T016')
        self.assertEqual('200 OK', res.status)
        
    def test_list_gebouwen(self):
        res = self.testapp.get('/crab/huisnummers/1/gebouwen')
        self.assertEqual('200 OK', res.status)
    
    def test_get_gebouw_by_id(self):
        res = self.testapp.get('/crab/gebouwen/1538575')
        self.assertEqual('200 OK', res.status)
        
    def test_get_wegobject(self):
        res = self.testapp.get('/crab/wegobjecten/53694755')
        self.assertEqual('200 OK', res.status)

