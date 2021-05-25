# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:20:41 2021

@author: Nathan

METHOD 1

Setup the electron diffraction setup using Tel-Atomic 555 electron diffraction tube and the
necessary power supply. Check your circuit before turning on the power. You will see two
diffraction rings on the fluorescent screen as shown in Fig. 1.Calculate the θ by the measured
values of the ring radius (R) and the distance L using tan(2θ) = R/L. Measure the angle θ for
various values of the accelerating voltages (at several values between 2.5 to 6.9 kV) and
calculate d values for both inner and outer rings.

Fifth trial is best according to the percent error.
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt 

# Constants
l = 13.5 # cm, length from cathode tube to end of diffraction tube
dIN = 2.13 # angstrom, accepted value for atomic spacing
dOUT = 1.23 # angstrom, accepted value for atomic spacing
N = 12 # number of samples per trial

def theta(R):
    return np.arctan(R/l)/2

def r_star(theta): # correction factor - project the sphereical radius r to planar surface r*
    return l*np.tan(theta)/2

def wavelength(V): # in angstrom
    V = V*1000 # convert to kV to V
    return np.sqrt(150/V)

def dval(theta, wl):
    return wl/(2*np.sin(theta))

def dAvg(d):
    n = len(d)
    t = 0
    
    for i in range(0, len(d)):
        t += d[i]
        
    return t/n


# Generate percent error between observed value and accepted value for te outer ring
# atomic plane spacing
def errorDout(dObserved):
    return abs(dObserved - dOUT)/dOUT*100

# Generate percent error between observed value and accepted value for te inner ring
# atomic plane spacing
def errorDin(dObserved):
    return abs(dObserved - dIN)/dIN*100

        

m1_data = pd.read_csv("Method 1 Data Trial 1.txt", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)'])
m2_data = pd.read_csv("Method 1 Data Trial 2 RND.txt", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)'])
m3_data = pd.read_csv("Method 1 Data Trial 3.txt", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)'])
m4_data = pd.read_csv("Method 1 Data Trial 4.txt", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)'])
m5_data = pd.read_csv("Method 1 Data Trial 5.txt", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)'])

thetaIn1 = theta(m1_data['Rin(cm)'])
thetaOut1 = theta(m1_data['Rout(cm)'])
thetaIn2 = theta(m2_data['Rin(cm)'])
thetaOut2 = theta(m2_data['Rout(cm)'])
thetaIn3 = theta(m3_data['Rin(cm)'])
thetaOut3 = theta(m3_data['Rout(cm)'])
thetaIn4 = theta(m4_data['Rin(cm)'])
thetaOut4 = theta(m4_data['Rout(cm)'])
thetaIn5 = theta(m5_data['Rin(cm)'])
thetaOut5 = theta(m5_data['Rout(cm)'])

m1_data['ThetaIn(deg)'] = thetaIn1
m1_data['ThetaOut(deg)'] = thetaOut1
m2_data['ThetaIn(deg)'] = thetaIn2
m2_data['ThetaOut(deg)'] = thetaOut2
m3_data['ThetaIn(deg)'] = thetaIn3
m3_data['ThetaOut(deg)'] = thetaOut3
m4_data['ThetaIn(deg)'] = thetaIn4
m4_data['ThetaOut(deg)'] = thetaOut4
m5_data['ThetaIn(deg)'] = thetaIn5
m5_data['ThetaOut(deg)'] = thetaOut5

wavelength1 = wavelength(m1_data['V(kV)'])
wavelength2 = wavelength(m1_data['V(kV)'])
wavelength3 = wavelength(m1_data['V(kV)'])
wavelength4 = wavelength(m1_data['V(kV)'])
wavelength5 = wavelength(m1_data['V(kV)'])

m1_data['Wavelength(angstrom)'] = wavelength1
m2_data['Wavelength(angstrom)'] = wavelength2
m3_data['Wavelength(angstrom)'] = wavelength3
m4_data['Wavelength(angstrom)'] = wavelength4
m5_data['Wavelength(angstrom)'] = wavelength5

dIn1 = dval(thetaIn1, wavelength1)
dOut1 = dval(thetaOut1, wavelength1)
dIn2 = dval(thetaIn2, wavelength2)
dOut2 = dval(thetaOut2, wavelength2)
dIn3 = dval(thetaIn3, wavelength3)
dOut3 = dval(thetaOut3, wavelength3)
dIn4 = dval(thetaIn4, wavelength4)
dOut4 = dval(thetaOut4, wavelength4)
dIn5 = dval(thetaIn5, wavelength5)
dOut5 = dval(thetaOut5, wavelength5)

m1_data['dIn(angstrom)'] = dIn1
m1_data['dOut(angstrom)'] = dOut1
m2_data['dIn(angstrom)'] = dIn2
m2_data['dOut(angstrom)'] = dOut2
m3_data['dIn(angstrom)'] = dIn3
m3_data['dOut(angstrom)'] = dOut3
m4_data['dIn(angstrom)'] = dIn4
m4_data['dOut(angstrom)'] = dOut4
m5_data['dIn(angstrom)'] = dIn5
m5_data['dOut(angstrom)'] = dOut5

