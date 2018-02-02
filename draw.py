from matplotlib import pyplot as plt
from math import log
import csv

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fname_fix = 'output/20180202-fix-dim.csv'
fname_var = 'output/20180202-var-dim.csv'

with open(fname_fix,'r') as f:
    r = csv.DictReader(f)
    αs = []
    βs = []
    ds = []
    Ds = []
    Ns = []
    rs = []
    cds = []
    bds = []
    for row in r:
        αs.append(float(row['α']))
        βs.append(float(row['β']))
        ds.append(1/(1+float(row['β'])))
        Ds.append(float(row['D']))
        Ns.append(float(row['N']))
        rs.append(float(row['r']))
        cds.append(float(row['cdim']))
        bds.append(float(row['bdim']))
    l = len(Ds)
    plt.figure(figsize=(7,3))
    plt.plot(αs, Ds, color='grey', linewidth=2)
    plt.plot(αs, [1/(α+1) for α in αs], color='grey', linewidth=1, linestyle=':')
    plt.plot(αs, [1/(β+1) for β in βs], color='grey', linewidth=1, linestyle=':')
    plt.plot(αs, bds, color='darkgrey', linewidth=1, linestyle='--')
    plt.plot(αs, cds, color='black', linewidth=1, linestyle='--')
    plt.axis([min(αs), max(αs), min(min(bds),min(cds))-0.05, max(max(bds),max(cds))+0.05])
    #plt.show()
    plt.savefig("output/20180202-fixed.eps", format='eps', dpi=1200)
    plt.close()

with open(fname_var,'r') as f:
    r = csv.DictReader(f)
    αs = []
    Ds = []
    cds = []
    bds = []
    for row in r:
        αs.append(float(row['α']))
        Ds.append(float(row['D']))
        cds.append(float(row['cdim']))
        bds.append(float(row['bdim']))


    rdbs = [b/d-1 for d, b in zip(Ds,bds)]
    rcbs = [c/d-1 for d, c in zip(Ds,cds)]
    plt.figure(figsize=(7,3))
    plt.plot(Ds, [0]*len(αs) , color='grey', linewidth=2)
    plt.plot(Ds, rdbs, color='darkgrey', linewidth=1, linestyle='--')
    plt.plot(Ds, rcbs, color='black', linewidth=1, linestyle='--')
    plt.axis([min(Ds), max(Ds), min(min(rdbs),min(rcbs))-0.01, max(max(rdbs),max(rcbs))+0.01])
    #plt.show()
    plt.savefig("output/20180202-variable.eps", format='eps', dpi=1200)
    plt.close()
