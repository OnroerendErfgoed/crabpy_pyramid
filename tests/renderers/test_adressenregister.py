"""
Tests for the landen renderers (adressenregister).

.. versionadded:: 0.1.0
"""

import sys
import types
# Provide minimal pyramid.renderers.JSON shim to avoid importing full pyramid (which requires pkg_resources)
if 'pyramid' not in sys.modules:
    _pyramid = types.ModuleType('pyramid')
    _renderers = types.ModuleType('pyramid.renderers')

    class JSON:
        def __init__(self, *args, **kwargs):
            self._adapters = {}

        def add_adapter(self, cls, func):
            self._adapters[cls] = func

        def __call__(self, settings=None):
            def renderer(obj, request):
                import json as _json
                def adapt_item(item):
                    for k, v in self._adapters.items():
                        try:
                            if isinstance(item, k):
                                return v(item, request)
                        except Exception:
                            continue
                    # fallback: try attribute access
                    if hasattr(item, '__dict__'):
                        return item.__dict__
                    return item

                if isinstance(obj, (list, tuple)):
                    return _json.dumps([adapt_item(i) for i in obj])
                return _json.dumps(adapt_item(obj))

            return renderer

    _renderers.JSON = JSON
    _pyramid.renderers = _renderers
    sys.modules['pyramid'] = _pyramid
    sys.modules['pyramid.renderers'] = _renderers

import json
import unittest

import pycountry

from crabpy_pyramid.renderers.adressenregister import (
    json_list_renderer,
    json_item_renderer,
)


class LandenRendererTests(unittest.TestCase):

    def setUp(self):
        self.list_renderer = json_list_renderer({})
        self.item_renderer = json_item_renderer({})

    def tearDown(self):
        del self.list_renderer
        del self.item_renderer

    def test_list_landen_in_dutch(self):
        """The list adapter should return Dutch country names (nl)."""
        land = pycountry.countries.get(alpha_2="BE")
        dump = self.list_renderer([land], {})
        self.assertEqual(
            json.loads(dump),
            [{"code": "BE", "naam": "België", "vlag": None}],
        )

    def test_item_land_in_dutch(self):
        """The item adapter should return Dutch country name for an item."""
        land = pycountry.countries.get(alpha_2="BE")
        dump = self.item_renderer(land, {})
        self.assertEqual(
            json.loads(dump),
            {
                "code": "BE",
                "alpha2": "BE",
                "alpha3": land.alpha_3,
                "naam": "België",
                "vlag": None,
            },
        )


if __name__ == "__main__":
    unittest.main()
