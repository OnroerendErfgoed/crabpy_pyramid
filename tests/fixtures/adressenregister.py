gemeenten = {
    "@context": "https://docs.basisregisters.vlaanderen.be/context"
    "/gemeente/2023-02-28/gemeente_lijst.jsonld",
    "gemeenten": [
        {
            "@type": "Gemeente",
            "identificator": {
                "id": "https://data.vlaanderen.be/id/gemeente/11001",
                "naamruimte": "https://data.vlaanderen.be/id/gemeente",
                "objectId": "11001",
                "versieId": "2002-08-13T16:33:18+02:00",
            },
            "detail": "https://api.basisregisters.vlaanderen.be/v2/gemeenten/11001",
            "gemeentenaam": {
                "geografischeNaam": {"spelling": "Aartselaar", "taal": "nl"}
            },
            "gemeenteStatus": "inGebruik",
        }
    ],
}

gemeente = {
    "@context": "https://docs.basisregisters.vlaanderen.be/context/gemeente"
    "/2023-02-28/gemeente_detail.jsonld",
    "@type": "Gemeente",
    "identificator": {
        "id": "https://data.vlaanderen.be/id/gemeente/11001",
        "naamruimte": "https://data.vlaanderen.be/id/gemeente",
        "objectId": "11001",
        "versieId": "2002-08-13T16:33:18+02:00",
    },
    "officieleTalen": ["nl"],
    "faciliteitenTalen": [],
    "gemeentenamen": [{"spelling": "Aartselaar", "taal": "nl"}],
    "gemeenteStatus": "inGebruik",
}

straten = {
    "@context": "https://docs.basisregisters.vlaanderen.be/context/straatnaam"
    "/2023-02-28/straatnaam_lijst.jsonld",
    "straatnamen": [
        {
            "@type": "Straatnaam",
            "identificator": {
                "id": "https://data.vlaanderen.be/id/straatnaam/1",
                "naamruimte": "https://data.vlaanderen.be/id/straatnaam",
                "objectId": "1",
                "versieId": "2011-04-29T13:34:14+02:00",
            },
            "detail": "https://api.basisregisters.vlaanderen.be/v2/straatnamen/1",
            "straatnaam": {
                "geografischeNaam": {"spelling": "Acacialaan", "taal": "nl"}
            },
            "straatnaamStatus": "inGebruik",
        },
        {
            "@type": "Straatnaam",
            "identificator": {
                "id": "https://data.vlaanderen.be/id/straatnaam/2",
                "naamruimte": "https://data.vlaanderen.be/id/straatnaam",
                "objectId": "2",
                "versieId": "2011-04-29T13:34:14+02:00",
            },
            "detail": "https://api.basisregisters.vlaanderen.be/v2/straatnamen/2",
            "straatnaam": {
                "geografischeNaam": {"spelling": "Adriaan Sanderslei", "taal": "nl"}
            },
            "straatnaamStatus": "inGebruik",
        },
    ],
}

straat = {
    "@context": (
        "https://docs.basisregisters.vlaanderen.be/context/straatnaam/2023-02-28"
        "/straatnaam_detail.jsonld"
    ),
    "@type": "Straatnaam",
    "identificator": {
        "id": "https://data.vlaanderen.be/id/straatnaam/1",
        "naamruimte": "https://data.vlaanderen.be/id/straatnaam",
        "objectId": "1",
        "versieId": "2011-04-29T13:34:14+02:00",
    },
    "gemeente": {
        "objectId": "11001",
        "detail": "https://api.basisregisters.vlaanderen.be/v2/gemeenten/11001",
        "gemeentenaam": {"geografischeNaam": {"spelling": "Aartselaar", "taal": "nl"}},
    },
    "straatnamen": [{"spelling": "Acacialaan", "taal": "nl"}],
    "homoniemToevoegingen": [],
    "straatnaamStatus": "inGebruik",
}

