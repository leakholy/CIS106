#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:18:34 2026

@author: omar
"""

# Calculate total exam points for a student

last_name = input("Enter the student's last name: ")
midterm_score = float(input("Enter the midterm exam score: "))
final_score = float(input("Enter the final exam score: "))

total_points = (midterm_score * 0.40) + (final_score * 0.60)

print(f"Student last name: {last_name}")
print(f"Total exam points: {total_points:.2f}")