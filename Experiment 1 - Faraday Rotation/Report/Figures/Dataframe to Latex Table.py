# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:37:24 2021

@author: Nate
"""

import pandas as pd
import numpy as np

#constants
u = 4*np.pi*1E-7 # vacuum permeability, H/m
n = 50/0.52 # turns in solenoid/m

# Returns magnitude of ideal B field in Tesla
def bfield(i,n): 
    return u*i*n



CalData = pd.read_csv("Hall_Sensor_Calibration.txt", comment = '#', sep=',', names=['i(A)','V(V)','di(A)','dV(V)'])
BProfile = pd.read_csv("B_Profile.txt", comment = '#', sep=',', names=['z(cm)','V(V)','dz(cm)','dV(V)'])
VerdetTrial = pd.read_csv("Verdet_Trial.txt", comment = '#', sep=',', names=['i(A)','Ang(deg)','di(a)','dAng(deg)'])

# B Field Tabulation and Plotting
B = bfield(CalData['i(A)'], n)*1000 # factor converts T to mT
CalData ['B(mT)'] = B

print(CalData.to_latex(index=False))
#print(BProfile.to_latex(index=False))
#print(VerdetTrial.to_latex(index=False))