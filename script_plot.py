import matplotlib.pyplot as plt
import numpy as np
import os

def calc_mean_g(line):
    vals = [float(v)**2 for v in line.split()]
    assert len(vals) == 3
    return (sum(vals))**0.5

n = 8
vect2 = []
for fn in os.listdir('D:\\gestures_zidian'):
    if "data1_" in fn:
        with open(fn, "r") as f:
            vect = []
            for _ in range(n):
                vect.append(calc_mean_g(f.readline()))
            vect2.append(sum(vect)/n)
                
                

x = np.arange(len(vect2))
y = np.array(vect2)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
