#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 

@author: omar
"""
# This program asks the user to enter the principal amount of a CD and the
# years to maturity. It uses both values to determine the interest rate, then
# calculates the first year interest amount.

# Get the principal amount and years to maturity from the user.
principal = float(input("Enter the principal amount: "))
years = int(input("Enter the years to maturity: "))

# Determine the interest rate based on the principal amount and maturity years.
if principal > 100000 and years == 5:
    interest_rate = 0.06
elif principal >= 50000 and principal <= 100000 and years == 10:
    interest_rate = 0.05
elif principal >= 50000 and principal <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

# Calculate the first year interest amount.
interest_amount = principal * interest_rate

# Display the results with decimal values aligned in columns.
print()
print("CD Interest Summary")
print("------------------------------")
print(f"{'Principal:':20s}{principal:10.2f}")
print(f"{'Years:':20s}{years:10d}")
print(f"{'Interest Rate:':20s}{interest_rate:10.2%}")
print(f"{'Interest Amount:':20s}{interest_amount:10.2f}")
