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

# w0 = 0.8927 # hz natural frequency of oscillator
# gamma = 0.378 # damped param 

# steady state amplitude
def resonance(f, C, f0, gamma):
    term1 = (2*np.pi*f0)**2 - (2*np.pi*f)**2
    term2 = 2*gamma*2*np.pi*f
    denom = np.sqrt(term1**2 + term2**2)
    return C/denom


dresonance= pd.read_csv("damped driven oscillation.txt", comment = '#', sep=',', names=['ang displacement (rad)','f(hz)'])

f = dresonance['f(hz)'] 
A = dresonance['ang displacement (rad)'] 

# Obtained from Jupyer Notebook "Damped resonance notebook.ipy"
# Look here: C:\Users\Nate\_PHYS460\_Lab Reports\Experiment 2 - Torsion Oscillator
params = [1.705, 0.904, 0.394] # C, f0, gamma. 
xfit = np.linspace(0, 1.4, 1000)
yfit = resonance(xfit, *params)


plt.plot(xfit, yfit,linewidth=2, label='Fit')
plt.plot(f,A, marker='o', label='Data', c='orange', linestyle='None', mec='black')
plt.xlabel('Driving Frequency \u03C9 (hz)')
plt.ylabel('Max. Amplitude \u03B8 (rad) ')
plt.legend()
plt.tight_layout()
plt.savefig('Damped Resonance (PDF).pdf', format='pdf')
plt.savefig('Damped Resonance (SVG).svg', format='svg')
plt.show()
