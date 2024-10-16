import logging
from collections.abc import Sequence

from pyramid.config import Configurator
from pyramid.settings import asbool


LOG = logging.getLogger(__name__)
GENERATE_ETAG_ROUTE_NAMES = set()


def add_route(config, name, pattern, *args, **kwargs):
    """
    Add a pyramid route to the config with etag tween support.

    All args and kwargs will be passed on to config.add_route.

    This exists so the default behaviour of including crabpy will still be to
    cache all crabpy routes.
    """
    config.add_route(name, pattern, *args, **kwargs)
    GENERATE_ETAG_ROUTE_NAMES.add(name)


def conditional_http_tween_factory(handler, registry):
    """
    Tween that automatically adds ETag headers enables conditional responses.
    """
    settings = registry.settings if hasattr(registry, "settings") else {}
    if "generate_etag_for.list" in settings:
        route_names = settings.get("generate_etag_for.list").split()
        GENERATE_ETAG_ROUTE_NAMES.update(route_names)

    def conditional_http_tween(request):
        response = handler(request)
        if request.matched_route is None:
            return response

        if request.matched_route.name in GENERATE_ETAG_ROUTE_NAMES:

            # If the Last-Modified header has been set, we want to enable the
            # conditional response processing.
            if response.last_modified is not None:
                response.conditional_response = True

            # We want to only enable the conditional machinery if either we
            # were given an explicit ETag header by the view or we have a
            # buffered response and can generate the ETag header ourself.
            if response.etag is not None:
                response.conditional_response = True
            elif (
                isinstance(response.app_iter, Sequence) and len(response.app_iter) == 1
            ) and response.body is not None:
                response.conditional_response = True
                response.md5_etag()

        return response

    return conditional_http_tween


def includeme(config: Configurator):
    """
    Include `crabpy_pyramid` in this `Pyramid` application.

    :param pyramid.config.Configurator config: A Pyramid configurator.
    """
    settings = config.registry.settings
    # http caching tween
    if not settings.get("etag_tween_disabled", False):
        config.add_tween("crabpy_pyramid.conditional_http_tween_factory")

    # capakey
    if "crabpy.capakey.include" in settings:
        LOG.info(
            "The 'capakey.include' setting is deprecated. Capakey will "
            "always be included."
        )
    config.include("crabpy_pyramid.capakey")

    # adressenregister
    if "crabpy.adressenregister.include" in settings:
        if asbool(settings["crabpy.adressenregister.include"]):
            config.include("crabpy_pyramid.adressenregister")


def main(global_config, **settings):
    """Create a Pyramid WSGI application."""
    config = Configurator(settings=settings)

    includeme(config)
    return config.make_wsgi_app()
