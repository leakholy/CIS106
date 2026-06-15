#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 

@author: omar
"""
# Read item, quantity, and price from a text file.
# Compute extended price for each order.
# Display item, quantity, price, and extended price.
# After the loop, display total, count, and average order.

f = open("orders.txt", "r")

total_extended_price = 0.0
count = 0

item = f.readline().rstrip('\n')

while item != "":
    quantity = float(f.readline())
    price = float(f.readline())

    extended_price = quantity * price

    total_extended_price = total_extended_price + extended_price
    count = count + 1

    print("Item:", item)
    print("Quantity:", quantity)
    print("Price: $", format(price, ",.2f"))
    print("Extended Price: $", format(extended_price, ",.2f"))
    print()

    item = f.readline().rstrip('\n')

average_order = total_extended_price / count

print("Total Extended Prices: $", format(total_extended_price, ",.2f"))
print("Number of Orders:", count)
print("Average Order: $", format(average_order, ",.2f"))

f.close()
