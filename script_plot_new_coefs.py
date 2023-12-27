import matplotlib.pyplot as plt
import numpy as np
from quaternion import quaternion
import os
from math import sqrt

theta0_theo = 0.15

g_ref = 9.8
interv = 0.001
g_arr = np.array([0, 0, -1])
x_arr = np.array([1, 0, 0])
theta0_1 = 0.1
theta0_2 = 0.2
theta0_3 = 0.3
radius = 0.6
    

def quat_rotate(quat, vect):
    v_q = quaternion(0, *vect)
    res_q = quat * v_q * quat.conjugate()
    return np.array([res_q.x, res_q.y, res_q.z])

def quat1(vals):
    cos2theta = np.dot(vals, g_arr) 
    theta = np.arccos(cos2theta) / 2
    axis = np.cross(vals, g_arr)
    axis /= (np.sum(axis**2))**0.5
    return quaternion(np.cos(theta), np.sin(theta) * axis[0], np.sin(theta) * axis[1], np.sin(theta) * axis[2])

def quat2(vals, lat):
    vals = np.array(vals)
    vals /= (np.sum(vals**2))**0.5
    q1 = quat1(vals)
    lat_local = quat_rotate(q1, lat)
    cos2theta = np.dot(lat_local, x_arr)
    theta = np.arccos(cos2theta) / 2
    axis = np.cross(lat_local, x_arr)
    axis /= (np.sum(axis**2))**0.5
    q2 = quaternion(np.cos(theta), np.sin(theta) * axis[0], np.sin(theta) * axis[1], np.sin(theta) * axis[2])
    return q2 * q1

ii = 0
iis = []
fns = [fn for fn in os.listdir('D:\\gestures_zidian') if "data1_" in fn]
def so(fn):
    return int(fn[6:].split(".")[0])
fns.sort(key=so)
vect_f = []
vect_g = []
vect_h = []
vect_x = []
vect_y = []
vect_z = []
vectx2 = []
vecty2 = []
vectz2 = []
vectxy = []
vectxz = []
vectyz = []
i = 0
vect = []
for fn in fns:
    #print(fn)
    ii = (ii + 1) % 2 
    with open(fn, "r") as f:
        ff = f.readlines()
        ll_len = len(ff)
        for line in ff:
            i += 1
            vals = [float(v) for v in line.split()]
            assert len(vals) == 3
            iis.append(ii+9)
            if 180 <= i <= 220:
                vect_f.append(vals[0])
                vect_g.append(vals[1])
                vect_h.append(vals[2])
            if fn == "data1_1.txt":
                vectx2.append(vals[0]**2)
                vecty2.append(vals[1]**2)
                vectz2.append(vals[2]**2)
                vectxy.append(vals[0]*vals[1])
                vectxz.append(vals[0]*vals[2])
                vectyz.append(vals[1]*vals[2])
                vect_x.append(vals[0])
                vect_y.append(vals[1])
                vect_z.append(vals[2])
def get_qqq(vect_f, vect_g, vect_h, vectx2, vecty2, vectz2, vectxy, vectxz, vectyz):                
    f = sum(vect_f)/len(vect_f)
    g = sum(vect_g)/len(vect_g)
    h = sum(vect_h)/len(vect_h)
    g_local = np.array([f, g, h])
    x2 = sum(vectx2)               
    y2 = sum(vecty2)                
    z2 = sum(vectz2)                
    xy = sum(vectxy)                
    xz = sum(vectxz)                
    yz = sum(vectyz)
    
    x_mean = sum(vect_x)/len(vect_x)
    y_mean = sum(vect_y)/len(vect_y)
    z_mean = sum(vect_z)/len(vect_z)
    mean = np.array([x_mean, y_mean, z_mean])
    
    b = (-f**2*yz + f*g*xz + f*h*xy - g*h*x2)/(f**2*y2 - 2*f*g*xy + g**2*x2)
    c = 1
    a = -(b*g + h)/f
    
    k1 = (b*h - g*c)/(g*a - b*f)
    k2 = (c*f - h*a)/(g*a - b*f)
    z_1 = 1 / sqrt(k1**2 + k2**2 + 1)
    lat_1 = np.array([k1*z_1, k2*z_1, z_1]) # unit vector in plane perpendicular to local g
    lat_2 = -lat_1
    lat = lat_1 if np.dot(lat_1, mean) > 0 else lat_2
    qqq = quat2(g_local, lat)
    return qqq


a_s = []
qqq = get_qqq(vect_f, vect_g, vect_h, vectx2, vecty2, vectz2, vectxy, vectxz, vectyz)


for fn in fns: 
    with open(fn, "r") as f:
        ff = f.readlines()
        ll_len = len(ff)
        for line in ff:
            vals = [float(v) for v in line.split()]
            assert len(vals) == 3
            if fn == "data1_1.txt":
                a_s.append(quat_rotate(qqq, vals))

