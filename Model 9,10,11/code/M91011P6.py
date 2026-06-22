#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 2026

@author: omar
"""

# Function to calculate total points and average exam score
def compute_exam_results(exam1, exam2, exam3):
    total_points = exam1 + exam2 + exam3
    average = total_points / 3

    # Return both values to the main part of the program
    return total_points, average


# Get the first student's last name
last_name = input("Enter student's last name (Done to stop): ")

# Continue until the user enters Done
while last_name.lower() != "done":
    exam1 = float(input("Enter exam 1 score: "))
    exam2 = float(input("Enter exam 2 score: "))
    exam3 = float(input("Enter exam 3 score: "))

    # Receive both values returned by the function
    total_points, average = compute_exam_results(
        exam1, exam2, exam3
    )

    # Display the results in the main part of the program
    print("Student's last name:", last_name)
    print(f"Total points: {total_points:.2f}")
    print(f"Average exam score: {average:.2f}")

    last_name = input(
        "\nEnter student's last name (Done to stop): "
    )