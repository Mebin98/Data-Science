# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:51:38 2023

@author: mebin
"""

import math 

def isPrime(n):
    tell = 0   
    tail = math.sqrt(n) 
    tailNum = int(tail) 
    for i in range(2, tailNum + 1):   
        if(n % i == 0): 
            tell = 1 
            print(i)
            break 
    if(tell == 1): 
        return False
    else:
        return True


n = int(input("Enter an integer number in [2,32767]"))

if(isPrime(n) == True):
    print("%d is prime number" %n)
else:
    print("%d is not prime number" %n )
    
            

    
            





   