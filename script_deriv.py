import sympy
from sympy.abc import b, f, g, h
from sympy.simplify import simplify

x2, y2, z2, xy, xz, yz = sympy.symbols("x2 y2 z2 xy xz yz")

#import re

#pat = r"\([^)]*\)"
#expr = (b*y+z-(b*g+h)*x/f)**2/((b*g+h)**2/f**2+b**2+1)

#diffb = sympy.diff(expr, b)
#eq = sympy.Eq(0, diffb)
#res = sympy.solve(eq, b)
#print(res)

#s = "-2*b**3*g**4*x**2/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4) + 4*b**3*g**3*x*y/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) - 2*b**3*g**2*x**2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 2*b**3*g**2*y**2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) + 4*b**3*g*x*y/(b**4*f + 2*b**4*g**2/f + b**4*g**4/f**3 + 4*b**3*g*h/f + 4*b**3*g**3*h/f**3 + 2*b**2*f + 2*b**2*g**2/f + 2*b**2*h**2/f + 6*b**2*g**2*h**2/f**3 + 4*b*g*h/f + 4*b*g*h**3/f**3 + f + 2*h**2/f + h**4/f**3) - 2*b**3*y**2/(b**4 + 2*b**4*g**2/f**2 + b**4*g**4/f**4 + 4*b**3*g*h/f**2 + 4*b**3*g**3*h/f**4 + 2*b**2 + 2*b**2*g**2/f**2 + 2*b**2*h**2/f**2 + 6*b**2*g**2*h**2/f**4 + 4*b*g*h/f**2 + 4*b*g*h**3/f**4 + 1 + 2*h**2/f**2 + h**4/f**4) - 6*b**2*g**3*h*x**2/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4) + 4*b**2*g**3*x*z/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) + 8*b**2*g**2*h*x*y/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) - 4*b**2*g**2*y*z/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 4*b**2*g*h*x**2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 2*b**2*g*h*y**2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) + 4*b**2*g*x*z/(b**4*f + 2*b**4*g**2/f + b**4*g**4/f**3 + 4*b**3*g*h/f + 4*b**3*g**3*h/f**3 + 2*b**2*f + 2*b**2*g**2/f + 2*b**2*h**2/f + 6*b**2*g**2*h**2/f**3 + 4*b*g*h/f + 4*b*g*h**3/f**3 + f + 2*h**2/f + h**4/f**3) + 4*b**2*h*x*y/(b**4*f + 2*b**4*g**2/f + b**4*g**4/f**3 + 4*b**3*g*h/f + 4*b**3*g**3*h/f**3 + 2*b**2*f + 2*b**2*g**2/f + 2*b**2*h**2/f + 6*b**2*g**2*h**2/f**3 + 4*b*g*h/f + 4*b*g*h**3/f**3 + f + 2*h**2/f + h**4/f**3) - 4*b**2*y*z/(b**4 + 2*b**4*g**2/f**2 + b**4*g**4/f**4 + 4*b**3*g*h/f**2 + 4*b**3*g**3*h/f**4 + 2*b**2 + 2*b**2*g**2/f**2 + 2*b**2*h**2/f**2 + 6*b**2*g**2*h**2/f**4 + 4*b*g*h/f**2 + 4*b*g*h**3/f**4 + 1 + 2*h**2/f**2 + h**4/f**4) - 6*b*g**2*h**2*x**2/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4) + 8*b*g**2*h*x*z/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) + 2*b*g**2*x**2/(b**2*f**2 + b**2*g**2 + 2*b*g*h + f**2 + h**2) - 2*b*g**2*z**2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) + 4*b*g*h**2*x*y/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) - 4*b*g*h*y*z/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 4*b*g*x*y/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) - 2*b*h**2*x**2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) + 4*b*h*x*z/(b**4*f + 2*b**4*g**2/f + b**4*g**4/f**3 + 4*b**3*g*h/f + 4*b**3*g**3*h/f**3 + 2*b**2*f + 2*b**2*g**2/f + 2*b**2*h**2/f + 6*b**2*g**2*h**2/f**3 + 4*b*g*h/f + 4*b*g*h**3/f**3 + f + 2*h**2/f + h**4/f**3) + 2*b*y**2/(b**2 + b**2*g**2/f**2 + 2*b*g*h/f**2 + 1 + h**2/f**2) - 2*b*z**2/(b**4 + 2*b**4*g**2/f**2 + b**4*g**4/f**4 + 4*b**3*g*h/f**2 + 4*b**3*g**3*h/f**4 + 2*b**2 + 2*b**2*g**2/f**2 + 2*b**2*h**2/f**2 + 6*b**2*g**2*h**2/f**4 + 4*b*g*h/f**2 + 4*b*g*h**3/f**4 + 1 + 2*h**2/f**2 + h**4/f**4) - 2*g*h**3*x**2/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4) + 4*g*h**2*x*z/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) + 2*g*h*x**2/(b**2*f**2 + b**2*g**2 + 2*b*g*h + f**2 + h**2) - 2*g*h*z**2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 2*g*x*z/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) - 2*h*x*y/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) + 2*y*z/(b**2 + b**2*g**2/f**2 + 2*b*g*h/f**2 + 1 + h**2/f**2)"

