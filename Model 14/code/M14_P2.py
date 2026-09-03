#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: omar
"""

class Student:

    # Initialize the student information
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.credits = credits

    # Calculate and return the tuition owed
    def calculate_tuition(self):

        # In-district students pay $250 per credit
        if self.district_code == "I":
            tuition = self.credits * 250

        # All other students pay $500 per credit
        else:
            tuition = self.credits * 500

        return tuition


# Create a student object
student_1 = Student("John", "Smith", "I", 12)


# Display the student information
print("Student Name:", student_1.first_name, student_1.last_name)
print("District Code:", student_1.district_code)
print("Enrolled Credits:", student_1.credits)


# Calculate the tuition
tuition = student_1.calculate_tuition()


# Display the tuition owed
print("Tuition Owed: $", tuition)