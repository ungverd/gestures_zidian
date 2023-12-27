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


def step(a_s_raw, a_s_axis, qqq):
    a_s_axis.append(quat_rotate(qqq, a_s_raw[-1]))
    
    

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


a_s_raw = []
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
                a_s_raw.append(np.array(vals))
                step(a_s_raw, a_s, qqq)

x_s = [a[0] for a in a_s]
y_s = [a[1] for a in a_s]
z_s = [a[2] for a in a_s]

def coef_theta(t_s, x_s, y_s, a, b, c, a1, b1, c1, d1, e1):
    x = sum(x_s)
    y = sum(y_s)
    t2x = sum(t_s[i]**2 + x_s[i] for i in range(len(t_s)))
    t2y = sum(t_s[i]**2 + y_s[i] for i in range(len(t_s)))
    t4x = sum(t_s[i]**4 + x_s[i] for i in range(len(t_s)))
    t4y = sum(t_s[i]**4 + y_s[i] for i in range(len(t_s)))
    t3x = sum(t_s[i]**3 + x_s[i] for i in range(len(t_s)))
    t3y = sum(t_s[i]**3 + y_s[i] for i in range(len(t_s)))
    tx = sum(t_s[i] + x_s[i] for i in range(len(t_s)))
    ty = sum(t_s[i] + y_s[i] for i in range(len(t_s)))
    
    coef = (-a*t2x + a1*t4y - b*tx + b1*t3y - c*x + c1*t2y + d1*ty + e1*y)/\
           (-a*t2y - a1*t4x - b*ty - b1*t3x - c*y - c1*t2x - d1*tx - e1*x)
    cosx = 1/(sqrt(coef**2 + 1))
    sinx = coef*cosx
    dif2 = cosx*(a*t2y + a1*t4x + b*ty + b1*t3x + c*y + c1*t2x + d1*tx + e1*x)\
         + sinx*(a*t2x - a1*t4y + b*tx - b1*t3y + c*x - c1*t2y - d1*ty - e1*y)
    if dif2 < 0:
        cosx = -cosx
        sinx = -sinx
    return sinx, cosx

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
     

t = np.arange(len(a_s))
'''plt.plot(t, x_s)
plt.plot(t, y_s)
plt.plot(t, z_s)'''
start, end = start_end(x_s)
start += 5
end -= 5
t_2 = list(range(end - start))
x_s_2 = x_s[start:end]
y_s_2 = y_s[start:end]
z_s_2 = z_s[start:end]
a1,b1,c1 = coef_sqr(x_s_2, t_2)
#a2,b2,c2,d2,e2 = coef_quat(z_s_2, t_2)
#t_2 = np.array(t_2)
xxx = [a1*i**2 + b1*i + c1 for i in t_2]
#zzz = [a2*i**4 + b2*i**3 + c2*i**2 + d2*i + e2 for i in t_2]
plt.plot(t_2, x_s_2)
plt.plot(t_2, y_s_2)
plt.plot(t_2, z_s_2)
plt.plot(t_2, xxx)
plt.plot(t_2, zzz)
plt.legend(["x", "y", "z", "x_pred", "z_pred"])
plt.show()