'''for line in re.findall(pat, s):
    if "x" in line or "y" in line or "z" in line:
        print(line)'''
expr = (-2*b**3*g**4*x2/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4) + 4*b**3*g**3*xy/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) - 2*b**3*g**2*x2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 2*b**3*g**2*y2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) + 4*b**3*g*xy/(b**4*f + 2*b**4*g**2/f + b**4*g**4/f**3 + 4*b**3*g*h/f + 4*b**3*g**3*h/f**3 + 2*b**2*f + 2*b**2*g**2/f + 2*b**2*h**2/f + 6*b**2*g**2*h**2/f**3 + 4*b*g*h/f + 4*b*g*h**3/f**3 + f + 2*h**2/f + h**4/f**3) - 2*b**3*y2/(b**4 + 2*b**4*g**2/f**2 + b**4*g**4/f**4 + 4*b**3*g*h/f**2 + 4*b**3*g**3*h/f**4 + 2*b**2 + 2*b**2*g**2/f**2 + 2*b**2*h**2/f**2 + 6*b**2*g**2*h**2/f**4 + 4*b*g*h/f**2 + 4*b*g*h**3/f**4 + 1 + 2*h**2/f**2 + h**4/f**4) - 6*b**2*g**3*h*x2/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4) + 4*b**2*g**3*xz/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) + 8*b**2*g**2*h*xy/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) - 4*b**2*g**2*yz/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 4*b**2*g*h*x2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 2*b**2*g*h*y2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) + 4*b**2*g*xz/(b**4*f + 2*b**4*g**2/f + b**4*g**4/f**3 + 4*b**3*g*h/f + 4*b**3*g**3*h/f**3 + 2*b**2*f + 2*b**2*g**2/f + 2*b**2*h**2/f + 6*b**2*g**2*h**2/f**3 + 4*b*g*h/f + 4*b*g*h**3/f**3 + f + 2*h**2/f + h**4/f**3) + 4*b**2*h*xy/(b**4*f + 2*b**4*g**2/f + b**4*g**4/f**3 + 4*b**3*g*h/f + 4*b**3*g**3*h/f**3 + 2*b**2*f + 2*b**2*g**2/f + 2*b**2*h**2/f + 6*b**2*g**2*h**2/f**3 + 4*b*g*h/f + 4*b*g*h**3/f**3 + f + 2*h**2/f + h**4/f**3) - 4*b**2*yz/(b**4 + 2*b**4*g**2/f**2 + b**4*g**4/f**4 + 4*b**3*g*h/f**2 + 4*b**3*g**3*h/f**4 + 2*b**2 + 2*b**2*g**2/f**2 + 2*b**2*h**2/f**2 + 6*b**2*g**2*h**2/f**4 + 4*b*g*h/f**2 + 4*b*g*h**3/f**4 + 1 + 2*h**2/f**2 + h**4/f**4) - 6*b*g**2*h**2*x2/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4) + 8*b*g**2*h*xz/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) + 2*b*g**2*x2/(b**2*f**2 + b**2*g**2 + 2*b*g*h + f**2 + h**2) - 2*b*g**2*z2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) + 4*b*g*h**2*xy/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) - 4*b*g*h*yz/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 4*b*g*xy/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) - 2*b*h**2*x2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) + 4*b*h*xz/(b**4*f + 2*b**4*g**2/f + b**4*g**4/f**3 + 4*b**3*g*h/f + 4*b**3*g**3*h/f**3 + 2*b**2*f + 2*b**2*g**2/f + 2*b**2*h**2/f + 6*b**2*g**2*h**2/f**3 + 4*b*g*h/f + 4*b*g*h**3/f**3 + f + 2*h**2/f + h**4/f**3) + 2*b*y2/(b**2 + b**2*g**2/f**2 + 2*b*g*h/f**2 + 1 + h**2/f**2) - 2*b*z2/(b**4 + 2*b**4*g**2/f**2 + b**4*g**4/f**4 + 4*b**3*g*h/f**2 + 4*b**3*g**3*h/f**4 + 2*b**2 + 2*b**2*g**2/f**2 + 2*b**2*h**2/f**2 + 6*b**2*g**2*h**2/f**4 + 4*b*g*h/f**2 + 4*b*g*h**3/f**4 + 1 + 2*h**2/f**2 + h**4/f**4) - 2*g*h**3*x2/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4) + 4*g*h**2*xz/(b**4*f**3 + 2*b**4*f*g**2 + b**4*g**4/f + 4*b**3*f*g*h + 4*b**3*g**3*h/f + 2*b**2*f**3 + 2*b**2*f*g**2 + 2*b**2*f*h**2 + 6*b**2*g**2*h**2/f + 4*b*f*g*h + 4*b*g*h**3/f + f**3 + 2*f*h**2 + h**4/f) + 2*g*h*x2/(b**2*f**2 + b**2*g**2 + 2*b*g*h + f**2 + h**2) - 2*g*h*z2/(b**4*f**2 + 2*b**4*g**2 + b**4*g**4/f**2 + 4*b**3*g*h + 4*b**3*g**3*h/f**2 + 2*b**2*f**2 + 2*b**2*g**2 + 2*b**2*h**2 + 6*b**2*g**2*h**2/f**2 + 4*b*g*h + 4*b*g*h**3/f**2 + f**2 + 2*h**2 + h**4/f**2) - 2*g*xz/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) - 2*h*xy/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) + 2*yz/(b**2 + b**2*g**2/f**2 + 2*b*g*h/f**2 + 1 + h**2/f**2))

