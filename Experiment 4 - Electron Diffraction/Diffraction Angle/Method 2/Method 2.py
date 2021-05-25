# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:20:41 2021

@author: Nathan

METHOD 2

Plot D vs. V−1/2 and calculate the value of d from the slope of the graph using L = 13.5 cm
Compare the d values (for both the rings) determined by the two methods and with the expected
values based on graphite crystal (see Fig. 2). What should the ratio of these two d values be for
the hexagonal lattice? Check if your results agree with this dimensionless geometric fact.

Trial 5 is closest to the accepted value based on the percent error values
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt 

import scipy as sp 
from scipy.optimize import curve_fit 

# Constants
l = 13.5 # cm, length from cathode tube to end of diffraction tube
dIN = 2.13 # angstrom, accepted value for atomic spacing
dOUT = 1.23 # angstrom, accepted value for atomic spacing

# Convert radius to diameter
def D(R): 
    arr = []
    
    for i in range(1, len(R)):
        R[i] = float(R[i]) # convert R to a float, it is read as a str
        t = R[i]*2
        arr.append(t)
    return arr
    
    
def Voltage(V):
    arr = []
    
    for i in range(1, len(V)):
        t = 1/(np.sqrt(V[i]))
        arr.append(t)
    return arr

def line(x, a0, a1):
    return a0 + a1*x

def get_d(m):
    d = (2*l*np.sqrt(150))/m
    return d

def deltad(dm, m, d):
    return np.sqrt((dm/m)**2)*d

# Generate percent error between observed value and accepted value for te outer ring
# atomic plane spacing
def errorDout(dObserved):
    return abs(dObserved - dOUT)/dOUT*100

# Generate percent error between observed value and accepted value for te inner ring
# atomic plane spacing
def errorDin(dObserved):
    return abs(dObserved - dIN)/dIN*100


m1_data = pd.read_csv("Method 1 Data Trial 1.csv", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)',
                                                                                  'ThetaIn(deg)', 'ThetaOut(deg)', 'Wavelength(angstrom)', 'dIn(angstrom)','dOut(angstrom)', 
                                                                                  'dInAvg(ang)', 'dOutAvg(ang)'])
m2_data = pd.read_csv("Method 1 Data Trial 2 RND.csv", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)',
                                                                                  'ThetaIn(deg)', 'ThetaOut(deg)', 'Wavelength(angstrom)', 'dIn(angstrom)','dOut(angstrom)', 
                                                                                  'dInAvg(ang)', 'dOutAvg(ang)'])
m3_data = pd.read_csv("Method 1 Data Trial 3.csv", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)',
                                                                                  'ThetaIn(deg)', 'ThetaOut(deg)', 'Wavelength(angstrom)', 'dIn(angstrom)','dOut(angstrom)', 
                                                                                  'dInAvg(ang)', 'dOutAvg(ang)'])
m4_data = pd.read_csv("Method 1 Data Trial 4.csv", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)',
                                                                                  'ThetaIn(deg)', 'ThetaOut(deg)', 'Wavelength(angstrom)', 'dIn(angstrom)','dOut(angstrom)', 
                                                                                  'dInAvg(ang)', 'dOutAvg(ang)'])
m5_data = pd.read_csv("Method 1 Data Trial 5.csv", comment = '#', sep=',', names=['V(kV)', 'Rin(cm)', 'Rout(cm)',
                                                                                  'ThetaIn(deg)', 'ThetaOut(deg)', 'Wavelength(angstrom)', 'dIn(angstrom)','dOut(angstrom)', 
                                                                                  'dInAvg(ang)', 'dOutAvg(ang)'])

# read in columns into list vars so we can work with them
v1 = m1_data['V(kV)']
rin1 = m1_data['Rin(cm)']
rout1 = m1_data['Rout(cm)']

m2_data['V(kV)'].sort_values()
m2_data['Rin(cm)'].sort_values()
m2_data['Rout(cm)'].sort_values()

v2 = m2_data['V(kV)']
rin2 = m2_data['Rin(cm)']
rout2 = m2_data['Rout(cm)']

