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
    a1=-1; b1=1;
#    
#    z1(j)=(lb(j)*b1-ub(j)*a1)/(b1-a1);
#    z(:,j)=((ub(j)-lb(j))/(b1-a1))*zet(:,j)+z1(j);
    
    lb0=(lb*b1-ub*a1)/(b1-a1);
    z=np.zeros(np.shape(x));#array(x);#((ub-lb)/(b1-a1))*np.array(x)+lb0;
    for j in range(len(x)):
        #lb0=(lb[j]*b1-ub[j]*a1)/(b1-a1);
        z[j] = ((ub[j]-lb[j])/(b1-a1))*x[j]+lb0[j];
    #print("x",x,"z",z)
    f=np.sin(z[0])+a*np.sin(z[1])**2+b*(z[2]**4)*np.sin(z[0]);
    return f

def ishigamiFunctionComplex(x):
    lb = np.array([0, -2*np.pi, -np.pi]);
    ub = np.array([np.pi, 3*np.pi, -np.pi/2]);
    a=7; b=0.1;
    
#    z = np.array(x)#*(ub-lb) + lb;
    a1=-1; b1=1;

    lb0=(lb*b1-ub*a1)/(b1-a1);
    z=((ub-lb)/(b1-a1))*np.array(x)+lb0;
    f = (np.sin(z[0])+np.sin(z[1]))+(a*np.sin(z[1])**2+a*np.sin(z[2])**2)+(
            b*(z[2]**4)*np.sin(z[0])+b*(z[0]**4)*np.sin(z[1]))+z[0]*z[1]*z[2];   
    return f  