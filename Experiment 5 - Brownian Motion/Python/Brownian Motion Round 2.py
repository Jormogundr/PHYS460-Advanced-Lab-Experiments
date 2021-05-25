# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:06:11 2021

@author: Nathan
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt 

import scipy as sp 
from scipy.optimize import curve_fit 

# Constants
PIX_TO_MM = 0.65 # micrometer per pixel
steps = 116 # the frame for which analysis should end
N = 6 # number of particles tracked
SQ_MICRON_TO_SQ_METER = 1E-12
r = 5E-7 # radius of the beads
VISC = 1E-3 # viscosicty of distilled water
R =  8.314 # gas constant in J/molK
T = 294.05 # temperature in K 
NaACCEPTED = 6.02214076E23 # accepted avagadros


def pixel_to_mm(data):
    arr = []
    for i in range(0, len(data)):
        d = data[i] * PIX_TO_MM
        arr.append(d)
    return arr

def mean_square_disp(x):
    arr = []
    
    for t in range(0, steps): # time index is col
        r = 0
        for n in range(0, N): # particle number is row
            r += abs(x[n][t] - x[n][0])**2
        r = r/N
        arr.append(r)
    
    return arr

def line(x, a1): # best fit equation
    return a1*x

def Na(m): # determine avagradros number using the best fit slope
    num = R*T
    denom = 3*np.pi*m*VISC*r
    return num/denom



traj1 = pd.read_csv("Traj 1.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj2 = pd.read_csv("Traj 2.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj3 = pd.read_csv("Traj 3.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj4 = pd.read_csv("Traj 4.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj5 = pd.read_csv("Traj 5.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj6 = pd.read_csv("Traj 6.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])

# Read in the data
x1 = traj1['x (pixel)']
x2 = traj2['x (pixel)']
x3 = traj3['x (pixel)']
x4 = traj4['x (pixel)']
x5 = traj5['x (pixel)']
x6 = traj6['x (pixel)']

xdata = np.concatenate((x1,x2,x3,x4,x5,x6))
x_squared = xdata**2
x_squared_avg = np.mean(x_squared,axis=0)
x_squared_sdom = np.std(x_squared,ddof=1,axis=0)/np.sqrt(N)


x_arr = np.zeros((N,steps))
x_arr[0] = xdata[0:116]
x_arr[1] = xdata[116:232]
x_arr[2] = xdata[232:348]
x_arr[3] = xdata[348:464]
x_arr[4] = xdata[464:580]
x_arr[5] = xdata[580:696]

xdata = x_arr

#Plots the paths of all N particles in a 500 by 500 square.    
fig, ax = plt.subplots(1,1,figsize=(8,8))
for n in np.arange(N):
    ax.plot(xdata[n],'-',linewidth=0.6)
ax.set_xlabel('x position',fontsize=16)
ax.set_ylabel('y position',fontsize=16)
title = 'Particles = ' + str(N) + ', Steps = ' + str(steps) 
ax.set_title(title,fontsize=18, color='black')
plt.show()
