# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:47:15 2021
PHYS401 HW 4 Q3.23

@author: Nate
"""

import numpy as np
import matplotlib.pyplot as plt  

#%matplotlib inline
#%config InlineBackend.figure_format = 'svg'

# Constants
A = 1
w = 1

def exponent(B, t):
    exponent = (-1)*B*t
    return np.exp(exponent)

def cosine(w, d, t):
    argument = (w*t)-d
    return np.cos(argument)

def undrDmpdOsc(A, w, B, d, t):
    exponent = (-1)*B*t
    argument = (w*t)-d
    return A*np.exp(exponent)*np.cos(argument)

t = np.linspace(0,20,100)
B = [0.1, 0.5, 0.9]
d = [0, np.pi/2, np.pi]

fig, ax = plt.subplots(1,3)


        
for i in range(0,3):
        x = undrDmpdOsc(A, w, B[i], d[i], t)
        ax[i].plot(t, exponent(B[i], t), linestyle='--', label='Decrement') # plot the exponent component
        ax[i].plot(t, cosine(w, d[i], t), '--', label='Harmonic') # plot the harmonic component
        ax[i].plot(t, x, label='Underdamped Oscillator', linewidth=2) # plot the underdamped component
        ax[i].set_title("\u03B2 = {0:.1f}, \u03B4 = {1:.3f}".format(B[i], d[i]))
        ax[i].set_xlabel('t')
        ax[i].set_ylabel('x')

plt.tight_layout()
plt.savefig('Theory Damped Oscillator (PDF).pdf', format='pdf')
plt.savefig('Theory Damped Oscillator (SVG)', format='svg')
plt.show()
