# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:25:09 2021

@author: Nathan
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

import scipy as sp 
from scipy.optimize import curve_fit 

c = 1
w0 = 0.8927 # hz natural frequency of oscillator
gamma = 0.001 # undamped 

# steady state amplitude
def amplitude(w, c, wo, gamma):
    numerator = c
    denom1 = w0**2-w**2
    sqrtdenom1 = np.sqrt(denom1**2)
    denom2 = 4*gamma**2*w**2
    sqrtdenom2 = np.sqrt(4*gamma**2*w**2)
    return numerator/(sqrtdenom1 + sqrtdenom2)


uresonance= pd.read_csv("undamped driven oscillation.txt", comment = '#', sep=',', names=['ang displacement (rad)','f(hz)'])

w = uresonance['f(hz)'] # driving frequency, independent var
A = uresonance['ang displacement (rad)'] # dependent var

xfit = np.linspace(0.1, 1.3, 1000)
yfit = amplitude(xfit)

plt.scatter(w,A, marker='o')
plt.plot(xfit, yfit)
