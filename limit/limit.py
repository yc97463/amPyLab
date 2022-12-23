import sympy as sp
from sympy import *
x = symbols("x")
ans = limit((x**2-1)/(x+1), x, -1)
print(ans)
ans = limit((x**3-4)/(2*abs(x)**3), x, -oo)
print(ans)