x_s = [a[0] for a in a_s]
y_s = [a[1] for a in a_s]
z_s = [a[2] for a in a_s]

def coef_sqr(y_s, x_s):
    print(x_s)
    x = sum(x_s)
    x4 = sum(i**4 for i in x_s)
    x3 = sum(i**3 for i in x_s)
    x2 = sum(i**2 for i in x_s)
    x2y = sum(x_s[i]**2*y_s[i] for i in range(len(x_s)))
    xy = sum(x_s[i]*y_s[i] for i in range(len(x_s)))
    y = sum(y_s)
    n = len(y_s)
    
    a = (-n*x2*x2y + n*x3*xy + x**2*x2y - x*x2*xy - x*x3*y\
        + x2**2*y)/(-n*x2*x4 + n*x3**2 + x**2*x4 - 2*x*x2*x3 + x2**3)
    b = (n*x2y*x3 - n*x4*xy - x*x2*x2y + x*x4*y + x2**2*xy\
        - x2*x3*y)/(-n*x2*x4 + n*x3**2 + x**2*x4 - 2*x*x2*x3 + x2**3)
    c = (-x*x2y*x3 + x*x4*xy + x2**2*x2y - x2*x3*xy - x2*x4*y\
        + x3**2*y)/(-n*x2*x4 + n*x3**2 + x**2*x4 - 2*x*x2*x3 + x2**3)
    return a, b, c

