# -*- coding: utf8 -*-

from pyramid import testing
from crabpy.gateway.crab import CrabGateway
from crabpy.client import crab_factory

from crabpy_pyramid import (
    get_crab,
    _parse_settings,
    _build_crab,
    ICrab
)

import warnings

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa
    
    
class TestRegistry(object):

    def __init__(self, settings=None):

        if settings is None:
            self.settings = {}
        else:
            self.settings = settings

        self.crab = None

    def queryUtility(self, iface):
        return self.crab

    def registerUtility(self, crab, iface):
        self.crab = crab


class TestGetAndBuild(unittest.TestCase):

    def test_get_crab(self):
        r = TestRegistry()
        G = CrabGateway(crab_factory(
            wsdl="http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
        ))
        r.registerUtility(G, ICrab)
        G2 = get_crab(r)
        self.assertIsInstance(G, CrabGateway)
        self.assertIsInstance(G2, CrabGateway)
        self.assertEqual(G, G2)

    def test_build_crab_already_exists(self):
        r = TestRegistry()
        G = CrabGateway(crab_factory(
            wsdl ="http://ws.agiv.be/crabws/nodataset.asmx?WSDL"
        ))
        r.registerUtility(G, ICrab)
        G2 = _build_crab(r)
        self.assertIsInstance(G, CrabGateway)
        self.assertIsInstance(G2, CrabGateway)
        self.assertEqual(G, G2)

    def test_build_crab_default_settings(self):
        r = TestRegistry()
        G = CrabGateway(crab_factory(
            wsdl="http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
        ))
        r.registerUtility(G, ICrab)
        G2 = _build_crab(r)
        self.assertIsInstance(G, CrabGateway)
        self.assertIsInstance(G2, CrabGateway)  
        self.assertEqual(G, G2)

    def test_build_rawes_custom_settings(self):
        settings = {
            'crab.wsdl': "http://ws.agiv.be/crabws/nodataset.asmx?WSDL",
            'root': './dogpile_data/',
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
        r = TestRegistry(settings)
        G = _build_crab(r)
        self.assertIsInstance(G, CrabGateway)
        
class TestSettings(unittest.TestCase):

    def _assert_contains_all_keys(self, args):
        self.assertIn('wsdl', args)

    def test_get_default_settings(self):
        settings = {}
        args = _parse_settings(settings, 'crab')
        self._assert_contains_all_keys(args)

    def test_get_settings(self):
        settings = {
            'crab.wsdl': "http://ws.agiv.be/crabws/nodataset.asmx?WSDL",
        }
        args = _parse_settings(settings, 'crab')
        self._assert_contains_all_keys(args)
        self.assertEqual(
            "http://ws.agiv.be/crabws/nodataset.asmx?WSDL",
            args['wsdl']
        )


    '''def test_missing_settings(self):
        settings = {}
        with warnings.catch_warnings(record=True) as w:
            _parse_settings(settings, 'capakey')
            self.assertEqual(2, len(w))'''
