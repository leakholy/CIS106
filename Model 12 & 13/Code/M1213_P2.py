#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: omar
"""

# Function to display names and scores in normal order
def display_students(names, scores):
    index = 0

    while index < len(names):
        print(names[index], scores[index])
        index = index + 1


# Function to display names and scores in reverse order
def display_reverse(names, scores):
    # Start at the last index in the list
    index = len(names) - 1

    # Move backward through both parallel lists
    while index >= 0:
        print(names[index], scores[index])
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


# Parallel list of exam scores
exam_scores = [
    85,
    92,
    78,
    88,
    95,
    81,
    90,
    76,
    89,
    93
]


# Display students and scores in original order
print("Names and scores in original order:")
display_students(last_names, exam_scores)

print()

# Display students and scores in reverse order
print("Names and scores in reverse order:")
display_reverse(last_names, exam_scores)