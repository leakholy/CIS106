#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: omar
"""

class Employee:

    # Initialize the employee information
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    # Return the employee's full name
    def fullname(self):
        return self.first + " " + self.last

    # Calculate and return the employee's bonus
    def calculate_bonus(self, bonus_rate):
        bonus = bonus_rate * self.pay
        return bonus


# Create an Employee object
emp_1 = Employee("John", "Smith", 50000)


# Display the employee information
print("Employee Name:", emp_1.fullname())
print("Email:", emp_1.email)
print("Salary: $", emp_1.pay)


# Ask the user to enter the bonus rate
bonus_rate = float(input("Enter bonus rate (example .10 for 10%): "))


# Calculate the employee bonus
bonus = emp_1.calculate_bonus(bonus_rate)


# Display the employee bonus
print("Employee Bonus: $", bonus)