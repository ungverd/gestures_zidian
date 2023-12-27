import matplotlib.pyplot as plt
import numpy as np
from quaternion import quaternion
import os
from math import sqrt
from copy import deepcopy

g_ref = 9.8
interv_n = [0.01, 0.012, 0.014, 0.016, 0.018, 0.02]
interv = 0.01
g_arr = np.array([0, 0, -1])
x_arr = np.array([1, 0, 0])
theta0_1 = 0.1
theta0_2 = 0.2
theta0_3 = 0.3
radius = 0.5

FILENAME = "data1_10.txt"


def step(a_s_raw, a_s, v_s, thetas, g_vect, axis, errors, qqq, v_qqq, pos_qqq, theta_qqq, a_qqq, radius_s, a_s_axis, theta0, interv):
    a_s_axis.append(quat_rotate(qqq, a_s_raw[-1]))
    cos_th = np.cos(thetas[-1]/2)
    sin_th = np.sin(thetas[-1]/2)
    q = quaternion(cos_th, *(axis * sin_th))
    a_s.append((quat_rotate(q, -a_s_raw[-1]) + g_vect))

    cos_th_qqq = np.cos(theta_qqq[-1]/2)
    sin_th_qqq = np.sin(theta_qqq[-1]/2)
    q_qqq = quaternion(cos_th_qqq, 0, -sin_th_qqq, 0)
    a_qqq.append(quat_rotate(q_qqq, -a_s_axis[-1]) + g_arr*g_ref)
    v_qqq.append(v_qqq[-1] + interv * a_qqq[-1])
    pos_qqq.append(pos_qqq[-1] + interv * v_qqq[-1])
    theta_qqq_0 = np.arctan2(pos_qqq[-1][2], pos_qqq[-1][0])
    theta_qqq.append(theta_qqq_0 + np.pi/2 - theta0)
    radius_s.append(sqrt(pos_qqq[-1][0]**2 + pos_qqq[-1][2]**2))
    
    v_in_init = v_s[-1] + a_s[-1]*interv
    theta_p = (theta0 + thetas[-1]) / 2
    cos_p = np.cos(theta_p)
    sin_p = np.sin(theta_p)
    q_p = quaternion(cos_p, *(axis * sin_p))
    perp_in_init = np.cross(axis, quat_rotate(q_p, g_vect))
    perp_in_init /= sqrt(np.dot(perp_in_init, perp_in_init))
    perp = np.dot(v_in_init, perp_in_init)
    v_s.append(perp_in_init * perp)
    v_err = v_in_init - v_s[-1]
    errors.append(np.dot(v_err, v_err))
    thetas.append(thetas[-1] + perp * interv / radius)
    
    

def quat_rotate(quat, vect):
    v_q = quaternion(0, *vect)
    res_q = quat * v_q * quat.conjugate()
    return np.array([res_q.x, res_q.y, res_q.z])
    

'''def integr(v0, v1, v_prev):
    return v_prev + (v0 + v1) * interv / 2'''

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

'''vals_ex = np.array([-0.923076923076923, 0.371390676354104, 0.0999897974799508])
lat_ex = np.array([0.230769230769231, 0.742781352708208, -0.628507298445407])
q_ex = quat2(vals_ex, lat_ex)
x_ex = np.array([3/13, 4/13, 12/13])
y_ex = np.array([4/sqrt(29), 3/sqrt(29), -2/sqrt(29)])
z_ex = np.array([-44/13/sqrt(29), 54/13/sqrt(29), -7/13/sqrt(29)])
print("x", x_ex, quat_rotate(q_ex, np.array([1,0,0])))
print("y", y_ex, quat_rotate(q_ex, np.array([0,1,0])))
print("z", z_ex, quat_rotate(q_ex, np.array([0,0,1])))
print("must be [0 0 -1]", quat_rotate(q_ex, vals_ex))
print("must be [1 0 0]", quat_rotate(q_ex, lat_ex))
# print(quat_rotate(q_ex, z_ex))
print("+++++++++")
qq = quat1(vals_ex)
print(quat_rotate(qq, vals_ex))
print(vals_ex, quat_rotate(qq.conjugate(), g_arr))'''
    
    

def calc_g(vals):
    return (sum([val**2 for val in vals]))**0.5
