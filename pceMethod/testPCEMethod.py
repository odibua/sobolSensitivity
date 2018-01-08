#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:16:21 2018

@author: odibua
"""

import numpy as np
from testFunctions import *
from sobolSensitivity import sobolIndices
from generatePCE import genPCEIntegral
import matplotlib.pyplot as plt
from generateLegendrePolynomials import customLegendre
import sys

testFuncArr = ['ishigamiFundamental','ishigamiComplex']
#chooseFunc = testFuncArr[1];
chooseFunc = sys.argv[1];

if (chooseFunc not in testFuncArr):
    sys.exit('Input test function does not exist');
a=7; b=0.1
if (chooseFunc==testFuncArr[0]):
    funcUse = ishigamiFunctionFundamental;
    D = (a**2)/8.0 + b*(np.pi**4)/5.0 + (b**2)*(np.pi**8)/18.0 + 1/2.0;
    D1 = b*(np.pi**4)/5.0+(b**2)*(np.pi**8)/50.0+0.5; D2 = (a**2)/8.0; D3 = 0;
    D12=0; D13=(b**2)*(np.pi**8)/18.0-(b**2)*(np.pi**8)/50.0; D23=0; D123=0;
    sobolAnalyt={};
    sobolAnalyt['1']=D1/D; sobolAnalyt['2']=D2/D; sobolAnalyt['3']=D3/D;
    sobolAnalyt['12']=D12/D; sobolAnalyt['13']=D13/D; sobolAnalyt['23']=D23/D; 
    sobolAnalyt['123']=D123/D;
elif (chooseFunc==testFuncArr[1]):
    funcUse = ishigamiFunctionComplex;
    sobolAnalyt={};
    sobolAnalyt['1']=0.02652633381; sobolAnalyt['2']=0.6968539968; sobolAnalyt['3']=0.0098354;
    sobolAnalyt['12']=0.2311640139; sobolAnalyt['13']=0.002524678425; sobolAnalyt['23']=0.02482185803; 
    sobolAnalyt['123']=0.0000827395268;
    
    
p=18; d = 3; level = p;#int(np.ceil((2*p+1)/2.0));

beta,polynomial,nodes,weights,powList,integralArr = genPCEIntegral(p,d,level,customLegendre,funcUse);

nTest=10;
x = np.zeros((nTest,d)); 
fAct=np.array([0.0]*nTest); fEst=np.array([0.0]*nTest); err=np.array([0.0]*nTest);
lb=-1; ub=1;
for l in range(nTest):
    fTemp=0;
    x[l,0:] = (ub-lb)*np.random.random(d) + lb
    for k in range(len(beta)): 
        poly=1.0;
        for j in range(d):
            poly=poly*customLegendre(powList[k][j],np.array([x[l][j]]));
        fTemp = fTemp+beta[k]*poly
    fAct[l]=(funcUse(np.array(x[l,0:])));
    fEst[l]=fTemp;
    err[l]=(np.abs(fAct[l]-fEst[l])/fAct[l])
sobolClass = sobolIndices();
###
sobolCache,sobolTotalCache,sTot = sobolClass.genSobolPCE(beta,nodes,weights,powList,customLegendre,integralArr)