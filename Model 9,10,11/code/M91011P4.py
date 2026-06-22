#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 2026

@author: omar
"""
# Function to calculate the automobile's out the door price
def compute_out_the_door_price(msrp, make, model, electric_code):
    make = make.lower()
    model = model.lower()
    electric_code = electric_code.lower()

    # Determine the discount percentage
    if electric_code == "y":
        discount_percent = 0.30
    elif make == "honda" and model == "accord":
        discount_percent = 0.10
    elif make == "toyota" and model == "rav4":
        discount_percent = 0.15
    else:
        discount_percent = 0.05

    # Calculate the discount and new MSRP
    discount_amount = msrp * discount_percent
    new_msrp = msrp - discount_amount

    # Add 7% sales tax to the discounted price
    sales_tax = new_msrp * 0.07
    sales_price = new_msrp + sales_tax

    return sales_price


# Store the total MSRP and sales prices
total_msrp = 0.0
total_sales_price = 0.0

# Ask whether the user wants to run the program
response = input("Would you like to enter an automobile? (Yes or No): ")

# Continue while the user enters Yes
while response.lower() == "yes":
    make = input("Enter the automobile make: ")
    model = input("Enter the automobile model: ")
    electric_code = input("Is this an electric vehicle? (Y or N): ")
    msrp = float(input("Enter the MSRP: $"))

    # Pass the automobile information to the function
    sales_price = compute_out_the_door_price(
        msrp, make, model, electric_code
    )

    # Add the prices to their running totals
    total_msrp = total_msrp + msrp
    total_sales_price = total_sales_price + sales_price

    # Display the current automobile's results
    print("Automobile:", make, model)
    print(f"MSRP: ${msrp:.2f}")
    print(f"Out-the-door price: ${sales_price:.2f}")

    response = input(
        "\nWould you like to enter another automobile? (Yes or No): "
    )

# Display the totals for all automobiles
print(f"\nTotal MSRP: ${total_msrp:.2f}")
print(f"Total sales price: ${total_sales_price:.2f}")
