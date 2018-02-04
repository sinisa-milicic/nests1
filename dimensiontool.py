from math import ceil, log
from epstool import epsoutput
from numba import jit
from numpy import linspace

def powers(ε0=2.0, start=-1, stop=-10, num=100):
    yield from (pow(ε0, k) for k in linspace(start, stop, num))

def m1(ε, f):
    n = 1
    while abs(f(n)-f(n+1)) > 2*ε:
        n+=1
    return n

def m2(ε, f, em1=None):
    if em1 is None:
        em1 = m1(ε, f)
    return ceil(f(em1+1)/(2*ε))

def m12(ε, f):
    em1 = m1(ε, f)
    em2 = m2(ε, f, em1=em1)
    return em1, em2

def nest_iterator(ε, func):
    em1, em2 = m12(ε, func)
    yield from (2*k*ε for k in range(1, em2+1))
    yield from (func(n) for n in range(em1+1,0, -1))


@jit
def fm1(ε, α):
    n = pow(α/ε/2, 1/(α+1))
    while abs(pow(n, -α) - pow(n+1, -α)) <= 2*ε:  n-=1
    while abs(pow(n, -α) - pow(n+1, -α)) > 2*ε:  n+=1
    return n

@jit
def fm2(ε, α, em1=None):
    if em1 is None:
        em1 = fm1(ε, α)
    return ceil(pow(em1+1, -α)/(2*ε))

@jit
def fm12(ε, α):
    em1 = fm1(ε, α)
    em2 = fm2(ε, α, em1=em1)
    return em1, em2

@jit
def fnest_iterator(ε, α):
    em1, em2 = fm12(ε, α)
    for k in range(1, em2+1):
        yield 2*k*ε
    for n in range(em1+1,0,-1):
        yield pow(n, -α)

def draw_nest(fname="test.eps", title="test",
              func=lambda n: 1/n,
              procedure=lambda *args: None,
              ε=0.1, background=False):
    assert procedure is not None, "No active procdure!"
    with epsoutput(fname, title=title, ε=ε, background=background):
        for R in nest_iterator(ε, func):
            procedure(R)

def cantor(a, b, N, r, ε=0.05, depth=15):
    assert 0 <= r <= 1/N
    F = (1-N*r)/(N-1)
    def cantor_iterator(a, b, depth):
        Δ = b-a
        ell = Δ*F
        if ell <= ε or depth<=0:
            ta = min(a,b)
            tb = max(a,b)
            yield (ta, tb)
            return
        lower = Δ * (F+r)
        part = Δ * r
        for k in range(N):
            yield from cantor_iterator(a+k*lower, a+k*lower+part, depth-1)
    yield from cantor_iterator(a,b, depth)

def count_cantor_nest(α, N, r, ε):
#    print(log(ε, 1/2))
    c1 = log((1-N*r)/(N-1)/2)
    c2 = log(r)
    def l(x):
        k = ceil((log(x)-c1)/c2)+1
        return pow(N*r, k)+2*x*pow(N,k)
    return sum(l(ε/R)*R/ε for R in fnest_iterator(ε, α))


def log_count_cantor_nest(α, N, r, εs):
    return [log(count_cantor_nest(α, N, r, ε)) for ε in εs]


def count_bifractal(α, β, ε):
#    print(log(ε, 1/2))
    return sum(sum(fm12(ε/R, β)) for R in fnest_iterator(ε, α))

def log_count_bifractal(α, β, εs):
    return [log(count_bifractal(α, β, ε)) for ε in εs]
