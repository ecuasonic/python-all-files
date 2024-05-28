import statistics as s
import re

#x = input('Give a list of x-values: ex. 1 2 3 4 5   : ')
#y = input('Give a list of y-values: ex. 1 2 3 4 5   : ')

x = [
    11,12,12,14,18,18,20,22,26,28
]

y = [
    66,65,107,105,163,166,179,226,232,281
]

x2 = [i*i for i in x]
y2 = [i*i for i in y]
xy = [i*j for i,j in zip(x,y)]
n = len(x)


Syy = sum(y2) - (sum(y)**2)/n
Sxx = sum(x2) - (sum(x)**2)/n
Sxy = sum(xy) - (sum(x)*sum(y))/n

SST = Syy
SSR = (Sxy**2)/Sxx
SSE = SST-SSR

r2 = SSR/SST
r = r2**(1/2)

m = Sxy/Sxx
b = (sum(y) - m*sum(x))/n
if m<0:
    r = r*(-1)

print(f'''SST: {SST}
SSR: {SSR}
SSE: {SSE}
r2: {r2:0.3f}
r: {r:0.3f}
eqn: y = {m:0.2f}*x + {b:0.2f}''')
