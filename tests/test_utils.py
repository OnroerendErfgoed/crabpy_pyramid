"""
Tests for the utility module.

.. versionadded:: 0.1.0
"""

import unittest

from pyramid.testing import DummyRequest

from crabpy_pyramid import utils
from crabpy_pyramid.utils import parse_range_header
from crabpy_pyramid.utils import range_return


class UtilsTests(unittest.TestCase):

    def test_parse_range_header(self):
        headers = [
            {"header": "items=0-19", "result": {"start": 0, "finish": 19, "count": 20}},
            {"header": "items:0-19", "result": False},
            {"header": "test", "result": False},
            {"header": "items=t-t", "result": False},
            {"header": "items=10-0", "result": {"start": 10, "finish": 10, "count": 1}},
        ]
        for header in headers:
            res = parse_range_header(header["header"])
            self.assertEqual(res, header["result"])

    def test_range_return_no_range(self):
        items = range(10)
        req = DummyRequest()
        filtered = range_return(req, items)
        self.assertEqual(items, filtered)
        self.assertEqual(req.response.headers["Content-Range"], "items 0-9/10")

    def test_range_return_filtered(self):
        items = range(10)
        req = DummyRequest()
        req.headers["Range"] = "items=0-4"
        filtered = range_return(req, items)
        self.assertEqual(items[0:5], filtered)
        self.assertEqual(req.response.headers["Content-Range"], "items 0-4/10")

    def test_range_return_x_or_not(self):
        items = range(10)
        req = DummyRequest()
        req.headers["Range"] = "items=0-4"
        filtered_no_x = range_return(req, items)
        req_x = DummyRequest()
        req_x.headers["X-Range"] = "items=0-4"
        filtered_x = range_return(req_x, items)
        self.assertEqual(filtered_x, filtered_no_x)

    def test_range_return_large_request(self):
        items = range(10)
        req = DummyRequest()
        req.headers["Range"] = "items=0-100"
        filtered = range_return(req, items)
        self.assertEqual(items, filtered)
        self.assertEqual(req.response.headers["Content-Range"], "items 0-9/10")

    def test_range_return_max_return(self):
        items = range(9999)
        req = DummyRequest()
        req.headers["Range"] = "items=0-9999"
        filtered = range_return(req, items)
        self.assertEqual(items[0:5000], filtered)
        self.assertEqual(req.response.headers["Content-Range"], "items 0-4999/9999")
        items = range(14999)
        req.headers["Range"] = "items=5000-15000"
        filtered = range_return(req, items)
        self.assertEqual(items[5000:10000], filtered)
        self.assertEqual(req.response.headers["Content-Range"], "items 5000-9999/14999")

    def test_filter_settings(self):
        settings = utils.filter_settings(
            {
                "cache.file.root": "/tmp",
                "capakey.include": False,
            },
            "capakey.",
        )
        self.assertEqual(1, len(settings))
        self.assertFalse(settings["include"])
        self.assertNotIn("cache.file.root", settings)
