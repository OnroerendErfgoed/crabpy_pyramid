.. _services:

========
Services
========

Crabpy_pyramid exposes the following services if both
:ref:`setting-capakey-include` and :ref:`setting-crab-include` are set to `True`.

Capakey
=======

.. http:get:: /capakey/gemeenten

    List all gemeenten

    **Example request**:

    .. sourcecode:: http

       GET /capakey/gemeenten HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json
       Range: items=0-4

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json
       Content-Range: 0-4/306

       [
        {
           'id': 44001,
           'naam': 'Aalter'
        }, {
           'id': 44011,
           'naam': 'Deinze'
        }, {
           'id': 44012,
           'naam': 'De Pinte'
        }, {
           'id': 44013,
           'naam': 'Destelbergen'
        }, {
           'id': 4401,
           'naam': 'Gent',
        }
       ]

    :reqheader Range: Can be used to ask for a certain set of results,
        eg. ``ìtems=0-24`` asks for the first 25 items.
    :resheader Content-Range: Tells the client what range of results is
        being returned, eg. ``items=0-24/306`` for the first 25 items out of 306.
    :statuscode 200: Gemeenten were found.

.. http:get:: /capakey/gemeenten/(int:gemeente_id)

    Get a gemeente by id

    **Example request**:

    .. sourcecode:: http

       GET /capakey/gemeenten/44021 HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

       {
          'id': 44021,
          'naam': 'Gent',
          'centroid': [104154.2225, 197300.703],
          'bbox': [94653.453, 185680.984, 113654.992, 208920.422]
       }

    :statuscode 200: Gemeente was found.
    :statuscode 404: Gemeente was not found.

.. http:get:: /capakey/gemeenten/(int:gemeente_id)/afdelingen

    List_kadastrale_afdelingen_by_gemeente

    **Example request**:

    .. sourcecode:: http

       GET /capakey/gemeenten/44021/afdelingen HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json
       Range: 0-1

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json
       Content-Range: 0-1/30

       [
        {
           'id': 44002,
           'naam': 'Afsnee',
           'gemeente': {
                'id': 44021,
                'naam': 'Gent'
           }
        }, {
           'id': 44017,
           'naam': 'Drongen',
           'gemeente': {
                'id': 44021,
                'naam': 'Gent'
           }
        }
       ]


    :reqheader Range: Can be used to ask for a certain set of results,
        eg. ``ìtems=0-24`` asks for the first 25 items.
    :resheader Content-Range: Tells the client what range of results is
        being returned, eg. ``items=0-9/30`` for the first 10 items out of 30.
    :statuscode 200: Gemeente was found.
    :statuscode 404: Gemeente was not found.

