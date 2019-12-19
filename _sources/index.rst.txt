.. pyCFB documentation master file, created by
   sphinx-quickstart on Tue Dec 17 16:04:32 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyCFB documentation
===================

``pyCFB`` is a Python package for calculating the Coffrey-Feingold-Bromberg measure for variability among weighted proportions.

For more information please see the original paper:
Coffrey, M.P., Feingold, M., and Bromberg J. `"A normed measure of variability among proportions" <https://doi.org/10.1016/0167-9473(88)90088-6>`_, Computational Statistics & Data Analysis, 1988

Example
=======

For a list of proportions with non-uniform weights:

.. code-block:: python

   >>> from pyCFB import coffrey
   >>> p = [0.3, 0.7, 0.7]
   >>> w = [0.1, 0.8, 0.1]
   >>> H = coffrey(p, w=w)
   0.3636363636363637


For uniform weights:

.. code-block:: python

   >>> from pyCFB import coffrey
   >>> p = [0.3, 0.7, 0.7]
   >>> H = coffrey(p)
   0.4500351603704095


``pyCFB.coffrey`` computes the CFB metric exactly and may take a long time for large problems.

Installation and download
=========================

Download code from `github <https://github.com/krosenfeld/pyCFB/>`_ and run from the command line:

.. code-block:: sh

   python setup.py install

Tests are included:

.. code-block:: sh

   python setup.py test

Requirements
============

- NumPy
- nose

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
