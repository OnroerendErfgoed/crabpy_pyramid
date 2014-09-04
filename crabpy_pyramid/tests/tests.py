# -*- coding: utf-8 -*-
'''
Testing of the initialization.
.. versionadded:: 0.1.0
'''

from pyramid import testing
from crabpy.gateway.capakey import CapakeyGateway
from crabpy.gateway.crab import CrabGateway
import os

from crabpy_pyramid import (
    includeme,
    ICapakey,
    ICrab,
    _filter_settings,
    _get_proxy_settings
)

import warnings

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa


class TestSettings(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp(
            settings = {
                'crabpy.capakey.include': True,
                'crabpy.capakey.user': 'Talissa',
                'crabpy.capakey.password': 'TalissaWachtwoord',
                'crabpy.cache.file.root': './dogpile_data/',
                'crabpy.capakey.cache_config.permanent.backend': 'dogpile.cache.dbm',
                'crabpy.capakey.cache_config.permanent.expiration_time': 604800,
                'crabpy.capakey.cache_config.permanent.arguments.filename': 'dogpile_data/capakey_permanent.dbm',
                'crabpy.capakey.cache_config.long.backend': 'dogpile.cache.dbm',
                'crabpy.capakey.cache_config.long.expiration_time': 86400,
                'crabpy.capakey.cache_config.long.arguments.filename': 'dogpile_data/capakey_long.dbm',
                'crabpy.capakey.cache_config.short.backend': 'dogpile.cache.dbm',
                'crabpy.capakey.cache_config.short.expiration_time': 3600,
                'crabpy.capakey.cache_config.short.arguments.filename': 'dogpile_data/capakey_short.dbm',
                'crabpy.crab.include': True,
                'crabpy.crab.cache_config.permanent.backend': 'dogpile.cache.dbm',
                'crabpy.crab.cache_config.permanent.expiration_time': 604800,
                'crabpy.crab.cache_config.permanent.arguments.filename': 'dogpile_data/crab_permanent.dbm',
                'crabpy.crab.cache_config.long.backend': 'dogpile.cache.dbm',
                'crabpy.crab.cache_config.long.expiration_time': 86400,
                'crabpy.crab.cache_config.long.arguments.filename': 'dogpile_data/crab_long.dbm',
                'crabpy.crab.cache_config.short.backend': 'dogpile.cache.dbm',
                'crabpy.crab.cache_config.short.expiration_time': 3600,
                'crabpy.crab.cache_config.short.arguments.filename': 'dogpile_data/crab_short.dbm'
            }
        )

    def tearDown(self):
        del self.config

    def test_filter_settings(self):
        settings = _filter_settings(
            {
                'cache.file.root' : '/tmp',
                'crab.include': True,
                'capakey.include': False,
            }, 
            'capakey.'
        )
        self.assertEquals(1, len(settings))
        self.assertFalse(settings['include'])
        self.assertNotIn('cache.file.root', settings)

    def test_filter_settings_with_proxy(self):
        settings = {
            'proxy.http' : 'http://proxy.example.com:3128',
            'proxy.https' : 'https://httpsproxy.example.com:3128',
            'crab.include': True,
            'crab.cache_config.permanent.backend': 'dogpile.cache.dbm',
        }
        base_settings = _get_proxy_settings(settings)
        crab_settings = dict(_filter_settings(settings, 'crab.'), **base_settings)
        self.assertIn('proxy', crab_settings)
        self.assertIn('http', crab_settings["proxy"])
        self.assertIn('https', crab_settings["proxy"])


    def test_includeme_existing_root(self):
        includeme(self.config)
        capakey = self.config.registry.queryUtility(ICapakey)
        self.assertIsInstance(capakey, CapakeyGateway)
        crab = self.config.registry.queryUtility(ICrab)
        self.assertIsInstance(crab, CrabGateway)
        
    def test_includeme_nonexisting_root(self):
        root = './testdir/'
        self.config.registry.settings['crabpy.cache.file.root'] = root
        includeme(self.config)
        capakey = self.config.registry.queryUtility(ICapakey)
        self.assertIsInstance(capakey, CapakeyGateway)
        crab = self.config.registry.queryUtility(ICrab)
        self.assertIsInstance(crab, CrabGateway)
        os.rmdir(root)
        
    def test_directive_was_added(self):
        includeme(self.config)
        r = self.config.registry.settings
        self.assertEqual('Talissa', r['crabpy.capakey.user'])
