# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# This program asks the user to enter the quantity of an item being ordered.
# It uses the quantity to determine the correct unit price, then calculates
# the extended price, sales tax, and final total.

# Get the quantity from the user.
quantity = int(input("Enter the quantity of the item: "))

# Determine the unit price based on the quantity entered.
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

# Calculate the extended price, tax, and total.
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

# Display the results with decimal values aligned in columns.
print()
print("Order Summary")
print("------------------------------")
print(f"{'Quantity:':20s}{quantity:10d}")
print(f"{'Unit Price:':20s}{unit_price:10.2f}")
print(f"{'Extended Price:':20s}{extended_price:10.2f}")
print(f"{'Tax:':20s}{tax:10.2f}")
print(f"{'Total:':20s}{total:10.2f}")
