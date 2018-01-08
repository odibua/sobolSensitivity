#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:24:04 2018

@author: odibua
"""
import copy
from kpusmolyak import * 

class sobolIndices():
    def genSobolPCE(self,beta,nodes,weights,powList,basisPolynomial,integralArr):
        index = 0; sobolCache = {}; sobolTotalCache={};
        d = np.shape(powList)[1]; p = np.max(np.array(powList));  
        nNodes = np.shape(nodes)[0]; level = int(np.ceil((2*p+1)/2.0));
        sobolArray=np.array([0]*d); sobolList=[];
        self.genIndicesList(index,d,sobolList,sobolArray,sobolCache,sobolTotalCache);
        integral = performIntegral();
        
        sTot = sum([beta[k+1]*beta[k+1]*integralArr[k+1] for k in range(len(beta)-1)]);#0;
        for i in range(len(sobolList)):   
            for k in range(1,len(beta),1): 
                setWhere=set(np.where(powList[k]>0)[0]+1);
                setSobol=set(sobolList[i])
                if len(setSobol)==len(setWhere) and sum(set.difference(setSobol,setWhere))==0 :
                    sobolCache[''.join(sorted(''.join(map(str,sobolList[i]))))]=sobolCache[''.join(sorted(''.join(map(str,sobolList[i]))))]+(beta[k]**2)*integralArr[k];
                            
        for key in sobolCache.keys():
            sobolCache[key]=sobolCache[key]/sTot;
            for l in range(d):
                if (l+1) in np.array(map(int,key)):
                    sobolTotalCache[str(l+1)]=sobolTotalCache[str(l+1)]+sobolCache[key];
        
        return (sobolCache,sobolTotalCache,sTot)
            
        
        
    def genIndicesList(self,index,d,sobolList,sobolArray,cache,cache2):
        for j in range(d): 
            sobolArray[index]=j+1;
            cache2[str(j+1)]=0.0
            if (len(sobolArray[0:index+1])==len(np.unique(sobolArray[0:index+1]))):
                if ''.join(sorted(''.join(map(str, sobolArray[0:index+1])))) not in [''.join(sorted(key)) for key in cache.keys()]:
                    cache[''.join(sorted(''.join(map(str, sobolArray[0:index+1]))))]=0.0;
                    sobolList.append(copy.deepcopy(sobolArray[0:index+1]));               
            if (index==(d-1)):                
                return sobolList
            else: 
                self. genIndicesList(index+1,d,sobolList,sobolArray,cache,cache2)