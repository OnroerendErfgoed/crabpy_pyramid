# -*- coding: utf-8 -*-
'''
Utility functions to help with range handling.

.. versionadded:: 0.1.0
'''

import re


def parse_range_header(range):
    '''
    Parse a dojo.store range header.

    :rtype: dict
    '''
    match = re.match('^items=([0-9]+)-([0-9]+)$', range)
    if match:
        start = int(match.group(1))
        einde = int(match.group(2))
        if einde < start:
            einde = start
        return {
        'start': start,
        'einde': einde,
        'aantal': einde - start + 1
        }
    else:
        return False


def range_return(request, total):
    range = False
    if ('Range' in request.headers):
        range = request.headers['Range']
        range = parse_range_header(range)
        start = range['start']
        einde = range['einde']
        request.response.headers['Content-Range'] = 'items %d-%d/%d' % (start, einde, total)
    elif ('X-Range' in request.headers):
        range = request.headers['X-Range']
        range = range_header(range)
        start = range['start']
        einde = range['einde']
        request.response.headers['X-Content-Range'] = 'items %d-%d/%d' % (start, einde, total)
    else:
        start = int(request.params.get('start', 0))
        aantal = int(request.params.get('aantal', 10))
        einde = start + aantal
    return (start, einde)
