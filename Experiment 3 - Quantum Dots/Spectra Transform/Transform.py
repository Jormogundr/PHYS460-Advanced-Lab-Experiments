# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:46:06 2021

@author: Nathan

Use your calibration coefficients to transform spectra from intensity vs. pixel to
intensity vs. wavelength
"""
#Spectra is from Mercury lamp.

import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

import scipy as sp 
from scipy.optimize import curve_fit 

def transform(pix, I, c1, c2, c3):
    term1 = I
    term2 = c1*pix
    term3 = c2*pix**2
    term4 = c3*pix**3
    return term1 + term2 + term3 + term4

a = ['I', 'c1', 'c2', 'c3'] # fit param ordering
cal_params =  [1.68754985e+02, 2.63820865e-01, -5.61298074e-05 , 1.54206416e-08] # fit params from calibration.py

# transform pixel number to wavelength
pix_data = pd.read_csv("pixel v intensity.txt", comment = '#', delim_whitespace=True, names=['Pixel Num', 'Intensity'])
pix = pix_data['Pixel Num']

intensity1 = pix_data['Intensity']
l1 = transform(pix, *cal_params) # lambda
pix_data['Wavelength (nm)'] = l1

int_data = pd.read_csv("wavelength vs intensity.txt", comment = '#', delim_whitespace=True, names=['Wavelength (nm)', 'Intensity'])
l2 = int_data['Wavelength (nm)']
intensity2 = int_data['Intensity']


plt.plot(l1, intensity1, label='Transformed Spectra') # transformed pixel number to wavelength  vs intensity
plt.plot(l2, intensity2, label='Spectra') # wavelength vs intensity spectra, collected (SEPARATE DATA SET)
plt.legend(fontsize=16)
plt.xlim(240,600)
plt.xlabel('Wavelength (nm)', fontsize=16)
plt.ylabel('Intensity', fontsize=16)
plt.tight_layout()

plt.savefig('Transformed Spectra vs Spectra (PDF).pdf', format='pdf')
plt.savefig('Transformed Spectra vs Spectra (SVG).svg', format='svg')
plt.show()

# clearly from the plot the spectrometer needs calibration! Peaks do not match