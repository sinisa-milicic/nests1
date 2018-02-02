from math import pow, pi
from numpy import linspace
from dimensiontool import draw_nest, nest_iterator, cantor
from epstool import arc, arc_point
from itertools import chain
from sys import stderr

Dmin = 1/4
Dmax = 1
DN = 1000
Ds = linspace(Dmin, Dmax, DN)

D = 3/4
αmin = 1/D-1
αmax = 1/D
αN = 1000
αs = linspace(αmin, αmax, αN)[1:]

N = 3
ε = 1/300

print("Same-dimension uniform Cantor nests...")
for α in αs:
    func = lambda n: pow(n, -α)
    δ = D*α+D-1
    r = pow(N, -1/δ)
    title = "Uniform ({:d},{:09.7f})-Cantor nest of dimension {:5.4f} (a={:5.4f})".format(N, r, D, α)
    fname = "output/CD{:5.4f}-{:5.4f}-fixed".format(D, α).replace('.','-')+".eps"
    def proc(R):
        for a, b in cantor(a=0, b=pi/2, N=N, r=r, ε=ε/R):
            print(arc(a,b, R))
    draw_nest(fname=fname, title=title, func=func, procedure=proc, ε=ε)

print("Variable-dimension unfiorm Cantor nests...")
for d in Ds:
    α = 1/d-1/2
    func = lambda n: pow(n, -α)
    δ = d*α+d-1
    r = pow(N, -1/δ)
    title = "Uniform ({:d},{:09.7f})-Cantor nest of dimension {:5.4f} (a={:5.4f})".format(N, r, d, α)
    fname = "output/CD{:5.4f}-{:5.4f}-variable-D".format(d, α).replace('.','-')+".eps"
    def proc(R):
        for a, b in cantor(a=0, b=pi/2, N=N, r=r, ε=ε/R):
            print(arc(a,b, R))
    draw_nest(fname=fname, title=title, func=func, procedure=proc, ε=ε)

print("Same-dimension bifractals...")
for α in αs:
    func = lambda n: pow(n, -α)
    δ = D*α+D-1
    β = 1/δ - 1
    func2 = lambda n: pow(n, -β)
    title = "({:05.4},{:05.4f})-bifractal of dimension {:5.4f}".format(α, β, D)
    fname = "output/BD{:05.4f}-({:5.4f}:{:5.4f})-fixed-D".format(D, α, β).replace('.','-')+".eps"
    def proc(R):
        print(arc_point(pi/4, R))
        for x in nest_iterator(ε/R*4/pi, func2):
            print(arc_point(pi/4*(1-x), R))
            print(arc_point(pi/4*(1+x), R))
    draw_nest(fname=fname, title=title, func=func, procedure=proc, ε=ε)

print("Variable-dimension bifractals...")
for d in Ds:
    α = 1/d-1/2
    func = lambda n: pow(n, -α)
    δ = d*α+d-1
    β = 1/δ - 1
    func2 = lambda n: pow(n, -β)
    title = "({:05.4},{:05.4f})-bifractal of dimension {:5.4f}".format(α, β, d)
    fname = "output/BD{:05.4f}-({:5.4f}:{:5.4f})-variable-D".format(d, α, β).replace('.','-')+".eps"
    def proc(R):
        print(arc_point(pi/4, R))
        for x in nest_iterator(ε/R*4/pi, func2):
            print(arc_point(pi/4*(1-x), R))
            print(arc_point(pi/4*(1+x), R))
    draw_nest(fname=fname, title=title, func=func, procedure=proc, ε=ε)
