# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:42:44 2021

@author: Nathan

SEE THE JUPYTER NOTEBOOK FOR CURRENT CODE.
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt 

import interactive_plot as ip
l
def Gaussian_And_Line(x, a0, a1, b0, b1, b2): # x is wavelenghth
    
    linear = a0 + a1*x
    
    exponent1 = (-0.5)*((x-b1)/b2)**2
    gauss1 = b0*np.exp(exponent1)
    
        
    return  linear + gauss1 

h2_data = pd.read_csv("unfiltered excited h2.txt", comment = '#', delim_whitespace=True, names=['W', 'I'])

l = h2_data['W']
i = h2_data['I']

# Cut the dataframe for data around the beta peaker in the Balmer lines
beta_peak = h2_data[(l>482) & (l<490)]

plt.plot(beta_peak['W'], beta_peak['I'], marker='o', linestyle='None')

fitparams = [['a0',1000,2000,1200,5],['a1',-10,10,0,0.1],['b0',3000,7000,4500,5],['b1',484,488,485.5,0.01],['b2',0.01,1,0.5,0.005]]
function = Gaussian_And_Line
plotparams = [['x',482,490],['y',0,8000],[700]]
xData = beta_peak['W']
yData = beta_peak['I']
xErr = None
yErr = None

%matplotlib qt
ip.slider_plot(fitparams,function,plotparams,xData,yData,xErr,yErr)