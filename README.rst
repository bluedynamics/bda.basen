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



Changes
=======

1.1.dev0
--------

- Support for python ``uuid`` module [jensens]

- more generic ``basex`` base class and special ``basej`` class with

1.0
---

- initial implementation [rnixx, jensens]
