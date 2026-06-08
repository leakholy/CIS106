#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 

@author: omar
"""

# This program asks the user to enter the number of concert tickets being purchased.
# It uses the number of tickets to determine the price per ticket, then calculates
# the total cost for the ticket order.

# Get the number of concert tickets from the user.
tickets = int(input("Enter the number of concert tickets: "))

# Determine the price per ticket based on the number of tickets purchased.
if tickets >= 25:
    price_per_ticket = 50.00
elif tickets >= 10:
    price_per_ticket = 60.00
elif tickets >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

# Calculate the total cost of the tickets.
total_cost = tickets * price_per_ticket

# Display the results with decimal values aligned in columns.
print()
print("Concert Ticket Summary")
print("------------------------------")
print(f"{'Tickets:':20s}{tickets:10d}")
print(f"{'Price Per Ticket:':20s}{price_per_ticket:10.2f}")
print(f"{'Total Cost:':20s}{total_cost:10.2f}")