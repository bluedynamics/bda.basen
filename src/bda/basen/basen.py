import types

from bda.basen import str2int
from bda.basen import int2str

class base62(object):
    
    ref = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def __init__(self, term):
        if type(term) in types.StringTypes:
            self._str = term
            self._int = str2int(term, self.ref)
        else:
            self._str = int2str(term, self.ref)
            self._int = term
    
    def __str__(self): return self._str
    
    def __int__(self): return self._int
    
    def __repr__(self): return '%i %s' % (int(self), str(self)) 