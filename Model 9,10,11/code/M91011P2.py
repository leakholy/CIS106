#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 2026

@author: omar
"""

# Function to calculate the player's batting average
def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        batting_average = 0.0
    else:
        batting_average = hits / at_bats

    return batting_average


# Stores the number of players entered
player_count = 0

# Get the first player's last name
last_name = input("Enter player's last name (Done to stop): ")

# Continue until the user enters Done
while last_name.lower() != "done":
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))

    # Pass hits and at bats to the function
    batting_average = compute_batting_average(hits, at_bats)

    # Display the player's information
    print("Player's last name:", last_name)
    print(f"Batting average: {batting_average:.3f}")

    # Increase the player count by one
    player_count = player_count + 1

    last_name = input("\nEnter player's last name (Done to stop): ")

# Display the total number of players entered
print("\nNumber of players entered:", player_count)