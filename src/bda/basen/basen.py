# -*- coding: utf-8 -*-
from bda.basen.convert import str2int
from bda.basen.convert import int2str

import types
import uuid


class basen(object):

    ref = None

    def __init__(self, term):
        if type(term) in types.StringTypes:
            self._str = term
            self._int = str2int(term, self.ref)
            return
        if isinstance(term, uuid.UUID):
            self._int = int(term)
        else:
            self._int = term
        self._str = int2str(self._int, self.ref)

    def __str__(self):
        return self._str

    def __int__(self):
        return self._int

    def __repr__(self):
        return '%i %s' % (int(self), str(self))


class base62(basen):

    ref = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# BBB
basen = base62

# avoid backslash and single-/doulequotes, other ascii
jref = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' \
       '!@#$%^&*()-_=+[]{};:,./<>?/~ '


class basej(basen):

    ref = jref
