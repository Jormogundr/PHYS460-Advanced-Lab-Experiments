# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:37:24 2021

@author: Nate
"""

import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

import scipy as sp 
from scipy.optimize import curve_fit 

def undrDmpdOsc(t, A, w0, gamma, d):
    exponent = (-1)*gamma*t
    argument = (w0*t-d)
    return A*np.exp(exponent)*np.cos(argument)

def exponent(t, gamma):
    exponent = (-1)*gamma*t
    return np.exp(exponent)

damped = pd.read_csv("d2.lvm", comment = '#', delim_whitespace=True, names=['Time(s)', 'Ang Vel(V)', 'Ang Disp(V)'])

t = damped['Time(s)']
theta = damped['Ang Disp(V)']
velocity = damped['Ang Vel(V)']

# Generate best fit parameters
popt, pcov = curve_fit(undrDmpdOsc, t, theta)
print(popt)
A = popt[0]
w0 = popt[1]
gamma = popt[2]
d = popt[3]

xFit = np.linspace(0, 5, 1000)
yFit = undrDmpdOsc(xFit, *popt)

#plt.plot(xFit, yFit, label='Best Fit')
plt.plot(t, theta, label='Angular Position Data', c='orange', marker='o', linestyle='None', markersize=1)
#plt.plot(t, velocity, label='Angular Velocity Data', c='blue')
plt.plot(t, exponent(t, gamma))
plt.legend()
plt.xlabel('Time (s)')

plt.tight_layout()
plt.savefig('Damped Harmonic Motion (PDF).pdf', format='pdf')
plt.savefig('Damped Harmonic Motion (SVG).svg', format='svg')
plt.show()