def coef_quat(y_s, x_s):
    x = int(sum(x_s))
    y = int(sum(y_s))
    x8 = int(sum(i**8 for i in x_s))
    x7 = int(sum(i**7 for i in x_s))
    x6 = int(sum(i**6 for i in x_s))
    x5 = int(sum(i**5 for i in x_s))
    x4 = int(sum(i**4 for i in x_s))
    x3 = int(sum(i**3 for i in x_s))
    x4y = int(sum(x_s[i]**4*y_s[i] for i in range(len(x_s))))
    x3y = int(sum(x_s[i]**3*y_s[i] for i in range(len(x_s))))
    x2y = int(sum(x_s[i]**2*y_s[i] for i in range(len(x_s))))
    x2 = int(sum(i**2 for i in x_s))
    xy = int(sum(x_s[i]*y_s[i] for i in range(len(x_s))))
    n = len(y_s)
    
    a = (-n*x2*x2y*x5*x7 + n*x2*x2y*x6**2 + n*x2*x3y*x4*x7 - n*x2*x3y*x5*x6\
        - n*x2*x4*x4y*x6 + n*x2*x4y*x5**2 + n*x2y*x3*x4*x7 - n*x2y*x3*x5*x6\
        - n*x2y*x4**2*x6 + n*x2y*x4*x5**2 - n*x3**2*x3y*x7 + n*x3**2*x4y*x6\
        + n*x3*x3y*x4*x6 + n*x3*x3y*x5**2 - 2*n*x3*x4*x4y*x5 + n*x3*x5*x7*xy\
        - n*x3*x6**2*xy - n*x3y*x4**2*x5 + n*x4**3*x4y - n*x4**2*x7*xy\
        + 2*n*x4*x5*x6*xy - n*x5**3*xy + x**2*x2y*x5*x7 - x**2*x2y*x6**2\
        - x**2*x3y*x4*x7 + x**2*x3y*x5*x6 + x**2*x4*x4y*x6 - x**2*x4y*x5**2\
        - x*x2*x2y*x4*x7 + x*x2*x2y*x5*x6 + 2*x*x2*x3*x3y*x7\
        - 2*x*x2*x3*x4y*x6 - x*x2*x3y*x4*x6 - x*x2*x3y*x5**2\
        + 2*x*x2*x4*x4y*x5 - x*x2*x5*x7*xy + x*x2*x6**2*xy - x*x2y*x3**2*x7\
        + 3*x*x2y*x3*x4*x6 - x*x2y*x3*x5**2 - x*x2y*x4**2*x5 - x*x3**2*x3y*x6\
        + 2*x*x3**2*x4y*x5 - 2*x*x3*x4**2*x4y + x*x3*x4*x7*xy - x*x3*x5*x6*xy\
        - x*x3*x5*x7*y + x*x3*x6**2*y + x*x3y*x4**3 - x*x4**2*x6*xy\
        + x*x4**2*x7*y + x*x4*x5**2*xy - 2*x*x4*x5*x6*y + x*x5**3*y\
        - x2**3*x3y*x7 + x2**3*x4y*x6 + x2**2*x2y*x3*x7 - x2**2*x2y*x4*x6\
        + x2**2*x3*x3y*x6 - 2*x2**2*x3*x4y*x5 + 2*x2**2*x3y*x4*x5\
        - x2**2*x4**2*x4y + x2**2*x4*x7*xy - x2**2*x5*x6*xy + x2**2*x5*x7*y\
        - x2**2*x6**2*y - x2*x2y*x3**2*x6 + x2*x2y*x4**3 - x2*x3**2*x3y*x5\
        + 3*x2*x3**2*x4*x4y - x2*x3**2*x7*xy - 2*x2*x3*x3y*x4**2\
        - 2*x2*x3*x4*x7*y + 2*x2*x3*x5**2*xy + 2*x2*x3*x5*x6*y\
        - x2*x4**2*x5*xy + 2*x2*x4**2*x6*y - 2*x2*x4*x5**2*y + x2y*x3**3*x5\
        - x2y*x3**2*x4**2 - x3**4*x4y + x3**3*x3y*x4 + x3**3*x6*xy\
        + x3**3*x7*y - 2*x3**2*x4*x5*xy - 2*x3**2*x4*x6*y - x3**2*x5**2*y\
        + x3*x4**3*xy + 3*x3*x4**2*x5*y - x4**4*y)/(-n*x2*x4*x6*x8\
        + n*x2*x4*x7**2 + n*x2*x5**2*x8 - 2*n*x2*x5*x6*x7 + n*x2*x6**3\
        + n*x3**2*x6*x8 - n*x3**2*x7**2 - 2*n*x3*x4*x5*x8 + 2*n*x3*x4*x6*x7\
        + 2*n*x3*x5**2*x7 - 2*n*x3*x5*x6**2 + n*x4**3*x8 - 2*n*x4**2*x5*x7\
        - n*x4**2*x6**2 + 3*n*x4*x5**2*x6 - n*x5**4 + x**2*x4*x6*x8\
        - x**2*x4*x7**2 - x**2*x5**2*x8 + 2*x**2*x5*x6*x7 - x**2*x6**3\
        - 2*x*x2*x3*x6*x8 + 2*x*x2*x3*x7**2 + 2*x*x2*x4*x5*x8\
        - 2*x*x2*x4*x6*x7 - 2*x*x2*x5**2*x7 + 2*x*x2*x5*x6**2\
        + 2*x*x3**2*x5*x8 - 2*x*x3**2*x6*x7 - 2*x*x3*x4**2*x8\
        + 4*x*x3*x4*x6**2 - 2*x*x3*x5**2*x6 + 2*x*x4**3*x7 - 4*x*x4**2*x5*x6\
        + 2*x*x4*x5**3 + x2**3*x6*x8 - x2**3*x7**2 - 2*x2**2*x3*x5*x8\
        + 2*x2**2*x3*x6*x7 - x2**2*x4**2*x8 + 4*x2**2*x4*x5*x7\
        - 2*x2**2*x4*x6**2 - x2**2*x5**2*x6 + 3*x2*x3**2*x4*x8\
        - 2*x2*x3**2*x5*x7 - x2*x3**2*x6**2 - 4*x2*x3*x4**2*x7\
        + 2*x2*x3*x4*x5*x6 + 2*x2*x3*x5**3 + 3*x2*x4**3*x6 - 3*x2*x4**2*x5**2\
        - x3**4*x8 + 2*x3**3*x4*x7 + 2*x3**3*x5*x6 - 3*x3**2*x4**2*x6\
        - 3*x3**2*x4*x5**2 + 4*x3*x4**3*x5 - x4**5)
    b = (n*x2*x2y*x5*x8 - n*x2*x2y*x6*x7 - n*x2*x3y*x4*x8 + n*x2*x3y*x6**2\
        + n*x2*x4*x4y*x7 - n*x2*x4y*x5*x6 - n*x2y*x3*x4*x8 + n*x2y*x3*x5*x7\
        + n*x2y*x4*x5*x6 - n*x2y*x5**3 + n*x3**2*x3y*x8 - n*x3**2*x4y*x7\
        - 2*n*x3*x3y*x5*x6 + n*x3*x4*x4y*x6 + n*x3*x4y*x5**2 - n*x3*x5*x8*xy\
        + n*x3*x6*x7*xy + n*x3y*x4*x5**2 - n*x4**2*x4y*x5 + n*x4**2*x8*xy\
        - n*x4*x5*x7*xy - n*x4*x6**2*xy + n*x5**2*x6*xy - x**2*x2y*x5*x8\
        + x**2*x2y*x6*x7 + x**2*x3y*x4*x8 - x**2*x3y*x6**2 - x**2*x4*x4y*x7\
        + x**2*x4y*x5*x6 + x*x2*x2y*x4*x8 - x*x2*x2y*x5*x7 - 2*x*x2*x3*x3y*x8\
        + 2*x*x2*x3*x4y*x7 + 2*x*x2*x3y*x5*x6 - x*x2*x4*x4y*x6\
        - x*x2*x4y*x5**2 + x*x2*x5*x8*xy - x*x2*x6*x7*xy + x*x2y*x3**2*x8\
        - x*x2y*x3*x4*x7 - x*x2y*x3*x5*x6 - x*x2y*x4**2*x6 + 2*x*x2y*x4*x5**2\
        - x*x3**2*x4y*x6 + 2*x*x3*x3y*x4*x6 - x*x3*x4*x8*xy + x*x3*x5*x8*y\
        + x*x3*x6**2*xy - x*x3*x6*x7*y - 2*x*x3y*x4**2*x5 + x*x4**3*x4y\
        + x*x4**2*x7*xy - x*x4**2*x8*y - x*x4*x5*x6*xy + x*x4*x5*x7*y\
        + x*x4*x6**2*y - x*x5**2*x6*y + x2**3*x3y*x8 - x2**3*x4y*x7\
        - x2**2*x2y*x3*x8 + x2**2*x2y*x4*x7 + x2**2*x3*x4y*x6\
        - 2*x2**2*x3y*x4*x6 - x2**2*x3y*x5**2 + 2*x2**2*x4*x4y*x5\
        - x2**2*x4*x8*xy + x2**2*x5*x7*xy - x2**2*x5*x8*y + x2**2*x6*x7*y\
        + x2*x2y*x3*x4*x6 + x2*x2y*x3*x5**2 - 2*x2*x2y*x4**2*x5\
        - x2*x3**2*x4y*x5 + x2*x3**2*x8*xy + 2*x2*x3*x3y*x4*x5\
        - 2*x2*x3*x4**2*x4y - x2*x3*x4*x7*xy + 2*x2*x3*x4*x8*y\
        - x2*x3*x5*x6*xy - x2*x3*x5*x7*y - x2*x3*x6**2*y + x2*x3y*x4**3\
        + 2*x2*x4**2*x6*xy - x2*x4**2*x7*y - x2*x4*x5**2*xy + x2*x5**3*y\
        - x2y*x3**2*x4*x5 + x2y*x3*x4**3 + x3**3*x4*x4y - x3**3*x8*y\
        - x3**2*x3y*x4**2 - x3**2*x4*x6*xy + x3**2*x4*x7*y + 2*x3**2*x5*x6*y\
        + 2*x3*x4**2*x5*xy - x3*x4**2*x6*y - 2*x3*x4*x5**2*y\
        - x4**4*xy + x4**3*x5*y)/(-n*x2*x4*x6*x8 + n*x2*x4*x7**2\
        + n*x2*x5**2*x8 - 2*n*x2*x5*x6*x7 + n*x2*x6**3 + n*x3**2*x6*x8\
        - n*x3**2*x7**2 - 2*n*x3*x4*x5*x8 + 2*n*x3*x4*x6*x7 + 2*n*x3*x5**2*x7\
        - 2*n*x3*x5*x6**2 + n*x4**3*x8 - 2*n*x4**2*x5*x7 - n*x4**2*x6**2\
        + 3*n*x4*x5**2*x6 - n*x5**4 + x**2*x4*x6*x8 - x**2*x4*x7**2\
        - x**2*x5**2*x8 + 2*x**2*x5*x6*x7 - x**2*x6**3 - 2*x*x2*x3*x6*x8\
        + 2*x*x2*x3*x7**2 + 2*x*x2*x4*x5*x8 - 2*x*x2*x4*x6*x7\
        - 2*x*x2*x5**2*x7 + 2*x*x2*x5*x6**2 + 2*x*x3**2*x5*x8\
        - 2*x*x3**2*x6*x7 - 2*x*x3*x4**2*x8 + 4*x*x3*x4*x6**2\
        - 2*x*x3*x5**2*x6 + 2*x*x4**3*x7 - 4*x*x4**2*x5*x6 + 2*x*x4*x5**3\
        + x2**3*x6*x8 - x2**3*x7**2 - 2*x2**2*x3*x5*x8 + 2*x2**2*x3*x6*x7\
        - x2**2*x4**2*x8 + 4*x2**2*x4*x5*x7 - 2*x2**2*x4*x6**2\
        - x2**2*x5**2*x6 + 3*x2*x3**2*x4*x8 - 2*x2*x3**2*x5*x7\
        - x2*x3**2*x6**2 - 4*x2*x3*x4**2*x7 + 2*x2*x3*x4*x5*x6 + 2*x2*x3*x5**3\
        + 3*x2*x4**3*x6 - 3*x2*x4**2*x5**2 - x3**4*x8 + 2*x3**3*x4*x7\
        + 2*x3**3*x5*x6 - 3*x3**2*x4**2*x6 - 3*x3**2*x4*x5**2 + 4*x3*x4**3*x5\
        - x4**5)
    c = (-n*x2*x2y*x6*x8 + n*x2*x2y*x7**2 + n*x2*x3y*x5*x8 - n*x2*x3y*x6*x7\
        - n*x2*x4y*x5*x7 + n*x2*x4y*x6**2 + n*x2y*x4**2*x8 - 2*n*x2y*x4*x5*x7\
        + n*x2y*x5**2*x6 - n*x3*x3y*x4*x8 + n*x3*x3y*x5*x7 + n*x3*x4*x4y*x7\
        - n*x3*x4y*x5*x6 + n*x3*x6*x8*xy - n*x3*x7**2*xy + n*x3y*x4*x5*x6\
        - n*x3y*x5**3 - n*x4**2*x4y*x6 + n*x4*x4y*x5**2 - n*x4*x5*x8*xy\
        + n*x4*x6*x7*xy + n*x5**2*x7*xy - n*x5*x6**2*xy + x**2*x2y*x6*x8\
        - x**2*x2y*x7**2 - x**2*x3y*x5*x8 + x**2*x3y*x6*x7 + x**2*x4y*x5*x7\
        - x**2*x4y*x6**2 + x*x2*x3y*x4*x8 - x*x2*x3y*x5*x7 - x*x2*x4*x4y*x7\
        + x*x2*x4y*x5*x6 - x*x2*x6*x8*xy + x*x2*x7**2*xy - 2*x*x2y*x3*x4*x8\
        + 2*x*x2y*x3*x5*x7 + 2*x*x2y*x4**2*x7 - 2*x*x2y*x4*x5*x6\
        + x*x3**2*x3y*x8 - x*x3**2*x4y*x7 - x*x3*x3y*x4*x7 - x*x3*x3y*x5*x6\
        + 3*x*x3*x4*x4y*x6 - x*x3*x4y*x5**2 + x*x3*x5*x8*xy - x*x3*x6*x7*xy\
        - x*x3*x6*x8*y + x*x3*x7**2*y - x*x3y*x4**2*x6 + 2*x*x3y*x4*x5**2\
        - x*x4**2*x4y*x5 - x*x4*x5*x7*xy + x*x4*x5*x8*y + x*x4*x6**2*xy\
        - x*x4*x6*x7*y - x*x5**2*x7*y + x*x5*x6**2*y - x2**2*x3*x3y*x8\
        + x2**2*x3*x4y*x7 + x2**2*x3y*x4*x7 - x2**2*x4*x4y*x6 + x2**2*x6*x8*y\
        - x2**2*x7**2*y + x2*x2y*x3**2*x8 - 2*x2*x2y*x3*x4*x7\
        + x2*x2y*x4**2*x6 - x2*x3**2*x4y*x6 + x2*x3*x3y*x4*x6\
        + x2*x3*x3y*x5**2 + x2*x3*x4*x8*xy - x2*x3*x5*x7*xy\
        - x2*x3*x5*x8*y + x2*x3*x6*x7*y - 2*x2*x3y*x4**2*x5 + x2*x4**3*x4y\
        - x2*x4**2*x7*xy - x2*x4**2*x8*y + x2*x4*x5*x6*xy + 3*x2*x4*x5*x7*y\
        - x2*x4*x6**2*y - x2*x5**2*x6*y - x2y*x3**2*x5**2 + 2*x2y*x3*x4**2*x5\
        - x2y*x4**4 + x3**3*x4y*x5 - x3**3*x8*xy - x3**2*x3y*x4*x5\
        - x3**2*x4**2*x4y + 2*x3**2*x4*x7*xy + x3**2*x4*x8*y + x3**2*x5*x6*xy\
        - x3**2*x5*x7*y + x3*x3y*x4**3 - 2*x3*x4**2*x6*xy - x3*x4**2*x7*y\
        - x3*x4*x5**2*xy + x3*x5**3*y + x4**3*x5*xy + x4**3*x6*y\
        - x4**2*x5**2*y)/(-n*x2*x4*x6*x8 + n*x2*x4*x7**2 + n*x2*x5**2*x8\
        - 2*n*x2*x5*x6*x7 + n*x2*x6**3 + n*x3**2*x6*x8 - n*x3**2*x7**2\
        - 2*n*x3*x4*x5*x8 + 2*n*x3*x4*x6*x7 + 2*n*x3*x5**2*x7\
        - 2*n*x3*x5*x6**2 + n*x4**3*x8 - 2*n*x4**2*x5*x7 - n*x4**2*x6**2\
        + 3*n*x4*x5**2*x6 - n*x5**4 + x**2*x4*x6*x8 - x**2*x4*x7**2\
        - x**2*x5**2*x8 + 2*x**2*x5*x6*x7 - x**2*x6**3 - 2*x*x2*x3*x6*x8\
        + 2*x*x2*x3*x7**2 + 2*x*x2*x4*x5*x8 - 2*x*x2*x4*x6*x7\
        - 2*x*x2*x5**2*x7 + 2*x*x2*x5*x6**2 + 2*x*x3**2*x5*x8\
        - 2*x*x3**2*x6*x7 - 2*x*x3*x4**2*x8 + 4*x*x3*x4*x6**2\
        - 2*x*x3*x5**2*x6 + 2*x*x4**3*x7 - 4*x*x4**2*x5*x6 + 2*x*x4*x5**3\
        + x2**3*x6*x8 - x2**3*x7**2 - 2*x2**2*x3*x5*x8 + 2*x2**2*x3*x6*x7\
        - x2**2*x4**2*x8 + 4*x2**2*x4*x5*x7 - 2*x2**2*x4*x6**2\
        - x2**2*x5**2*x6 + 3*x2*x3**2*x4*x8 - 2*x2*x3**2*x5*x7\
        - x2*x3**2*x6**2 - 4*x2*x3*x4**2*x7 + 2*x2*x3*x4*x5*x6 + 2*x2*x3*x5**3\
        + 3*x2*x4**3*x6 - 3*x2*x4**2*x5**2 - x3**4*x8 + 2*x3**3*x4*x7\
        + 2*x3**3*x5*x6 - 3*x3**2*x4**2*x6 - 3*x3**2*x4*x5**2 + 4*x3*x4**3*x5\
        - x4**5)
    d = (n*x2y*x3*x6*x8 - n*x2y*x3*x7**2 - n*x2y*x4*x5*x8 + n*x2y*x4*x6*x7\
        + n*x2y*x5**2*x7 - n*x2y*x5*x6**2 - n*x3*x3y*x5*x8 + n*x3*x3y*x6*x7\
        + n*x3*x4y*x5*x7 - n*x3*x4y*x6**2 + n*x3y*x4**2*x8 - n*x3y*x4*x5*x7\
        - n*x3y*x4*x6**2 + n*x3y*x5**2*x6 - n*x4**2*x4y*x7 + 2*n*x4*x4y*x5*x6\
        - n*x4*x6*x8*xy + n*x4*x7**2*xy - n*x4y*x5**3 + n*x5**2*x8*xy\
        - 2*n*x5*x6*x7*xy + n*x6**3*xy - x*x2*x2y*x6*x8 + x*x2*x2y*x7**2\
        + x*x2*x3y*x5*x8 - x*x2*x3y*x6*x7 - x*x2*x4y*x5*x7 + x*x2*x4y*x6**2\
        + x*x2y*x3*x5*x8 - x*x2y*x3*x6*x7 - x*x2y*x4*x5*x7 + x*x2y*x4*x6**2\
        - x*x3*x3y*x4*x8 + x*x3*x3y*x6**2 + x*x3*x4*x4y*x7 - x*x3*x4y*x5*x6\
        + x*x3y*x4**2*x7 - x*x3y*x4*x5*x6 - x*x4**2*x4y*x6 + x*x4*x4y*x5**2\
        + x*x4*x6*x8*y - x*x4*x7**2*y - x*x5**2*x8*y + 2*x*x5*x6*x7*y\
        - x*x6**3*y - x2**2*x3y*x4*x8 + x2**2*x3y*x5*x7 + x2**2*x4*x4y*x7\
        - x2**2*x4y*x5*x6 + x2**2*x6*x8*xy - x2**2*x7**2*xy + x2*x2y*x3*x4*x8\
        - x2*x2y*x3*x5*x7 - x2*x2y*x4**2*x7 + x2*x2y*x4*x5*x6\
        + x2*x3**2*x3y*x8 - x2*x3**2*x4y*x7 - x2*x3*x3y*x4*x7\
        - x2*x3*x3y*x5*x6 + 2*x2*x3*x4y*x5**2 - 2*x2*x3*x5*x8*xy\
        + 2*x2*x3*x6*x7*xy - x2*x3*x6*x8*y + x2*x3*x7**2*y + 2*x2*x3y*x4**2*x6\
        - x2*x3y*x4*x5**2 - x2*x4**2*x4y*x5 + 2*x2*x4*x5*x7*xy + x2*x4*x5*x8*y\
        - 2*x2*x4*x6**2*xy - x2*x4*x6*x7*y - x2*x5**2*x7*y + x2*x5*x6**2*y\
        - x2y*x3**3*x8 + 2*x2y*x3**2*x4*x7 + x2y*x3**2*x5*x6\
        - 2*x2y*x3*x4**2*x6 - x2y*x3*x4*x5**2 + x2y*x4**3*x5 + x3**3*x4y*x6\
        - x3**2*x3y*x4*x6 - 2*x3**2*x4*x4y*x5 + x3**2*x4*x8*xy + x3**2*x5*x8*y\
        - x3**2*x6**2*xy - x3**2*x6*x7*y + 2*x3*x3y*x4**2*x5 + x3*x4**3*x4y\
        - 2*x3*x4**2*x7*xy - x3*x4**2*x8*y + 2*x3*x4*x5*x6*xy\
        + 2*x3*x4*x6**2*y - x3*x5**2*x6*y - x3y*x4**4 + x4**3*x6*xy\
        + x4**3*x7*y - x4**2*x5**2*xy - 2*x4**2*x5*x6*y\
        + x4*x5**3*y)/(-n*x2*x4*x6*x8 + n*x2*x4*x7**2 + n*x2*x5**2*x8\
        - 2*n*x2*x5*x6*x7 + n*x2*x6**3 + n*x3**2*x6*x8 - n*x3**2*x7**2\
        - 2*n*x3*x4*x5*x8 + 2*n*x3*x4*x6*x7 + 2*n*x3*x5**2*x7\
        - 2*n*x3*x5*x6**2 + n*x4**3*x8 - 2*n*x4**2*x5*x7 - n*x4**2*x6**2\
        + 3*n*x4*x5**2*x6 - n*x5**4 + x**2*x4*x6*x8 - x**2*x4*x7**2\
        - x**2*x5**2*x8 + 2*x**2*x5*x6*x7 - x**2*x6**3 - 2*x*x2*x3*x6*x8\
        + 2*x*x2*x3*x7**2 + 2*x*x2*x4*x5*x8 - 2*x*x2*x4*x6*x7\
        - 2*x*x2*x5**2*x7 + 2*x*x2*x5*x6**2 + 2*x*x3**2*x5*x8\
        - 2*x*x3**2*x6*x7 - 2*x*x3*x4**2*x8 + 4*x*x3*x4*x6**2\
        - 2*x*x3*x5**2*x6 + 2*x*x4**3*x7 - 4*x*x4**2*x5*x6 + 2*x*x4*x5**3\
        + x2**3*x6*x8 - x2**3*x7**2 - 2*x2**2*x3*x5*x8 + 2*x2**2*x3*x6*x7\
        - x2**2*x4**2*x8 + 4*x2**2*x4*x5*x7 - 2*x2**2*x4*x6**2\
        - x2**2*x5**2*x6 + 3*x2*x3**2*x4*x8 - 2*x2*x3**2*x5*x7\
        - x2*x3**2*x6**2 - 4*x2*x3*x4**2*x7 + 2*x2*x3*x4*x5*x6 + 2*x2*x3*x5**3\
        + 3*x2*x4**3*x6 - 3*x2*x4**2*x5**2 - x3**4*x8 + 2*x3**3*x4*x7\
        + 2*x3**3*x5*x6 - 3*x3**2*x4**2*x6 - 3*x3**2*x4*x5**2 + 4*x3*x4**3*x5\
        - x4**5)
    e = (-x*x2y*x3*x6*x8 + x*x2y*x3*x7**2 + x*x2y*x4*x5*x8 - x*x2y*x4*x6*x7\
        - x*x2y*x5**2*x7 + x*x2y*x5*x6**2 + x*x3*x3y*x5*x8 - x*x3*x3y*x6*x7\
        - x*x3*x4y*x5*x7 + x*x3*x4y*x6**2 - x*x3y*x4**2*x8 + x*x3y*x4*x5*x7\
        + x*x3y*x4*x6**2 - x*x3y*x5**2*x6 + x*x4**2*x4y*x7 - 2*x*x4*x4y*x5*x6\
        + x*x4*x6*x8*xy - x*x4*x7**2*xy + x*x4y*x5**3 - x*x5**2*x8*xy\
        + 2*x*x5*x6*x7*xy - x*x6**3*xy + x2**2*x2y*x6*x8 - x2**2*x2y*x7**2\
        - x2**2*x3y*x5*x8 + x2**2*x3y*x6*x7 + x2**2*x4y*x5*x7\
        - x2**2*x4y*x6**2 - x2*x2y*x3*x5*x8 + x2*x2y*x3*x6*x7\
        - x2*x2y*x4**2*x8 + 3*x2*x2y*x4*x5*x7 - x2*x2y*x4*x6**2\
        - x2*x2y*x5**2*x6 + 2*x2*x3*x3y*x4*x8 - x2*x3*x3y*x5*x7\
        - x2*x3*x3y*x6**2 - 2*x2*x3*x4*x4y*x7 + 2*x2*x3*x4y*x5*x6\
        - x2*x3*x6*x8*xy + x2*x3*x7**2*xy - x2*x3y*x4**2*x7 + x2*x3y*x5**3\
        + 2*x2*x4**2*x4y*x6 - 2*x2*x4*x4y*x5**2 + x2*x4*x5*x8*xy\
        - x2*x4*x6*x7*xy - x2*x4*x6*x8*y + x2*x4*x7**2*y - x2*x5**2*x7*xy\
        + x2*x5**2*x8*y + x2*x5*x6**2*xy - 2*x2*x5*x6*x7*y + x2*x6**3*y\
        + x2y*x3**2*x4*x8 - x2y*x3**2*x5*x7 - x2y*x3*x4**2*x7 + x2y*x3*x5**3\
        + x2y*x4**3*x6 - x2y*x4**2*x5**2 - x3**3*x3y*x8 + x3**3*x4y*x7\
        + x3**2*x3y*x4*x7 + 2*x3**2*x3y*x5*x6 - 2*x3**2*x4*x4y*x6\
        - x3**2*x4y*x5**2 + x3**2*x5*x8*xy - x3**2*x6*x7*xy + x3**2*x6*x8*y\
        - x3**2*x7**2*y - x3*x3y*x4**2*x6 - 2*x3*x3y*x4*x5**2\
        + 3*x3*x4**2*x4y*x5 - x3*x4**2*x8*xy - 2*x3*x4*x5*x8*y\
        + 2*x3*x4*x6**2*xy + 2*x3*x4*x6*x7*y - x3*x5**2*x6*xy\
        + 2*x3*x5**2*x7*y - 2*x3*x5*x6**2*y + x3y*x4**3*x5 - x4**4*x4y\
        + x4**3*x7*xy + x4**3*x8*y - 2*x4**2*x5*x6*xy - 2*x4**2*x5*x7*y\
        - x4**2*x6**2*y + x4*x5**3*xy + 3*x4*x5**2*x6*y\
        - x5**4*y)/(-n*x2*x4*x6*x8 + n*x2*x4*x7**2 + n*x2*x5**2*x8\
        - 2*n*x2*x5*x6*x7 + n*x2*x6**3 + n*x3**2*x6*x8 - n*x3**2*x7**2\
        - 2*n*x3*x4*x5*x8 + 2*n*x3*x4*x6*x7 + 2*n*x3*x5**2*x7\
        - 2*n*x3*x5*x6**2 + n*x4**3*x8 - 2*n*x4**2*x5*x7 - n*x4**2*x6**2\
        + 3*n*x4*x5**2*x6 - n*x5**4 + x**2*x4*x6*x8 - x**2*x4*x7**2\
        - x**2*x5**2*x8 + 2*x**2*x5*x6*x7 - x**2*x6**3 - 2*x*x2*x3*x6*x8\
        + 2*x*x2*x3*x7**2 + 2*x*x2*x4*x5*x8 - 2*x*x2*x4*x6*x7\
        - 2*x*x2*x5**2*x7 + 2*x*x2*x5*x6**2 + 2*x*x3**2*x5*x8\
        - 2*x*x3**2*x6*x7 - 2*x*x3*x4**2*x8 + 4*x*x3*x4*x6**2\
        - 2*x*x3*x5**2*x6 + 2*x*x4**3*x7 - 4*x*x4**2*x5*x6 + 2*x*x4*x5**3\
        + x2**3*x6*x8 - x2**3*x7**2 - 2*x2**2*x3*x5*x8 + 2*x2**2*x3*x6*x7\
        - x2**2*x4**2*x8 + 4*x2**2*x4*x5*x7 - 2*x2**2*x4*x6**2\
        - x2**2*x5**2*x6 + 3*x2*x3**2*x4*x8 - 2*x2*x3**2*x5*x7\
        - x2*x3**2*x6**2 - 4*x2*x3*x4**2*x7 + 2*x2*x3*x4*x5*x6 + 2*x2*x3*x5**3\
        + 3*x2*x4**3*x6 - 3*x2*x4**2*x5**2 - x3**4*x8 + 2*x3**3*x4*x7\
        + 2*x3**3*x5*x6 - 3*x3**2*x4**2*x6 - 3*x3**2*x4*x5**2 + 4*x3*x4**3*x5\
        - x4**5)

    return a, b, c, d, e

