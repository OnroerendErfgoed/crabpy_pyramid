# -*- coding: utf-8 -*-
'''
Tests for the capakey renderers module.

.. versionadded:: 0.1.0
'''

from __future__ import unicode_literals

from crabpy_pyramid.renderers.capakey import (
    json_list_renderer,
    json_item_renderer
)

from crabpy.gateway.capakey import (
    Gemeente,
    Afdeling,
    Sectie,
    Perceel
)

import unittest
import json

class CapakeyListTests(unittest.TestCase):

    def setUp(self):
        self.renderer = json_list_renderer({})

    def tearDown(self):
        del self.renderer

    def test_list_gemeenten(self):
        gemeenten = [
            Gemeente(44021, 'Gent'),
            Gemeente(31043, 'Knokke-Heist')
        ]
        dump = self.renderer(gemeenten,{})
        self.assertEquals(
            json.loads(dump),
            [
                {
                    'id': 44021,
                    'naam': 'Gent'
                }, {
                    'id': 31043,
                    'naam': 'Knokke-Heist'
                }
            ]
        )


    def test_list_afdelingen(self):
        afdelingen = [
            Afdeling(44021, 'GENT  1 AFD', Gemeente(44021, 'Gent')),
            Afdeling(31043, 'KNOKKE-HEIST  1 AFD', Gemeente(31043, 'Knokke-Heist'))
        ]
        dump = self.renderer(afdelingen,{})
        self.assertEquals(
            json.loads(dump),
            [
                {
                    'id': 44021,
                    'naam': 'GENT  1 AFD',
                    'gemeente': {
                        'id': 44021,
                        'naam': 'Gent'
                    }
                }, {
                    'id': 31043,
                    'naam': 'KNOKKE-HEIST  1 AFD',
                    'gemeente': {
                        'id': 31043,
                        'naam': 'Knokke-Heist'
                    }
                }
            ]
        )

    def test_list_secties(self):
        secties = [
            Sectie('A', Afdeling(44021, 'GENT  1 AFD', Gemeente(44021, 'Gent')))
        ]
        dump = self.renderer(secties,{})
        self.assertEquals(
            json.loads(dump),
            [
                {
                    'id': 'A',
                    'afdeling': {
                        'id': 44021,
                        'naam': 'GENT  1 AFD',
                        'gemeente': {
                            'id': 44021,
                            'naam': 'Gent'
                        }
                    }
                }
            ]
        )

    def test_list_percelen(self):
        percelen = [
            Perceel(
                '1154/02C000', 
                Sectie(
                    'A', 
                    Afdeling(
                        46013,
                        'KRUIBEKE 1 AFD/KRUIBEKE/',
                        Gemeente(46013, 'Kruibeke')
                    )
                ),
                '46013A1154/02C000', 
                '46013_A_1154_C_000_02'
            )
        ]
        dump = self.renderer(percelen, {})
        self.assertEquals(
            json.loads(dump),
            [
                {
                    'id': '1154/02C000',
                    'sectie': {
                        'id': 'A',
                        'afdeling': {
                            'id': 46013,
                            'naam': 'KRUIBEKE 1 AFD/KRUIBEKE/',
                            'gemeente': {
                                'id': 46013,
                                'naam': 'Kruibeke'
                            }
                        }
                    },
                    'percid': '46013_A_1154_C_000_02',
                    'capakey': '46013A1154/02C000'
                }
            ]
        )
