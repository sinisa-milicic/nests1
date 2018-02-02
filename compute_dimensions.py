from sys import stderr
from epstool import epsbuf
from dimensiontool import log_count_cantor_nest, log_count_bifractal, powers
from math import pow, log, pi, exp, ceil
from matplotlib import pyplot as plt
from analysis import regression_coef
from numpy import linspace
import csv

εs = list(powers(2, -10, -25, 10))
εlog = [-log(ε) for ε in εs]
N = 3
D = 3/4
Dmin = 1/4
Dmax = 1
DN = 300
Ds = linspace(Dmin, Dmax, DN)[1:]

D = 3/4
αmin = 1/D-1
αmax = 1/D
αN = 300
αs = linspace(αmin, αmax, αN)[1:]

fieldnames = ['D', 'α', 'β', 'bdim', 'N', 'r', 'cdim']
line = lambda *args: {k:"{:23.17f}".format(v) for k,v in zip(fieldnames, args)}

with open("fix_dim.csv", "w") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for α in αs:
        δ = D*α+D-1
        β = 1/δ - 1
        r = pow(N, -1/δ)
        cantors = log_count_cantor_nest(α, N, r, εs)
        bifractals = log_count_bifractal(α, β, εs)
        cdim = regression_coef(εlog, cantors)[0]
        bdim = regression_coef(εlog, bifractals)[0]
        print([line(D, α, β, bdim, N, r, cdim)[x] for x in ['D','bdim','cdim','α']])
        w.writerow(line(D, α, β, bdim, N, r, cdim))


with open("var_dim.csv", "w") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for d in Ds:
        α = 1/d-1/2
        δ = d*α+d-1
        β = 1/δ - 1
        r = pow(N, -1/δ)
        cantors = log_count_cantor_nest(α, N, r, εs)
        bifractals = log_count_bifractal(α, β, εs)
        cdim = regression_coef(εlog, cantors)[0]
        bdim = regression_coef(εlog, bifractals)[0]
        print([line(d, α, β, bdim, N, r, cdim)[x] for x in ['D','bdim','cdim','α']])
        w.writerow(line(d, α, β, bdim, N, r, cdim))