.. http:get:: /capakey/afdelingen

    List_kadastrale_afdelingen

    **Example request**:

    .. sourcecode:: http

       GET /capakey/afdelingen HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json
       Range: 0-1

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json
       Content-Range: 0-1/1433

            [
                {
                   "id": 44002,
                   "naam": "Afsnee",
                   "gemeente": {
                        "id": 44021,
                        "naam": "Gent"
                   }
                }, {
                   "id": 44017,
                   "naam": "Drongen",
                   "gemeente": {
                        "id": 44021,
                        "naam": "Gent"
                   }
                }
            ]

    :reqheader Range: Can be used to ask for a certain set of results,
        eg. ``ìtems=0-24`` asks for the first 25 items.
    :resheader Content-Range: Tells the client what range of results is
        being returned, eg. ``items=0-99/1433`` for the first 100 items out of 1433.
    :statuscode 200: Afdelingen were found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)

    Get_kadastrale_afdeling_by_id

    **Example request**:

    .. sourcecode:: http

       GET /capakey/afdelingen/44017 HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

           {
               "id": 44017,
               "naam": "Drongen",
               "gemeente": {
                    "id": 44021,
                    "naam": "Gent"
               },
               "centroid": [104154.2225, 197300.703],
               "bbox": [94653.453, 185680.984, 113654.992, 208920.422]
           }

    :statuscode 200: Afdeling was found.
    :statuscode 404: Afdeling was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties

    List_secties_by_afdeling

    **Example request**:

    .. sourcecode:: http

       GET /capakey/afdelingen/44017/secties HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json


    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

        [
          {
            "afdeling": {
              "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
              "id": 44017,
              "gemeente": {
                "naam": "Gent",
                "id": 44021
              }
            },
            "id": "A"
          },
          {
            "afdeling": {
              "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
              "id": 44017,
              "gemeente": {
                "naam": "Gent",
                "id": 44021
              }
            },
            "id": "B"
          },
          {
            "afdeling": {
              "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
              "id": 44017,
              "gemeente": {
                "naam": "Gent",
                "id": 44021
              }
            },
            "id": "C"
          },
          {
            "afdeling": {
              "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
              "id": 44017,
              "gemeente": {
                "naam": "Gent",
                "id": 44021
              }
            },
            "id": "D"
          }
        ]


    :statuscode 200: Afdeling was found.
    :statuscode 404: Afdeling was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)

    Get_sectie_by_id_and_afdeling

    **Example request**:

    .. sourcecode:: http

       GET /capakey/afdelingen/44017/secties/A HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json



    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

       {
          "afdeling": {
            "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
            "bounding_box": [
              94653.7508750036,
              190442.133125,
              101151.588,
              197371.0951875
            ],
            "centroid": [
              97902.6694375016,
              193906.61415625
            ],
            "id": 44017,
            "gemeente": {
              "naam": "Gent",
              "bounding_box": [
                94653.4530000016,
                185680.984000001,
                113654.991999999,
                208920.421999998
              ],
              "centroid": [
                104154.2225,
                197300.703
              ],
              "id": 44021
            }
          },
          "bounding_box": [
            96205.7660000026,
            194208.691374999,
            101032.139624998,
            197371.0951875
          ],
          "centroid": [
            98618.9528125003,
            195789.893281249
          ],
          "id": "A"
        }


    :statuscode 200: Sectie was found.
    :statuscode 404: Sectie was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)/percelen

    List_percelen_by_sectie

    **Example request**:

    .. sourcecode:: http

       GET /capakey/afdelingen/44017/secties/A/percelen HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json
       Range: 0-4


    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

       [
          {
            "capakey": "44017A0003/00C000",
            "id": "0003/00C000",
            "percid": "44017_A_0003_C_000_00",
            "sectie": {
              "afdeling": {
                "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
                "id": 44017,
                "gemeente": {
                  "naam": "Gent",
                  "id": 44021
                }
              },
              "id": "A"
            }
          },
          {
            "capakey": "44017A0004/00D000",
            "id": "0004/00D000",
            "percid": "44017_A_0004_D_000_00",
            "sectie": {
              "afdeling": {
                "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
                "id": 44017,
                "gemeente": {
                  "naam": "Gent",
                  "id": 44021
                }
              },
              "id": "A"
            }
          },
          {
            "capakey": "44017A0004/00F000",
            "id": "0004/00F000",
            "percid": "44017_A_0004_F_000_00",
            "sectie": {
              "afdeling": {
                "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
                "id": 44017,
                "gemeente": {
                  "naam": "Gent",
                  "id": 44021
                }
              },
              "id": "A"
            }
          },
          {
            "capakey": "44017A0004/00G000",
            "id": "0004/00G000",
            "percid": "44017_A_0004_G_000_00",
            "sectie": {
              "afdeling": {
                "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
                "id": 44017,
                "gemeente": {
                  "naam": "Gent",
                  "id": 44021
                }
              },
              "id": "A"
            }
          },
          {
            "capakey": "44017A0006/00A000",
            "id": "0006/00A000",
            "percid": "44017_A_0006_A_000_00",
            "sectie": {
              "afdeling": {
                "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
                "id": 44017,
                "gemeente": {
                  "naam": "Gent",
                  "id": 44021
                }
              },
              "id": "A"
            }
          }
        ]

    :reqheader Range: Can be used to ask for a certain set of results,
        eg. ``ìtems=0-5`` asks for the first 6 items.
    :resheader Content-Range: Tells the client what range of results is
        being returned, eg. ``items=0-5/145`` for the first 6 items out of 145.
    :statuscode 200: Sectie was found.
    :statuscode 404: Sectie was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)/percelen/(int:perceel_id)

    Get_perceel_by_sectie_and_id

    **Example request**:

    .. sourcecode:: http

       GET /capakey/afdelingen/44017/secties/A/percelen/452 HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json


    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

       {
          "percid": "44017_A_0003_C_000_00",
          "sectie": {
            "afdeling": {
              "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
              "id": 44017,
              "gemeente": {
                "naam": "Gent",
                "id": 44021
              }
            },
            "id": "A"
          },
          "capakey": "44017A0003/00C000",
          "bounding_box": [
            98798.1679999977,
            197135.57,
            98989.2730000019,
            197356.498
          ],
          "centroid": [
            98893.7204999998,
            197246.034
          ],
          "id": "0003/00C000"
       }


    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

