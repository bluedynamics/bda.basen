=========
bda.basen
=========

Module to represent integers as any other based representation string.

There exist direct converter functions.

::

    >>> from bda.basen import str2int
    >>> from bda.basen import int2str

    >>> ref = 'abcde'

    >>> int2str(12345, ref)
    'deddea'

    >>> str2int('abcde', ref)
    194

Or a direct representation call for a 62 ascii based base.

::

    >>> from bda.basen import base62
    >>> term = base62(100)
    >>> str(term)
    '1C'

    >>> term = base62('1D')
    >>> int(term)
    101

This works also with uuids, which is with ~22 chars less than the default hex with 32 chars::

    >>> term = base62(uuid.uuid4())

``basej`` uses 91 chars ascii as base (no backslash, no single/double quotes, no control chars).
With this a chance to get 20 chars for a uuid is high::

    >>> term = basej(uuid.uuid4())


Source Code and Contributions
=============================

If you want to help with the development (improvement, update, bug-fixing, ...) of ``bda.basen`` this is a great idea!
Submit issues or pull requests!

The code is located at `github <https://github.com/bluedynamics/bda.basen>`_.

Maintainer is Jens Klein, Robert Niederreiter and the BlueDynamics Alliance developer team.
We appreciate any contribution and if a release is needed to be done on pypi,
please just contact one of us `dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_

Code is licensed under GPL v2.
