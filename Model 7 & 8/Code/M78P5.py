#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 
@author: omar
"""
# Read student last name, district code, and credits from a text file.
# Compute tuition owed based on district code.
# Display student last name, credits taken, and tuition owed.
# After the loop, display total tuition owed and number of students.

f = open("students.txt", "r")

total_tuition = 0.0
count = 0

last_name = f.readline().rstrip('\n')

while last_name != "":
    district_code = f.readline().rstrip('\n')
    credits = float(f.readline())

    if district_code == "I":
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00

    tuition = credits * cost_per_credit

    total_tuition = total_tuition + tuition
    count = count + 1

    print("Student Last Name:", last_name)
    print("Credits Taken:", credits)
    print("Tuition Owed: $", format(tuition, ",.2f"))
    print()

    last_name = f.readline().rstrip('\n')

print("Total Tuition Owed: $", format(total_tuition, ",.2f"))
print("Number of Students:", count)

f.close()
