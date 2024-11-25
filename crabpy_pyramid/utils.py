"""
Utility functions to help with range handling.

.. versionadded:: 0.1.0
"""

import re
from typing import Literal
from typing import Sequence


MAX_NUMBER_ITEMS = 5000


def parse_range_header(range) -> dict[str, int] | Literal[False]:
    """
    Parse a range header as used by the dojo Json Rest store.

    :param str range: The content of the range header to be parsed.
        eg. `items=0-9`
    :returns: A dict with keys start, finish and number or `False` if the
        range is invalid.
    """
    match = re.match("^items=([0-9]+)-([0-9]+)$", range)

    if match:
        start = int(match.group(1))
        finish = int(match.group(2))

        if finish < start:
            finish = start
        return {"start": start, "finish": finish, "count": finish - start + 1}
    else:
        return False


def range_return(request, items: Sequence):
    """
    Determine what range of objects to return.

    Will check fot both `Range` and `X-Range` headers in the request and
    set both `Content-Range` and 'X-Content-Range' headers.

    :rtype: list
    """
    if "Range" in request.headers:
        range = parse_range_header(request.headers["Range"])
        if not range:
            raise ValueError(request.headers["Range"])
    elif "X-Range" in request.headers:
        range = parse_range_header(request.headers["X-Range"])
        if not range:
            raise ValueError(request.headers["X-Range"])
    else:
        range = {"start": 0, "finish": MAX_NUMBER_ITEMS - 1, "count": MAX_NUMBER_ITEMS}
    filtered = items[range["start"] : range["finish"] + 1]
    if len(filtered) < range["count"]:
        # Something was stripped, deal with it
        range["count"] = len(filtered)
        range["finish"] = range["start"] + range["count"] - 1
    if range["finish"] - range["start"] + 1 >= MAX_NUMBER_ITEMS:
        range["finish"] = range["start"] + MAX_NUMBER_ITEMS - 1
        filtered = items[range["start"] : range["finish"] + 1]

    request.response.headers["Content-Range"] = "items %d-%d/%d" % (
        range["start"],
        range["finish"],
        len(items),
    )
    request.response.headers["X-Content-Range"] = request.response.headers[
        "Content-Range"
    ]
    return filtered


def set_http_caching(request, gateway="crab", region="permanent"):
    """
    Set an HTTP Cache Control header on a request.

    :param pyramid.request.Request request: Request to set headers on.
    :param str gateway: What gateway are we caching for? Defaults to `crab`.
    :param str region: What caching region to use? Defaults to `permanent`.
    :rtype: pyramid.request.Request
    """
    crabpy_exp = request.registry.settings.get(
        "crabpy.%s.cache_config.%s.expiration_time" % (gateway, region), None
    )
    if crabpy_exp is None:
        return request
    ctime = int(int(crabpy_exp) * 1.05)
    request.response.cache_expires(ctime, public=True)
    return request


def filter_settings(settings, prefix):
    """
    Filter all settings to only return settings that start with a certain
    prefix.

    :param dict settings: A settings dictionary.
    :param str prefix: A prefix.
    """
    ret = {}
    for skey in settings.keys():
        if skey.startswith(prefix):
            key = skey[len(prefix) :]
            ret[key] = settings[skey]
    return ret
