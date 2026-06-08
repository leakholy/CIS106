#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 

@author: omar
"""
# This program asks the user to enter a part number and quantity.
# It uses the part number to determine the cost per unit, then calculates
# the total cost by multiplying the quantity by the unit cost.

# Get the part number and quantity from the user.
part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))

# Determine the unit cost based on the part number entered.
if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

# Calculate the total cost.
total_cost = quantity * unit_cost

# Display the results with decimal values aligned in columns.
print()
print("Part Order Summary")
print("------------------------------")
print(f"{'Part Number:':20s}{part_number:>10s}")
print(f"{'Quantity:':20s}{quantity:10d}")
print(f"{'Unit Cost:':20s}{unit_cost:10.2f}")
print(f"{'Total Cost:':20s}{total_cost:10.2f}")