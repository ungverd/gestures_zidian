# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 19:58:34 2023

@author: User
"""
import matplotlib.pyplot as plt
def coef_sqr(y_s, x_s):
    print(x_s)
    print(y_s)
    x = sum(x_s)
    x4 = sum(i**4 for i in x_s)
    x3 = sum(i**3 for i in x_s)
    x2 = sum(i**2 for i in x_s)
    x2y = sum(x_s[i]**2*y_s[i] for i in range(len(x_s)))
    xy = sum(x_s[i]*y_s[i] for i in range(len(x_s)))
    y = sum(y_s)
    
    a = (x**2*x2y - x*x2*xy - x*x3*y + x2**2*y - x2*x2y + x3*xy)/(x**2*x4 - 2*x*x2*x3 + x2**3 - x2*x4 + x3**2)
    b = (-x*x2*x2y + x*x4*y + x2**2*xy - x2*x3*y + x2y*x3 - x4*xy)/(x**2*x4\
        - 2*x*x2*x3 + x2**3 - x2*x4 + x3**2)
    c = (-x*x2y*x3 + x*x4*xy + x2**2*x2y - x2*x3*xy - x2*x4*y\
         + x3**2*y)/(x**2*x4 - 2*x*x2*x3 + x2**3 - x2*x4 + x3**2)
    print((y_s[2] - (x_s[2]*(y_s[1]-y_s[0]) + x_s[1]*y_s[0] - x_s[0]*y_s[1])/(x_s[1] - x_s[0]))/(x_s[2]*(x_s[2] - x_s[0] - x_s[1]) + x_s[0]*x_s[1]))
    print(2*a*x4 + 2*b*x3 + 2*c*x2 - 2*x2y)
    print(2*a*x3 + 2*b*x2 + 2*c*x - 2*xy)
    print(2*a*x2 + 2*b*x + 2*c - 2*y)
    return a, b, c

a = 0.1
b = 12
c = -345
x = list(range(-25, 26, 25))
y = [a*xx**2 + b*xx + c for xx in x]
a1, b1, c1 = coef_sqr(y, x)
print(a1,b1,c1)
plt.plot(x,y)
y2 = [a1*xx**2 + b1*xx + c1 for xx in x]
plt.plot(x,y2)
plt.legend(["1", "2"])
plt.show()