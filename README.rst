bda.basen
=========

Module to represent integers as any other based representation string.

There exist direct converter functions.

  >>> from bda.basen import str2int
  >>> from bda.basen import int2str
  
  >>> ref = 'abcde'
  
  >>> int2str(12345, ref)
  'deddea'
  
  >>> str2int('abcde', ref)
  194
  
Or a direct representation call. this might be more in future.

  >>> from bda.basen import base62
  >>> term = base62(100)
  >>> str(term)
  '1C'
  
  >>> term = base62('1D')
  >>> int(term)
  101