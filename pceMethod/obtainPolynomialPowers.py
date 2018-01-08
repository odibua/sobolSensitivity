#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 08:46:44 2018

@author: odibua
"""
import copy

def validPowersRecur(powOptions,index,target,powArray,powList):
    for j in range(len(powOptions)):
        powArray[index]=powOptions[j];
        if (index==(len(powArray)-1)):          
            if sum(powArray)==target:
                powList.append(copy.deepcopy(powArray));   
        else:
            validPowersRecur(powOptions,index+1,target,powArray,powList)
        