.. http:get:: /capakey/percelen/(string:capakey1)/(string:capakey2)

    Get Perceel_by_capakey

    **Example request**:

    .. sourcecode:: http

       GET /capakey/percelen/44021A3675/00A000 HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

       {
        "percid": "44021_A_3675_A_000_00",
        "sectie": {
          "afdeling": {
            "naam": "GENT  1 AFD",
            "bounding_box": [
              104002.076624997,
              194168.341499999,
              105784.050875001,
              197876.1466875
            ],
            "centroid": [
              104893.063749999,
              196022.24409375
            ],
            "id": 44021,
            "gemeente": {
              "naam": "Gent",
              "bounding_box": [
                94653.4530000016,
                185680.984000001,
                113654.991999999,
                208920.421999998
              ],
              "centroid": [
                104154.2225,
                197300.703
              ],
              "id": 44021
            }
          },
          "bounding_box": [
            104002.076624997,
            194168.341499999,
            105784.050875001,
            197876.1466875
          ],
          "centroid": [
            104893.063749999,
            196022.24409375
          ],
          "id": "A"
        },
        "capakey": "44021A3675/00A000",
        "bounding_box": [
          105182.648999996,
          197425.741999999,
          105199.199000001,
          197454.061999999
        ],
        "centroid": [
          105190.923999999,
          197439.901999999
        ],
        "id": "3675/00A000"
       }


    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

.. http:get:: /capakey/percelen/(string:percid)

    Get_perceel_by_percid

    **Example request**:

    .. sourcecode:: http

       GET /capakey/percelen/44017_A_0004_D_000_00 HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json


    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json


       {
          "percid": "44017_A_0004_D_000_00",
          "sectie": {
            "afdeling": {
              "naam": "GENT 27 AFD/DRONGEN  1 AFD/",
              "bounding_box": [
                94653.7508750036,
                190442.133125,
                101151.588,
                197371.0951875
              ],
              "centroid": [
                97902.6694375016,
                193906.61415625
              ],
              "id": 44017,
              "gemeente": {
                "naam": "Gent",
                "bounding_box": [
                  94653.4530000016,
                  185680.984000001,
                  113654.991999999,
                  208920.421999998
                ],
                "centroid": [
                  104154.2225,
                  197300.703
                ],
                "id": 44021
              }
            },
            "bounding_box": [
              96205.7660000026,
              194208.691374999,
              101032.139624998,
              197371.0951875
            ],
            "centroid": [
              98618.9528125003,
              195789.893281249
            ],
            "id": "A"
          },
          "capakey": "44017A0004/00D000",
          "bounding_box": [
            98800.686999999,
            197101.388,
            98857.4720000029,
            197133.022
          ],
          "centroid": [
            98829.0795000009,
            197117.205
          ],
          "id": "0004/00D000"
        }

    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

Crab
====

.. http:get:: /crab/gewesten

    List_gewesten

    **Example request**:

    .. sourcecode:: http

        GET /crab/gewesten HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "naam": "Brussels Hoofdstedelijk Gewest",
                "id": 1
            }, {
                "naam": "Vlaams Gewest",
                "id": 2
            }, {
                "naam": "Waals Gewest",
                "id": 3
            }
        ]

    :statuscode 200: Gewesten were found.

