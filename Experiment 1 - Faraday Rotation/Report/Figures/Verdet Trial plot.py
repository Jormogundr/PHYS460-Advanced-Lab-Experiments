# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:10:11 2021

@author: Nate
"""
import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

import scipy as sp 
from scipy.optimize import curve_fit 

# Constants
k = 5.492 # Hall sensor calibration constant, mT/V
Bo = 2.027*k # gives the scaling factor Bo - used to find strength of magnetic field for various I
f = 0.961197042540088 # ratio of the b field integrated area over the maximum possible area 
L = 10 # cm

def bfield(i):
    return (i)*Bo

def line(x, a0, a1):
    return a0+a1*x
    
VerdetTrial = pd.read_csv("Verdet_Trial.txt", comment = '#', sep=',', names=['i(A)','Ang(deg)','di(a)','dAng(deg)'])
b = bfield(VerdetTrial['i(A)'])
theta = VerdetTrial['Ang(deg)']
VerdetTrial['B(mT)'] = b

print(VerdetTrial.to_latex(index=False))

popt, pcov = curve_fit(line, b, theta, sigma=VerdetTrial['dAng(deg)'])

fit = pd.DataFrame()
fit['x'] = np.linspace(0,34,100)
fit['y'] = line(fit['x'], *popt)

bestFitYInt = popt[0]
bestFitSlope= popt[1]

da0 = np.sqrt(pcov[0][0]) # uncertainty in y-int best fit
da1 = np.sqrt(pcov[1][1]) # uncertainty in slope best fit

verdet = bestFitSlope/(f*L) # degrees per mTcm
convertToSI = verdet*(np.pi/180)*1000*100 # convert degree/(mTcm) to rad/(Tm)

print(VerdetTrial)
print('Calculated verdet constant is ', verdet, " in SI: ", convertToSI, " rad/Tm")
print('Best fit params m = {} +/- {}, y-int = {} +/- {}'.format(bestFitSlope, da1, bestFitYInt, da0))

fig, ax = plt.subplots(1,2, figsize=(6.4,4.8))

ax[0].errorbar(VerdetTrial['i(A)'],VerdetTrial['Ang(deg)'],yerr=VerdetTrial['dAng(deg)'],linestyle='', marker='o', markersize=3, color='blue',ecolor='red',capsize=2)
ax[0].set_xlabel('Current (A)', fontsize=18)
ax[0].set_ylabel('Angle (degrees)', fontsize=18)

ax[1].errorbar(VerdetTrial['B(mT)'],VerdetTrial['Ang(deg)'],yerr=VerdetTrial['dAng(deg)'],linestyle='', marker='o', markersize=3, color='blue',ecolor='red',
               label='Data', capsize=2)
ax[1].plot(fit['x'], fit['y'], label='Fit', color='orange')
ax[1].set_xlabel('Magnetic Field (mT)', fontsize=18)
ax[1].set_ylabel('Angle (degrees)', fontsize=18)
ax[1].legend()


plt.tight_layout()
plt.savefig('Verdet Trial 1 (PDF).pdf', format='pdf')
plt.savefig('Verdet Trial 1 (SVG).svg', format='svg')
plt.show()


