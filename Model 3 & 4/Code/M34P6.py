#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:38:00 2026

@author: omar
"""

# Calculate stock value increase or decrease

purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price per share: "))
quantity = int(input("Enter the quantity of stock: "))

value_change = (current_price - purchase_price) * quantity

print(f"Value change: ${value_change:.2f}")

if value_change > 0:
    print("The stock value increased.")
elif value_change < 0:
    print("The stock value decreased.")
else:
    print("The stock value stayed the same.")