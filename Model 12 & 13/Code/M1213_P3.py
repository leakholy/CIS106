#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: omar
"""

# Function to display all names and scores
def display_students(names, scores):
    index = 0

    while index < len(names):
        print(names[index], scores[index])
        index = index + 1


# Function to find and display the highest score
def display_highest(names, scores):
    high_var = 0
    high_index = 0

    # Check each score in the list
    index = 0

    while index < len(scores):
        if scores[index] > high_var:
            high_var = scores[index]
            high_index = index

        index = index + 1

    print("Highest score:")
    print(names[high_index], high_var)


# Function to find and display the lowest score
def display_lowest(names, scores):
    low_var = 999
    low_index = 0

    # Check each score in the list
    index = 0

    while index < len(scores):
        if scores[index] < low_var:
            low_var = scores[index]
            low_index = index

        index = index + 1

    print("Lowest score:")
    print(names[low_index], low_var)


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


# Display all students and scores
print("Student names and exam scores:")
display_students(last_names, exam_scores)

print()

# Display the highest score
display_highest(last_names, exam_scores)

print()

# Display the lowest score
display_lowest(last_names, exam_scores)