v3 = m3_data['V(kV)']
rin3 = m3_data['Rin(cm)']
rout3 = m3_data['Rout(cm)']

v4 = m4_data['V(kV)']
rin4 = m4_data['Rin(cm)']
rout4 = m4_data['Rout(cm)']

v5 = m5_data['V(kV)']
rin5 = m5_data['Rin(cm)']
rout5 = m5_data['Rout(cm)']


# convert kV to V
for i in range(1, len(v1)):
    v1[i] = float(v1[i]) # Voltage is read in as a string from the spreadsheet
    v1[i] = v1[i]*1000
    
    v2[i] = float(v2[i]) # Voltage is read in as a string from the spreadsheet
    v2[i] = v2[i]*1000
    
    v3[i] = float(v3[i]) # Voltage is read in as a string from the spreadsheet
    v3[i] = v3[i]*1000
    
    v4[i] = float(v4[i]) # Voltage is read in as a string from the spreadsheet
    v4[i] = v4[i]*1000
    
    v5[i] = float(v5[i]) # Voltage is read in as a string from the spreadsheet
    v5[i] = v5[i]*1000

# convert voltage to the v^(-1/2) form needed for the eqn
invSqrtV1 = Voltage(v1)
Din1 = D(rin1)
Dout1 = D(rout1)

invSqrtV2 = Voltage(v2)
Din2 = D(rin2)
Dout2 = D(rout2)

invSqrtV3 = Voltage(v3)
Din3 = D(rin3)
Dout3 = D(rout3)

invSqrtV4 = Voltage(v4)
Din4 = D(rin4)
Dout4 = D(rout4)

invSqrtV5 = Voltage(v5)
Din5 = D(rin5)
Dout5 = D(rout5)

"""
Trial 1
"""
print(10*'-',"Trial 1",10*'-')


# find the slope of the line for Rin1, trial 1
popt, pcov = curve_fit(line, invSqrtV1, Din1) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Din', c='dodgerblue')
print('Slope of fit Rin1 is ', m)

# calculate din1
din1 = get_d(m)
print(errorDin(din1), 'percent error din1 (observed vs actual value)') 
dm = np.sqrt(pcov[1][1])
dd = deltad(dm, m, din1)
print('Uncertainty in din1 is ', dd)
print('Uncertainty in slope for din1 ', dm)
print('d (ang) for inner ring trial 1 is ', din1)

# find the slope of the line for Rout1, trial 1
popt, pcov = curve_fit(line, invSqrtV1, Dout1) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Dout', c='orangered')

# plot the data for trial 1
plt.plot(invSqrtV1, Din1, label='Data Din', marker='o', linestyle='None', mec='black', c='darkgoldenrod')
plt.plot(invSqrtV1, Dout1, label='Data Dout', marker='o', linestyle='None', mec='black', c='slategrey')

print('Slope of fit Rout1 is ', m)

# calculate dout1
dout1 = get_d(m)
print(errorDout(dout1), 'percent error dout1 (observed vs actual value)') 

dm = np.sqrt(pcov[1][1])
print('Uncertainty in slope for dout1 ', dm)
print('d (ang) for outer ring trial 1 is ', dout1)
dd = deltad(dm, m, dout1)
print('Uncertainty in dout1 is ', dd, '\n\n')

