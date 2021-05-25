# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:06:11 2021

@author: Nathan
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt 

import scipy as sp 
from scipy.optimize import curve_fit 

# Constants
PIX_TO_MM = 0.65 # micrometer per pixel
MAX_FRAME = 116 # the frame for which analysis should end
PART_NUM = 6 # number of particles tracked
SQ_MICRON_TO_SQ_METER = 1E-12
r = 5E-7 # radius of the beads
VISC = 1E-3 # viscosicty of distilled water
R =  8.314 # gas constant in J/molK
T = 294.05 # temperature in K 
NaACCEPTED = 6.02214076E23 # accepted avagadros
dt = 0.2 # frames extracted per second 

def disp(a):
    arr = []
    for i in range(0, len(a)):
        r = a[i] - a[0]
        arr.append(r)
    return arr
    


def pixel_to_mm(data):
    arr = []
    for i in range(0, len(data)):
        d = data[i] * PIX_TO_MM
        arr.append(d)
    return arr

def mean_square_disp(x):
    arr = []
    N = PART_NUM
    
    for t in range(0, MAX_FRAME): # time index is col
        r = 0
        for n in range(0, PART_NUM): # particle number is row
            r += abs(x[n][t] - x[n][0])**2
        m = r/N
        arr.append(m)
    
    return arr

def line(x, a1): # best fit equation
    return a1*x

def Na(m): # determine avagradros number using the best fit slope
    num = R*T
    denom = 3*np.pi*m*VISC*r
    return num/denom

def dN(m, dm, N):
    quad = np.sqrt((dm/m)**2)
    return quad*N