.. http:get:: /crab/gewesten/(int:gewest_id)

    Get_gewest_by_id

    **Example request**:

    .. sourcecode:: http

        GET /crab/gewesten/2 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json



    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
          "namen": {
            "fr": "Région flamande",
            "de": "Die Flämische Region",
            "nl": "Vlaams Gewest"
          },
          "bounding_box": [
            22279.17,
            153050.23,
            258873.3,
            244022.31
          ],
          "centroid": [
            138165.09,
            189297.53
          ],
          "id": 2
        }

    :statuscode 200: Gewest was found.
    :statuscode 404: Gewest was not found.

.. http:get:: /crab/gewesten/(int:gewest_id)/provincies

    Retrieve alle provincies in a gewest.

    **Example request**:

    .. sourcecode:: http

        GET /crab/gewesten/2/provincies HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json
        Content-Range: items 0-4/5

        [
            {
                "naam": "Antwerpen",
                "gewest": {"naam": "Vlaams Gewest", "id": 2},
                "niscode": 10000
            }, {
                "naam": "Vlaams-Brabant",
                "gewest": {"naam": "Vlaams Gewest", "id": 2},
                "niscode": 20001
            }, {
                "naam": "West-Vlaanderen",
                "gewest": {"naam": "Vlaams Gewest", "id": 2},
                "niscode": 30000
            }, {
                "naam": "Oost-Vlaanderen",
                "gewest": {"naam": "Vlaams Gewest", "id": 2},
                "niscode": 40000
            }, {
                "naam": "Limburg",
                "gewest": {"naam": "Vlaams Gewest", "id": 2},
                "niscode": 70000
            }
        ]

    :statuscode 200: Gewest was found.
    :statuscode 404: Gewest does not exist.

.. http:get:: /crab/provincies/(int:provincie_id)

    Get information about a certain provincie.

    **Example request**:

    .. sourcecode:: http

        GET /crab/provincies/30000 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "naam": "West-Vlaanderen",
            "gewest": {"naam": "Vlaams Gewest", "id": 2},
            "niscode": 30000
        }

    :statuscode 200: Provincie was found.
    :statuscode 404: Provincie was not found.

.. http:get:: /crab/gewesten/(int:gewest_id)/gemeenten

    List all gemeenten in a certain gewest.

    **Example request**:

    .. sourcecode:: http

        GET /crab/gewesten/2/gemeenten HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        Range: items=0-4


    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json


        [
          {
            "naam": "Aartselaar",
            "id": 1
          },
          {
            "naam": "Antwerpen",
            "id": 2
          },
          {
            "naam": "Boechout",
            "id": 3
          },
          {
            "naam": "Boom",
            "id": 4
          },
          {
            "naam": "Borsbeek",
            "id": 5
          }
        ]

    :query sort: One of ``id``, ``naam`` or ``niscode`` (default).
    :statuscode 200: Gemeenten were found.
    :statuscode 404: Gewest does not exist.

.. http:get:: /crab/provincies/(int:provincie_id)/gemeenten

    List all gemeenten in a certain provincie.

    **Example request**:

    .. sourcecode:: http

        GET /crab/provincies/30000/gemeenten HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
          {
            "naam": "Beernem",
            "id": 182
          },
          {
            "naam": "Blankenberge",
            "id": 183
          },
          {
            "naam": "Brugge",
            "id": 184
          },
          {
            "naam": "Damme",
            "id": 185
          },
          {
            "naam": "Jabbeke",
            "id": 186
          }
        ]

    :statuscode 200: Gemeenten were found.
    :statuscode 404: Provincie does not exist.

.. http:get:: /crab/gemeenten/(int:id of int:niscode)

    Get_gemeente_by_id

    **Example request**:

    .. sourcecode:: http

        GET /crab/gemeenten/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json


    Get_gemeente_by_niscode

    **Example request**:

    .. sourcecode:: http

        GET /crab/gemeenten/11001 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json


    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
          "naam": "Aartselaar",
          "bounding_box": [
            148950.36,
            199938.28,
            152811.77,
            204575.39
          ],
          "centroid": [
            150881.07,
            202256.84
          ],
          "id": 1,
          "metadata": {
            "begin_tijd": "2002-08-13 17:32:32",
            "begin_datum": "1830-01-01 00:00:00",
            "begin_organisatie": {
              "naam": "NGI",
              "definitie": "Nationaal Geografisch Instituut.",
              "id": "6"
            },
            "begin_bewerking": {
              "naam": "invoer",
              "definitie": "Invoer in de databank.",
              "id": "1"
            }
          }
        }

    :statuscode 200: Gemeente was found.
    :statuscode 404: Gemeente was not found.

