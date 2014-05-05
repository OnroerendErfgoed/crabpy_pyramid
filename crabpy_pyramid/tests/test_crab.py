# -*- coding: utf-8 -*-
'''
Testing of the crab specific aspects.
.. versionadded:: 0.1.0
'''

from pyramid import testing
from crabpy.gateway.crab import CrabGateway
from crabpy.client import crab_factory

from crabpy_pyramid import (
    get_crab,
    _build_crab,
    ICrab,
    _parse_settings,
    _filter_settings
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
        G = CrabGateway(crab_factory())
        r.registerUtility(G, ICrab)
        G2 = get_crab(r)
        self.assertIsInstance(G, CrabGateway)
        self.assertIsInstance(G2, CrabGateway)
        self.assertEqual(G, G2)

    def test_build_crab_already_exists(self):
        r = TestRegistry()
        G = CrabGateway(crab_factory())
        r.registerUtility(G, ICrab)
        G2 = _build_crab(r, {})
        self.assertIsInstance(G, CrabGateway)
        self.assertIsInstance(G2, CrabGateway)
        self.assertEqual(G, G2)

    def test_build_crab_default_settings(self):
        r = TestRegistry()
        G = CrabGateway(crab_factory())
        r.registerUtility(G, ICrab)
        G2 = _build_crab(r, {})
        self.assertIsInstance(G, CrabGateway)
        self.assertIsInstance(G2, CrabGateway)  
        self.assertEqual(G, G2)

    def test_build_crab_custom_settings(self):
        settings = {
            'crabpy.cache.file.root': './dogpile_data/',
            'crabpy.crab.permanent.backend': 'dogpile.cache.dbm',
            'crabpy.crab.permanent.expiration_time': 604800,
            'crabpy.crab.permanent.arguments.filename': 'dogpile_data/crab_permanent.dbm',
            'crabpy.crab.long.backend': 'dogpile.cache.dbm',
            'crabpy.crab.long.expiration_time': 86400,
            'crabpy.crab.long.arguments.filename': 'dogpile_data/crab_long.dbm',
            'crabpy.crab.short.backend': 'dogpile.cache.dbm',
            'crabpy.crab.short.expiration_time': 3600,
            'crabpy.crab.short.arguments.filename': 'dogpile_data/crab_short.dbm'
        }
        r = TestRegistry(settings)
        crab_settings = _filter_settings(_parse_settings(settings), 'crab.')
        if 'include' in crab_settings:
            del crab_settings['include']
        G = _build_crab(r, crab_settings)
        self.assertIsInstance(G, CrabGateway)
