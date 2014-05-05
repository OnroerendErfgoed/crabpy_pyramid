# -*- coding: utf-8 -*-
'''
Testing of the capakey specific aspects.
.. versionadded:: 0.1.0
'''

from pyramid import testing
from crabpy.gateway.capakey import CapakeyGateway
from crabpy.client import capakey_factory

from crabpy_pyramid import (
    get_capakey,
    includeme,
    _parse_settings,
    _filter_settings,
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
        G = CapakeyGateway(capakey_factory(
            user=None,
            password=None
        ))
        r.registerUtility(G, ICapakey)
        G2 = get_capakey(r)
        self.assertIsInstance(G, CapakeyGateway)
        self.assertIsInstance(G2, CapakeyGateway)
        self.assertEqual(G, G2)

    def test_build_capakey_already_exists(self):
        r = TestRegistry()
        G = CapakeyGateway(capakey_factory(
            user=None,
            password='TalissaWachtwoord'
        ))
        r.registerUtility(G, ICapakey)
        G2 = _build_capakey(r, {})
        self.assertIsInstance(G, CapakeyGateway)
        self.assertIsInstance(G2, CapakeyGateway)
        self.assertEqual(G, G2)

    def test_build_capakey_default_settings(self):
        r = TestRegistry()
        G = CapakeyGateway(capakey_factory(
            user=None,
            password=None
        ))
        r.registerUtility(G, ICapakey)
        G2 = _build_capakey(r, {})
        self.assertIsInstance(G, CapakeyGateway)
        self.assertIsInstance(G2, CapakeyGateway)
        self.assertEqual(G, G2)

    def test_build_capakey_custom_settings(self):
        settings = {
            'crabpy.capakey.user': 'Talissa',
            'crabpy.capakey.password': 'TalissaWachtwoord',
            'crabpy.cache.file.root': './dogpile_data/',
            'crabpy.capakey.permanent.backend': 'dogpile.cache.dbm',
            'crabpy.capakey.permanent.expiration_time': 604800,
            'crabpy.capakey.permanent.arguments.filename': 'dogpile_data/capakey_permanent.dbm',
            'crabpy.capakey.long.backend': 'dogpile.cache.dbm',
            'crabpy.capakey.long.expiration_time': 86400,
            'crabpy.capakey.long.arguments.filename': 'dogpile_data/capakey_long.dbm',
            'crabpy.capakey.short.backend': 'dogpile.cache.dbm',
            'crabpy.capakey.short.expiration_time': 3600,
            'crabpy.capakey.short.arguments.filename': 'dogpile_data/capakey_short.dbm'
        }
        r = TestRegistry(settings)
        capakey_settings = _filter_settings(_parse_settings(settings), 'capakey.')
        if 'include' in capakey_settings:
            del capakey_settings['include']
        G = _build_capakey(r, capakey_settings)
        self.assertIsInstance(G, CapakeyGateway)
        
class TestSettings(unittest.TestCase):

    def _assert_contains_all_keys(self, args):
        self.assertIn('capakey.user', args)
        self.assertIn('capakey.password', args)

    def test_get_default_settings(self):
        settings = {}
        args = _parse_settings(settings)
        self._assert_contains_all_keys(args)

    def test_get_some_settings(self):
        settings = {
            'crabpy.capakey.user': 'Talissa',
            'crabpy.capakey.password': 'TalissaWachtwoord',
        }
        args = _parse_settings(settings)
        self._assert_contains_all_keys(args)
        self.assertEqual('Talissa', args['capakey.user'])
        self.assertEqual('TalissaWachtwoord', args['capakey.password'])

    def test_get_all_settings(self):
        settings = {
            'crabpy.capakey.user': 'Talissa',
            'crabpy.capakey.password': 'TalissaWachtwoord'
        }
        args = _parse_settings(settings)
        self._assert_contains_all_keys(args)
        self.assertEqual('Talissa', args['capakey.user'])
        self.assertEqual('TalissaWachtwoord', args['capakey.password'])

    '''def test_missing_settings(self):
        settings = {}
        with warnings.catch_warnings(record=True) as w:
            _parse_settings(settings, 'capakey')
            self.assertEqual(2, len(w))'''
        