#plt.title('Trial 1')
plt.xlabel('Inverse Square Voltage (V-\u00BD)', fontsize=12)
plt.ylabel('Diameter (cm)', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('D vs Inverse Square V for Trial 1.pdf', format='pdf')
plt.show()


"""
Trial 2
"""
print(10*'-',"Trial 2",10*'-')


# find the slope of the line for Rin, trial 2
popt, pcov = curve_fit(line, invSqrtV2, Din2) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Din', c='dodgerblue')
print('Slope of fit Rin2 is ', m)

# calculate din2
din2 = get_d(m)
print(errorDin(din2), 'percent error din2 (observed vs actual value)') 
dm = np.sqrt(pcov[1][1])
print('Uncertainty in slope for din2 ', dm)
print('d (ang) for inner ring trial 2 is ', din2)
dd = deltad(dm, m, din2)
print('Uncertainty in din2 is ', dd)

# find the slope of the line for Rout, trial 2
popt, pcov = curve_fit(line, invSqrtV2, Dout2) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Dout', c='orangered')

# plot the data for trial 2
plt.plot(invSqrtV2, Din2, label='Data Din', marker='o', linestyle='None', mec='black', c='darkgoldenrod')
plt.plot(invSqrtV2, Dout2, label='Data Dout', marker='o', linestyle='None', mec='black', c='slategrey')

# calculate dout2
dout2 = get_d(m)
print(errorDout(dout2), 'percent error dout2 (observed vs actual value)') 

dm = np.sqrt(pcov[1][1])
print('Uncertainty in slope for dout2 ', dm)
print('Slope of fit Rout2 is ', m)
dd = deltad(dm, m, dout2)
print('Uncertainty in dout2 is ', dd)

print('d (ang) for outer ring trial 2 is ', dout2, '\n\n')

#plt.title('Trial 2 - Random Sampling Sequence')
plt.xlabel('Inverse Square Voltage (V-\u00BD)', fontsize=12)
plt.ylabel('Diameter (cm)', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('D vs Inverse Square V for Trial 2.pdf', format='pdf')
plt.show()

"""
Trial 3
"""
print(10*'-',"Trial 3",10*'-')


# find the slope of the line for Rin, trial 3
popt, pcov = curve_fit(line, invSqrtV3, Din3) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Din', c='dodgerblue')


print('Slope of fit Rin3 is ', m)

# calculate din3
din3 = get_d(m)
print(errorDin(din3), 'percent error din3 (observed vs actual value)') 
dm = np.sqrt(pcov[1][1])
dd = deltad(dm, m, din3)
print('Uncertainty in din3 is ', dd)
print('Uncertainty in slope for din3 ', dm)
print('d (ang) for inner ring trial 3 is ', din3)

# find the slope of the line for Rout, trial 3
popt, pcov = curve_fit(line, invSqrtV3, Dout3) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Dout', c='orangered')

# plot the data for trial 3
plt.plot(invSqrtV3, Din3, label='Data Rin', marker='o', linestyle='None', mec='black', c='darkgoldenrod')
plt.plot(invSqrtV3, Dout3, label='Data Rout', marker='o', linestyle='None', mec='black', c='slategrey')

# calculate dout3
dout3 = get_d(m)
print(errorDout(dout3), 'percent error dout3 (observed vs actual value)') 

dm = np.sqrt(pcov[1][1])
print('Uncertainty in slope for dout3 ', dm)

dd = deltad(dm, m, dout3)
print('Uncertainty in dou3 is ', dd)

print('Slope of fit Rout3 is ', m)

print('d (ang) for outer ring trial 3 is ', dout3, '\n\n')

#plt.title('Trial 3')
plt.xlabel('Inverse Square Voltage (V-\u00BD)', fontsize=12)
plt.ylabel('Diameter (cm)', fontsize=12)
#plt.legend()
plt.tight_layout()
plt.savefig('D vs Inverse Square V for Trial 3.pdf', format='pdf')
plt.show()

"""
Trial 4
"""
print(10*'-',"Trial 4",10*'-')


# find the slope of the line for Rin, trial 4
popt, pcov = curve_fit(line, invSqrtV4, Din4) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Din', c='dodgerblue')
print('Slope of fit Rin4 is ', m)


# calculate din4
din4 = get_d(m)
print(errorDin(din4), 'percent error din4 (observed vs actual value)') 
dm = np.sqrt(pcov[1][1])
print('Uncertainty in slope for din4 ', dm)

dd = deltad(dm, m, din4)
print('Uncertainty in din4 is ', dd)

print('d (ang) for inner ring trial 4 is ', din4)

# find the slope of the line for Rout, trial 4
popt, pcov = curve_fit(line, invSqrtV4, Dout4) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Dout', c='orangered')

# plot the data for trial 4
plt.plot(invSqrtV4, Din4, label='Data Din', marker='o', linestyle='None', mec='black', c='darkgoldenrod')
plt.plot(invSqrtV4, Dout4, label='Data Dout', marker='o', linestyle='None', mec='black', c='slategrey')

# calculate dout4
dout4 = get_d(m)
dm = np.sqrt(pcov[1][1])
print(errorDout(dout4), 'percent error dout4 (observed vs actual value)') 
dd = deltad(dm, m, dout4)
print('Uncertainty in dout4 is ', dd)
print('Uncertainty in slope for dout4 ', dm)
print('Slope of fit Rout4 is ', m)

print('d (ang) for outer ring trial 4 is ', dout4, '\n\n')

#plt.title('Trial 4')
plt.xlabel('Inverse Square Voltage (V-\u00BD)', fontsize=12)
plt.ylabel('Diameter (cm)', fontsize=12)
#plt.legend()
plt.tight_layout()
plt.savefig('D vs Inverse Square V for Trial 4.pdf', format='pdf')
plt.show()

"""
Trial 5
"""
print(10*'-',"Trial 5",10*'-')


# find the slope of the line for Rin, trial 5
popt, pcov = curve_fit(line, invSqrtV5, Din5) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Din', c='dodgerblue')
print('Slope of fit Rin5 is ', m)


# calculate din5
din5 = get_d(m)
print(errorDin(din5), 'percent error din5 (observed vs actual value)') 



# Generate uncertainties 
dm = np.sqrt(pcov[1][1])
print('Uncertainty in slope for din5 ', dm)
print('d (ang) for inner ring trial 5 is ', din5)
dd = deltad(dm, m, din5)
print('Uncertainty in din5 is ', dd)

# find the slope of the line for Rout, trial 5
popt, pcov = curve_fit(line, invSqrtV5, Dout5) 

xfit = np.linspace(0.014, 0.020, 1000)
yfit = line(xfit, *popt)
m = popt[1]
yint = popt[0]
plt.plot(xfit, yfit, label='Fit Dout', c='orangered')

# plot the data for trial 5
plt.plot(invSqrtV5, Din5, label='Data Din', marker='o', linestyle='None', mec='black', c='darkgoldenrod')
plt.plot(invSqrtV5, Dout5, label='Data Dout', marker='o', linestyle='None', mec='black', c='slategrey')


# calculate dout5
dout5 = get_d(m)

# Generate uncertainties 
dm = np.sqrt(pcov[1][1])
print('Uncertainty in slope for dout5 ', dm)
print('Slope of fit Rout5 is ', m)
dd = deltad(dm, m, dout5)
print('Uncertainty in dout5 is ', dd)
print(errorDout(dout5), 'percent error dout5 (observed vs actual value)') 
print('d (ang) for outer ring trial 5 is ', dout5, '\n\n')



#plt.title('Trial 5')
plt.xlabel('Inverse Square Voltage (V-\u00BD)', fontsize=12)
plt.ylabel('Diameter (cm)', fontsize=12)
#plt.legend()
plt.tight_layout()
plt.savefig('D vs Inverse Square V for Trial 5.pdf', format='pdf')
plt.show()

m1_data['dIn (ang)'] = din1
m1_data['dOut (ang)'] = dout1

m2_data['dIn (ang)'] = din2
m2_data['dOut (ang)'] = dout2

m3_data['dIn (ang)'] = din3
m3_data['dOut (ang)'] = dout3

m4_data['dIn (ang)'] = din4
m4_data['dOut (ang)'] = dout4

m5_data['dIn (ang)'] = din5
m5_data['dOut (ang)'] = dout5

# write to and save dataframes
m1_data.to_csv('Out Method 2 Data Trial 1.csv', index=False)
m2_data.to_csv('Out Method 2 Data Trial 2 RND.csv', index=False)
m3_data.to_csv('Out Method 2 Data Trial 3.csv', index=False)
m4_data.to_csv('Out Method 2 Data Trial 4.csv', index=False)
m5_data.to_csv('Out Method 2 Data Trial 5.csv', index=False)

