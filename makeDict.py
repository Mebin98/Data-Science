# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:43:10 2023

@author: mebin
"""

key = ['Korean', 'Mathematics', 'English']
point = [90.3, 85.5, 92.7]

def makeDict(K,V):
        D = {}
        for i in range(len(K)):
            D[K[i]] = V[i]
        print(D)
        return D
makeDict(key,point)