adressen = {
    "@context": "https://docs.basisregisters.vlaanderen.be/context/adres/2023-02-28"
    "/adres_lijst.jsonld",
    "adressen": [
        {
            "@type": "Adres",
            "identificator": {
                "id": "https://data.vlaanderen.be/id/adres/307106",
                "naamruimte": "https://data.vlaanderen.be/id/adres",
                "objectId": "307106",
                "versieId": "2011-04-29T14:50:10+02:00",
            },
            "detail": "https://api.basisregisters.vlaanderen.be/v2/adressen/307106",
            "huisnummer": "4",
            "volledigAdres": {
                "geografischeNaam": {
                    "spelling": "Acacialaan 4, 2630 Aartselaar",
                    "taal": "nl",
                }
            },
            "adresStatus": "inGebruik",
        },
        {
            "@type": "Adres",
            "identificator": {
                "id": "https://data.vlaanderen.be/id/adres/364340",
                "naamruimte": "https://data.vlaanderen.be/id/adres",
                "objectId": "364340",
                "versieId": "2011-04-29T14:50:10+02:00",
            },
            "detail": "https://api.basisregisters.vlaanderen.be/v2/adressen/364340",
            "huisnummer": "11",
            "busnummer": "1",
            "volledigAdres": {
                "geografischeNaam": {
                    "spelling": "Acacialaan 11, 2630 Aartselaar",
                    "taal": "nl",
                }
            },
            "adresStatus": "inGebruik",
        },
    ],
}

adres = {
    "@context": "https://docs.basisregisters.vlaanderen.be/context/adres"
    "/2023-02-28/adres_detail.jsonld",
    "@type": "Adres",
    "identificator": {
        "id": "https://data.vlaanderen.be/id/adres/900746",
        "naamruimte": "https://data.vlaanderen.be/id/adres",
        "objectId": "900746",
        "versieId": "2016-12-19T15:23:28+01:00",
    },
    "gemeente": {
        "objectId": "44021",
        "detail": "https://api.basisregisters.vlaanderen.be/v2/gemeenten/44021",
        "gemeentenaam": {"geografischeNaam": {"spelling": "Gent", "taal": "nl"}},
    },
    "postinfo": {
        "objectId": "9000",
        "detail": "https://api.basisregisters.vlaanderen.be/v2/postinfo/9000",
    },
    "straatnaam": {
        "objectId": "71608",
        "detail": "https://api.basisregisters.vlaanderen.be/v2/straatnamen/71608",
        "straatnaam": {"geografischeNaam": {"spelling": "Sint-Jansvest", "taal": "nl"}},
    },
    "huisnummer": "50",
    "volledigAdres": {
        "geografischeNaam": {"spelling": "Sint-Jansvest 50, 9000 Gent", "taal": "nl"}
    },
    "adresPositie": {
        "geometrie": {
            "type": "Point",
            "gml": '<gml:Point srsName="https://www.opengis.net/def/crs/EPSG/0/31370" '
            'xmlns:gml="http://www.opengis.net/gml/3.2"><gml:pos>105052.34 '
            "193542.11</gml:pos></gml:Point>",
        },
        "positieGeometrieMethode": "aangeduidDoorBeheerder",
        "positieSpecificatie": "perceel",
    },
    "adresStatus": "inGebruik",
    "officieelToegekend": True,
}

percelen = {
    "@context": "https://docs.basisregisters.vlaanderen.be/context/perceel"
    "/2023-02-28/perceel_lijst.jsonld",
    "percelen": [
        {
            "@type": "Perceel",
            "identificator": {
                "id": "https://data.vlaanderen.be/id/perceel/13013C0384-02H003",
                "naamruimte": "https://data.vlaanderen.be/id/perceel",
                "objectId": "13013C0384-02H003",
                "versieId": "2004-02-13T05:34:17+01:00",
            },
            "detail": (
                "https://api.basisregisters.vlaanderen.be/v2/percelen/13013C0384-02H003"
            ),
            "perceelStatus": "gerealiseerd",
        }
    ],
}