expr = (-b**2*f**3*yz + b**2*f**2*g*xz + b**2*f**2*h*xy - b**2*f*g**2*yz - b**2*f*g*h*x2 + b**2*f*g*h*y2 + b**2*g**3*xz - b**2*g**2*h*xy + b*f**3*y2 - b*f**3*z2 - 2*b*f**2*g*xy + 2*b*f**2*h*xz + b*f*g**2*x2 - b*f*g**2*z2 - b*f*h**2*x2 + b*f*h**2*y2 + 2*b*g**2*h*xz - 2*b*g*h**2*xy + f**3*yz - f**2*g*xz - f**2*h*xy + f*g*h*x2 - f*g*h*z2 + f*h**2*yz + g*h**2*xz - h**3*xy)
"2*f*(-b**2*f**3*yz + b**2*f**2*g*xz + b**2*f**2*h*xy - b**2*f*g**2*yz - b**2*f*g*h*x2 + b**2*f*g*h*y2 + b**2*g**3*xz - b**2*g**2*h*xy + b*f**3*y2 - b*f**3*z2 - 2*b*f**2*g*xy + 2*b*f**2*h*xz + b*f*g**2*x2 - b*f*g**2*z2 - b*f*h**2*x2 + b*f*h**2*y2 + 2*b*g**2*h*xz - 2*b*g*h**2*xy + f**3*yz - f**2*g*xz - f**2*h*xy + f*g*h*x2 - f*g*h*z2 + f*h**2*yz + g*h**2*xz - h**3*xy)/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4)"
eq = sympy.Eq(0, expr)
res = sympy.solve(eq, b)
print(res)

