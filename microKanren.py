from Utils.utils import *

def walk(u, s):
    pr = is_var(u) and assp(lambda v: var_equals(u, v), s)
    return walk(assp(s, u), s) if pr else u

def eq(u, v):
    def _equals(sc):
        s = unify(u, v, car(sc))
        if s is not False: return (s, cdr(sc)), MZERO
        else: return MZERO
    return _equals

def unify(u, v, s):
    u = walk(u, s)
    v = walk(v, s)

    if var_equals(u, v):
        return s
    elif is_var(u):
        return ext_s(u, v, s)
    elif is_var(v):
        return ext_s(v, u, s)
    elif is_pair(u) and is_pair(v) and len(u) == len(v):
        new_s = unify(car(u), car(v), s)
        return unify(cdr(u), cdr(v), new_s)
    elif u == v:
        return s
    else:
        return False

def call_fresh(f):
    def _call_fresh(sc):
        c = cdr(sc)
        g = f(Variable(c))
        return g((car(sc), c + 1))
    return _call_fresh

def mplus(s1, s2):
    if is_null(s1): return s2
    elif callable(s1): return lambda: mplus(s2,s1())
    else: return cons(car(s1), mplus(cdr(s1), s2))

def bind(s, g):
    if is_null(s): return MZERO
    elif callable(s): return lambda : bind(s(), g)
    else: return mplus(g(car(s)), bind(cdr(s), g))

def disj(g1, g2):
    return lambda sc: mplus(g1(sc), g2(sc))

def conj(g1, g2):
    return lambda sc: bind(g1(sc), g2)
