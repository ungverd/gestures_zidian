from sympy import Symbol, expand, solve, diff, Eq
from sympy.simplify import simplify

a = Symbol("a", real=True)
b = Symbol("b", real=True)
c = Symbol("c", real=True)
x1 = Symbol("x1", real=True)
x2 = Symbol("x2", real=True)
x3 = Symbol("x3", real=True)
y1 = Symbol("y1", real=True)
y2 = Symbol("y2", real=True)
y3 = Symbol("y3", real=True)

x = x1 + x2 + x3
y = y1 + y2 + y3
x_4 = x1**4 + x2**4 + x3**4
x_3 = x1**3 + x2**3 + x3**3
x_2y = x1**2*y1 + x2**2*y2 + x3**2*y3
x_2 = x1**2 + x2**2 + x3**2
xy = x1*y1 + x2*y2 + x3*y3
y_2 = y1**2 + y2**2 + y3**2

eq1 = Eq(a*x_4 + b*x_3 + c*x_2 - x_2y, 0)
eq2 = Eq(a*x_3 + b*x_2 + c*x - xy, 0)
eq3 = Eq(a*x_2 + b*x + c - y, 0)


rr = solve([eq1, eq2, eq3], (a, b, c))
print(simplify(rr[a]))
#{a: (x**2*x2y - x*x2*xy - x*x3*y + x2**2*y - x2*x2y + x3*xy)/(x**2*x4 - 2*x*x2*x3 + x2**3 - x2*x4 + x3**2), b: (-x*x2*x2y + x*x4*y + x2**2*xy - x2*x3*y + x2y*x3 - x4*xy)/(x**2*x4 - 2*x*x2*x3 + x2**3 - x2*x4 + x3**2), c: (-x*x2y*x3 + x*x4*xy + x2**2*x2y - x2*x3*xy - x2*x4*y + x3**2*y)/(x**2*x4 - 2*x*x2*x3 + x2**3 - x2*x4 + x3**2)}