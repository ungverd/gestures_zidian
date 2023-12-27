import matplotlib.pyplot as plt
import numpy as np
from quaternion import quaternion
import os
from math import sqrt, inf
DIR = "/media/eka/Новый том/gestures_zidian"


g_arr = np.array([0, 0, -1])
x_arr = np.array([1, 0, 0])
    

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

def get_qqq(vect_f, vect_g, vect_h, vectx2, vecty2, vectxy, vectxz, vectyz):
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

def get_local_minima(seq):
    res = [(seq[0], 0), (seq[-1], len(seq) - 1)]
    for i in range(1, len(seq) - 1):
        if seq[i] <= seq[i+1] and seq[i] <= seq[i-1]:
            res.append((seq[i], i))
    return res

def start_end(x_s):
     local_is = get_local_minima(x_s)
     local_is.sort(key = lambda x: x[0])
     v1 = local_is[0]
     for v in local_is[1:]:
         if abs(v1[1] - v[1]) > 10:
             return sorted([v1[1], v[1]])

def start_end_2(no):
    i1 = 0
    while no[i1] < 90:
        i1 += 1
    i2 = len(no) - 1
    while no[i2] < 90:
        i2 -= 1
    return i1, i2

def my_argmax(z_s):
    ma = -inf
    i_ma = 0
    for i in range(len(z_s) - 6):
        zz = sum(z_s[i:i+7])
        if zz > ma:
            ma = zz
            i_ma = i + 3
    return i_ma

ii = 0
iis = []
fns = [fn for fn in os.listdir(DIR) if "data2_" in fn]
def so(fn):
    return int(fn[6:].split(".")[0])
fns.sort(key=so)

qqqs = []
for fn in fns:
    with open(fn, "r") as f:
        ff = f.readlines()
        ll_len = len(ff)
        vect_f = []
        vect_g = []
        vect_h = []
        vect_x = []
        vect_y = []
        vect_z = []
        vectx2 = []
        vecty2 = []
        vectxy = []
        vectxz = []
        vectyz = []
        for i, line in enumerate(ff):
            vals = [float(v) for v in line.split()]
            assert len(vals) == 3
            if i <= 35:
                vect_f.append(vals[0])
                vect_g.append(vals[1])
                vect_h.append(vals[2])
            vectx2.append(vals[0]**2)
            vecty2.append(vals[1]**2)
            vectxy.append(vals[0]*vals[1])
            vectxz.append(vals[0]*vals[2])
            vectyz.append(vals[1]*vals[2])
            vect_x.append(vals[0])
            vect_y.append(vals[1])
            vect_z.append(vals[2])
    qqqs.append(get_qqq(vect_f, vect_g, vect_h, vectx2, vecty2, vectxy, vectxz, vectyz))


mesurements = 0
sums = [0] * 40
z_ss = []
for i, fn in enumerate(fns): 
    with open(fn, "r") as f:
        ff = f.readlines()
        ll_len = len(ff)
        a_s = []
        for line in ff:
            vals = [float(v) for v in line.split()]
            assert len(vals) == 3
            a_s.append(quat_rotate(qqqs[i], vals))
    #no = [a[0]**2 + a[1]**2 + a[2]**2 for a in a_s]
    #plt.plot(range(len(no)), no)
    x_s = [a[0] for a in a_s]
    y_s = [a[1] for a in a_s]
    z_s = [a[2] for a in a_s]
    no = [a[0]**2 + a[1]**2 for a in a_s]
    no2 = [a**0.5 for a in no]
    start, end = start_end_2(no)
    #start += 5
    #end -= 5
    len_data = end - start
    if 40 < len_data < 60:
        mesurements += 1
        t_2 = list(range(end - start))
        x_s_2 = x_s[start:end]
        #y_s_2 = y_s[start:end]
        z_s_2 = z_s[start:end]
        i_ma = my_argmax(z_s_2)
        i_ma2 = start + i_ma
        t = list(range(-20, 20))
        #plt.plot(t, x_s_2)
        #plt.plot(t, y_s)
        z_s_3 = z_s[i_ma2 - 20: i_ma2 + 20]
        no3 = no2[i_ma2 - 20: i_ma2 + 20]
        z_ss.append(no3)
        for i, z in enumerate(no3):
            sums[i] += z
        #plt.plot(t, no2[i_ma2 - 20: i_ma2 + 20])
err_max = 0
avrs = [s / mesurements for s in sums]
for zz in z_ss:
    err = 0
    for i, z in enumerate(zz):
        err += (z - avrs[i])**2
    if err > err_max:
        err_max = err

plt.plot(range(40), avrs)
print(mesurements)
print(avrs)
print(err_max)
plt.show()