"[(f**3*y2/2 - f**3*z2/2 - f**2*g*xy + f**2*h*xz + f*g**2*x2/2 - f*g**2*z2/2 - f*h**2*x2/2 + f*h**2*y2/2 - f*sqrt(f**4*y2**2 - 2*f**4*y2*z2 + 4*f**4*yz**2 + f**4*z2**2 - 4*f**3*g*xy*y2 + 4*f**3*g*xy*z2 - 8*f**3*g*xz*yz - 8*f**3*h*xy*yz + 4*f**3*h*xz*y2 - 4*f**3*h*xz*z2 + 2*f**2*g**2*x2*y2 - 2*f**2*g**2*x2*z2 + 4*f**2*g**2*xy**2 + 4*f**2*g**2*xz**2 - 2*f**2*g**2*y2*z2 + 4*f**2*g**2*yz**2 + 2*f**2*g**2*z2**2 + 8*f**2*g*h*x2*yz - 4*f**2*g*h*y2*yz - 4*f**2*g*h*yz*z2 - 2*f**2*h**2*x2*y2 + 2*f**2*h**2*x2*z2 + 4*f**2*h**2*xy**2 + 4*f**2*h**2*xz**2 + 2*f**2*h**2*y2**2 - 2*f**2*h**2*y2*z2 + 4*f**2*h**2*yz**2 - 4*f*g**3*x2*xy + 4*f*g**3*xy*z2 - 8*f*g**3*xz*yz - 4*f*g**2*h*x2*xz + 8*f*g**2*h*xz*y2 - 4*f*g**2*h*xz*z2 - 4*f*g*h**2*x2*xy - 4*f*g*h**2*xy*y2 + 8*f*g*h**2*xy*z2 - 4*f*h**3*x2*xz - 8*f*h**3*xy*yz + 4*f*h**3*xz*y2 + g**4*x2**2 - 2*g**4*x2*z2 + 4*g**4*xz**2 + g**4*z2**2 + 4*g**3*h*x2*yz - 8*g**3*h*xy*xz - 4*g**3*h*yz*z2 + 2*g**2*h**2*x2**2 - 2*g**2*h**2*x2*y2 - 2*g**2*h**2*x2*z2 + 4*g**2*h**2*xy**2 + 4*g**2*h**2*xz**2 + 2*g**2*h**2*y2*z2 + 4*g**2*h**2*yz**2 + 4*g*h**3*x2*yz - 8*g*h**3*xy*xz - 4*g*h**3*y2*yz + h**4*x2**2 - 2*h**4*x2*y2 + 4*h**4*xy**2 + h**4*y2**2)/2 + g**2*h*xz - g*h**2*xy)/(f**3*yz - f**2*g*xz - f**2*h*xy + f*g**2*yz + f*g*h*x2 - f*g*h*y2 - g**3*xz + g**2*h*xy), (f**3*y2/2 - f**3*z2/2 - f**2*g*xy + f**2*h*xz + f*g**2*x2/2 - f*g**2*z2/2 - f*h**2*x2/2 + f*h**2*y2/2 + f*sqrt(f**4*y2**2 - 2*f**4*y2*z2 + 4*f**4*yz**2 + f**4*z2**2 - 4*f**3*g*xy*y2 + 4*f**3*g*xy*z2 - 8*f**3*g*xz*yz - 8*f**3*h*xy*yz + 4*f**3*h*xz*y2 - 4*f**3*h*xz*z2 + 2*f**2*g**2*x2*y2 - 2*f**2*g**2*x2*z2 + 4*f**2*g**2*xy**2 + 4*f**2*g**2*xz**2 - 2*f**2*g**2*y2*z2 + 4*f**2*g**2*yz**2 + 2*f**2*g**2*z2**2 + 8*f**2*g*h*x2*yz - 4*f**2*g*h*y2*yz - 4*f**2*g*h*yz*z2 - 2*f**2*h**2*x2*y2 + 2*f**2*h**2*x2*z2 + 4*f**2*h**2*xy**2 + 4*f**2*h**2*xz**2 + 2*f**2*h**2*y2**2 - 2*f**2*h**2*y2*z2 + 4*f**2*h**2*yz**2 - 4*f*g**3*x2*xy + 4*f*g**3*xy*z2 - 8*f*g**3*xz*yz - 4*f*g**2*h*x2*xz + 8*f*g**2*h*xz*y2 - 4*f*g**2*h*xz*z2 - 4*f*g*h**2*x2*xy - 4*f*g*h**2*xy*y2 + 8*f*g*h**2*xy*z2 - 4*f*h**3*x2*xz - 8*f*h**3*xy*yz + 4*f*h**3*xz*y2 + g**4*x2**2 - 2*g**4*x2*z2 + 4*g**4*xz**2 + g**4*z2**2 + 4*g**3*h*x2*yz - 8*g**3*h*xy*xz - 4*g**3*h*yz*z2 + 2*g**2*h**2*x2**2 - 2*g**2*h**2*x2*y2 - 2*g**2*h**2*x2*z2 + 4*g**2*h**2*xy**2 + 4*g**2*h**2*xz**2 + 2*g**2*h**2*y2*z2 + 4*g**2*h**2*yz**2 + 4*g*h**3*x2*yz - 8*g*h**3*xy*xz - 4*g*h**3*y2*yz + h**4*x2**2 - 2*h**4*x2*y2 + 4*h**4*xy**2 + h**4*y2**2)/2 + g**2*h*xz - g*h**2*xy)/(f**3*yz - f**2*g*xz - f**2*h*xy + f*g**2*yz + f*g*h*x2 - f*g*h*y2 - g**3*xz + g**2*h*xy)]"
