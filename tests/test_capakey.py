"""
Testing of the capakey specific aspects.
.. versionadded:: 0.1.0
"""

import unittest

from crabpy.gateway.capakey import CapakeyRestGateway
from pyramid import testing
from pyramid.registry import Registry

from crabpy_pyramid import capakey
from crabpy_pyramid.capakey import ICapakey
from crabpy_pyramid.capakey import build_capakey
from crabpy_pyramid.capakey import get_capakey


class TestGetAndBuild(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.registry: Registry = self.config.registry  # type: ignore

    def tearDown(self):
        testing.tearDown()

    def test_get_capakey(self):
        gateway = CapakeyRestGateway()
        self.registry.registerUtility(gateway, ICapakey)
        gateway_2 = get_capakey(self.registry)
        self.assertEqual(gateway, gateway_2)

    def test_build_capakey_already_exists(self):
        gateway = CapakeyRestGateway()
        self.registry.registerUtility(gateway, ICapakey)
        gateway_2 = build_capakey(self.config)
        self.assertEqual(gateway, gateway_2)

    def test_parse_settings(self):
        settings = {
            "crabpy.cache.file.root": "./dogpile_data/",
            "crabpy.capakey.cache_config.permanent.backend": "dogpile.cache.dbm",
            "crabpy.capakey.cache_config.permanent.expiration_time": 604800,
            "crabpy.capakey.cache_config.permanent.arguments.filename": (
                "dogpile_data/capakey_permanent.dbm"
            ),
            "crabpy.capakey.cache_config.long.backend": "dogpile.cache.dbm",
            "crabpy.capakey.cache_config.long.expiration_time": 86400,
            "crabpy.capakey.cache_config.long.arguments.filename": (
                "dogpile_data/capakey_long.dbm"
            ),
            "crabpy.capakey.cache_config.short.backend": "dogpile.cache.dbm",
            "crabpy.capakey.cache_config.short.expiration_time": 3600,
            "crabpy.capakey.cache_config.short.arguments.filename": (
                "dogpile_data/capakey_short.dbm"
            ),
        }
        parsed_settings = capakey.parse_settings(settings)
        self.assertIsNotNone(parsed_settings)
        expected = {
            "long.arguments.filename": "dogpile_data/capakey_long.dbm",
            "long.backend": "dogpile.cache.dbm",
            "long.expiration_time": 86400,
            "permanent.arguments.filename": "dogpile_data/capakey_permanent.dbm",
            "permanent.backend": "dogpile.cache.dbm",
            "permanent.expiration_time": 604800,
            "short.arguments.filename": "dogpile_data/capakey_short.dbm",
            "short.backend": "dogpile.cache.dbm",
            "short.expiration_time": 3600,
        }
        self.assertEqual(expected, parsed_settings.cache_config)
