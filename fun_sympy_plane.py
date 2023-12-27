from sympy import Symbol, sqrt, expand, diff, solve
from sympy.simplify import simplify

a = Symbol("a", real=True)
b = Symbol("b", real=True)
#c = 1
#d = 0
x = Symbol("x", real=True)
y = Symbol("y", real=True)
z = Symbol("z", real=True)
dist2 = (a*x+b*y+z)**2

#print(simplify(expand(dist2)))
#a**2*x**2 + 2*a*b*x*y + 2*a*x*z + b**2*y**2 + 2*b*y*z + z**2

x2 = Symbol("x2", real=True)
xy = Symbol("xy", real=True)
xz = Symbol("xz", real=True)
y2 = Symbol("y2", real=True)
yz = Symbol("yz", real=True)
z2 = Symbol("z2", real=True)


eq = a**2*x2 + 2*a*b*xy + 2*a*xz + b**2*y2 + 2*b*yz + z2
 
di_a = diff(eq, a) 
di_b = diff(eq, b)
rr = solve([di_a, di_b], (a,b))
print(rr)
# {a: (xy*yz - xz*y2)/(x2*y2 - xy**2), b: (-x2*yz + xy*xz)/(x2*y2 - xy**2)}


