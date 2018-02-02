from math import pow, pi, sqrt
from numpy import linspace
from scipy.special import gamma as Γ
from dimensiontool import draw_nest, nest_iterator
from epstool import point, epsoutput
from itertools import chain
from sys import stderr

αmin = 0
αmax = 5
αN = 50
αs = linspace(αmin, αmax, αN)[1:]

ε = 1/500

cfunc = lambda α: pow(2/α/sqrt(pi), -α/(α+1)**2)*pow((α+1)*Γ(α/(α+1)/2+1),-1/(α+1))
M = max(cfunc(a) for a in αs)
print("A list of fractal nests...")
with epsoutput("output/nests.eps", "Fractal nests of various dimensions", Y=1.2, X=M, ε=ε):
    for k,α in enumerate(αs):
        func = lambda n: pow(n, -α)*cfunc(α)
        print(k*0.05, α, func(1), file=stderr)
        for R in nest_iterator(ε, func):
            print(point(R,k*0.025))

