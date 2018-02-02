from dimensiontool import cantor, epsoutput
from sys import stderr

N = 3
r = 1/4
print("A list of fractal nests...")
with epsoutput("output/cantor.eps", "Fractal nests of various dimensions", ε=1/180, Y=0.5):
    for k in range(5,-1,-1):
        hole_size = (1-N*r)/(N-1)*(r**(k))
        print("{} setlinewidth".format(min(1/180, hole_size/2)))
        for a,b in cantor(0,1, N, r, hole_size, k):
            print("{:11.7f} {:11.7f} moveto {:11.7f} 0 rlineto stroke".format(a,0.4-k*0.1,b-a))
