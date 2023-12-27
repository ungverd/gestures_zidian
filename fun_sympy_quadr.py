from sympy import *
from sympy.simplify import simplify

t = Symbol("t")
a = Symbol("a")
b = Symbol("b")
c = Symbol("c")
x = Symbol("x")
y = Symbol("y")
x1 = x*cos(t) - y*sin(t)
y1 = x*sin(t) + y*cos(t)
eq = (a*(x1)**2 + b*x1 + c - y1)**2
#print(expand(eq))
x4 = Symbol("x4")
x3y = Symbol("x3y")
x2y2 = Symbol("x2y2")
xy3 = Symbol("xy3")
y4 = Symbol("y4")
x3 = Symbol("x3")
x2y = Symbol("x2y")
xy2 = Symbol("xy2")
y3 = Symbol("y3")
x2 = Symbol("x2")
xy = Symbol("xy")
y2 = Symbol("y2")
eq = a**2*x4*cos(t)**4 - 4*a**2*x3y*sin(t)*cos(t)**3 + 6*a**2*x2y2*sin(t)**2*cos(t)**2 - 4*a**2*xy3*sin(t)**3*cos(t) + a**2*y4*sin(t)**4\
 + 2*a*b*x3*cos(t)**3 - 6*a*b*x2y*sin(t)*cos(t)**2 + 6*a*b*xy2*sin(t)**2*cos(t) - 2*a*b*y3*sin(t)**3 + 2*a*c*x2*cos(t)**2\
 - 4*a*c*xy*sin(t)*cos(t) + 2*a*c*y2*sin(t)**2 - 2*a*x3*sin(t)*cos(t)**2 + 4*a*x2y*sin(t)**2*cos(t) - 2*a*x2y*cos(t)**3 - 2*a*xy2*sin(t)**3\
 + 4*a*xy2*sin(t)*cos(t)**2 - 2*a*y3*sin(t)**2*cos(t) + b**2*x2*cos(t)**2 - 2*b**2*xy*sin(t)*cos(t) + b**2*y2*sin(t)**2 + 2*b*c*x*cos(t)\
 - 2*b*c*y*sin(t) - 2*b*x2*sin(t)*cos(t) + 2*b*xy*sin(t)**2 - 2*b*xy*cos(t)**2 + 2*b*y2*sin(t)*cos(t) + c**2 - 2*c*x*sin(t) - 2*c*y*cos(t)\
 + x2*sin(t)**2 + 2*xy*sin(t)*cos(t) + y2*cos(t)**2
 
di_t = diff(eq, t)
di_a = diff(eq, a)
di_b = diff(eq, b)
di_c = diff(eq, c)

rr = solve([di_t, di_a, di_b, di_c],
           (t, a, b, c))
print(rr)

