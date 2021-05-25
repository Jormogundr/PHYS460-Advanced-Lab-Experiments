# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:32:37 2021

@author: Nathan

Calibration using spectra of ionized mercurcy (mercury lamp)
"""

# Calibration spectra from Mercury lamp.

import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

import scipy as sp 
from scipy.optimize import curve_fit 

def calibration(pixel1, I, c1, c2, c3):
    term1 = I
    term2 = c1*pixel1
    term3 = c2*pixel1**2
    term4 = c3*pixel1**3
    return term1 + term2 + term3 + term4

def line(x, a0, a1): # a line
    return a0+a1*x
    
cal_data = pd.read_csv("calibration data.txt", comment = '#', sep=',', names=['Wavelength (nm)', 'Pixel Num 1'])
lambda_true = cal_data['Wavelength (nm)']
pixel1 = cal_data['Pixel Num 1']

pixel2 = pixel1**2
pixel3 = pixel1**3

cal_data['Pixel Num 2'] = pixel2
cal_data['Pixel Num 3'] = pixel3

p = pixel1 + pixel2 + pixel3

# Find the calibration parameters
popt, pcov = curve_fit(calibration, pixel1, lambda_true) 
I = popt[0]
c1 = popt[1]
c2 = popt[2]
c3 = popt[3]
a = ['I', 'c1', 'c2', 'c3']
print('Calibration params are {0} = {1}'.format(a, popt))


# Calculate uncertainty for calibration equation
uI = np.sqrt(pcov[0][0])
uc1 = np.sqrt(pcov[1][1])
uc2 = np.sqrt(pcov[2][2])
uc3 = np.sqrt(pcov[3][3])
print("Uncertainty in coeffs C1, C2, C3: ", uc1, uc2, uc3)


# predict wavelength using the fit parameters
lambda_pred = []

for i in range(0, len(pixel1)):
    t = calibration(pixel1[i], *popt)
    lambda_pred.append(t)

diff = lambda_true - lambda_pred
cal_data['Predicted Wavelength (nm)'] = lambda_pred
cal_data['Difference'] = diff


# best fit curve
popt, pcov = curve_fit(line, pixel1, lambda_true)

# to plot
xfit = np.linspace(250,2000,1000)
yfit = line(xfit, *popt)
m = popt[1]

uYInt = np.sqrt(pcov[0][0])
uSlope = np.sqrt(pcov[1][1])
print("Y-Int, Slope: ", *popt)
print("Uncertainty in y-int, slope: ", uYInt, uSlope)

# Calculate R-Square for calibration line
# residuals = lambda_true - line(pixel1, *popt)
# ss_res = np.sum(residuals**2)
# ss_tot = np.sum((lambda_true - np.mean(lambda_true)**2))
# r_squared = 1 - (ss_res / ss_tot)
# print("R-squared:", r_squared)

# Generate LaTeX table
print(cal_data.to_latex(index=False))



plt.plot(xfit,yfit)
plt.plot(pixel1, lambda_true, linestyle='None', marker='o', mec='black', c='red')

plt.xlabel('Pixel Number', fontsize=16)
plt.ylabel('True Wavelength (nm)', fontsize=16)


plt.savefig('Calibration Plot (PDF).pdf', format='pdf')
plt.savefig('Calibration Plot (SVG).svg', format='svg')
plt.title('Calibration constant k = {0:.3f} Wavelength/Pixel'.format(m), fontsize=8)
plt.show()