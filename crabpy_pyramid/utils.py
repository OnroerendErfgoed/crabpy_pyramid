# -*- coding: utf-8 -*-
'''
Utility functions to help with range handling.

.. versionadded:: 0.1.0
'''

import re

MAX_NUMBER_ITEMS = 5000

def parse_range_header(range):
    '''
    Parse a range header as used by the dojo Json Rest store.

    :param str range: The content of the range header to be parsed. 
        eg. `items=0-9`
    :returns: A dict with keys start, finish and number or `False` if the
        range is invalid.
    '''
    match = re.match('^items=([0-9]+)-([0-9]+)$', range)

    if match:
        start = int(match.group(1))
        finish = int(match.group(2))

        if finish < start:
            finish = start
        return {
            'start': start,
            'finish': finish,
            'count': finish - start + 1
        }
    else:
        return False

def range_return(request, items):
    '''
    Determine what range of objects to return.

    Will check fot both `Range` and `X-Range` headers in the request and
    set both `Content-Range` and 'X-Content-Range' headers.

    :rtype: list
    '''
    if ('Range' in request.headers):
        range = parse_range_header(request.headers['Range'])
    elif 'X-Range' in request.headers:
        range = parse_range_header(request.headers['X-Range'])
    else:
        range = {
            'start': 0,
            'finish': MAX_NUMBER_ITEMS - 1,
            'count': MAX_NUMBER_ITEMS
        }
    filtered = items[range['start']:range['count']]
    if len(filtered) < range['count']:
        # Something was stripped, deal with it
        range['count'] = len(filtered)
        range['finish'] = range['start'] + range['count'] - 1

    request.response.headers['Content-Range'] = 'items %d-%d/%d' % (range['start'], range['finish'], len(items))
    request.response.headers['X-Content-Range'] = request.response.headers['Content-Range']
    return filtered