'''q0 = sqrt(1 - qa*qa - qb*qb - qc*qc)
qp = Quaternion(q0, qa, qb, qc)
qm = Quaternion(q0, -qa, -qb, -qc)
x = b1 + b2*t + b3*t**2
y = 0
z = a1 + a2*t + a3*t**2 + a4*t**3 + a5*t**4
xr = Symbol("xr")
yr = Symbol("yr")
zr = Symbol("zr")
res = qp*Quaternion(0, xr, yr, zr)*qm - Quaternion(0, x, y, z)
res2 = res.b**2 + res.c**2 + res.d**2
res_a1 = diff(res2, a1)
res_a2 = diff(res2, a2)
res_a3 = diff(res2, a3)
res_a4 = diff(res2, a4)
res_a5 = diff(res2, a5)
res_b1 = diff(res2, b1)
res_b2 = diff(res2, b2)
res_b3 = diff(res2, b3)
res_qa = diff(res2, qa)
res_qb = diff(res2, qb)
res_qc = diff(res2, qc)

et = Symbol("et")
et2 = Symbol("et2")
et3 = Symbol("et3")
et4 = Symbol("et4")
et5 = Symbol("et5")
et6 = Symbol("et6")
et7 = Symbol("et7")
et8 = Symbol("et8")
exr = Symbol("exr")
eyr = Symbol("eyr")
ezr = Symbol("ezr")
etzr = Symbol("etzr")
etxr = Symbol("etxr")
etyr = Symbol("etyr")
et2zr = Symbol("et2zr")
et2xr = Symbol("et2xr")
et2yr = Symbol("et2yr")
et3zr = Symbol("et3zr")
et3xr = Symbol("et3xr")
et3yr = Symbol("et3yr")
et4zr = Symbol("et4zr")
et4xr = Symbol("et4xr")
et4yr = Symbol("et4yr")

res_a1 = 2*a1 + 2*a2*et + 2*a3*et2 + 2*a4*et3 + 2*a5*et4 + 4*qa**2*ezr - 4*qa*qc*exr \
- 4*qa*eyr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 4*qb**2*ezr - 4*qb*qc*eyr \
+ 4*qb*exr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 2*ezr

res_a2 = 2*a1*et + 2*a2*et2 + 2*a3*et3 + 2*a4*et4 + 2*a5*et5 + 4*qa**2*etzr \
- 4*qa*qc*etxr  - 4*qa*etyr *sqrt(-qa**2 - qb**2 - qc**2 + 1) + 4*qb**2*etzr \
- 4*qb*qc*etyr  + 4*qb*etxr *sqrt(-qa**2 - qb**2 - qc**2 + 1) - 2*etzr

res_a3 = 2*a1*et2 + 2*a2*et3 + 2*a3*et4 + 2*a4*et5 + 2*a5*et6 + 4*qa**2*et2zr \
- 4*qa*qc*et2xr - 4*qa*et2yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 4*qb**2*et2zr \
- 4*qb*qc*et2yr + 4*qb*et2xr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 2*et2zr

res_a4 = 2*a1*et3 + 2*a2*et4 + 2*a3*et5 + 2*a4*et6 + 2*a5*et7 + 4*qa**2*et3zr \
- 4*qa*qc*et3xr - 4*qa*et3yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 4*qb**2*et3zr \
- 4*qb*qc*et3yr + 4*qb*et3xr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 2*et3zr

res_a5 = 2*a1*et4 + 2*a2*et5 + 2*a3*et6 + 2*a4*et7 + 2*a5*et8 + 4*qa**2*et4zr \
- 4*qa*qc*et4xr - 4*qa*et4yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 4*qb**2*et4zr \
- 4*qb*qc*et4yr + 4*qb*et4xr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 2*et4zr

res_b1 = 2*b1 + 2*b2*et + 2*b3*et2 - 4*qa*qb*eyr - 4*qa*qc*ezr + 4*qb**2*exr \
- 4*qb*ezr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 4*qc**2*exr \
+ 4*qc*eyr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 2*exr

res_b2 = 2*b1*et + 2*b2*et2 + 2*b3*et3 - 4*qa*qb*etyr  - 4*qa*qc*etzr + 4*qb**2*etxr  \
- 4*qb*etzr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 4*qc**2*etxr  \
+ 4*qc*etyr *sqrt(-qa**2 - qb**2 - qc**2 + 1) - 2*etxr 

res_b3 = 2*b1*et2 + 2*b2*et3 + 2*b3*et4 - 4*qa*qb*et2yr - 4*qa*qc*et2zr \
+ 4*qb**2*et2xr - 4*qb*et2zr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 4*qc**2*et2xr \
+ 4*qc*et2yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 2*et2xr'''

