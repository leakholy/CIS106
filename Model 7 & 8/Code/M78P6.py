#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 

@author: omar
"""

# Ask the user if they want to enter student data.
# If the user enters yes, y, or Yes, continue the loop.
# Prompt for last name and two exam scores.
# Compute and display the average.
# After the loop, display the number of students entered.

count = 0

response = input("Do you want to enter student data? Enter Yes or No: ").lower()

while response == "yes" or response == "y":
    last_name = input("Enter student last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))

    average = (exam1 + exam2) / 2

    count = count + 1

    print("Student Last Name:", last_name)
    print("Average Exam Score:", format(average, ".2f"))
    print()

    response = input("Do you want to enter another student? Enter Yes or No: ").lower()

print("Number of Students Entered:", count)