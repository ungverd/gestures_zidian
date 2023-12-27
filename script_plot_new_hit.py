import matplotlib.pyplot as plt
import numpy as np
from quaternion import quaternion
import os
from math import sqrt
DIR = "/media/eka/Новый том/gestures_zidian"


g_arr = np.array([0, 0, -1])
x_arr = np.array([1, 0, 0])
    


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
     
ii = 0
iis = []
fns = [fn for fn in os.listdir(DIR) if "data3_" in fn]
def so(fn):
    return int(fn[6:].split(".")[0])
fns.sort(key=so)
#fns = [fn for fn in fns if 0 < so(fn) < 12]

qqqs = []
for fn in fns:
    with open(fn, "r") as f:
        ff = f.readlines()
        ll_len = len(ff)
        vect_x = []
        vect_y = []
        vect_z = []
        vect_tot = []
        for i, line in enumerate(ff):
            vals = [float(v) for v in line.split()]
            assert len(vals) == 3
            vect_x.append(vals[0])
            vect_y.append(vals[1])
            vect_z.append(vals[2])
            vect_tot.append(vals[0]**2 + vals[1]**2 + vals[2]**2)
    a_max = 0
    i_max = 0
    finished = False
    i = len(vect_tot) - 2
    while not finished:
        if vect_tot[i] > 800:
            if vect_tot[i-1] < vect_tot[i] and vect_tot[i+1] < vect_tot[i]:
                i_max = i
                finished = True
        i -= 1
    

    if 1 < i_max < (len(vect_tot) - 2):
        plt.plot(range(5), vect_tot[i_max - 2: i_max + 3])
        print(max(vect_tot[i_max] - vect_tot[i_max + 1], vect_tot[i_max] - vect_tot[i_max - 1]))
    '''print(max(vect_x))
    print(max(vect_y))
    print(max(vect_z))'''
    '''if fn == "data3_1.txt":
        plt.plot(range(len(vect_tot)), vect_tot)'''
plt.show()