traj1 = pd.read_csv("Traj 1.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj2 = pd.read_csv("Traj 2.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj3 = pd.read_csv("Traj 3.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj4 = pd.read_csv("Traj 4.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj5 = pd.read_csv("Traj 5.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])
traj6 = pd.read_csv("Traj 6.txt", comment = '%', delim_whitespace=True, names=['frame','x (pixel)','y (pixel)','z (pixel)','m0','m1','m2','m3','m4','s' ])

# Read in the data
x1 = traj1['x (pixel)']
x2 = traj2['x (pixel)']
x3 = traj3['x (pixel)']
x4 = traj4['x (pixel)']
x5 = traj5['x (pixel)']
x6 = traj6['x (pixel)']

y1 = traj1['y (pixel)']
y2 = traj2['y (pixel)']
y3 = traj3['y (pixel)']
y4 = traj4['y (pixel)']
y5 = traj5['y (pixel)']
y6 = traj6['y (pixel)']

# convert pixel data to sptatial distance - note its actually microns, not mm
x1_mm = pixel_to_mm(x1)
x2_mm = pixel_to_mm(x2)
x3_mm = pixel_to_mm(x3)
x4_mm = pixel_to_mm(x4)
x5_mm = pixel_to_mm(x5)
x6_mm = pixel_to_mm(x6)

y1_mm = pixel_to_mm(y1)
y2_mm = pixel_to_mm(y2)
y3_mm = pixel_to_mm(y3)
y4_mm = pixel_to_mm(y4)
y5_mm = pixel_to_mm(y5)
y6_mm = pixel_to_mm(y6)

# generate list of displacements 
x1_disp = disp(x1_mm)
x2_disp = disp(x2_mm)
x3_disp = disp(x3_mm)
x4_disp = disp(x4_mm)
x5_disp = disp(x5_mm)
x6_disp = disp(x6_mm)

y1_disp = disp(y1_mm)
y2_disp = disp(y2_mm)
y3_disp = disp(y3_mm)
y4_disp = disp(y4_mm)
y5_disp = disp(y5_mm)
y6_disp = disp(y6_mm)

x_disp = np.concatenate((x1_disp,x2_disp,x3_disp,x4_disp,x5_disp,x6_disp))




# initialize the 1D lists used to store displacements
reshaped_disp_x1 = np.zeros(MAX_FRAME)
reshaped_disp_x2 = np.zeros(MAX_FRAME)
reshaped_disp_x3 = np.zeros(MAX_FRAME)
reshaped_disp_x4 = np.zeros(MAX_FRAME)
reshaped_disp_x5 = np.zeros(MAX_FRAME)
reshaped_disp_x6 = np.zeros(MAX_FRAME)

reshaped_disp_y1 = np.zeros(MAX_FRAME)
reshaped_disp_y2 = np.zeros(MAX_FRAME)
reshaped_disp_y3 = np.zeros(MAX_FRAME)
reshaped_disp_y4 = np.zeros(MAX_FRAME)
reshaped_disp_y5 = np.zeros(MAX_FRAME)
reshaped_disp_y6 = np.zeros(MAX_FRAME)

# splice the displacement data into new arrays with only the first MAX_FRAME frames
for i in range(0, MAX_FRAME):
    reshaped_disp_x1[i] = x1_mm[i] 
    reshaped_disp_x2[i] = x2_mm[i] 
    reshaped_disp_x3[i] = x3_mm[i] 
    reshaped_disp_x4[i] = x4_mm[i] 
    reshaped_disp_x5[i] = x5_mm[i] 
    reshaped_disp_x6[i] = x6_mm[i] 
    
    reshaped_disp_y1[i] = y1_mm[i] 
    reshaped_disp_y2[i] = y2_mm[i] 
    reshaped_disp_y3[i] = y3_mm[i] 
    reshaped_disp_y4[i] = y4_mm[i] 
    reshaped_disp_y5[i] = y5_mm[i] 
    reshaped_disp_y6[i] = y6_mm[i] 

# Create 1D array of particle number displacement
x = np.concatenate((reshaped_disp_x1, reshaped_disp_x2, reshaped_disp_x3, reshaped_disp_x4,
                    reshaped_disp_x5, reshaped_disp_x6))

y = np.concatenate((reshaped_disp_y1, reshaped_disp_y2, reshaped_disp_y3, reshaped_disp_y4,
                    reshaped_disp_y5, reshaped_disp_y6))

# Create 2D array of time (row) vs particle number (column) displacement
x_arr = np.zeros((PART_NUM,MAX_FRAME))
x_arr[0] = x[0:116]
x_arr[1] = x[116:232]
x_arr[2] = x[232:348]
x_arr[3] = x[348:464]
x_arr[4] = x[464:580]
x_arr[5] = x[580:696]


y_arr = np.zeros((PART_NUM,MAX_FRAME))
y_arr[0] = y[0:116]
y_arr[1] = y[116:232]
y_arr[2] = y[232:348]
y_arr[3] = y[348:464]
y_arr[4] = y[464:580]
y_arr[5] = y[580:696]
        
mean_square_x = mean_square_disp(x_arr)
mean_square_y = mean_square_disp(y_arr)

time = np.linspace(0, MAX_FRAME*dt, MAX_FRAME)

x_squared = x_arr**2
y_squared = y_arr**2
x_squared_avg = np.mean(x_squared,axis=0)
y_squared_avg = np.mean(y_squared,axis=0)
x_squared_sdom = np.std(x_squared,ddof=1,axis=0)/np.sqrt(PART_NUM)
y_squared_sdom = np.std(y_squared,ddof=1,axis=0)/np.sqrt(PART_NUM)

for n in np.arange(PART_NUM):
    plt.plot(x_squared[n],'-',linewidth=0.5)


poptx, pcovx = curve_fit(line, time, mean_square_x, sigma=x_squared_sdom) 
xfitx = np.linspace(0,MAX_FRAME*dt,1000)
yfitx = line(xfitx, *poptx)

m = poptx[0]*SQ_MICRON_TO_SQ_METER # slope in square meter
print('-'*10, 'x data', '-'*10)
print('Slope is ', m)
NaExperimental = Na(m)
print("Avadagros number experiment is ", NaExperimental)

dm = np.sqrt(pcovx[0][0])*SQ_MICRON_TO_SQ_METER
print("With uncertainty in slope, dm = ", dm)

print("Experimental Na over Accepted Na is ", NaExperimental/NaACCEPTED)
print('With uncertainty in Na, dN = ', dN(m, dm, NaExperimental))

popty, pcovy = curve_fit(line, time, mean_square_y) 
xfity = np.linspace(0,23.2,1000)
yfity = line(xfity, *popty)

m = popty[0]*SQ_MICRON_TO_SQ_METER # slope in square meter
print('-'*10, 'y data', '-'*10)
print('Slope is ', m)
NaExperimental = Na(m)
print("Avadagros number experiment is ", NaExperimental)

dm = np.sqrt(pcovy[0][0])*SQ_MICRON_TO_SQ_METER
print("With uncertainty in slope, dm = ", dm*SQ_MICRON_TO_SQ_METER)

print("Experimental Na over Accepted Na is ", NaExperimental/NaACCEPTED)
print('With uncertainty in Na, dN = ', dN(m, dm, NaExperimental))

#Plots the mean squared displacement, with uncertainties,
#and the best fit.
fig, ax = plt.subplots(1,1,figsize=(8,6))


ax.plot(xfitx,yfitx,'-',c='tab:blue', linewidth=4,label='<x\u00B2> Fit')
ax.plot(xfity,yfity,'-',c='tab:red',linewidth=4,label='<y\u00B2> Fit') 
ax.plot(time, line(time, 6.27), '--', linewidth=4,label='<r\u00B2> Fit', c='orange') # plot the average slope
ax.plot(time, mean_square_x, linestyle='', marker='o', markersize=6, color='tab:blue',label='<x\u00B2> data',mec='black')
ax.plot(time, mean_square_y, linestyle='None', marker='o', markersize=6, color='tab:red',label='<y\u00B2> data',mec='black')

ax.set_xlabel('Time (s)',fontsize=18)
ax.set_ylabel('Mean Square Displacement ( (\u03BCm\u00B2)',fontsize=18)


plt.tight_layout()
plt.savefig('Mean Square Displacement over Time.pdf', format='pdf')
plt.savefig('Mean Square Displacement over Time.png', format='png')
plt.show()

