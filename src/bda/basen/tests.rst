basic test::

    >>> from bda.basen import str2int
    >>> from bda.basen import int2str

    >>> ref = 'abcde'

    >>> int2str(12345, ref)
    'deddea'

    >>> str2int('abcde', ref)
    194

    >>> from bda.basen import base62
    >>> term = base62(100)
    >>> str(term)
    '1C'

    >>> term = base62('1D')
    >>> int(term)
    101

test with uuid::

    >>> import uuid
    >>> value = uuid.uuid4()
    >>> term = base62(value)
    >>> len(str(term)) < 23
    True
