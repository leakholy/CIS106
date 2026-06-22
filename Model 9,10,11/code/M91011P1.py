#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 2026

@author: omar
"""

# Function to calculate the extended price
def compute_extended_price(quantity, unit_price):
    extended_price = quantity * unit_price

    # Apply a 10% discount when the price is over $10,000
    if extended_price > 10000.00:
        extended_price = extended_price * 0.90

    return extended_price


# Stores the total extended price for all items
total_extended_price = 0.0

# Get the first quantity
quantity = float(input("Enter quantity (0 to stop): "))

# Continue until the user enters the signal value of 0
while quantity != 0:
    unit_price = float(input("Enter unit price: $"))

    # Pass the quantity and price to the function
    extended_price = compute_extended_price(quantity, unit_price)

    # Display the results for the current item
    print("Quantity:", quantity)
    print(f"Unit price: ${unit_price:.2f}")
    print(f"Extended price: ${extended_price:.2f}")

    # Add the extended price to the running total
    total_extended_price = total_extended_price + extended_price

    quantity = float(input("\nEnter quantity (0 to stop): "))

# Display the total for all items
print(f"\nTotal extended price: ${total_extended_price:.2f}")