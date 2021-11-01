from collections import namedtuple
from variable import Variable

MZERO = ()

State = namedtuple('State', ['alist', 'counter'])

def cons(x, y):
    return x, y

def is_pair(pair):
    return isinstance(pair, tuple)

def car(pair):
    return pair[0]

def cdr(pair):
    return pair[1]

def is_null(x):
    return len(x) == 0

def is_var(v):
    return isinstance(v, Variable)

def ext_s(x, v, s):
    s = s.copy()
    s[x] = v
    return s