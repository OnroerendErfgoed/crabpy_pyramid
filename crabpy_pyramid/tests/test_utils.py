# -*- coding: utf-8 -*-
'''
Tests for the utility module.

.. versionadded:: 0.1.0
'''

from crabpy_pyramid.utils import (
    parse_range_header,
    range_return
)

import unittest

class UtilsTests(unittest.TestCase):

    def test_parse_range_header(self):
        headers = [
            {
                'header': 'items=0-19',
                'result': {
                    'start': 0,
                    'einde': 19,
                    'aantal': 20
                }
            }, {
                'header': 'items:0-19',
                'result': False
            }, {
                'header': 'test',
                'result': False
            }, {
                'header': 'items=t-t',
                'result': False
            }, {
                'header': 'items=10-0',
                'result': {
                    'start': 10,
                    'einde': 10,
                    'aantal': 1
                }
            }]
        for header in headers:
            res = parse_range_header(header['header'])
            self.assertEquals(res, header['result'])
