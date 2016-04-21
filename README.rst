crabpy_pyramid
==============

Bindings for the crabpy library and the pyramid framework

.. image:: https://badge.fury.io/py/crabpy_pyramid.png
        :target: http://badge.fury.io/py/crabpy_pyramid
.. image:: https://readthedocs.org/projects/crabpy-pyramid/badge/?version=latest
        :target: https://readthedocs.org/projects/crabpy-pyramid/?badge=latest

.. image:: https://travis-ci.org/OnroerendErfgoed/crabpy_pyramid.png?branch=master
        :target: https://travis-ci.org/OnroerendErfgoed/crabpy_pyramid
.. image:: https://coveralls.io/repos/OnroerendErfgoed/crabpy_pyramid/badge.png?branch=master 
        :target: https://coveralls.io/r/OnroerendErfgoed/crabpy_pyramid?branch=master
.. image:: https://scrutinizer-ci.com/g/OnroerendErfgoed/crabpy_pyramid/badges/quality-score.png?b=master
        :target: https://scrutinizer-ci.com/g/OnroerendErfgoed/crabpy_pyramid/?branch=master

Building the docs
-----------------

More information about this library can be found in `docs`. The docs can be 
built using `Sphinx <http://sphinx-doc.org>`_.

Please make sure you have installed Sphinx in the same environment where 
crabpy\_pyramid is present.

.. code-block:: bash

    # activate your virtual env
    $ pip install sphinx sphinxcontrib-httpdomain
    $ python setup.py develop
    $ cd docs
    $ make html
