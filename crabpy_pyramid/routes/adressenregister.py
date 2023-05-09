import crabpy_pyramid


def includeme(config):
    crabpy_pyramid.add_route(
        config, "adressenregister_list_gewesten", "/adressenregister/gewesten"
    )
    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_gewest_by_niscode",
        "/adressenregister/gewesten/{gewest_niscode}",
    )

    crabpy_pyramid.add_route(
        config,
        "adressenregister_list_provincies",
        "/adressenregister/gewesten/{gewest_niscode}/provincies",
    )
    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_provincie",
        "/adressenregister/provincies/{provincie_niscode}",
    )
    crabpy_pyramid.add_route(
        config,
        "adressenregister_list_deelgemeenten",
        "/adressenregister/gewesten/{gewest_niscode}/deelgemeenten",
    )
    crabpy_pyramid.add_route(
        config,
        "adressenregister_list_deelgemeenten_by_gemeente",
        "/adressenregister/gemeenten/{niscode}/deelgemeenten",
    )
    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_deelgemeente_by_id",
        "/adressenregister/deelgemeenten/{deelgemeente_niscode}",
    )

    crabpy_pyramid.add_route(
        config,
        "adressenregister_list_gemeenten_by_provincie",
        "/adressenregister/provincies/{provincie_niscode}/gemeenten",
    )
    crabpy_pyramid.add_route(
        config,
        "list_gemeenten_adressenregister",
        "/adressenregister/gewesten/{gewest_niscode}/gemeenten",
    )

    crabpy_pyramid.add_route(
        config, "get_gemeente_adressenregister", "/adressenregister/gemeenten/{niscode}"
    )

    crabpy_pyramid.add_route(
        config,
        "adressenregister_list_straten",
        "/adressenregister/gemeenten/{niscode}/straten",
    )

    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_straat_by_id",
        "/adressenregister/straten/{straat_id}",
    )

    crabpy_pyramid.add_route(
        config,
        "adressenregister_list_adressen",
        "/adressenregister/straten/{straat_id}/adressen",
    )

    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_adres_by_straat_and_huisnummer",
        "/adressenregister/straten/{straat_id}/huisnummers/{huisnummer}",
    )

    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_adres_by_straat_and_huisnummer_and_busnummer",
        "/adressenregister/straten/{straat_id}/huisnummers/{huisnummer}/busnummers/{busnummer}",
    )

    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_adres_by_id",
        "/adressenregister/adressen/{adres_id}",
    )

    crabpy_pyramid.add_route(
        config,
        "adressenregister_list_percelen_by_adres",
        "/adressenregister/adressen/{adres_id}/percelen",
    )
    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_perceel_by_id",
        "/adressenregister/percelen/{perceel_id}",
    )
    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_perceel_by_id_parts",
        "/adressenregister/percelen/{perceel_id_part1}/{perceel_id_part2}",
    )
    crabpy_pyramid.add_route(
        config,
        "adressenregister_list_postinfo_by_gemeente",
        "/adressenregister/gemeenten/{gemeente_naam_niscode}/postinfo",
    )
    crabpy_pyramid.add_route(
        config,
        "adressenregister_get_postinfo_by_postcode",
        "/adressenregister/postinfo/{postcode}",
    )

    crabpy_pyramid.add_route(
        config, "adressenregister_list_landen", "/adressenregister/landen"
    )
    crabpy_pyramid.add_route(
        config, "adressenregister_get_land_by_id", "/adressenregister/landen/{land_id}"
    )
