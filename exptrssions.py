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
+ 4*qc*et2yr*sqrt(-qa**2 - qb**2 - qc**2 + 1) - 2*et2xr

res_qa = 4*a1*qa**2*eyr/sqrt(-qa**2 - qb**2 - qc**2 + 1) \
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
+ 4*b3*et2yr*sqrt(-qa**2 - qb**2 - qc**2 + 1)

et
et2
et3
et4
et5
et6
et7
et8
etxr
etyr
etzr
et2xr
et2yr
et2zr
et3xr
et3yr
et3zr
et4xr
et4yr
et4zr
exr
eyr
ezr