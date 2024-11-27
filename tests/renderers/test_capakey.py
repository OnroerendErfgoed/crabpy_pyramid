"""
Tests for the capakey renderers module.

.. versionadded:: 0.1.0
"""

import json
import unittest

from crabpy.gateway.capakey import Afdeling
from crabpy.gateway.capakey import Gemeente
from crabpy.gateway.capakey import Perceel
from crabpy.gateway.capakey import Sectie

from crabpy_pyramid.renderers.capakey import json_item_renderer
from crabpy_pyramid.renderers.capakey import json_list_renderer


class CapakeyListTests(unittest.TestCase):

    def setUp(self):
        self.renderer = json_list_renderer({})

    def tearDown(self):
        del self.renderer

    def test_list_gemeenten(self):
        gemeenten = [Gemeente(44021, "Gent"), Gemeente(31043, "Knokke-Heist")]
        dump = self.renderer(gemeenten, {})
        self.assertEqual(
            json.loads(dump),
            [{"id": 44021, "naam": "Gent"}, {"id": 31043, "naam": "Knokke-Heist"}],
        )

    def test_list_afdelingen(self):
        afdelingen = [
            Afdeling(44021, "GENT  1 AFD", Gemeente(44021, "Gent")),
            Afdeling(31043, "KNOKKE-HEIST  1 AFD", Gemeente(31043, "Knokke-Heist")),
        ]
        dump = self.renderer(afdelingen, {})
        self.assertEqual(
            json.loads(dump),
            [
                {
                    "id": 44021,
                    "naam": "GENT  1 AFD",
                    "gemeente": {"id": 44021, "naam": "Gent"},
                },
                {
                    "id": 31043,
                    "naam": "KNOKKE-HEIST  1 AFD",
                    "gemeente": {"id": 31043, "naam": "Knokke-Heist"},
                },
            ],
        )

    def test_list_secties(self):
        secties = [Sectie("A", Afdeling(44021, "GENT  1 AFD", Gemeente(44021, "Gent")))]
        dump = self.renderer(secties, {})
        self.assertEqual(
            json.loads(dump),
            [
                {
                    "id": "A",
                    "afdeling": {
                        "id": 44021,
                        "naam": "GENT  1 AFD",
                        "gemeente": {"id": 44021, "naam": "Gent"},
                    },
                }
            ],
        )

    def test_list_percelen(self):
        percelen = [
            Perceel(
                "1154/02C000",
                Sectie(
                    "A",
                    Afdeling(
                        46013, "KRUIBEKE 1 AFD/KRUIBEKE/", Gemeente(46013, "Kruibeke")
                    ),
                ),
                "46013A1154/02C000",
                "46013_A_1154_C_000_02",
            )
        ]
        dump = self.renderer(percelen, {})
        self.assertEqual(
            json.loads(dump),
            [
                {
                    "id": "1154/02C000",
                    "sectie": {
                        "id": "A",
                        "afdeling": {
                            "id": 46013,
                            "naam": "KRUIBEKE 1 AFD/KRUIBEKE/",
                            "gemeente": {"id": 46013, "naam": "Kruibeke"},
                        },
                    },
                    "percid": "46013_A_1154_C_000_02",
                    "capakey": "46013A1154/02C000",
                }
            ],
        )


class CapakeyItemTests(unittest.TestCase):

    def setUp(self):
        self.renderer = json_item_renderer({})

    def tearDown(self):
        del self.renderer

    def test_item_gemeente(self):
        g = Gemeente(
            44021,
            "Gent",
            (104154.2225, 197300.703),
            (94653.453, 185680.984, 113654.992, 208920.422),
        )
        dump = self.renderer(g, {})
        self.assertEqual(
            json.loads(dump),
            {
                "id": 44021,
                "naam": "Gent",
                "centroid": [104154.2225, 197300.703],
                "bounding_box": [94653.453, 185680.984, 113654.992, 208920.422],
            },
        )

    def test_item_afdeling(self):
        a = Afdeling(
            44021,
            "GENT  1 AFD",
            Gemeente(44021, "Gent"),
            (104893.06375, 196022.244094),
            (104002.076625, 194168.3415, 105784.050875, 197876.146688),
        )
        dump = self.renderer(a, {})
        self.assertEqual(
            json.loads(dump),
            {
                "id": 44021,
                "naam": "GENT  1 AFD",
                "gemeente": {"id": 44021, "naam": "Gent"},
                "centroid": [104893.06375, 196022.244094],
                "bounding_box": [
                    104002.076625,
                    194168.3415,
                    105784.050875,
                    197876.146688,
                ],
            },
        )

    def test_item_sectie(self):
        s = Sectie(
            "A",
            Afdeling(44021, "GENT  1 AFD", Gemeente(44021, "Gent")),
            (104893.06375, 196022.244094),
            (104002.076625, 194168.3415, 105784.050875, 197876.146688),
        )
        dump = self.renderer(s, {})
        self.assertEqual(
            json.loads(dump),
            {
                "id": "A",
                "afdeling": {
                    "id": 44021,
                    "naam": "GENT  1 AFD",
                    "gemeente": {"id": 44021, "naam": "Gent"},
                },
                "centroid": [104893.06375, 196022.244094],
                "bounding_box": [
                    104002.076625,
                    194168.3415,
                    105784.050875,
                    197876.146688,
                ],
            },
        )

    def test_item_perceel(self):
        p = Perceel(
            id="1154/02C000",
            sectie=Sectie(
                "A",
                Afdeling(
                    46013, "KRUIBEKE 1 AFD/KRUIBEKE/", Gemeente(46013, "Kruibeke")
                ),
            ),
            capakey="40613A1154/02C000",
            percid="40613_A_1154_C_000_02",
            capatype="capaty",
            cashkey="cashkey",
            centroid=(104893.06375, 196022.244094),
            bounding_box=(104002.076625, 194168.3415, 105784.050875, 197876.146688),
            shape={"shape": "one"},
        )
        dump = self.renderer(p, {})
        self.assertEqual(
            json.loads(dump),
            {
                "id": "1154/02C000",
                "sectie": {
                    "id": "A",
                    "afdeling": {
                        "id": 46013,
                        "naam": "KRUIBEKE 1 AFD/KRUIBEKE/",
                        "gemeente": {"id": 46013, "naam": "Kruibeke"},
                    },
                },
                "capakey": "40613A1154/02C000",
                "percid": "40613_A_1154_C_000_02",
                "centroid": [104893.06375, 196022.244094],
                "bounding_box": [
                    104002.076625,
                    194168.3415,
                    105784.050875,
                    197876.146688,
                ],
                "shape": {"shape": "one"},
            },
        )
