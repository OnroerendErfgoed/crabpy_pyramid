# -*- coding: utf8 -*-

from pyramid import testing
from crabpy.gateway import capakey
from crabpy.gateway.capakey import CapakeyGateway
from crabpy.client import capakey_factory

from crabpy_pyramid import (
    get_capakey,
    includeme,
    _parse_settings,
    _build_capakey,
    ICapakey
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

        self.capakey = None

    def queryUtility(self, iface):
        return self.capakey

    def registerUtility(self, capakey, iface):
        self.capakey = capakey


class TestGetAndBuild(unittest.TestCase):

    def test_get_capakey(self):
        r = TestRegistry()
        G = capakey.CapakeyGateway(capakey_factory(
            user=None,
            password=None,
            wsdl="http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
        ))
        r.registerUtility(G, ICapakey)
        G2 = get_capakey(r)
        self.assertEqual(G, G2)


    def test_build_capakey_already_exists(self):
        r = TestRegistry()
        G = capakey.CapakeyGateway(capakey_factory(
            user=None,
            password='TalissaWachtwoord',
            wsdl="http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
        ))
        r.registerUtility(G, ICapakey)
        G2 = _build_capakey(r)
        self.assertEqual(G, G2)

    def test_build_capakey_default_settings(self):
        r = TestRegistry()
        G = capakey.CapakeyGateway(capakey_factory(
            user=None,
            password=None,
            wsdl="http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
        ))
        r.registerUtility(G, ICapakey)
        G2 = _build_capakey(r)
        self.assertIsInstance(G, capakey.CapakeyGateway)
        self.assertIsInstance(G2, capakey.CapakeyGateway)
        self.assertEqual(G, G2)

    def test_build_rawes_custom_settings(self):
        settings = {
            'capakey.user': 'Talissa',
            'capakey.password': 'TalissaWachtwoord',
            'capakey.wsdl': "http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
        }
        r = TestRegistry(settings)
        G = _build_capakey(r)
        self.assertIsInstance(G, capakey.CapakeyGateway)

class TestSettings(unittest.TestCase):

    def _assert_contains_all_keys(self, args):
        self.assertIn('user', args)
        self.assertIn('password', args)
        self.assertIn('wsdl', args)

    def test_get_default_settings(self):
        settings = {}
        args = _parse_settings(settings)
        self._assert_contains_all_keys(args)

    def test_get_some_settings(self):
        settings = {
            'capakey.user': 'Talissa',
            'capakey.password': 'TalissaWachtwoord',
        }
        args = _parse_settings(settings)
        self._assert_contains_all_keys(args)
        self.assertEqual('Talissa', args['user'])
        self.assertEqual('TalissaWachtwoord', args['password'])

    def test_get_all_settings(self):
        settings = {
            'capakey.user': 'Talissa',
            'capakey.password': 'TalissaWachtwoord',
            'capakey.wsdl': "http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL",
        }
        args = _parse_settings(settings)
        self._assert_contains_all_keys(args)
        self.assertEqual(
            "http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL",
            args['wsdl']
        )
        self.assertEqual('Talissa', args['user'])
        self.assertEqual('TalissaWachtwoord', args['password'])

    '''def test_missing_settings(self):
        settings = {}
        with warnings.catch_warnings(record=True) as w:
            _parse_settings(settings)
            self.assertEqual(2, len(w))'''


class TestIncludeMe(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.config.registry.settings['capakey.user'] = 'Talissa'
        self.config.registry.settings['capakey.password'] = 'TalissaWachtwoord'
        self.config.registry.settings['capakey.wsdl'] = \
            "http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"

    def tearDown(self):
        del self.config

    def test_includeme(self):
        includeme(self.config)
        ES = self.config.registry.queryUtility(ICapakey)
        self.assertIsInstance(ES, capakey.CapakeyGateway)

    def test_directive_was_added(self):
        includeme(self.config)
        r = self.config.registry.settings
        self.assertEqual('Talissa', r['capakey.user'])  
