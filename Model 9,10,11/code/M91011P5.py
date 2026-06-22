#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 2026

@author: omar
"""

# Function to calculate the discount amount and discounted price
def compute_discount(quantity, price, discount_rate):
    extended_price = quantity * price
    discount_amount = extended_price * discount_rate
    discounted_price = extended_price - discount_amount

    # Return two values to the main part of the program
    return discount_amount, discounted_price


# Get the first quantityy
quantity = float(input("Enter quantity (0 to stop): "))

# Continue until the user enters the signal value of 0
while quantity != 0:
    price = float(input("Enter unit price: $"))
    discount_rate = float(
        input("Enter discount rate as a decimal (example: 0.10): ")
    )

    # Receive both values returned by the function
    discount_amount, discounted_price = compute_discount(
        quantity, price, discount_rate
    )

    # Display the results in the main part of the program
    print("Quantity:", quantity)
    print(f"Unit price: ${price:.2f}")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Discounted price: ${discounted_price:.2f}")

    quantity = float(input("\nEnter quantity (0 to stop): "))