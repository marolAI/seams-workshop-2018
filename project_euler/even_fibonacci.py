#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 07:07:24 2018

@author: maro
    -----
This is a python program to find the sum of even valued terms
in Fibonacci sequence

"""

# Initialize previous, current values and the sum
# of terms in Fibonacci sequence.
prev_val, curr_val = 0, 1
_sum = 0

# Iterate over all the fibonacci values below 4000000
while True:
    prev_val, curr_val = curr_val, prev_val + curr_val
    if curr_val > 4000000:
        break
    if curr_val%2 == 0:
        _sum += curr_val

# Display the result
print(_sum)
