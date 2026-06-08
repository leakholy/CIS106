#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 

@author: omar
"""

# This program asks the user to enter the quantity of widgets being purchased.
# It uses the quantity to determine the correct price per widget, then calculates
# the extended price, tax amount, and final total.

# Get the widget quantity from the user.
quantity = int(input("Enter the quantity of widgets: "))

# Determine the price per widget based on the quantity entered.
if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00

# Calculate the extended price, tax, and total.
extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

# Display the results with decimal values aligned in columns.
print()
print("Widget Order Summary")
print("------------------------------")
print(f"{'Quantity:':20s}{quantity:10d}")
print(f"{'Price:':20s}{price:10.2f}")
print(f"{'Extended Price:':20s}{extended_price:10.2f}")
print(f"{'Tax:':20s}{tax:10.2f}")
print(f"{'Total:':20s}{total:10.2f}")