# bruteForce
from numpy import arange
import math

def f(x) :
    return  x**2-3*x+1 


for x in arange(-100, 100, 0.001):
    if abs(f(x)) < 0.001:
        print("x=", x, " f(x)=", f(x)) 


# iterative
f1 = lambda x : (x-1)**2
f2 = lambda x : (3*x-2) / (x+1) +1
f3 = lambda x: (3*x-1)**0.5

x1 =x2=x3=1

for i in range(100):
     x1, x2, x3 = f1(x1), f2(x2), f3(x3)
     print('x1:', x1, 'x2', x2, 'x3', x3)
