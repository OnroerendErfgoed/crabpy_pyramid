import logging
import sys

from crabpy.client import AdressenRegisterClientException
from pyramid.view import view_config

LOGGER = logging.getLogger(__name__)

@view_config(
    context=AdressenRegisterClientException,
    renderer="json",
    accept="application/json"
)
def internal_server_error(exception, request):
    LOGGER.exception(exception)
    original_exception = exception.__cause__
    request.response.status_int = 500
    errors = [str(original_exception)]

    return {
        "message": "Er ging iets fout in de vraag naar adressenregister API.",
        "Errors": errors

    }