def calc_a1(vals):
    return np.arctan2(vals[1], vals[0])
def calc_a2(vals):
    return np.arctan2(vals[2], (vals[1]**2 + vals[0]**2)**0.5)

ii = 0
iis = []
vect2 = []
fns = [fn for fn in os.listdir('D:\\gestures_zidian') if "data1_" in fn]
def so(fn):
    return int(fn[6:].split(".")[0])
fns.sort(key=so)
vect3 = []
vect4 = []
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
            vect2.append(calc_g(vals))
            vect3.append(calc_a1(vals))
            vect4.append(calc_a2(vals))
            iis.append(ii+9)
            if 180 <= i <= 220:
                vect.append(calc_g(vals))
                vect_f.append(vals[0])
                vect_g.append(vals[1])
                vect_h.append(vals[2])
            if fn == FILENAME:
                vectx2.append(vals[0]**2)
                vecty2.append(vals[1]**2)
                vectz2.append(vals[2]**2)
                vectxy.append(vals[0]*vals[1])
                vectxz.append(vals[0]*vals[2])
                vectyz.append(vals[1]*vals[2])
                vect_x.append(vals[0])
                vect_y.append(vals[1])
                vect_z.append(vals[2])
                
print(sum(vect)/len(vect))
f = sum(vect_f)/len(vect)
g = sum(vect_g)/len(vect)
h = sum(vect_h)/len(vect)
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

b = (f**3*y2/2 - f**3*z2/2 - f**2*g*xy + f**2*h*xz + f*g**2*x2/2 - f*g**2*z2/2 - f*h**2*x2/2 + f*h**2*y2/2 - f*sqrt(f**4*y2**2 - 2*f**4*y2*z2 + 4*f**4*yz**2 + f**4*z2**2 - 4*f**3*g*xy*y2 + 4*f**3*g*xy*z2 - 8*f**3*g*xz*yz - 8*f**3*h*xy*yz + 4*f**3*h*xz*y2 - 4*f**3*h*xz*z2 + 2*f**2*g**2*x2*y2 - 2*f**2*g**2*x2*z2 + 4*f**2*g**2*xy**2 + 4*f**2*g**2*xz**2 - 2*f**2*g**2*y2*z2 + 4*f**2*g**2*yz**2 + 2*f**2*g**2*z2**2 + 8*f**2*g*h*x2*yz - 4*f**2*g*h*y2*yz - 4*f**2*g*h*yz*z2 - 2*f**2*h**2*x2*y2 + 2*f**2*h**2*x2*z2 + 4*f**2*h**2*xy**2 + 4*f**2*h**2*xz**2 + 2*f**2*h**2*y2**2 - 2*f**2*h**2*y2*z2 + 4*f**2*h**2*yz**2 - 4*f*g**3*x2*xy + 4*f*g**3*xy*z2 - 8*f*g**3*xz*yz - 4*f*g**2*h*x2*xz + 8*f*g**2*h*xz*y2 - 4*f*g**2*h*xz*z2 - 4*f*g*h**2*x2*xy - 4*f*g*h**2*xy*y2 + 8*f*g*h**2*xy*z2 - 4*f*h**3*x2*xz - 8*f*h**3*xy*yz + 4*f*h**3*xz*y2 + g**4*x2**2 - 2*g**4*x2*z2 + 4*g**4*xz**2 + g**4*z2**2 + 4*g**3*h*x2*yz - 8*g**3*h*xy*xz - 4*g**3*h*yz*z2 + 2*g**2*h**2*x2**2 - 2*g**2*h**2*x2*y2 - 2*g**2*h**2*x2*z2 + 4*g**2*h**2*xy**2 + 4*g**2*h**2*xz**2 + 2*g**2*h**2*y2*z2 + 4*g**2*h**2*yz**2 + 4*g*h**3*x2*yz - 8*g*h**3*xy*xz - 4*g*h**3*y2*yz + h**4*x2**2 - 2*h**4*x2*y2 + 4*h**4*xy**2 + h**4*y2**2)/2 + g**2*h*xz - g*h**2*xy)/(f**3*yz - f**2*g*xz - f**2*h*xy + f*g**2*yz + f*g*h*x2 - f*g*h*y2 - g**3*xz + g**2*h*xy)
c = 1
a = -(b*g + h)/f

