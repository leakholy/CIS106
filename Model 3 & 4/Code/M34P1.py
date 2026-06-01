#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:25:40 2026

@author: omar
"""

# Calculate weighted exam score

exam1 = float(input("Enter the first exam score: "))
exam2 = float(input("Enter the second exam score: "))

total_score = (exam1 * 0.60) + (exam2 * 0.40)

print(f"Total score: {total_score:.2f}")