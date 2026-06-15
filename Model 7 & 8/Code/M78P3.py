#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 

@author: omar
"""
# Read employee last name and salary from a text file.
# Determine bonus rate, compute bonus, and display results.
# After the loop, display the total bonuses paid.

f = open("employees.txt", "r")

total_bonus = 0.0

last_name = f.readline().rstrip('\n')

while last_name != "":
    salary = float(f.readline())

    if salary >= 100000:
        bonus_rate = 0.20
    elif salary >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10

    bonus = salary * bonus_rate
    total_bonus = total_bonus + bonus

    print("Employee Last Name:", last_name)
    print("Salary: $", format(salary, ",.2f"))
    print("Bonus: $", format(bonus, ",.2f"))
    print()

    last_name = f.readline().rstrip('\n')

print("Total Bonuses Paid: $", format(total_bonus, ",.2f"))

f.close()