.. http:get:: /crab/gewesten/(int:gewest_id)/deelgemeenten

    List all deelgemeenten in a certain gewest.

    **Example request**:

    .. sourcecode:: http

        GET /crab/gewesten/2/deelgemeenten HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        Range: items=0-4


    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "naam": "Sint-Joris-Winge",
                "id": "24135C"
            }, {
                "naam": "Meensel-Kiezegem",
                "id": "24135B"
            }, {
                "naam": "Tielt",
                "id": "24135A"
            }, {
                "naam": "Ertvelde",
                "id": "44019C"
            }, {
                "naam": "Kluizen", 
                "id": "44019D"
            }
        ]

    :statuscode 200: Deelgemeenten were found.
    :statuscode 404: Gewest does not exist.

.. http:get:: /crab/gemeenten/(int:gemeente_id or int:niscode)/deelgemeenten

    List all `deelgemeenten` in a certain `gemeente`.

    **Example request**:

    .. sourcecode:: http

        GET /crab/gemeenten/90/deelgemeenten HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example request**:

    .. sourcecode:: http

        GET /crab/gemeenten/11002/deelgemeenten HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json
        [
            {"naam": "Asse", "id": "23002A"},
            {"naam": "Kobbegem", "id": "23002C"},
            {"naam": "Mollem", "id": "23002B"},
            {"naam": "Zellik", "id": "23002E"},
            {"naam": "Relegem", "id": "23002D"},
            {"naam": "Bekkerzeel", "id": "23002F"}
        ]

    :statuscode 200: Deelgemeenten were found.
    :statuscode 404: The Gemeente for which you are requesting Deelgemeenten
        does not exist.

.. http:get:: /crab/deelgemeenten/(string:deelgemeente_id)

    Get all information on a certain `deelgemeente`.

    **Example request**:

    .. sourcecode:: http

        GET /crab/deelgemeenten/45062 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json
        {
            "naam": "Sint-Maria-Horebeke",
            "id": "45062A",
            "gemeente": {
                "id": 300,
                "naam": "Horebeke"
            }
        }

    :statuscode 200: Deelgemeente was found.
    :statuscode 404: The Deelgemeente does not exist.

.. http:get:: /crab/gemeenten/(int:gemeente_id)/postkantons

    List all `postkantons` in a certain `gemeente`.

    **Example request**:

    .. sourcecode:: http

        GET /crab/gemeenten/90/postkantons HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json
        [
            {"id": 1730},
            {"id": 1731}
        ]

    :statuscode 200: Postkantons were found.
    :statuscode 404: The Gemeente for which you are requesting Postkantons
        does not exist.

.. http:get:: /crab/gemeenten/(int:id of int:niscode)/straten

    List all straten in a `gemeente`.

    **Example request**:

    .. sourcecode:: http

            GET /crab/gemeenten/11001/straten HTTP/1.1
            Host: example.onroerenderfgoed.be
            Accept: application/json
            Range: items=0-4


    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 1,
            "label": "Acacialaan"
          },
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 2,
            "label": "Adriaan Sanderslei"
          },
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 3,
            "label": "Ahornelaan"
          },
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 4,
            "label": "Antoon van Brabantstraat"
          },
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 5,
            "label": "Antwerpsesteenweg"
          }
        ]

    :statuscode 200: Straat was found.

