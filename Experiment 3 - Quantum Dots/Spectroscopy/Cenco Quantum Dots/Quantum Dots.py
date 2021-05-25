# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:32:37 2021

@author: Nathan
"""

import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt 

# Constants
h = 4.1357E-15 # plancks constant, ev s
c = 2.998E8 # speed of light, m/s 
jtoEv = 6.242E18 # number of eV per J - J to eV conversion factor
pi = np.pi
T = 295.4833 # K 
k = 8.617E-5 # eV


def cnvrtWavLenToEn(l):
    return (h*c)/l

def intensity(l):
    factor_num = (2*pi*h*c**2)
    factor_denom = l**5
    exponent_factor_num = (h*c)
    exponent_factor_denom = l*k*T
    exponent = (-1)*np.exp(exponent_factor_num/exponent_factor_denom - 1)
    return (factor_num/factor_denom)*exponent

def energy(l): # zero point energy
    e = [] 
    for i in range(0, len(l)):
        t = (h*c)/l[i]
        t = t
        e.append(t)
    return e

# Use arbitrary units to generate Gaussian curve.

def Gaussian(x, en):
    a0 = 0.5
    a2 = 0.25
    a1 = en
    exponent1 = (-0.5)*((x-a1)/a2)**2
    gauss1 = a0*np.exp(exponent1)
           
    return  gauss1

l = [626.97E-9, 591.82E-9, 562.68E-9, 532.43E-9] # Wavelengths of red, orange, yellow, green
l_nm = [627.0, 591.8, 562.7, 532.4]
en = energy(l) # energy of l in eV
print('en', en)

xaxis = np.linspace(0,3,1000)
yaxis = []

for i in range(0, len(en)):
    t = Gaussian(xaxis, en[i])
    yaxis.append(t)
    
plt.plot(xaxis, yaxis[0], label='\u03BB = {} nm, E = {:.2f} eV'.format(l_nm[0], en[0]), c='Red')
plt.plot(xaxis, yaxis[1], label='\u03BB = {} nm, E = {:.2f} eV'.format(l_nm[1], en[1]), c='Orange')
plt.plot(xaxis, yaxis[2], label='\u03BB = {} nm, E = {:.2f} eV'.format(l_nm[2], en[2]), c='Gold')
plt.plot(xaxis, yaxis[3], label='\u03BB = {} nm, E = {:.2f} eV'.format(l_nm[3], en[3]), c='Green')
plt.xlabel('Energy (eV)', fontsize=16)
plt.ylabel('Intensity (a.u.)', fontsize=16)
plt.xlim(0.5, 3)
plt.grid(b=True, which='both')
plt.yticks([])
plt.legend()
plt.tight_layout()
plt.savefig('Intensity vs Wavelength (PDF).pdf', format='pdf')
plt.savefig('Intensity vs Wavelength (SVG)', format='svg')
plt.show()

