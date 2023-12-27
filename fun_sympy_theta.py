from sympy import Symbol, sin, cos, expand, diff, solve
from sympy.simplify import simplify

th = Symbol("th", real=True)
t = Symbol("t", real=True)
a = Symbol("a", real=True)
b = Symbol("b", real=True)
c = Symbol("c", real=True)
a1 = Symbol("a1", real=True)
b1 = Symbol("b1", real=True)
c1 = Symbol("c1", real=True)
d1 = Symbol("d1", real=True)
e1 = Symbol("e1", real=True)
x = Symbol("x", real=True)
y = Symbol("y", real=True)
x1 = x*cos(th) - y*sin(th)
y1 = x*sin(th) + y*cos(th)
eq = (a*(t)**2 + b*t + c - y1)**2 + (a1*(t)**4 + b1*t**3 + c1*t**2 + d1*t + e1 - x1)**2
#print(simplify(expand(eq)))

t4 = Symbol("t4", real=True)
t3 = Symbol("t3", real=True)
t2 = Symbol("t2", real=True)
t2x = Symbol("t2x", real=True)
t2y = Symbol("t2y", real=True)
t8 = Symbol("t8", real=True)
t7 = Symbol("t7", real=True)
t6 = Symbol("t6", real=True)
t5 = Symbol("t5", real=True)
t4x = Symbol("t4x", real=True)
t4y = Symbol("t4y", real=True)
tx = Symbol("tx", real=True)
ty = Symbol("ty", real=True)
t3x = Symbol("t3x", real=True)
t3y = Symbol("t3y", real=True)
x2 = Symbol("x2", real=True)
y2 = Symbol("y2", real=True)
n = Symbol("n", real=True)


eq = a**2*t4 + 2*a*b*t3 + 2*a*c*t2 - 2*a*t2x*sin(th)\
    - 2*a*t2y*cos(th) + a1**2*t8 + 2*a1*b1*t7 + 2*a1*c1*t6\
    + 2*a1*d1*t5 + 2*a1*e1*t4 - 2*a1*t4x*cos(th) + 2*a1*t4y*sin(th)\
    + b**2*t2 + 2*b*c*t - 2*b*tx*sin(th) - 2*b*ty*cos(th) + b1**2*t6\
    + 2*b1*c1*t5 + 2*b1*d1*t4 + 2*b1*e1*t3 - 2*b1*t3x*cos(th)\
    + 2*b1*t3y*sin(th) + c**2*n - 2*c*x*sin(th) - 2*c*y*cos(th) + c1**2*t4\
    + 2*c1*d1*t3 + 2*c1*e1*t2 - 2*c1*t2x*cos(th) + 2*c1*t2y*sin(th)\
    + d1**2*t2 + 2*d1*e1*t - 2*d1*tx*cos(th) + 2*d1*ty*sin(th) + e1**2*n\
    - 2*e1*x*cos(th) + 2*e1*y*sin(th) + x2\
    + y2
 
di_th = diff(eq, th)
print(di_th)
didi_th = diff(di_th, th)
print()
print(didi_th)
