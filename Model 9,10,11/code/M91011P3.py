#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:04:00 2026

@author: omar
"""

# Function to calculate next month's sales forecast
def compute_forecast(month, sales):
    month = month.lower()

    # Determine the forecast percentage
    if month == "jan" or month == "feb" or month == "mar":
        forecast_percent = 0.10
    elif month == "apr" or month == "may" or month == "jun":
        forecast_percent = 0.15
    elif month == "jul" or month == "aug" or month == "sep":
        forecast_percent = 0.20
    elif month == "oct" or month == "nov" or month == "dec":
        forecast_percent = 0.25
    else:
        forecast_percent = 0.0

    # Calculate and return next month's sales
    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales


# Ask whether the user wants to run the program
response = input("Would you like to enter a sales forecast? (Yes or No): ")

# Continue while the user enters Yes
while response.lower() == "yes":
    last_name = input("Enter salesperson's last name: ")
    month = input("Enter the month abbreviation: ")
    sales = float(input("Enter current sales: $"))

    # Pass the month and sales to the function
    next_month_sales = compute_forecast(month, sales)

    # Display the forecast
    print("Salesperson's last name:", last_name)
    print(f"Next month's sales forecast: ${next_month_sales:.2f}")

    response = input(
        "\nWould you like to enter another sales forecast? (Yes or No): "
    )