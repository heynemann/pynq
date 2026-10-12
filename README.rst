Introduction
------------

Microsoft created Linq (Language Integrated Query) using Expression trees, which is a math concept on how to parse operations into trees in a way that you can analyze the operations independently from the result.

Pynq is an implementation in Python of the Expression Tree theory and some of the providers. There will be more providers gradually, but Pynq will strive to make it as easy as possible to write your own provider.

Download the Source
-------------------

To download the source code for Pynq, use::

    git clone git://github.com/heynemann/pynq.git pynq

Documentation
-------------

To learn more about Pynq visit it's wiki by clicking on the wiki tab here in GitHub or visiting http://wiki.github.com/heynemann/pynq.

Installing
----------

Installing Pynq is detailed in the wiki Installing page (http://wiki.github.com/heynemann/pynq/installing).

Grouping by expressions
-----------------------

Simple field names can be passed directly to ``group_by``. Calculations and
nested attribute expressions refer to the current record as ``item``::

    from pynq import From
    From([1, 2, 3]).group_by("item % 2").select_many()
    # {0: [2], 1: [1, 3]}

Run the unit tests on the project's Python 2 runtime from the repository root::

    python2 -m unittest discover -s tests/unit
