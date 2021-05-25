# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:52:22 2021

@author: Nathan
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

import scipy as sp 
from scipy.optimize import curve_fit 

# c = 0.2
# w0 = 0.8927 # hz natural frequency of oscillator
# gamma = 0.378 # undamped 
N = 4000 # number of samples per data frame
TOTAL_TIME = 20 # total sample time, in seconds
PI = np.pi

def underDampedMotion(t, A, gamma, w1, d):
    exponent = (-1)*gamma*t
    argument = (w1*t) - d
    return A*np.exp(exponent)*np.cos(argument)

damped_osc = pd.read_csv("d5.lvm", comment = '#', delim_whitespace=True, 
                            names=['time (s)', 'ang vel (rad/s)', 'ang position (theta)'])


t = damped_osc['time (s)']
theta = damped_osc['ang position (theta)'] 
v = damped_osc['ang vel (rad/s)']

time_between_samples = TOTAL_TIME/N
zero_crossings = np.where(np.diff(np.sign(theta)))[0]
time_zero_crossings = []

# Store the time at each zero crossing
for i in zero_crossings:
    time_zero_crossings.append(t[i])
    
# motion crosses the x-axis three times for every wavelength 
period = []
i = 0
while i + 2 < len(time_zero_crossings):
    p = time_zero_crossings[i+2] - time_zero_crossings[i]
    period.append(p)
    i += 1
    
avg_period = np.mean(period)
print(avg_period) 

# convert to angular velocity
w = 2*PI/avg_period
print(w)

# Generate best fit parameters
popt, pcov = curve_fit(underDampedMotion, t, theta)
print('A, gamma, w1, d ', popt) 
A = popt[0]
gamma = popt[1]
w1 = popt[2]
d = popt[3]

xFit = np.linspace(0, 5, 1000)
yFit = underDampedMotion(xFit, A, gamma, w1, d)

plt.plot(xFit, yFit, label='Fit', linewidth=5)
plt.plot(t, theta, marker='o', markersize=2, linestyle='None', label='Data')
plt.xlabel('Time (s)', fontsize=16)
plt.ylabel('Displacement (Rad)', fontsize=16)
plt.tight_layout()
plt.legend(fontsize=16)
plt.savefig('Light Damping Motion (PDF).pdf', format='pdf')
plt.savefig('Light Damping Motion (SVG).svg', format='svg')
plt.show()
