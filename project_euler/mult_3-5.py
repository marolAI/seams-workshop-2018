#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 06:56:20 2018

@author: maro
"""
# Initialize the sum
s = 0

for n  in range(1000):
    """"
    check if n is multiple by 3
    and 5 then add their sum
    below 1000
    """
    if n % 3 == 0 or n % 5 == 0:
        s = s + n

# display result
print(s)