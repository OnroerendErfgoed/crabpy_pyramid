# -*- coding: utf8 -*-

from pyramid import testing

from pyramid_capakey import (
    ICapakey,
    get_capakey,
    _build_capakey,
    includeme,
    _parse_settings
)

import capakey

import warnings

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa


def dummy_encoder(obj):
    return obj


class TestRegistry(object):

    def __init__(self, settings=None):

        if settings is None:
            self.settings = {}
        else:
            self.settings = settings

        self.capakey = None

    def queryUtility(self, iface):
        return self.capakey

    def registerUtility(self, rawes, iface):
        self.rawes = rawes


class TestGetAndBuild(unittest.TestCase):

    def test_get_capakey(self):
        r = TestRegistry()
        ES = capakey.Elastic(url='http://localhost:9200')
        r.registerUtility(ES, ICapakey)
        ES2 = get_capakey(r)
        self.assertEqual(ES, ES2)

    def test_build_capakey_already_exists(self):
        r = TestRegistry()
        ES = capakey.Elastic('http://localhost:9200')
        r.registerUtility(ES, ICapakey)
        ES2 = _build_capakey(r)
        self.assertEqual(ES, ES2)

    def test_build_capakey_default_settings(self):
        r = TestRegistry()
        ES = _build_capakey(r)
        self.assertIsInstance(ES, capakey.Elastic)
        self.assertEqual('localhost:9200', ES.url.netloc)

    def test_build_capakey_custom_settings(self):
        settings = {
            'capakey.user': 'Talissa',
            'capakey.password': 'TalissaWachtwoord',
            'capakey. wsdl': "http://ws.agiv.be/capakeyws/nodataset.asmx?WSDL"
        }
        r = TestRegistry(settings)
        ES = _build_capakey(r)
        self.assertIsInstance(ES, capakey.Elastic)
        self.assertEqual('elastic.search.org:9200', ES.url.netloc)


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

    def test_get_dotted_function_settings(self):
        settings = {
            'capakey.json_encoder': 'pyramid_capakey.tests.dummy_encoder'
        }
        args = _parse_settings(settings)
        self.assertEqual(dummy_encoder, args['json_encoder'])

    def test_missing_settings(self):
        settings = {
            'capakey.except_on_error': False
        }
        with warnings.catch_warnings(record=True) as w:
            args = _parse_settings(settings)
            self.assertEqual(1, len(w))


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
        self.assertIsInstance(ES, capakey.Elastic)
        self.assertEqual('localhost:9300', ES.url.netloc)
        self.assertEqual('test', ES.json_encoder('test'))
        self.assertEqual(dummy_encoder, ES.json_encoder)
        self.assertEqual({'test': 'DUMMY'}, ES.connection.kwargs['json_decoder']('{"test": 1}'))

    def test_directive_was_added(self):
        includeme(self.config)
        ES = self.config.get_capakey()
        self.assertIsInstance(ES, capakey.Elastic)
        self.assertEqual('localhost:9300', ES.url.netloc)