def get_local_minima(seq):
    res = []
    for i in range(1, len(seq) - 1):
        if seq[i] < seq[i+1] and seq[i] < seq[i-1]:
            res.append((seq[i], i))
    return res

def start_end(x_s):
     local_is = get_local_minima(x_s)
     local_is.sort(key = lambda x: x[0])
     v1 = local_is[0]
     for v in local_is[1:]:
         if abs(v1[1] - v[1]) > 10:
             return sorted([v1[1], v[1]])
     

start, end = start_end(x_s)
#start += 5
#end -= 5
t_2 = list(range(end - start))
x_s_2 = x_s[start:end]
y_s_2 = y_s[start:end]
z_s_2 = z_s[start:end]
a1,b1,c1 = coef_sqr(x_s_2, t_2)
a2,b2,c2,d2,e2 = coef_quat(z_s_2, t_2)
xxx = [a1*i**2 + b1*i + c1 for i in t_2]
zzz = [a2*i**4 + b2*i**3 + c2*i**2 + d2*i + e2 for i in t_2]
t22 = list(range(start, end))
t = list(range(len(x_s)))
plt.plot(t, x_s)
plt.plot(t, y_s)
plt.plot(t, z_s)
plt.plot(t22, xxx)
plt.plot(t22, zzz)
plt.legend(["x", "y", "z", "x_pred", "z_pred"])
plt.show()