.. http:get:: /crab/straten/(int:straat_id)

    Get information on a `straat`, based on the `ID`.

    **Example request**:

    .. sourcecode:: http

        GET /crab/straten/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json


    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
          "status": {
            "naam": "inGebruik",
            "definitie": null,
            "id": "3"
          },
          "namen": [
            [
              "Acacialaan",
              "nl"
            ],
            [
              null,
              null
            ]
          ],
          "taal": {
            "naam": "Nederlands",
            "definitie": "Nederlands.",
            "id": "nl"
          },
          "label": "Acacialaan",
          "bounding_box": [
            "150339.255243488",
            "200079.666892901",
            "150812.200907812",
            "201166.401677653"
          ],
          "id": 1,
          "metadata": {
            "begin_tijd": "2013-04-12 20:07:25.960000",
            "begin_datum": "1830-01-01 00:00:00",
            "begin_organisatie": {
              "naam": "gemeente",
              "definitie": "Gemeente.",
              "id": "1"
            },
            "begin_bewerking": {
              "naam": "correctie",
              "definitie": "Correctie van de attributen.",
              "id": "3"
            }
          }
        }

    :statuscode 200: Straat was found.
    :statuscode 404: Straat was not found.

.. http:get:: /crab/straten/(int:straat_id)/huisnummers

    List all huisnummers in a `straat`.

    **Example request**:

    .. sourcecode:: http

        GET /crab/straten/1/huisnummers HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        Range: items=0-4

    **Example response**:

    .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

        [
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 78036,
            "label": "21"
          },
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 153134,
            "label": "4"
          },
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 221505,
            "label": "11"
          },
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 379090,
            "label": "23"
          },
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "3"
            },
            "id": 526418,
            "label": "13"
          }
        ]

    :statuscode 200: Huisnummers were found.

.. http:get:: /crab/straten/(int:straat_id)/huisnummers/(string:huisnummer_label)

    Get more information on a huisnummer by it's straat_id and it's huisnummer.

    **Example request**:

    .. sourcecode:: http

        GET /crab/straten/1/huisnummers/23 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
          "status": {
            "naam": "inGebruik",
            "definitie": null,
            "id": "3"
          },
          "bounding_box": [
            150786.11,
            200189.33,
            150786.11,
            200189.33
          ],
          "postadres": "Acacialaan 23, 2630 Aartselaar",
          "huisnummer": "23",
          "id": 379090,
          "metadata": {
            "begin_tijd": "2013-04-12 20:06:33.720000",
            "begin_datum": "1830-01-01 00:00:00",
            "begin_organisatie": {
              "naam": "gemeente",
              "definitie": "Gemeente.",
              "id": "1"
            },
            "begin_bewerking": {
              "naam": "correctie",
              "definitie": "Correctie van de attributen.",
              "id": "3"
            }
          }
        }

    :statuscode 200: Huisnummer was found.
    :statuscode 404: Huisnummer was not found.

.. http:get:: /crab/huisnummers/(int:huisnummer_id)

    Get more information on a huisnummer, based on an `ID`.

    **Example request**:

    .. sourcecode:: http

        GET /crab/huisnummers/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
          "status": {
            "naam": "inGebruik",
            "definitie": null,
            "id": "3"
          },
          "bounding_box": [
            190700.24,
            224649.87,
            190700.24,
            224649.87
          ],
          "huisnummer": "51",
          "postadres": "Steenweg op Oosthoven 51, 2300 Turnhout",
          "id": 1,
          "metadata": {
            "begin_tijd": "2014-03-19 17:00:27",
            "begin_datum": "1830-01-01 00:00:00",
            "begin_organisatie": {
              "naam": "gemeente",
              "definitie": "Gemeente.",
              "id": "1"
            },
            "begin_bewerking": {
              "naam": "correctie",
              "definitie": "Correctie van de attributen.",
              "id": "3"
            }
          }
        }

    :statuscode 200: Huisnummer was found.
    :statuscode 404: Huisnummer was not found.

.. http:get:: /crab/huisnummers/(int:huisnummer_id)/percelen

    List all `percelen` linked to  a certain `huisnummer`.

    **Example request**:

    .. sourcecode:: http

        GET /crab/huisnummers/1/percelen HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
          {
            "id": "13040C1747/00G002"
          }
        ]
    :statuscode 200: Percelen were found.