k1 = (b*h - g*c)/(g*a - b*f)
k2 = (c*f - h*a)/(g*a - b*f)
z_1 = 1 / sqrt(k1**2 + k2**2 + 1)
lat_1 = np.array([k1*z_1, k2*z_1, z_1])
lat_2 = -lat_1
lat = lat_1 if np.dot(lat_1, mean) > 0 else lat_2

# mean1 = mean - g_local * (np.dot(g_local, mean)/np.dot(g_local, g_local))
# print("dot", np.dot(lat_1/sqrt(np.dot(lat_1, lat_1)), mean1/sqrt(np.dot(mean1, mean1))))
# print("cross", np.cross(lat_1/sqrt(np.dot(lat_1, lat_1)), mean1/sqrt(np.dot(mean1, mean1))))
# lat = -mean1 / sqrt(np.dot(mean1, mean1))

qqq = quat2(g_local, lat)

axis = np.cross(g_local, lat)
axis /= sqrt(np.dot(axis, axis))
# print("qqq axis", quat_rotate(qqq, axis))

i = 0

a_s_raw = []
a_s = []
v_s = [np.array([0,0,0])]
thetas = [0]
errors = []
i_s = []
a_s_axis = []

v_qqq_1 = [np.array([0,0,0])]
pos_qqq_1 = [radius*np.array([np.sin(theta0_1), 0, -np.cos(theta0_1)])]
theta_qqq_1 = [0]
a_qqq_1 = [np.array([0,0,0])]
radius_s_1 = [radius]

def arr_fill(x, n):
    res = []
    for i in range(n):
        res.append(deepcopy(x))
    return res

v_qqq_n = arr_fill(v_qqq_1, 6)
pos_qqq_n = arr_fill(pos_qqq_1, 6)
theta_qqq_n = arr_fill(theta_qqq_1, 6)
a_qqq_n = arr_fill(a_qqq_1, 6)
radius_s_n = arr_fill(radius_s_1, 6)

for fn in fns: 
    with open(fn, "r") as f:
        ff = f.readlines()
        ll_len = len(ff)
        for line in ff:
            i += 1
            vals = [float(v) for v in line.split()]
            assert len(vals) == 3
            if fn == FILENAME:
                i_s.append(i)
                a_s_raw.append(np.array(vals))
                for j in range(6):
                    step(a_s_raw, a_s, v_s, thetas, g_local, axis, errors, qqq, v_qqq_n[j], pos_qqq_n[j], theta_qqq_n[j], a_qqq_n[j], radius_s_n[j], a_s_axis, theta0_1, interv_n[j])
i_s.append(i_s[-1] + 1)



errors.append(errors[-1])


# q_base = quat2(g_local, lat)
                
                

x = np.arange(len(vect2))
y = np.array(vect2)
y3 = np.array(vect3)
y4 = np.array(vect4)
y2 = np.array(iis)
fig, ax = plt.subplots()
#ax.plot(x, y)
#ax.plot(x, y2)
#ax.plot(x, y3)
#ax.plot(x, y4)
i_s = np.array(i_s)
a_s_axis = np.array(a_s_axis)
'''thetas = np.array(thetas)
ax.plot(i_s, thetas)'''
'''a_qqq = np.array(a_qqq)
ax.plot(i_s, a_qqq[:,0])
ax.plot(i_s, a_qqq[:,1])
ax.plot(i_s, a_qqq[:,2])
ax.plot(i_s, theta_qqq)'''
'''ax.plot(i_s, errors)
ax.plot(i_s, radius_s)'''
'''ax.plot(i_s, a_s_axis[:,0])
ax.plot(i_s, a_s_axis[:,1])
ax.plot(i_s, a_s_axis[:,2])'''
'''ax.plot(i_s, theta_qqq_1)
ax.plot(i_s, theta_qqq_2)
ax.plot(i_s, theta_qqq_3)'''
'''for j in range(6):
    radius_s_n[j] = np.array(radius_s_n[j])
    ax.plot(i_s, radius_s_n[j])'''
ax.plot(i_s, theta_qqq_n[0])
ax.plot(i_s, radius_s_n[0])
#ax.legend(["10", "12", "14", "16", "18", "20"])
ax.legend(["theta", "radius"])
plt.show()
