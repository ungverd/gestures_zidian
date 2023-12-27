import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

x2 = 10435.32003377204
y2 = 2171.8292323553273
z2 = 16996.157477228164
xy = 2431.2134198882877
xz = -11068.327327272764
yz = -330.16763237875216

f = 5.612937365853658
g = 1.6330583414634143
h = -7.4907676097561

racines = [(f**3*y2/2 - f**3*z2/2 - f**2*g*xy + f**2*h*xz + f*g**2*x2/2 - f*g**2*z2/2 - f*h**2*x2/2 + f*h**2*y2/2 - f*sqrt(f**4*y2**2 - 2*f**4*y2*z2 + 4*f**4*yz**2 + f**4*z2**2 - 4*f**3*g*xy*y2 + 4*f**3*g*xy*z2 - 8*f**3*g*xz*yz - 8*f**3*h*xy*yz + 4*f**3*h*xz*y2 - 4*f**3*h*xz*z2 + 2*f**2*g**2*x2*y2 - 2*f**2*g**2*x2*z2 + 4*f**2*g**2*xy**2 + 4*f**2*g**2*xz**2 - 2*f**2*g**2*y2*z2 + 4*f**2*g**2*yz**2 + 2*f**2*g**2*z2**2 + 8*f**2*g*h*x2*yz - 4*f**2*g*h*y2*yz - 4*f**2*g*h*yz*z2 - 2*f**2*h**2*x2*y2 + 2*f**2*h**2*x2*z2 + 4*f**2*h**2*xy**2 + 4*f**2*h**2*xz**2 + 2*f**2*h**2*y2**2 - 2*f**2*h**2*y2*z2 + 4*f**2*h**2*yz**2 - 4*f*g**3*x2*xy + 4*f*g**3*xy*z2 - 8*f*g**3*xz*yz - 4*f*g**2*h*x2*xz + 8*f*g**2*h*xz*y2 - 4*f*g**2*h*xz*z2 - 4*f*g*h**2*x2*xy - 4*f*g*h**2*xy*y2 + 8*f*g*h**2*xy*z2 - 4*f*h**3*x2*xz - 8*f*h**3*xy*yz + 4*f*h**3*xz*y2 + g**4*x2**2 - 2*g**4*x2*z2 + 4*g**4*xz**2 + g**4*z2**2 + 4*g**3*h*x2*yz - 8*g**3*h*xy*xz - 4*g**3*h*yz*z2 + 2*g**2*h**2*x2**2 - 2*g**2*h**2*x2*y2 - 2*g**2*h**2*x2*z2 + 4*g**2*h**2*xy**2 + 4*g**2*h**2*xz**2 + 2*g**2*h**2*y2*z2 + 4*g**2*h**2*yz**2 + 4*g*h**3*x2*yz - 8*g*h**3*xy*xz - 4*g*h**3*y2*yz + h**4*x2**2 - 2*h**4*x2*y2 + 4*h**4*xy**2 + h**4*y2**2)/2 + g**2*h*xz - g*h**2*xy)/(f**3*yz - f**2*g*xz - f**2*h*xy + f*g**2*yz + f*g*h*x2 - f*g*h*y2 - g**3*xz + g**2*h*xy), (f**3*y2/2 - f**3*z2/2 - f**2*g*xy + f**2*h*xz + f*g**2*x2/2 - f*g**2*z2/2 - f*h**2*x2/2 + f*h**2*y2/2 + f*sqrt(f**4*y2**2 - 2*f**4*y2*z2 + 4*f**4*yz**2 + f**4*z2**2 - 4*f**3*g*xy*y2 + 4*f**3*g*xy*z2 - 8*f**3*g*xz*yz - 8*f**3*h*xy*yz + 4*f**3*h*xz*y2 - 4*f**3*h*xz*z2 + 2*f**2*g**2*x2*y2 - 2*f**2*g**2*x2*z2 + 4*f**2*g**2*xy**2 + 4*f**2*g**2*xz**2 - 2*f**2*g**2*y2*z2 + 4*f**2*g**2*yz**2 + 2*f**2*g**2*z2**2 + 8*f**2*g*h*x2*yz - 4*f**2*g*h*y2*yz - 4*f**2*g*h*yz*z2 - 2*f**2*h**2*x2*y2 + 2*f**2*h**2*x2*z2 + 4*f**2*h**2*xy**2 + 4*f**2*h**2*xz**2 + 2*f**2*h**2*y2**2 - 2*f**2*h**2*y2*z2 + 4*f**2*h**2*yz**2 - 4*f*g**3*x2*xy + 4*f*g**3*xy*z2 - 8*f*g**3*xz*yz - 4*f*g**2*h*x2*xz + 8*f*g**2*h*xz*y2 - 4*f*g**2*h*xz*z2 - 4*f*g*h**2*x2*xy - 4*f*g*h**2*xy*y2 + 8*f*g*h**2*xy*z2 - 4*f*h**3*x2*xz - 8*f*h**3*xy*yz + 4*f*h**3*xz*y2 + g**4*x2**2 - 2*g**4*x2*z2 + 4*g**4*xz**2 + g**4*z2**2 + 4*g**3*h*x2*yz - 8*g**3*h*xy*xz - 4*g**3*h*yz*z2 + 2*g**2*h**2*x2**2 - 2*g**2*h**2*x2*y2 - 2*g**2*h**2*x2*z2 + 4*g**2*h**2*xy**2 + 4*g**2*h**2*xz**2 + 2*g**2*h**2*y2*z2 + 4*g**2*h**2*yz**2 + 4*g*h**3*x2*yz - 8*g*h**3*xy*xz - 4*g*h**3*y2*yz + h**4*x2**2 - 2*h**4*x2*y2 + 4*h**4*xy**2 + h**4*y2**2)/2 + g**2*h*xz - g*h**2*xy)/(f**3*yz - f**2*g*xz - f**2*h*xy + f*g**2*yz + f*g*h*x2 - f*g*h*y2 - g**3*xz + g**2*h*xy)]

