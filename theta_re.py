# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:20:49 2023

@author: User
"""

import re

diff1 = " - 2*a*t2x*cos(th) + 2*a*t2y*sin(th) + 2*a1*t4x*sin(th) + 2*a1*t4y*cos(th) - 2*b*tx*cos(th) + 2*b*ty*sin(th) + 2*b1*t3x*sin(th) + 2*b1*t3y*cos(th) - 2*c*x*cos(th) + 2*c*y*sin(th) + 2*c1*t2x*sin(th) + 2*c1*t2y*cos(th) + 2*d1*tx*sin(th) + 2*d1*ty*cos(th) + 2*e1*x*sin(th) + 2*e1*y*cos(th)"
diff2 = " + 2*a*t2x*sin(th) + 2*a*t2y*cos(th) + 2*a1*t4x*cos(th) - 2*a1*t4y*sin(th) + 2*b*tx*sin(th) + 2*b*ty*cos(th) + 2*b1*t3x*cos(th) - 2*b1*t3y*sin(th) + 2*c*x*sin(th) + 2*c*y*cos(th) + 2*c1*t2x*cos(th) - 2*c1*t2y*sin(th) + 2*d1*tx*cos(th) - 2*d1*ty*sin(th) + 2*e1*x*cos(th) - 2*e1*y*sin(th)"

reg_cos = r" [-,+] [^ ]+cos\(th\)"
reg_sin = r" [-,+] [^ ]+sin\(th\)"
print("".join(exp[:-8] for exp in re.findall(reg_cos, diff1)))
print()
print("".join(exp[:-8] for exp in re.findall(reg_sin, diff1)))
print()
print("".join(exp[:-8] for exp in re.findall(reg_cos, diff2)))
print()
print("".join(exp[:-8] for exp in re.findall(reg_sin, diff2)))