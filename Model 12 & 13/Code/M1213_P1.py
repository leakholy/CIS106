#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: omar
"""

# Function to display the names in normal order
def display_names(names):
    for name in names:
        print(name)


# Function to display the names in reverse order
def display_reverse(names):
    # Start at the last index in the list
    index = len(names) - 1

    # Move backward through the list until index reaches 0
    while index >= 0:
        print(names[index])
        index = index - 1


# List of 10 last names
last_names = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Wilson",
    "Anderson"
]


# Display the names in their original order
print("Names in original order:")
display_names(last_names)

# Print a blank line between sections
print()

# Display the names in reverse order
print("Names in reverse order:")
display_reverse(last_names)