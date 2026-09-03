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

        # Dictionary containing district codes and tuition rates
        tuition_rates = {
            "I": 250,
            "O": 500,
            "X": 800,
            "G": 250
        }

        # Get the tuition rate using the student's district code
        rate = tuition_rates[self.district_code]

        # Calculate tuition based on credits and rate
        tuition = self.credits * rate

        return tuition


# Create one student for each district code
student_1 = Student("John", "Smith", "I", 12)
student_2 = Student("Maria", "Garcia", "O", 12)
student_3 = Student("James", "Wilson", "X", 12)
student_4 = Student("Sarah", "Brown", "G", 12)


# Create a list containing all student objects
students = [student_1, student_2, student_3, student_4]


# Display each student's information
for student in students:

    print("Student Name:", student.first_name, student.last_name)
    print("District Code:", student.district_code)
    print("Enrolled Credits:", student.credits)
    print("Tuition Owed: $", student.calculate_tuition())
    print()