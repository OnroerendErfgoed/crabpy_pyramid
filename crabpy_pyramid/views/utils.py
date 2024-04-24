import inspect

from crabpy.client import AdressenRegisterClientException
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotFound


def handle_gateway_response(gateway_method, *args, **kwargs):
    try:
        result = gateway_method(*args, **kwargs)
        if not result and not isinstance(result, list):
            raise HTTPNotFound()
        return result
    except AdressenRegisterClientException as ae:
        cause = ae.__cause__
        if hasattr(cause, "response"):
            status_code = cause.response.status_code
            if status_code == 404:
                raise HTTPNotFound()
            if status_code == 400:
                detail = getattr(cause.response, "text", "")
                raise HTTPBadRequest(detail=detail)
        raise ae


def extract_valid_params(method, request):
    """
    Extract valid parameters from a method signature and request.

    :param method: the method to extract param names from
    :param request: the request object to extract param values from
    """
    signature = inspect.signature(method)
    parameters = signature.parameters
    kwargs_names = [
        param.name for param in parameters.values() if
        (
            param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
            or param.kind == inspect.Parameter.KEYWORD_ONLY
        )
    ]

    return {
        name: request.params.get(name)
        for name in kwargs_names
        if request.params.get(name)
    }
