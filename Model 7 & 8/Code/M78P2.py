#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 

@author: omar
"""

# Allow the user to enter a start value, stop value, and increment value.
# Display numbers from start to stop using the increment value.
# Uses a while loop.

start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
increment = int(input("Enter the increment value: "))

num = start

while num <= stop:
    print(num)
    num = num + increment