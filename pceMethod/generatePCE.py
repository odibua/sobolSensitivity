#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 09:29:20 2018
@author: odibua
"""
import numpy as np
import math
import copy
from obtainPolynomialPowers import validPowersRecur
from kpusmolyak import *
import scipy.integrate.quadrature
 
def genPCEIntegral(p,d,level,basisPolynomial,func):        
    P = math.factorial(p+d)/(math.factorial(p)*math.factorial(d));
    powList = []; integral = performIntegral();
    
    powList.append(copy.deepcopy(np.array([0.0]*d)));
    for j in range(p):
        powArray = np.array([0.0]*d);
        target = j+1; 
        index=0;
        powOptions=np.array(range(target+1)); 
        validPowersRecur(powOptions,index,target,powArray,powList) 
    
    nodes, weights = copy.deepcopy(integral.obtainNodesandWeightsKPU(d,level));
    nNodes=np.shape(nodes)[0];
    lb=-1; ub=1;
    nodes = (ub-lb)*nodes+lb
    
    beta = [0.0]*P;
    integralArr = [0.0]*P
    for k in range(P):      
        if (k==0):
            f=np.array([0.0]*nNodes)
            for j in range(nNodes):
                f[j]=func(nodes[j]);
                  
        polynomial=np.array([0.0]*nNodes)
        for l in range(nNodes):
            poly=1.0;
            for j in range(d):
                poly=poly*basisPolynomial(powList[k][j],np.array([nodes[l][j]]));
            polynomial[l]=poly

        integralArr[k] = integral.integrate(
                weights,[polynomial[l]*polynomial[l] for l in range(nNodes)])
        beta[k] = integral.integrate(weights,[polynomial[l]*f[l] for l in range(nNodes)])/integralArr[k]

    return (beta,polynomial,nodes,weights,powList,integralArr) 
         

