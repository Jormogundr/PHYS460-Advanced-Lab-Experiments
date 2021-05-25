# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:47:59 2021

@author: Nathan
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt 

import scipy as sp 
from scipy.optimize import curve_fit 

# Constants
l = 13.5 # cm, length from cathode tube to end of diffraction tube
dIN = 2.13 # angstrom, accepted value for atomic spacing
dOUT = 1.23 # angstrom, accepted value for atomic spacing

# Convert radius to diameter
def D(R): 
    arr = []
    
    for i in range(1, len(R)):
        R[i] = float(R[i]) # convert R to a float, it is read as a str
        t = R[i]*2
        arr.append(t)
    return arr
    
    
def invSqrVoltage(V):
    arr = []
    for i in range(0, len(V)):
        t = 1/(np.sqrt(V[i]))
        arr.append(t)
    return arr

def line(x, a0, a1):
    return a0 + a1*x


m2_data = pd.read_csv("Method 1 Data Trial 2 RND Out.csv", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)',
                                                                                  'ThetaIn(deg)', 'ThetaOut(deg)', 'Wavelength(angstrom)', 'dIn(angstrom)','dOut(angstrom)', 
                                                                                  'dInAvg(ang)', 'dOutAvg(ang)'])

v = m2_data['V(kV)']
rin = m2_data['Rin(cm)']
rout = m2_data['Rout(cm)']



inv = invSqrVoltage(vol)
Din = D(rin)
Dout = D(rout)

# Generate best fit parameters
popt, pcov = curve_fit(line, inv, Din) 

# Calculate residuals
m2_data['e'] = Din - line(inv,*popt)


