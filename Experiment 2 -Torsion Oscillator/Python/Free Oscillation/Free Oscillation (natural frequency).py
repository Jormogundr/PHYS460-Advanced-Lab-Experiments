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

free_osc = pd.read_csv("free oscillation.lvm", comment = '#', delim_whitespace=True, 
                            names=['time (s)', 'ang vel (rad/s)', 'ang position (theta)'])


t = free_osc['time (s)']
theta = free_osc['ang position (theta)'] 
v = free_osc['ang vel (rad/s)']

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