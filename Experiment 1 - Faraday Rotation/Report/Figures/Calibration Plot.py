# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:37:24 2021

@author: Nate
"""

import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

import scipy as sp 
from scipy.optimize import curve_fit 

#%matplotlib inline
#%config InlineBackend.figure_format = 'svg'

#constants
u = 4*np.pi*1E-7 # vacuum permeability, Tesla meter per amp 
n = 50/0.52 # turns in solenoid/m

# Returns magnitude of ideal B field in Tesla
def bfield(i): 
    return u*i*n

def bestFit(x, a0, a1):
    return a0+a1*x


# Dataframes
CalData = pd.read_csv("Hall_Sensor_Calibration.txt", comment = '#', sep=',', names=['i(A)','V(V)','di(A)','dV(V)'])


# B Field Tabulation and Plotting
B = bfield(CalData['i(A)'])*1000 # factor converts T to mT
CalData ['B(mT)'] = B

# now best curve WITH uncertainties
popt, pcov = curve_fit(bestFit, CalData['V(V)'], B) 
a0 = popt[0] # best fit y-int
a1 = popt[1] # best fit slope

xfit = np.linspace(0, 0.066, 1000)
yfit = bestFit(xfit, a0, a1)

print(CalData)

fig, ax = plt.subplots(1,2,figsize=(4,3))
fig.suptitle('Calibration constant k = {0:.3f} mT/V'.format(a1), fontsize=8)

ax[0].plot(CalData['V(V)'],CalData['i(A)'],'o',markersize=3)
ax[0].set_xlabel('Voltage (V)', fontsize=14)
ax[0].set_ylabel('Current(A)', fontsize=14)

ax[1].plot(xfit,yfit, label='Fit')
ax[1].errorbar(CalData['V(V)'],B, yerr=CalData['di(A)'], label='Data', linestyle='', marker='o', markersize=3, color='blue', 
            ecolor='red', capsize=2,)
ax[1].set_xlabel('Voltage (V)', fontsize=14)
ax[1].set_ylabel('Magnetic Field (mT)',fontsize=14)
ax[1].legend(labelcolor='black')



plt.tight_layout()
plt.savefig('Calibration Plot (PDF).pdf', format='pdf')
plt.savefig('Calibration Plot (SVG).svg', format='svg')
plt.show()

