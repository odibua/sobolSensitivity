#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 18:39:35 2018

@author: odibua
"""

import numpy as np
def ishigamiFunctionFundamental(x):
    lb = np.array([-np.pi, -np.pi, -np.pi]);
    ub = np.array([np.pi, np.pi, np.pi]);
    a=7; b=0.1;
    
    f=np.sin(z[:,0])+a*np.sin(z[:,1])**2+b*(z[:,2]**4)*np.sin(z[:,0]);
    return f

def ishigamiFunctionComplex(x):
    lb = np.array([0, -2*np.pi, -np.pi]);
    ub = np.array([np.pi, 3*np.pi, -np.pi/2]);
    a=7; b=0.1;
    
    z = np.array(x)*(ub-lb) + lb;
    f = (np.sin(z[:,0])+np.sin(z[:,1]))+(a*np.sin(z[:,1])**2+a*np.sin(z[:,2])**2)+(
            b*(z[:,2]**4)*np.sin(z[:,0])+b*(z[:,0]**4)*np.sin(z[:,1]))+z[:,0]*z[:,1]*z[:,2];   
   return f  