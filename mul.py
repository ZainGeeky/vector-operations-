# -*- coding: utf-8 -*-
"""mul.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sUsQM-X9ioqzo8da2ragt7Wkn8OELfHr
"""

import numpy as np
import matplotlib.pyplot as plt
v1=[2,1]
v2=[1,5]
v=np.array(v1)
w=np.array(v2)
vw=v*w
print("vectors from list 1:")
print(v)
print("vectors from list 2:")
print(w)
print("Addition of 2 vectors")
print(vw)
origin=[0,0]
fig, ax =plt.subplots()
ax.set_xlim(-1, 11)
ax.set_ylim(-3, 8)
ax.quiver(origin[0], origin[1], v[0],v[1], angles='xy',scale_units='xy', scale=1, color='r')
ax.quiver(origin[0], origin[1], w[0],w[1], angles='xy',scale_units='xy', scale=1,color='g')
ax.quiver(origin[0], origin[1], vw[0],vw[1], angles='xy',scale_units='xy', scale=1,color='y')
plt.show