perceel = {
    "@context": "https://docs.basisregisters.vlaanderen.be/context/perceel"
    "/2023-02-28/perceel_detail.jsonld",
    "@type": "Perceel",
    "identificator": {
        "id": "https://data.vlaanderen.be/id/perceel/13013C0384-02H003",
        "naamruimte": "https://data.vlaanderen.be/id/perceel",
        "objectId": "13013C0384-02H003",
        "versieId": "2004-02-13T05:34:17+01:00",
    },
    "perceelStatus": "gerealiseerd",
    "adressen": [
        {
            "objectId": "200001",
            "detail": "https://api.basisregisters.vlaanderen.be/v2/adressen/200001",
        }
    ],
}

postinfos = {
    "@context": "https://docs.basisregisters.vlaanderen.be/context"
    "/postinfo/2023-02-28/postinfo_lijst.jsonld",
    "postInfoObjecten": [
        {
            "@type": "PostInfo",
            "identificator": {
                "id": "https://data.vlaanderen.be/id/postinfo/1000",
                "naamruimte": "https://data.vlaanderen.be/id/postinfo",
                "objectId": "1000",
                "versieId": "2020-02-10T12:44:14+01:00",
            },
            "detail": "https://api.basisregisters.vlaanderen.be/v2/postinfo/1000",
            "postInfoStatus": "gerealiseerd",
            "postnamen": [{"geografischeNaam": {"spelling": "BRUSSEL", "taal": "nl"}}],
        },
        {
            "@type": "PostInfo",
            "identificator": {
                "id": "https://data.vlaanderen.be/id/postinfo/1020",
                "naamruimte": "https://data.vlaanderen.be/id/postinfo",
                "objectId": "1020",
                "versieId": "2020-02-10T12:44:14+01:00",
            },
            "detail": "https://api.basisregisters.vlaanderen.be/v2/postinfo/1020",
            "postInfoStatus": "gerealiseerd",
            "postnamen": [{"geografischeNaam": {"spelling": "Laken", "taal": "nl"}}],
        },
    ],
}

postinfo_1000 = {
    "@context": "https://docs.basisregisters.vlaanderen.be/context"
    "/postinfo/2023-02-28/postinfo_detail.jsonld",
    "@type": "PostInfo",
    "identificator": {
        "id": "https://data.vlaanderen.be/id/postinfo/1000",
        "naamruimte": "https://data.vlaanderen.be/id/postinfo",
        "objectId": "1000",
        "versieId": "2020-02-10T12:44:14+01:00",
    },
    "gemeente": {
        "objectId": "21004",
        "detail": "https://api.basisregisters.vlaanderen.be/v2/gemeenten/21004",
        "gemeentenaam": {"geografischeNaam": {"spelling": "Brussel", "taal": "nl"}},
    },
    "postnamen": [{"geografischeNaam": {"spelling": "BRUSSEL", "taal": "nl"}}],
    "postInfoStatus": "gerealiseerd",
}
postinfo_1020 = {
    "@context": (
        "https://docs.basisregisters.vlaanderen.be/context/postinfo/2023-02-28/postinfo_detail.jsonld"
    ),
    "@type": "PostInfo",
    "identificator": {
        "id": "https://data.vlaanderen.be/id/postinfo/1020",
        "naamruimte": "https://data.vlaanderen.be/id/postinfo",
        "objectId": "1020",
        "versieId": "2020-02-10T12:44:14+01:00",
    },
    "gemeente": {
        "objectId": "21004",
        "detail": "https://api.basisregisters.vlaanderen.be/v2/gemeenten/21004",
        "gemeentenaam": {"geografischeNaam": {"spelling": "Brussel", "taal": "nl"}},
    },
    "postnamen": [{"geografischeNaam": {"spelling": "Laken", "taal": "nl"}}],
    "postInfoStatus": "gerealiseerd",
}
