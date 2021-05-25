# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:54:07 2021

@author: Nate
"""

import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt  

from scipy.integrate import simps

%matplotlib inline
%config InlineBackend.figure_format = 'svg'

# Constants
k = 5.492 # Hall sensor calibration constant, mT/V
L = 10 # length, cm

def bfield(v):
    return k*v

# Dataframes
BProfile = pd.read_csv("B_Profile.txt", comment = '#', sep=',', names=['z(cm)','V(V)','dz(cm)','dV(V)'])

B = bfield(BProfile['V(V)'])
BProfile['B(mT)'] = B
BProfile['Vmax(V)'] = 2.027
z = BProfile['z(cm)']
Vmax = BProfile['Vmax(V)']
V = BProfile['V(V)']

print(bfield(Vmax))

# The maximum area under the curve - assuming the field is uniform over L and at Vmax over L
Bmax = bfield(Vmax) # pass Vmax

# First integration method - Simpson's Method through the scipy library
integral1 = simps(B[:27], z[:27]) # this is Bo at i=1, used for scaling in verdet plot
integral2 = simps(Bmax[:27], z[:27])
integral2 = 11.13*L/2
ratio1 = (integral1/integral2)

print(BProfile['B(mT)'][:27]) # this is Bo at i=1, used for scaling in verdet plot

#area = simps(BProfileUpdated['B(mT)'][:27],BProfileUpdated['z(cm)'][:27])

print("\nIntegral ", integral1, "Max ideal ", integral2 )
print("The ratio of the data integral over ideal maximum uniform area is ", ratio1)

# Using voltage
integral3 = simps(V[:27], z[:27]) # this is Bo at i=1, used for scaling in verdet plot
integral4 = simps(Vmax[:27], z[:27])
ratio2 = integral3/integral4

print("\nIntegral ", integral3, "Max ideal ", integral4 )
print("The ratio of the data integral over ideal maximum uniform area is ", ratio2)


fig, ax = plt.subplots(1,2)

ax[0].plot(z, BProfile['V(V)'],'o', markersize=5, color = 'tab:orange', mec='black')
ax[0].set_xlabel('Position (cm)')
ax[0].set_ylabel('Voltage (V)')

ax[1].plot(z,B,'o',markersize=5, color='orange', mec='black', label='Data')
ax[1].set_xlabel('Position (cm)')
ax[1].set_ylabel('Magneitc Field (mT)')
ax[1].set_ylim(0)

ax[1].fill_between(z, B, 0, where=(z > 3.3) & (z < 3.3 + 5.0), ec='black',
                    label='Integral, B = {0:.3f} mT*cm'.format(integral1*2)) # 2 factor to account for symmetry of integral
ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)

plt.tight_layout()
plt.show()

