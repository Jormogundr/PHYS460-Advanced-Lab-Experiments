# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:05:02 2021

@author: Nathan
"""

import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

import scipy as sp 
from scipy.optimize import curve_fit 

%matplotlib inline
%config InlineBackend.figure_format = 'svg'

# Consts
EQ = 2.882 # rads at equilibrium position
r = 0.01125 # meter, radius of hub
g = 9.81 # gravity

def bestFit(x, a0, a1):
    return a0+a1*x

def theta(data): # convert raw theta to delta theta
    return EQ-data

def torque(mass):
    return r*g*mass
        
    
CalData = pd.read_csv("Torsion Constant (txt).txt", comment = '#', sep=',', names=['Mass(g)','Theta Raw (rads)'])

m = CalData['Mass(g)']
t = theta(CalData['Theta Raw (rads)'])
CalData['Angular Displacement(rads)'] = t
tau = torque(m)
CalData['Torque (Nm)'] = tau
print(CalData)

popt, pcov = curve_fit(bestFit, t, tau) 
a0 = popt[0] # best fit y-int
a1 = popt[1] # best fit slope

print(a0, a1)
print(pcov)
print(np.sqrt(pcov[1][1]))

xfit = np.linspace(0, 1.5, 1000)
yfit = bestFit(xfit, a0, a1)

plt.plot(xfit, yfit, label='Best Fit')

plt.plot(t,tau,'o',markersize=7, mec='black', label='Data')
plt.xlabel('Angular Displacement \u03B8 (rad)', fontsize=16)
plt.ylabel('Torque (Nm)', fontsize=16)
plt.legend(fontsize=14)


plt.tight_layout()
plt.savefig('Calibration Plot (PDF).pdf', format='pdf')
plt.savefig('Calibration Plot (SVG).svg', format='svg')
plt.show()