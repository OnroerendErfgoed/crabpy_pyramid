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
       ]

    :reqheader Range: Can be used to ask for a certain set of results, 
        eg. ``ìtems=0-24`` asks for the first 25 items.
    :resheader Content-Range: Tells the client what range of results is
        being returned, eg. ``items=0-24/306`` for the first 25 items out of 306.
    :statuscode 200: Gemeenten were found.

.. http:get:: /capakey/gemeenten/(int:gemeente_id)

    Get a gemeente by id

    :statuscode 200: Gemeente was found.
    :statuscode 404: Gemeenten was not found.

.. http:get:: /capakey/gemeenten/(int:gemeente_id)/afdelingen

    List_kadastrale_afdelingen_by_gemeente

    :statuscode 200: Gemeente was found.
    :statuscode 404: Gemeente was not found.
    
.. http:get:: /capakey/afdelingen

    List_kadastrale_afdelingen

    :statuscode 200: Afdelingen were found.

.. http:get:: /capakey/afdelingen/(int:afdeling_id)

    Get_kadastrale_afdeling_by_id

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
