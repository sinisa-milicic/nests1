import csv
from matplotlib import pyplot as plt
from math import exp
from analysis import regression_coef

from matplotlib import rc
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.figure(figsize=(7,3))


data = list(csv.reader(open("output/individual.csv")))
header, data = data[0], data[1:]
data = [[float(x) for x in d] for d in data]
elog, c45log, c45an, b45log, b45an, c43log, c43an, b43log, b43an, c93log, c93an, b93log, b93an = zip(*data)

print(regression_coef(elog, b43log, 0.5))
print(regression_coef(elog, b45log, 0.5))
print(regression_coef(elog, c43log, 0.5))
print(regression_coef(elog, c45log, 0.5))

b93 = [(b-ba)/ba for b, ba in zip(b93log,b93an)]
c93 = [(c-ca)/ca for c, ca in zip(c93log,c93an)]
b43 = [(b-ba)/ba for b, ba in zip(b43log,b43an)]
c43 = [(c-ca)/ca for c, ca in zip(c43log,c43an)]
b45 = [(b-ba)/ba for b, ba in zip(b45log,b45an)]
c45 = [(c-ca)/ca for c, ca in zip(c45log,c45an)]
z = [0]*len(elog)

plt.figure(figsize=(7,3))
plt.plot(elog, z, color='grey', linewidth=2)
plt.plot(elog, b45, color='darkgrey', linewidth=1, linestyle='--')
plt.plot(elog, b93, color='darkgrey', linewidth=1, linestyle=':')
plt.plot(elog, b43, color='black', linewidth=1, linestyle='--')
#plt.show()
plt.savefig("output/individual-bifractal--45--43:93-0-7534-0-8193-0-7540.eps", format='eps', dpi=1200)
plt.close()

plt.figure(figsize=(7,3))
plt.plot(elog, z, color='grey', linewidth=2)
plt.plot(elog, c45, color='darkgrey', linewidth=1, linestyle='--')
plt.plot(elog, c93, color='darkgrey', linewidth=1, linestyle=':')
plt.plot(elog, c43, color='black', linewidth=1, linestyle='--')
#plt.show()
plt.savefig("output/individual-cantor--45--43:93-0-7511-0-8181-0-7532.eps", format='eps', dpi=1200)
plt.close()