.. http:get:: /crab/percelen/(string:perceel_id1)/(string:perceel_id2)

    Get a perceel by it's id.

    **Example request**:

    .. sourcecode:: http

        GET /crab/percelen/13040C1747/00G002 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json


    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
          "centroid": [
            190708.59,
            224667.59
          ],
          "id": "13040C1747/00G002",
          "postadressen": [
            "Steenweg op Oosthoven 51, 2300 Turnhout",
            "Steenweg op Oosthoven 53, 2300 Turnhout"
          ],
          "metadata": {
            "begin_tijd": "2009-09-11 12:46:55.693000",
            "begin_datum": "1998-01-01 00:00:00",
            "begin_organisatie": {
              "naam": "AAPD",
              "definitie": "Algemene Administratie der Patrimoniumdocumentatie.",
              "id": "3"
            },
            "begin_bewerking": {
              "naam": "correctie",
              "definitie": "Correctie van de attributen.",
              "id": "3"
            }
          }
        }

    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

.. http:get:: /crab/percelen/(string:perceel_id1)/(string:perceel_id2)/huisnummers

    Get the huisnummers linked to a perceel.

    **Example request**:

    .. sourcecode:: http

        GET /crab/percelen/13040C1747/00G002 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json


    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "status": {"naam": "inGebruik", "definitie": null, "id": "3"},
                "id": 1, 
                "label": "51"
            }, {
                "status": {"naam": "buitenGebruik", "definitie": null, "id": "4"},
                "id": 2021223,
                "label": "53"
            }
        ]

    :statuscode 200: Huisnummers were found.
    :statuscode 404: Perceel was not found.

.. http:get:: /crab/huisnummers/(int:huisnummer_id)/gebouwen

    List all gebouwen associated with a certain huisnummer.

    **Example request**:

    .. sourcecode:: http

        GET /crab/huisnummer/1/gebouwen HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
          {
            "status": {
              "naam": "inGebruik",
              "definitie": null,
              "id": "4"
            },
            "aard": {
              "naam": "hoofdgebouw",
              "definitie": "hoofdgebouw volgens het GRB",
              "id": "1"
            },
            "id": 1538575
          }
        ]

    :statuscode 200: Gebouwen were found.

.. http:get:: /crab/gebouwen/(int:gebouw_id)

    Get a Gebouw by it's id.

    **Example request**:

    .. sourcecode:: http

        GET /crab/gebouwen/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
          "status": {
            "naam": "inGebruik",
            "definitie": null,
            "id": "4"
          },
          "aard": {
            "naam": "hoofdgebouw",
            "definitie": "hoofdgebouw volgens het GRB",
            "id": "1"
          },
          "geometriemethode": {
            "naam": "grb",
            "definitie": null,
            "id": "3"
          },
          "geometrie": "POLYGON ((205574.52184166759 176477.42431658879, 205579.1574896723 176476.68550058827, 205578.6424176693 176472.64633258432, 205588.81227367371 176471.11494058371, 205589.80452967435 176478.83282858878, 205587.36587367207 176479.30028459057, 205588.38680167496 176487.107260596, 205576.12900967151 176488.87878059596, 205574.52184166759 176477.42431658879))",
          "id": 1,
          "metadata": {
            "begin_tijd": "2011-04-29 13:11:28.540000",
            "begin_datum": "1830-01-01 00:00:00",
            "begin_organisatie": {
              "naam": "AGIV",
              "definitie": "Agentschap voor Geografische Informatie Vlaanderen.",
              "id": "5"
            },
            "begin_bewerking": {
              "naam": "invoer",
              "definitie": "Invoer in de databank.",
              "id": "1"
            }
          }
        }
    :statuscode 200: Gebouw was found.
    :statuscode 404: Gebouw was not found.

.. http:get:: /crab/huisnummers/(int:huisnummer_id)/subadressen

    List all Subadressen for a certain Huisnummer.

    **Example request**:

    .. sourcecode:: http

        GET /crab/huisnummer/1/subadressen HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "status":{
                    "naam": "inGebruik",
                    "definitie": null,
                    "id": "3"
                },
                "id": 1120936,
                "subadres": "B"
            },{
                "status":{
                    "naam": "inGebruik",
                    "definitie": null,
                    "id": "3"
                },
                "id": 1120937,
                "subadres": "C"
            }
        ]

    :statuscode 200: Subadressen were found.
    :statuscode 404: The Huisnummer for which you are requesting Subadressen
        does not exist.

