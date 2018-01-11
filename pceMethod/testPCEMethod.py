#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:16:21 2018

@author: Ohi Dibua
This code tests the construction of sobol sensitivity indices using polynomial chaos expansions
as illustrated in [1]. The functions tested are a basic ishigami function with uniform boundaries
and a significantly more complicated one with non-uniform boundarie. 

[1] T. Crestaux, O. Maitre, J-M Martinez, "Polynomial Chaoes expansion for sensitivity analysis," 
    Reliability Engineering and System Safety, 2008.   
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
#Inputs from terminal that determing the chosen function, the maximum power of an individual
#polynomial, the level of accuracy of the ingeration, and the dimension, d, of the input.
chooseFunc = sys.argv[1]; p = int(sys.argv[2]); level=int(sys.argv[3]); d=int(sys.argv[4]);

#Checkts to make sure that inputs into terminal.
if (chooseFunc not in testFuncArr):
    sys.exit('Input test function does not exist');
elif (d!=3):
    sys.exit('Not a valid dimension of input. Choose integer 3');
elif (level<1):
    sys.exit('Not a valid level of accuracy. Must be >=1');
elif (p<(level-1)):
    sys.exit('Not a valid maximum polynomial power. Select p to be <= level');

#Gives analytical solution to sobol sensitivity indices as comparison to numerical  
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
    D=420.26428;
    sobolAnalyt['1']=0.02652633381; sobolAnalyt['2']=0.6968539968; sobolAnalyt['3']=0.0098354;
    sobolAnalyt['12']=0.2311640139; sobolAnalyt['13']=0.002524678425; sobolAnalyt['23']=0.02482185803; 
    sobolAnalyt['123']=0.0000827395268;
    
    
#p=18; d = 3; level = p;#int(np.ceil((2*p+1)/2.0));
#Constructs PCE expansion of function of interest, and returns coefficients of expansion
#the corresponding polynomials, the nodes and weights of the quadrature used to calculate
#the inner product, a list of powers of inputs that exist in each polynomial, and a list of
#the inner products of each polynomial. 
beta,polynomial,nodes,weights,powList,integralArr = genPCEIntegral(p,d,level,customLegendre,funcUse);

#Declares class that will be used to calculate sobol indices.
sobolClass = sobolIndices();
###
#Calculates sobol indices, total sobol indices, and total variance. 
sobolCache,sobolTotalCache,sTot = sobolClass.genSobolPCE(beta,nodes,weights,powList,customLegendre,integralArr)
print("\n")
print('Analytic totral variance',D,'Numeric Total Variance',sTot)
print('Analytic Sobol Indices',sobolAnalyt,'Numerical Sobol Indices',sobolCache)
