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

    **Example request**:

    .. sourcecode:: http

       GET /capakey/afdelingen/44017/secties HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json

    :statuscode 200: Afdeling was found.
    :statuscode 404: Afdeling was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)

    Get_sectie_by_id_and_afdeling

    **Example request**:

    .. sourcecode:: http

       GET /capakey/afdelingen/44017/secties/A HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json

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

    :reqheader Range: Can be used to ask for a certain set of results, 
        eg. ``ìtems=0-5`` asks for the first 6 items.
    :resheader Content-Range: Tells the client what range of results is
        being returned, eg. ``items=0-5/145`` for the first 6 items out of 145.
    :statuscode 200: Sectie was found.
    :statuscode 404: Sectie was not found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)/percelen/(int:perceel_id)

    Get_perceel_by_id_and_sectie

    **Example request**:

    .. sourcecode:: http

       GET /capakey/afdelingen/44017/secties/A/percelen/452 HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json

    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

.. http:get:: /capakey/percelen/(string:capakey)

    Get Perceel_by_capakey

    **Example request**:

    .. sourcecode:: http

       GET /capakey/percelen/(string:capakey) HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json

    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

.. http:get:: /capakey/percelen/(string:percid)

    Get_perceel_by_percid

    **Example request**:

    .. sourcecode:: http

       GET /capakey/percelen/(string:percid) HTTP/1.1
       Host: example.onroerenderfgoed.be
       Accept: application/json

    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

Crab
-----

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
        Content-Type: application/javascript

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
        
    :statuscode 200: Gewest was found.
    :statuscode 404: Gewest was not found.

.. http:get:: /crab/gewesten/(int:gewest_id)/gemeenten
    
    List_gemeenten
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /crab/gewesten/2/gemeenten HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        
    :query sort: One of ``id``, ``naam`` or ``niscode`` (default).
    :statuscode 200: Gemeenten were found.

.. http:get:: /crab/gemeente/(int:id of int:niscode)
    
    Get_gemeente_by_id
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /crab/gewesten/1/gemeenten/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        
    Get_gemeente_by_niscode
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /crab/gewesten/2/gemeenten/11001 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
    
    :statuscode 200: Gemeente was found.
    :statuscode 404: Gemeente was not found.

.. http:get:: /crab/gemeente/(int:id of int:niscode)/straten

    List_straten
    
    **Example request**:
    
    .. sourcecode:: http
            
            GET /crab/gemeente/11001/straten HTTP/1.1
            Host: example.onroerenderfgoed.be
            Accept: application/json
            
        :statuscode 200: Straten were found.

.. http:get:: /crab/straten/(int:straat_id)

    Get_straat_by_id
    
    **Example request**:
    
    ..sourcecode:: http
    
        GET /crab/straten/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        
    :statuscode 200: Straat was found.
    :statuscode 404: Straat was not found.
        
.. http:get:: /crab/straten/(int:straat_id)/huisnummers

    List_huisnummers
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /crab/straten/1/huisnummers HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        
    :statuscode 200: Huisnummers were found.

.. http:get:: /crab/straten/(int:straat_id)/huisnummers/(string:huisnummer_label)
    
    Get_huisnummer_by_nummer_and_label
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /crab/straten/1/huisnummers/23 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        
    :statuscode 200: Huisnummer was found.
    :statuscode 404: Huisnummer was not found.

.. http:get:: /crab/huisnummers/(int:huisnummer_id)

    Get_huisnummer_by_id
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /crab/huisnummers/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
    
    :statuscode 200: Huisnummer was found.
    :statuscode 404: Huisnummer was not found.

.. http:get:: /crab/huisnummers/(int:huisnummer_id)/percelen

    List_percelen
    
    **Example request**:
    
    .. sourcecode:: http
        
        GET /crab/huisnummers/1/percelen HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        
    :statuscode 200: Percelen were found.

.. http:get:: /crab/percelen/(int:perceel_id)

    Get_perceel_by_id
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /crab/percelen/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        
    :statuscode 200: Perceel was found.
    :statuscode 404: Perceel was not found.

.. http:get:: /crab/huisnummers/(int:huisnummer_id)/gebouwen

    List_gebouwen
    
    **Example request**:
    
    .. sourcecode:: http
        
        GET /crab/huisnummer/1/gebouwen HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        
    :statuscode 200: Gebouwen were found.

.. http:get:: /crab/gebouwen/(int:gebouw_id)

    Get_gebouw_by_id
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /crab/gebouwen/1 HTTP/1.1
        Host: example.onroerenderfgoed.be
        Accept: application/json
        
    :statuscode 200: Gebouw was found.
    :statuscode 404: Gebouw was not found.