'''res_qa = 4*a1*qa**2*eyr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a1*qa*qb*exr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a1*qa*ezr - 4*a1*qc*exr \
- 4*a1*eyr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 4*a2*qa**2*etyr /sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a2*qa*qb*etxr /sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a2*qa*etzr - 4*a2*qc*etxr  \
- 4*a2*etyr *sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 4*a3*qa**2*et2yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a3*qa*qb*et2xr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a3*qa*et2zr - 4*a3*qc*et2xr \
- 4*a3*et2yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 4*a4*qa**2*et3yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a4*qa*qb*et3xr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a4*qa*et3zr - 4*a4*qc*et3xr \
- 4*a4*et3yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 4*a5*qa**2*et4yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a5*qa*qb*et4xr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a5*qa*et4zr - 4*a5*qc*et4xr \
- 4*a5*et4yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 4*b1*qa*qb*ezr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*b1*qa*qc*eyr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*b1*qb*eyr - 4*b1*qc*ezr \
+ 4*b2*qa*qb*etzr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*b2*qa*qc*etyr /sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*b2*qb*etyr  - 4*b2*qc*etzr \
+ 4*b3*qa*qb*et2zr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*b3*qa*qc*et2yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*b3*qb*et2yr - 4*b3*qc*et2zr

res_qb = 4*a1*qa*qb*eyr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a1*qb**2*exr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a1*qb*ezr - 4*a1*qc*eyr \
+ 4*a1*exr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 4*a2*qa*qb*etyr /sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a2*qb**2*etxr /sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a2*qb*etzr - 4*a2*qc*etyr  \
+ 4*a2*etxr *sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 4*a3*qa*qb*et2yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a3*qb**2*et2xr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a3*qb*et2zr \
- 4*a3*qc*et2yr + 4*a3*et2xr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 4*a4*qa*qb*et3yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a4*qb**2*et3xr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a4*qb*et3zr - 4*a4*qc*et3yr \
+ 4*a4*et3xr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 4*a5*qa*qb*et4yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*a5*qb**2*et4xr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*a5*qb*et4zr - 4*a5*qc*et4yr \
+ 4*a5*et4xr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*b1*qa*eyr + 4*b1*qb**2*ezr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*b1*qb*qc*eyr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*b1*qb*exr \
- 4*b1*ezr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*b2*qa*etyr  \
+ 4*b2*qb**2*etzr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*b2*qb*qc*etyr /sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*b2*qb*etxr  \
- 4*b2*etzr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*b3*qa*et2yr \
+ 4*b3*qb**2*et2zr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*b3*qb*qc*et2yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*b3*qb*et2xr \
- 4*b3*et2zr*sqrt(-qa**2 - qb**2 - qc**2 + 1)

res_qc = 4*a1*qa*qc*eyr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a1*qa*exr \
- 4*a1*qb*qc*exr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a1*qb*eyr \
+ 4*a2*qa*qc*etyr /sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a2*qa*etxr  \
- 4*a2*qb*qc*etxr /sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a2*qb*etyr  \
+ 4*a3*qa*qc*et2yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a3*qa*et2xr \
- 4*a3*qb*qc*et2xr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a3*qb*et2yr \
+ 4*a4*qa*qc*et3yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a4*qa*et3xr \
- 4*a4*qb*qc*et3xr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a4*qb*et3yr \
+ 4*a5*qa*qc*et4yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a5*qa*et4xr \
- 4*a5*qb*qc*et4xr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*a5*qb*et4yr \
- 4*b1*qa*ezr + 4*b1*qb*qc*ezr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*b1*qc**2*eyr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*b1*qc*exr \
+ 4*b1*eyr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*b2*qa*etzr \
+ 4*b2*qb*qc*etzr/sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*b2*qc**2*etyr /sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 8*b2*qc*etxr  + 4*b2*etyr *sqrt(-qa**2 - qb**2 - qc**2 + 1) - 4*b3*qa*et2zr \
+ 4*b3*qb*qc*et2zr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- 4*b3*qc**2*et2yr/sqrt(-qa**2 - qb**2 - qc**2 + 1) + 8*b3*qc*et2xr \
+ 4*b3*et2yr*sqrt(-qa**2 - qb**2 - qc**2 + 1)'''

