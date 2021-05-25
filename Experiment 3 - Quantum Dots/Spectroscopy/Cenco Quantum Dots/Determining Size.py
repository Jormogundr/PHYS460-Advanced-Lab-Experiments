# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:18:38 2021

@author: Nathan
Determine the size of the quantum dotes based on their observed peak wavelengths.
"""
6
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

# Constants
Eg = 2.15E-19 # band gap energy, J
# Eg = 1.3419245088 # eV
me = 7.29E-32 # mass of electron, kg
mh = 5.47E-31 # mass of hole, kg
h = 6.626E-34 # plancks constant, Js
c = 2.998E8 # speed of light, m/s
eVtoJ = 1.602E-19  # number of J per eV - 
pi = np.pi



def energy(l): # zero point energy
    e = [] 
    for i in range(0, len(l)):
        t = (h*c)/l[i]
        e.append(t)
    return e

def radius(e):
    r = []
    for i in range(0, len(e)):
        num = h**2*pi**2
        denom = 2*(e[i]-Eg)*(me+mh)
        ratio = abs(num/denom)
        sqrt = np.sqrt(ratio)
        r.append(sqrt/2) # divide by two yields correct numbers but shouldn't appear according to eqn...
    
    return r

# Mathematica's solution for R
# def radius(e):
#     r = []
#     for i in range(0, len(e)):
#         num = h*np.sqrt(me + mh)*pi
#         denom = np.sqrt((-2*Eg*me*mh) + (2*me*mh*e[i]))
#         rad = num/denom
#         r.append(rad)
        
#     return r

def Gaussian(x, en):
    a0 = 0.5
    a2 = 0.25
    a1 = en
    exponent1 = (-0.5)*((x-a1)/a2)**2
    gauss1 = a0*np.exp(exponent1)
           
    return  gauss1


    

l = [626.97E-9, 591.82E-9, 562.68E-9, 532.43E-9] # Wavelengths of red, orange, yellow, green
l_nm = [627.0, 591.8, 562.7, 532.4]
#l = [630E-9, 600E-9, 570E-9, 540E-9] # meters

en = energy(l)
#energy = [1.9793787675606638, 2.0964152308810844, 2.204314571184753, 2.3605126223203743] # eV


       
# convert eV to J
# for i in range(0, len(energy)):
#      energy[i] = energy[i]*eVtoJ

  
radius = radius(en)

print(radius) # in meters


xaxis = np.linspace(0,3,1000)
yaxis = []


xaxis = np.linspace(0,3,1000)
yaxis = []

# convert J to eV
for i in range(0, len(en)):
        en[i] = en[i]/eVtoJ   
print(en)  

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


    
