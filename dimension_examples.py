from math import pow, log, exp
from analysis import regression_coef
from dimensiontool import log_count_cantor_nest, log_count_bifractal, powers
import csv

εs = list(powers(2, -5, -35, 300))
εlog = [-log(ε) for ε in εs]
N = 3

D = 3/4
α = 4/5
δ = D*α+D-1
β = 1/δ - 1
r = pow(N, -1/δ)
c45log = log_count_cantor_nest(α, N, r, εs)
b45log = log_count_bifractal(α, β, εs)
ca, cb = regression_coef(εlog, c45log)
ba, bb = regression_coef(εlog, b45log)
X = ca, ba
c45an = [ca*ε+cb for ε in εlog]
b45an = [ba*ε+bb for ε in εlog]

D = 3/4
α = 4/3
δ = D*α+D-1
β = 1/δ - 1
r = pow(N, -1/δ)
c43log = log_count_cantor_nest(α, N, r, εs)
b43log = log_count_bifractal(α, β, εs)
ca, cb = regression_coef(εlog, c43log)
ba, bb = regression_coef(εlog, b43log)
c43an = [ca*ε+cb for ε in εlog]
b43an = [ba*ε+bb for ε in εlog]
Y = ca, ba

D = 3/4
α = 9/3
δ = D
β = 1/δ - 1
r = pow(N, -1/δ)
c93log = log_count_cantor_nest(α, N, r, εs)
b93log = log_count_bifractal(α, β, εs)
ca, cb = regression_coef(εlog, c93log)
ba, bb = regression_coef(εlog, b93log)
c93an = [ca*ε+cb for ε in εlog]
b93an = [ba*ε+bb for ε in εlog]

print(*X, *Y, ca, ba)

with open("output/individual.csv", "w") as f:
    w = csv.writer(f)
    w.writerow(['εlog', 'c45log', 'c45an', 'b45log', 'b45an',
                'c43log', 'c43an', 'b43log', 'b43an', 'c93log', 'c93an', 'b93log',
                'b93an'])
    w.writerows(zip(εlog, c45log, c45an, b45log, b45an, c43log, c43an,
                    b43log, b43an, c93log, c93an, b93log, b93an))
