import matplotlib.pyplot as plt
import numpy as np
import os

vectx2 = []
vecty2 = []
vectz2 = []
vectxy = []
vectxz = []
vectyz = []
with open("data1_1.txt", "r") as f:
    for line in f.readlines():
        vals = [float(v) for v in line.split()]
        vectx2.append(vals[0]**2)
        vecty2.append(vals[1]**2)
        vectz2.append(vals[2]**2)
        vectxy.append(vals[0]*vals[1])
        vectxz.append(vals[0]*vals[2])
        vectyz.append(vals[1]*vals[2])
                
print("x2", sum(vectx2))                
print("y2", sum(vecty2))                
print("z2", sum(vectz2))                
print("xy", sum(vectxy))                
print("xz", sum(vectxz))                
print("yz", sum(vectyz))
