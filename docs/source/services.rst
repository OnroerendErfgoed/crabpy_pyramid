Services
========

Crabpy_pyramid exposes the following services:

Capakey
-------

.. http:get:: /capakey/gemeenten

    List all gemeenten

.. http:get:: /capakey/gemeenten/(int:gemeente_id)

    Get a gemeente by id

.. http:get:: /capakey/gemeenten/(int:gemeente_id)/afdelingen

    List_kadastrale_afdelingen_by_gemeente

    
.. http:get:: /capakey/afdelingen

    List_kadastrale_afdelingen

.. http:get:: /capakey/afdelingen/(int:afdeling_id)

    Get_kadastrale_afdeling_by_id

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties

    List_secties_by_afdeling

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)

    Get_sectie_by_id_and_afdeling

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)/percelen

    List_percelen_by_sectie

.. http:get:: /capakey/afdelingen/(int:afdeling_id)/secties/(string:sectie_id)/percelen/(int:perceel_id)

    Get_perceel_by_id_and_sectie

.. http:get:: /capakey/percelen/(string:capakey)

    Get Perceel_by_capakey

.. http:get:: /capakey/percelen/(string:percid)

    Get_perceel_by_percid
