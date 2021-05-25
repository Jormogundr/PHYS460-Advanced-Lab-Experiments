# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:59:24 2021

@author: Nathan
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt 

import scipy as sp 
from scipy.optimize import curve_fit 

# Constants
c = 343 # speed of sound, m/s
pi = np.pi


def normModeFreq(n,b):
    factor = c/(2*pi)
    radical1 = 0
    radical2 = (pi*n/b)**2
    return factor*np.sqrt(radical1 + radical2)

def hzToKhz(f):
    return f/1000
    
    
data1 = pd.read_csv("cyl height 30mm.txt", comment = '#', sep=',', names=['Peak #', 'Observed Modes (kHz)'])
n1 = data1['Peak #']
f1 = data1['Observed Modes (kHz)']
normal_modes1 = normModeFreq(n1, 0.030)

data2 = pd.read_csv("cyl height 20mm.txt", comment = '#', sep=',', names=['Peak #', 'Observed Modes (kHz)'])
n2 = data2['Peak #']
f2 = data2['Observed Modes (kHz)']
normal_modes1 = normModeFreq(n2, 0.020)


data3 = pd.read_csv("cyl height 50mm.txt", comment = '#', sep=',', names=['Peak #', 'Observed Modes (kHz)'])
n3 = data3['Peak #']
f3 = data3['Observed Modes (kHz)']
normal_modes3 = normModeFreq(n3, 0.050)


freq_N1 = hzToKhz(normModeFreq(n1, 0.030))
freq_N2 = hzToKhz(normModeFreq(n2, 0.020))
freq_N3 = hzToKhz(normModeFreq(n3, 0.050))

data1['f(n,0,0) modes (kHz)'] = freq_N1
data2['f(n,0,0) modes (kHz)'] = freq_N2
data3['f(n,0,0) modes (kHz)'] = freq_N3

print(data3)