.. http:get:: /crab/subadressen/(int:subadres_id)

    Get a Subadres based on it's id.

    **Example request**:

    .. sourcecode:: http

        GET /crab/subadressen/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "status": {
                "naam": "inGebruik",
                "definitie": null,
                "id": "3"
            },
            "metadata": {
                "begin_tijd": "2013-04-12 20:07:13.180000",
                "begin_datum": "1830-01-01 00:00:00",
                "begin_organisatie": {
                    "naam": "gemeente",
                    "definitie": "Gemeente.",
                    "id": "1"
                },
                "begin_bewerking": {
                    "naam": "correctie",
                    "definitie": "Correctie van de attributen.",
                    "id": "3"
                }
            },
            "aard": {
                "naam": "rijksregister",
                "definitie": "Rijksregister.",
                "id": "2"
            },
            "id": 1120936,
            "subadres": "B"
        }

    :statuscode 200: Subadres was found.
    :statuscode 404: Subadres was not found.

.. http:get:: /crab/huisnummers/(int:huisnummer_id)/adresposities

    List all adresposities for a certain huisnummer.

    **Example request**:

    .. sourcecode:: http

        GET /crab/huisnummer/1/adresposities HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "herkomst": {
                    "naam": "manueleAanduidingVanPerceel",
                    "definitie": null,
                    "id": "2"
                },
                "id": 4087928
            }
        ]

    :statuscode 200: A (possibly empty) list of adresposities is available.
    :statuscode 404: The Huisnummer for which you are requesting Adresposities
        does not exist.

.. http:get:: /crab/subadressen/(int:subadres_id)/adresposities

    List all adresposities for a certain subadres.

    **Example request**:

    .. sourcecode:: http

        GET /crab/huisnummer/800000/adresposities HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "herkomst": {
                    "naam": "afgeleidVanGebouw",
                    "definitie": null,
                    "id": "10"
                },
                "id": 2706297
            }
        ]

    :statuscode 200: A (possibly empty) list of adresposities is available.
    :statuscode 404: The Subadres for which you are requesting Adresposities
        does not exist.

.. http:get:: /crab/adresposities/(int:adrespositie_id)

    List all information on a certain adrespositie.

    **Example request**:

    .. sourcecode:: http

        GET /crab/adresposities/2706297 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "herkomst": {
                "naam": "afgeleidVanGebouw",
                "definitie": null,
                "id": "10"
            },
            "metadata": {
                "begin_tijd": "2013-01-19 06:28:57.483000",
                "begin_datum": "1830-01-01 00:00:00",
                "begin_organisatie": {
                    "naam": "AGIV",
                    "definitie": "Agentschap voor Geografische Informatie
        Vlaanderen.",
                    "id": "5"
                },
                "begin_bewerking": {
                    "naam": "correctie",
                    "definitie": "Correctie van de attributen.",
                    "id": "3"
                }
            },
            "geometrie": "POINT (154546.38 216367)",
            "id": 2706297,
            "aard": {
                "naam": "subAdres",
                "definitie": "Aanduiding van een plaats op een huisnummer",
                "id": "1"
            }
        }

.. http:get:: /crab/landen

    List all landen.

    **Example request**:

    .. sourcecode:: http

        GET /crab/landen HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json
        Content-Range: 0-6/249

        [
            {
                "naam": "Afghanistan",
                "id": "AF"
            },{
                "naam": "\u00c5land Islands",
                "id": "AX"
            },{
                "naam": "Albania",
                "id": "AL"
            },{
                "naam": "Algeria",
                "id": "DZ"
            },{
                "naam": "American Samoa",
                "id": "AS"
            },{
                "naam": "Andorra",
                "id": "AD"
            },{
                "naam": "Angola",
                "id": "AO"
            }
        ]

    :statuscode 200: List of landen was found.

.. http:get:: /crab/landen/BE

    List all information for a certain land.

    **Example request**:

    .. sourcecode:: http

        GET /crab/landen/BE HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "alpha2": "BE",
            "alpha3": "BEL",
            "id": "BE",
            "naam": "Belgium"
        }

    :statuscode 200: Land was found.
    :statuscode 404: Land was not found.