# Means
dInAvg1 = dAvg(dIn1)
dOutAvg1 = dAvg(dOut1)
dInAvg2 = dAvg(dIn2)
dOutAvg2 = dAvg(dOut2)
dInAvg3 = dAvg(dIn3)
dOutAvg3 = dAvg(dOut3)
dInAvg4 = dAvg(dIn4)
dOutAvg4 = dAvg(dOut4)
dInAvg5 = dAvg(dIn5)
dOutAvg5 = dAvg(dOut5)
m1_data['dIn Avg(ang)'] = dInAvg1
m1_data['dOut Avg(ang)'] = dOutAvg1
m2_data['dIn Avg(ang)'] = dInAvg2
m2_data['dOut Avg(ang)'] = dOutAvg2
m3_data['dIn Avg(ang)'] = dInAvg3
m3_data['dOut Avg(ang)'] = dOutAvg3
m4_data['dIn Avg(ang)'] = dInAvg4
m4_data['dOut Avg(ang)'] = dOutAvg4
m5_data['dIn Avg(ang)'] = dInAvg5
m5_data['dOut Avg(ang)'] = dOutAvg5

# Uncertainties
sdIn1 = np.std(dIn1,ddof=1)
sdomIn1 = sdIn1/np.sqrt(N)
sdOut1 = np.std(dOut1,ddof=1)
sdomOut1 = sdOut1/np.sqrt(N)

sdIn2 = np.std(dIn2,ddof=1)
sdomIn2 = sdIn2/np.sqrt(N)
sdOut2 = np.std(dOut2,ddof=1)
sdomOut2 = sdOut2/np.sqrt(N)

sdIn3 = np.std(dIn3,ddof=1)
sdomIn3 = sdIn3/np.sqrt(N)
sdOut3 = np.std(dOut3,ddof=1)
sdomOut3 = sdOut3/np.sqrt(N)

sdIn4 = np.std(dIn4,ddof=1)
sdomIn4 = sdIn4/np.sqrt(N)
sdOut4 = np.std(dOut4,ddof=1)
sdomOut4 = sdOut4/np.sqrt(N)

sdIn5 = np.std(dIn5,ddof=1)
sdomIn5 = sdIn5/np.sqrt(N)
sdOut5 = np.std(dOut5,ddof=1)
sdomOut5 = sdOut5/np.sqrt(N)


# Save dataframes
m1_data.to_csv('Method 1 Data Trial 1 Out.csv', index=False)
m2_data.to_csv('Method 1 Data Trial 2 RND Out.csv', index=False)
m3_data.to_csv('Method 1 Data Trial 3 Out.csv', index=False)
m4_data.to_csv('Method 1 Data Trial 4 Out.csv', index=False)
m5_data.to_csv('Method 1 Data Trial 5 Out.csv', index=False)


# Print out percent errors
print('\n', 10*'-',"Trial 1",10*'-')
print('Print dInAvg1', dInAvg1, ' with uncertainty ', sdomIn1)
print(errorDin(dInAvg1), 'percent error dInAvg1 (observed vs actual value)')
print('Print dOutAvg1', dOutAvg1, ' with uncertainty ', sdomOut1)
print(errorDout(dOutAvg1), 'percent error dOutAvg1 (observed vs actual value)\n')


print(10*'-',"Trial 2",10*'-')
print('Print dInAvg2', dInAvg2, ' with uncertainty ', sdomIn2)
print(errorDin(dInAvg2), 'percent error dInAvg2 (observed vs actual value)') 
print('Print dOutAvg2', dOutAvg2, ' with uncertainty ', sdomOut2)
print(errorDout(dOutAvg2), 'percent error dOutAvg2 (observed vs actual value)\n')

print(10*'-',"Trial 3",10*'-')
print('Print dInAvg3', dInAvg3, ' with uncertainty ', sdomIn3)
print(errorDin(dInAvg3), 'percent error dInAvg3 (observed vs actual value)') 
print('Print dOutAvg3', dOutAvg3, ' with uncertainty ', sdomOut1)
print(errorDout(dOutAvg3), 'percent error dOutAvg3 (observed vs actual value)\n')

print(10*'-',"Trial 4",10*'-')
print('Print dInAvg4', dInAvg4, ' with uncertainty ', sdomIn4)
print(errorDin(dInAvg4), 'percent error dInAvg4 (observed vs actual value)') 
print('Print dOutAvg4', dOutAvg4, ' with uncertainty ', sdomOut4)
print(errorDout(dOutAvg4), 'percent error dOutAvg4 (observed vs actual value)\n')

print(10*'-',"Trial 5",10*'-')
print('Print dInAvg5', dInAvg5, ' with uncertainty ', sdomIn5)
print(errorDin(dInAvg5), 'percent error dInAvg5 (observed vs actual value)')  
print('Print dOutAvg5', dOutAvg5, ' with uncertainty ', sdomOut5)
print(errorDout(dOutAvg5), 'percent error dOutAvg5 (observed vs actual value)')