'''res_qa = 4*(-a1*exr*qa*qb + a1*eyr*qa**2 - a2*etxr*qa*qb + a2*etyr*qa**2 - a3*et2xr*qa*qb + a3*et2yr*qa**2 \
- a4*et3xr*qa*qb + a4*et3yr*qa**2 - a5*et4xr*qa*qb + a5*et4yr*qa**2 - b1*eyr*qa*qc + b1*ezr*qa*qb - b2*etyr*qa*qc \
+ b2*etzr*qa*qb - b3*et2yr*qa*qc + b3*et2zr*qa*qb + sqrt(-qa**2 - qb**2 - qc**2 + 1)*(-a1*exr*qc \
- a1*eyr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 2*a1*ezr*qa - a2*etxr*qc - a2*etyr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 2*a2*etzr*qa - a3*et2xr*qc - a3*et2yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 2*a3*et2zr*qa - a4*et3xr*qc \
- a4*et3yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 2*a4*et3zr*qa - a5*et4xr*qc - a5*et4yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
+ 2*a5*et4zr*qa - b1*eyr*qb - b1*ezr*qc - b2*etyr*qb - b2*etzr*qc - b3*et2yr*qb - b3*et2zr*qc))

res_qb = 4*(-a1*exr*qb**2 + a1*eyr*qa*qb - a2*etxr*qb**2 + a2*etyr*qa*qb - a3*et2xr*qb**2 + a3*et2yr*qa*qb \
- a4*et3xr*qb**2 + a4*et3yr*qa*qb - a5*et4xr*qb**2 + a5*et4yr*qa*qb - b1*eyr*qb*qc + b1*ezr*qb**2 - b2*etyr*qb*qc \
+ b2*etzr*qb**2 - b3*et2yr*qb*qc + b3*et2zr*qb**2 + sqrt(-qa**2 - qb**2 - qc**2 + 1)*(a1*exr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- a1*eyr*qc + 2*a1*ezr*qb + a2*etxr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - a2*etyr*qc + 2*a2*etzr*qb + a3*et2xr*sqrt(-qa**2 \
- qb**2 - qc**2 + 1) - a3*et2yr*qc + 2*a3*et2zr*qb + a4*et3xr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - a4*et3yr*qc + 2*a4*et3zr*qb \
+ a5*et4xr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - a5*et4yr*qc + 2*a5*et4zr*qb + 2*b1*exr*qb - b1*eyr*qa - b1*ezr*sqrt(-qa**2 \
- qb**2 - qc**2 + 1) + 2*b2*etxr*qb - b2*etyr*qa - b2*etzr*sqrt(-qa**2 - qb**2 - qc**2 + 1) + 2*b3*et2xr*qb - b3*et2yr*qa \
- b3*et2zr*sqrt(-qa**2 - qb**2 - qc**2 + 1)))

res_qc = 4*(-a1*exr*qb*qc + a1*eyr*qa*qc - a2*etxr*qb*qc + a2*etyr*qa*qc - a3*et2xr*qb*qc + a3*et2yr*qa*qc \
- a4*et3xr*qb*qc + a4*et3yr*qa*qc - a5*et4xr*qb*qc + a5*et4yr*qa*qc - b1*eyr*qc**2 + b1*ezr*qb*qc \
- b2*etyr*qc**2 + b2*etzr*qb*qc - b3*et2yr*qc**2 + b3*et2zr*qb*qc + sqrt(-qa**2 - qb**2 \
- qc**2 + 1)*(-a1*exr*qa - a1*eyr*qb - a2*etxr*qa - a2*etyr*qb - a3*et2xr*qa - a3*et2yr*qb \
- a4*et3xr*qa - a4*et3yr*qb - a5*et4xr*qa - a5*et4yr*qb + 2*b1*exr*qc + b1*eyr*sqrt(-qa**2 - qb**2 - qc**2 + 1) \
- b1*ezr*qa + 2*b2*etxr*qc + b2*etyr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - b2*etzr*qa + 2*b3*et2xr*qc \
+ b3*et2yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - b3*et2zr*qa))

rr = solve([res_a1, res_a2, res_a3, res_a4, res_a5, res_b1, res_b2, res_b3, res_qa, res_qb, res_qc],
           (a1, a2, a3, a4, a5, b1, b2, b3, qa, qb, qc))'''

#print(rr)
#print(simplify(res_b3))
#print(simplify(pos_x))


