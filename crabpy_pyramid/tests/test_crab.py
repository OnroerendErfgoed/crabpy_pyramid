# -*- coding: utf8 -*-

from pyramid import testing
from crabpy.gateway.crab import CrabGateway
from crabpy.client import crab_factory

from crabpy_pyramid import (
    get_crab,
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
        G2 = _build_crab(r)
        self.assertIsInstance(G, CrabGateway)
        self.assertIsInstance(G2, CrabGateway)
        self.assertEqual(G, G2)

    def test_build_crab_default_settings(self):
        r = TestRegistry()
        G = CrabGateway(crab_factory())
        r.registerUtility(G, ICrab)
        G2 = _build_crab(r)
        self.assertIsInstance(G, CrabGateway)
        self.assertIsInstance(G2, CrabGateway)  
        self.assertEqual(G, G2)

    def test_build_rawes_custom_settings(self):
        settings = {
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
