crabpy_pyramid
==============

Bindings for the crabpy library and the pyramid framework

.. image:: https://travis-ci.org/OnroerendErfgoed/crabpy_pyramid.png?branch=master
        :target: https://travis-ci.org/OnroerendErfgoed/crabpy_pyramid
.. image:: https://badge.fury.io/py/crabpy_pyramid.png
        :target: http://badge.fury.io/py/crabpy_pyramid

Building the docs
-----------------

Informatie over het werken met deze toepassing kun je vinden in de :file:`docs` 
folder. Deze kan gebuild worden tot propere documentatie met behulp van 
More information about this library can be found in :file:`docs`. The docs can be 
built using `Sphinx <http://sphinx-doc.org>`_.

Please make sure you have installed Sphinx in the same environment where 
crabpy\_pyramid is present.

.. code-block:: bash

    # activate your virtual env
    $ pip install sphinx sphinxcontrib-httpdomain
    $ python setup.py develop
    $ cd docs
    $ make html
