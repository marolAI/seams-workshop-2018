
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 17:59:24 2018

@author: maro
    -----

This is a python program to find the largest prime factor
 of the number 600851475143.
"""
# create a function 
def largest_prime_factor(x):
    lpf = 2
    while (x > lpf):
        if (x%lpf==0):
            x = x/lpf
            lpf = 2
        else:
            lpf+=1
    return lpf

ans = largest_prime_factor(600851475143)
# display the result
print("The largest prime factor of the number 600851475143 is", ans)
