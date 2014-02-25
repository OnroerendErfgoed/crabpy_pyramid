Services
========

* Return format is same as dojo rest store
* Uses Range header for slicing (eg. items=1-10)
* Mime-type is application/json

Crabpy_pyramid exposes the following services.

Capakey
-------

.. http:get:: /capakey/gemeenten

    List all gemeenten

    **Example request**:

    .. sourcecode:: http

       GET /capakey/gemeenten HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json
       Range: 0-4

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/javascript
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
       Content-Type: application/javascript

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
       Content-Type: application/javascript
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
       Content-Type: application/javascript
       Content-Range: 0-1/1433

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
       Content-Type: application/javascript

       {
           'id': 44017,
           'naam': 'Drongen',
           'gemeente': {
                'id': 44021,
                'naam': 'Gent'
           },
           'centroid': [104154.2225, 197300.703],
           'bbox': [94653.453, 185680.984, 113654.992, 208920.422]
       }

    :statuscode 200: Afdeling was found.
    :statuscode 404: Afdeling was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties

    List_secties_by_afdeling

    :statuscode 200: Afdeling was found.
    :statuscode 404: Afdeling was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)

    Get_sectie_by_id_and_afdeling

    :statuscode 200: Sectie was found.
    :statuscode 404: Sectie was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)/percelen

    List_percelen_by_sectie

    :statuscode 200: Sectie was found.
    :statuscode 404: Sectie was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)/percelen/(int:perceel_id)

    Get_perceel_by_id_and_sectie

    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

.. http:get:: /capakey/percelen/(string:capakey)

    Get Perceel_by_capakey

    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

.. http:get:: /capakey/percelen/(string:percid)

    Get_perceel_by_percid

    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.
