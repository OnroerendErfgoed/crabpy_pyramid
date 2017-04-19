.. _setup:

=======================
Setup and configuration
=======================

Installing `crabpy_pyramid` is fairly straightforward, configuring it can be a
bit more complicated. Fundamentally, `crabpy_pyramid` uses the :mod:`crabpy` 
library to offer users access to both the CRAB and the CAPAKEY werbservice.
It's possible to include none, one or both of the services.

To add `crabpy_pyramid` to you project, just include it.

.. code-block:: python

    config.include('crabpy_pyramid')

Out of the box, this will add the :class:`crabpy.gateway.crab.CrabGateway` and
the accompanying REST services. It will not add the 
:class:`crabpy.gateway.capakey.CapakeyRestGateway` and it's accompanying services.
If you want to use this service, you need to set the 
:ref:`setting-capakey-include` setting to `True`.

The default will also set a :ref:`setting-cache-file-root` parameter. This is
the default location for writing :mod:`dogpile.cache` file caches. It exists 
to set a default that should work, but won't really help you very much. 
Please change it.

Settings
========

The following settings can be configured:

.. _setting-cache-file-root:

crabpy.cache.file.root
----------------------

Location where `dogpile.cache <http://dogpilecache.readthedocs.org/en/latest/>`_ 
can create file caches. By default it's set to :file:`/tmp/dogpile_data`. 
Should be changed for any setup that actually wants to use caching.

.. _setting-proxy-http:

crabpy.proxy.http
-----------------

Will be passed on to the Gateways, in case the services need to be called 
through a proxy.

.. _setting-proxy-https:

crabpy.proxy.https
------------------

Will be passed on to the Gateways, in case the services need to be called 
through a proxy.

.. _setting-crab-include:

crabpy.crab.include
-------------------

This setting controls whether the CRAB Gateway is configured or not. By default
this is set to `True`.

.. _setting-crab-cache-config:

crabpy.crab.cache_config
------------------------

This controls the caching settings for the CRAB Gateway. It's actually a prefix
for a number of settings, which are all passed on to the CRAB Gateway.

.. _setting-capakey-include:

crabpy.capakey.include
----------------------

This setting controls whether the CAPAKEY Gateway is configured or not. By default
this is set to `False`. If you set this to `True`.

.. _setting-capakey-cache-config:

crabpy.capakey.cache_config
---------------------------

This controls the caching settings for the CAPAKEY Gateway. It's actually a prefix
for a number of settings, which are all passed on to the CAPAKEY Gateway.
