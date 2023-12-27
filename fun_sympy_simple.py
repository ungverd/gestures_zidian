from sympy import Symbol, expand, solve, diff
from sympy.simplify import simplify

a = Symbol("a", real=True)
b = Symbol("b", real=True)
c = Symbol("c", real=True)
x = Symbol("x", real=True)
y = Symbol("y", real=True)
n = Symbol("n", real=True)

eq = (a*x**2 + b*x + c - y)**2
print(expand(eq))
print()
#a**2*x**4 + 2*a*b*x**3 + 2*a*c*x**2 - 2*a*x**2*y + b**2*x**2 + 2*b*c*x - 2*b*x*y + c**2 - 2*c*y + y**2
#a**2*x4 + 2*a*b*x3 + 2*a*c*x2 - 2*a*x2y + b**2*x2 + 2*b*c*x - 2*b*xy + c**2 - 2*c*y + y2
x4 = Symbol("x4", real=True)
x3 = Symbol("x3", real=True)
x2y = Symbol("x2y", real=True)
x2 = Symbol("x2", real=True)
xy = Symbol("xy", real=True)
y2 = Symbol("y2", real=True)
eq = a**2*x4 + 2*a*b*x3 + 2*a*c*x2 - 2*a*x2y + b**2*x2 + 2*b*c*x\
    - 2*b*xy + c**2*n - 2*c*y + y2
di_a = diff(eq, a)
di_b = diff(eq, b)
di_c = diff(eq, c)
print(di_a)
print(di_b)
print(di_c)
print()

rr = solve([di_a, di_b, di_c], (a, b, c))
print(rr)
#{a: (-n*x2*x2y + n*x3*xy + x**2*x2y - x*x2*xy - x*x3*y + x2**2*y)/(-n*x2*x4 + n*x3**2 + x**2*x4 - 2*x*x2*x3 + x2**3), b: (n*x2y*x3 - n*x4*xy - x*x2*x2y + x*x4*y + x2**2*xy - x2*x3*y)/(-n*x2*x4 + n*x3**2 + x**2*x4 - 2*x*x2*x3 + x2**3), c: (-x*x2y*x3 + x*x4*xy + x2**2*x2y - x2*x3*xy - x2*x4*y + x3**2*y)/(-n*x2*x4 + n*x3**2 + x**2*x4 - 2*x*x2*x3 + x2**3)}