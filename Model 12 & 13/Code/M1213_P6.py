#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: omar
"""

def display_players(players):

    # Print column headings
    print("Player Name\tBatting Average")
    print("--------------------------------")

    # Loop through each player in the dictionary
    for name in players:
        print(name, "\t\t", players[name])


# Create an empty dictionary to hold the player information
player_dictionary = {}


# Open the file containing the player names and batting averages
with open("players.txt", "r") as player_file:

    # Read each line from the file
    for line in player_file:

        # Separate the player's name and batting average
        data = line.strip().split(",")

        # Store the player's name
        player_name = data[0]

        # Convert the batting average to a decimal number
        batting_average = float(data[1])

        # Add the player and batting average to the dictionary
        player_dictionary[player_name] = batting_average


# Call the function to display the dictionary
display_players(player_dictionary)