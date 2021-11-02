from microKanren import *

def take(n, stream):
    if n == 0: return MZERO
    else: return cons(car(stream), take(n-1, cdr(stream)))

a_and_b = conj(
    call_fresh(lambda a: eq(a, 7)),
    call_fresh(lambda b: disj(eq(b, 5), eq(b, 6)))
)

fives = lambda x: disj(
    eq(x, 5),
    lambda ac: lambda: fives(x)(ac)
)

relo = (
    lambda x:
        call_fresh(lambda x1:
              call_fresh(lambda x2:
                 conj(
                      eq(x, cons(x1, x2)),
                 disj(
                      eq(x1, x2),
        lambda sc: lambda: relo(x)(sc)))))
)

many_non_ans = call_fresh(
    lambda x:
        disj(
            relo([5, 6]),
            eq(x, 3))
)
