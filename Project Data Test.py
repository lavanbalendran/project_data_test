#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:48:14 2020

@author: lavanbalendran
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exp_func(x,a,c):

  return np.exp(x*a) + c

def log_func(x,s,r): 
    return np.log(x*s)+r

def linear(x,m,b): 
    return(m*x)+b
    

x1 , y1 = np.loadtxt("Lavan_assignment_exp.txt")
x2 , y2 = np.loadtxt("Lavan_assignment_linear.txt")
x3 , y3 = np.loadtxt("Lavan_assignment_log.txt")

#LINEAR
plt.figure("Linear")
plt.title("Linear")
plt.plot(x2, y2, label='linear', marker='.', linestyle='none')
x_2 = np.linspace(0, max(x2),100)
y_2 = np.linspace(0,max(y2),100)
popt, pcov = curve_fit(linear,x_2, y_2) 

plt.plot(x_2, linear(x_2, *popt))

plt.show()


#EXPONENTIAL
plt.figure("Exponential")
plt.title("Exponential")
plt.plot(x1, y1, label='exp', marker='.', linestyle='none')
x_1 = np.linspace(0, max(x1),100)
y_1 = np.linspace(0,max(y1),100)
popt, pcov = curve_fit(exp_func,x_1, y_1)

plt.plot(x_1, exp_func(x_1, *popt))

plt.show()


#LOGORITHM
plt.figure("Logorithm")
plt.title("Logorithm")
plt.plot(x3, y3, label='log', marker='.', linestyle = 'none')
x_3 = np.linspace(0, max(x3),100)
y_3 = np.linspace(0,max(y3),100)

popt, pcov = curve_fit(log_func,x_3, y_3)

plt.plot(x_3, log_func(x_3, *popt))

plt.show()
