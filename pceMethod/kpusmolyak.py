#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:44:21 2018

@author: odibua
"""
from pathlib import Path
import numpy as np
import sys

class performIntegral():        
    def obtainNodesandWeightsKPU(self,dim,level):
        integralPath="./integralNodesWeights/KPU_d"+str(dim)+"/KPU_d"+str(dim)+"_l"+str(level)+".asc";
        integralFile = Path(integralPath,delimeter=",");
        if not integralFile.is_file():
            sys.exit("File containing this combination of nodes and weights does not exixst") 
        else:    
            integralTable=np.loadtxt(integralPath,delimiter=',');
            shpTable=np.shape(integralTable);
        return (integralTable[0:,0:dim],integralTable[0:,-1])
      
    def integrate(self,weights,f):
        I = 0;    
        for j in range(len(f)):          
            I = I + f[j]*weights[j];
        return I