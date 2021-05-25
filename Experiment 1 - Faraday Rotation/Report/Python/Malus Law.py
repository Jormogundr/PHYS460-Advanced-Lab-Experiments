# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:35:48 2021

@author: Nate
"""

import numpy as np
import matplotlib.pyplot as plt

# to output .svg vector plot
%matplotlib inline
%config InlineBackend.figure_format = 'svg'

# Malus's Law
def f(theta):
    return (np.cos(theta))**2

I_o = 1
x = np.linspace(0,2*np.pi, 1000) # radians
y = f(x)*I_o

x_tick = [0, np.pi/2, np.pi, (3/2)*np.pi, 2*np.pi]
x_label = [r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$",   r"$2\pi$"]


fig = plt.figure()
ax  = fig.add_subplot(111)
plt.grid(b=True, which='both')
ax.plot(x,y, c='red', linewidth=3)

ax.set_xticks(x_tick)
ax.set_xticklabels(x_label, fontsize=15)

plt.xlabel("\u03B8", fontsize=15)
plt.ylabel("Icos\u00b2(\u03B8)", fontsize=15)
plt.xlim(0, (2*np.pi))
plt.show()