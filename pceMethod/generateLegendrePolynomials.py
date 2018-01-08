#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 09:02:43 2018

@author: odibua
"""
import math
import numpy as np

def customLegendre(n,x):
    init=np.array([0.0]*len(x));
    for k in range(int(n/2+1)):
        useK=k;
        p1=(math.factorial(n))/((math.factorial(n-useK)*math.factorial(useK)));
        p2=math.factorial((2*n-2*useK))/(math.factorial((2*n-2*useK)-n)*math.factorial(n));
        init=init+((-1)**useK)*p1*p2*x**(n-2*useK);    
    init=init/(2**n);
    return init