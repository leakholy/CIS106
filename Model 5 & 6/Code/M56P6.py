#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 

@author: omar
"""
# This program asks the user to enter an employee's last name, salary, and job level.
# It uses the job level to determine the bonus rate, then calculates the employee's
# bonus by multiplying the salary by the bonus rate.

# Get the employee information from the user.
last_name = input("Enter the employee's last name: ")
salary = float(input("Enter the employee's salary: "))
job_level = int(input("Enter the job level: "))

# Determine the bonus rate based on the employee's job level.
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

# Calculate the employee's bonus.
bonus = salary * bonus_rate

# Display the employee name and bonus with decimal values aligned in columns.
print()
print("Employee Bonus Summary")
print("------------------------------")
print(f"{'Last Name:':20s}{last_name:>10s}")
print(f"{'Salary:':20s}{salary:10.2f}")
print(f"{'Job Level:':20s}{job_level:10d}")
print(f"{'Bonus Rate:':20s}{bonus_rate:10.2%}")
print(f"{'Bonus:':20s}{bonus:10.2f}")
