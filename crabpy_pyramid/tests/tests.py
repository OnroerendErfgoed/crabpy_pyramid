# -*- coding: utf8 -*-

from pyramid import testing
from crabpy.gateway.capakey import CapakeyGateway
from crabpy.gateway.crab import CrabGateway
import os

from crabpy_pyramid import (
    includeme,
    ICapakey,
    ICrab
)

import warnings

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa


class TestIncludeMe(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp(
            settings = {
                'capakey.user': 'Talissa',
                'capakey.password': 'TalissaWachtwoord',
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
        )

    def tearDown(self):
        del self.config

    def test_includeme_existing_root(self):
        includeme(self.config)
        ES = self.config.registry.queryUtility(ICapakey)
        self.assertIsInstance(ES, CapakeyGateway)
        ES = self.config.registry.queryUtility(ICrab)
        self.assertIsInstance(ES, CrabGateway)
        
    def test_includeme_nonexisting_root(self):
        root = './testdir/'
        self.config.registry.settings['root'] = root
        includeme(self.config)
        ES = self.config.registry.queryUtility(ICapakey)
        self.assertIsInstance(ES, CapakeyGateway)
        ES = self.config.registry.queryUtility(ICrab)
        self.assertIsInstance(ES, CrabGateway)
        os.rmdir(root)
        
        
    def test_directive_was_added(self):
        includeme(self.config)
        r = self.config.registry.settings
        self.assertEqual('Talissa', r['capakey.user'])
