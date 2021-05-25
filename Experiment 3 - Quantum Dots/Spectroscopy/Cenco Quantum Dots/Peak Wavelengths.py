# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:28:05 2021

@author: Nate
"""


import pandas as pd
import numpy as np

import matplotlib as mpl 
import matplotlib.pyplot as plt 

green = pd.read_csv("green.txt", comment = '#', delim_whitespace=True, names=['Wavelength', 'Intensity'])
yellow = pd.read_csv("yellow.txt", comment = '#', delim_whitespace=True, names=['Wavelength', 'Intensity'])
orange = pd.read_csv("orange.txt", comment = '#', delim_whitespace=True, names=['Wavelength', 'Intensity'])
red = pd.read_csv("red.txt", comment = '#', delim_whitespace=True, names=['Wavelength', 'Intensity'])

peak_green = np.amax(green['Intensity'])
peak_yellow = np.amax(yellow['Intensity'])
peak_orange = np.amax(orange['Intensity'])
peak_red = np.amax(red['Intensity'])

print('Red', peak_red, 'Orange', peak_orange, 'Yellow', peak_yellow, 'Green', peak_green)