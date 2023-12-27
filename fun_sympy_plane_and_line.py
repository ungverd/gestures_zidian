from sympy import Symbol, sqrt, expand, diff, solve
from sympy.simplify import simplify

x = Symbol("x", real=True)
y = Symbol("y", real=True)
z = Symbol("z", real=True)
f = Symbol("f", real=True)
g = Symbol("g", real=True)
h = Symbol("h", real=True)
b = Symbol("b", real=True)
a = -b*g/f - h/f
dist2 = (a*x+b*y+z)**2
#print(expand(dist2))
#b**2*y**2 - 2*b**2*g*x*y/f + b**2*g**2*x**2/f**2 + 2*b*y*z - 2*b*g*x*z/f\
#- 2*b*h*x*y/f + 2*b*g*h*x**2/f**2 + z**2 - 2*h*x*z/f + h**2*x**2/f**2
x2 = Symbol("x2", real=True)
xy = Symbol("xy", real=True)
xz = Symbol("xz", real=True)
y2 = Symbol("y2", real=True)
yz = Symbol("yz", real=True)
z2 = Symbol("z2", real=True)


eq = b**2*y2 - 2*b**2*g*xy/f + b**2*g**2*x2/f**2 + 2*b*yz - 2*b*g*xz/f\
- 2*b*h*xy/f + 2*b*g*h*x2/f**2 + z2 - 2*h*xz/f + h**2*x2/f**2
 
di_b = diff(eq, b)
rr = solve(di_b, b)
print(rr)
# (-f**2*yz + f*g*xz + f*h*xy - g*h*x2)/(f**2*y2 - 2*f*g*xy + g**2*x2)


