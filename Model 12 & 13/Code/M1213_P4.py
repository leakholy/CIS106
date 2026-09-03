#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: omar
"""

# Dictionary with student names as keys and grades as values
student_grades = {
    "Smith": 85,
    "Johnson": 92,
    "Williams": 78,
    "Brown": 88,
    "Jones": 95,
    "Garcia": 81,
    "Miller": 90,
    "Davis": 76,
    "Wilson": 89,
    "Anderson": 93
}


# Variables used to calculate the class average
total = 0
count = 0


# Print column headers
print("Student".ljust(15), "Grade")
print("--------------------")


# Display each student and grade
for name in student_grades:
    print(name.ljust(15), student_grades[name])

    # Add each grade to the total
    total = total + student_grades[name]
    count = count + 1


# Calculate the class average
average = total / count


# Display the class average
print()
print("Class Average:", format(average, ".2f"))