print(racines)

b = np.linspace(-5, 5, 500)

expr = b**2*g**2*x2/(b**2*f**2 + b**2*g**2 + 2*b*g*h + f**2 + h**2) - 2*b**2*g*xy/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) + b**2*y2/(b**2 + b**2*g**2/f**2 + 2*b*g*h/f**2 + 1 + h**2/f**2) + 2*b*g*h*x2/(b**2*f**2 + b**2*g**2 + 2*b*g*h + f**2 + h**2) - 2*b*g*xz/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) - 2*b*h*xy/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) + 2*b*yz/(b**2 + b**2*g**2/f**2 + 2*b*g*h/f**2 + 1 + h**2/f**2) + h**2*x2/(b**2*f**2 + b**2*g**2 + 2*b*g*h + f**2 + h**2) - 2*h*xz/(b**2*f + b**2*g**2/f + 2*b*g*h/f + f + h**2/f) + z2/(b**2 + b**2*g**2/f**2 + 2*b*g*h/f**2 + 1 + h**2/f**2)

expr_graph = 2*f*(-b**2*f**3*yz + b**2*f**2*g*xz + b**2*f**2*h*xy - b**2*f*g**2*yz - b**2*f*g*h*x2 + b**2*f*g*h*y2 + b**2*g**3*xz - b**2*g**2*h*xy + b*f**3*y2 - b*f**3*z2 - 2*b*f**2*g*xy + 2*b*f**2*h*xz + b*f*g**2*x2 - b*f*g**2*z2 - b*f*h**2*x2 + b*f*h**2*y2 + 2*b*g**2*h*xz - 2*b*g*h**2*xy + f**3*yz - f**2*g*xz - f**2*h*xy + f*g*h*x2 - f*g*h*z2 + f*h**2*yz + g*h**2*xz - h**3*xy)/(b**4*f**4 + 2*b**4*f**2*g**2 + b**4*g**4 + 4*b**3*f**2*g*h + 4*b**3*g**3*h + 2*b**2*f**4 + 2*b**2*f**2*g**2 + 2*b**2*f**2*h**2 + 6*b**2*g**2*h**2 + 4*b*f**2*g*h + 4*b*g*h**3 + f**4 + 2*f**2*h**2 + h**4)

fig, ax = plt.subplots()
ax.plot(b, expr_graph)
ax.plot(b, expr)
plt.show()
