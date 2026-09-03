#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: omar
"""

def student_averages(grades):
    averages = []

    # Loop through each student in the dictionary
    for name in grades:
        total = 0

        # Add all three grades for the student
        for grade in grades[name]:
            total = total + grade

        # Calculate the student's average
        average = total / 3

        # Store the student's name and average in a list
        averages.append([name, average])

    # Return the completed list of student averages
    return averages


# This function calculates the class average for each of the three grades
def class_averages(grades):
    grade1_total = 0
    grade2_total = 0
    grade3_total = 0
    student_count = 0

    # Loop through each student
    for name in grades:
        # Add each grade to its matching total
        grade1_total = grade1_total + grades[name][0]
        grade2_total = grade2_total + grades[name][1]
        grade3_total = grade3_total + grades[name][2]

        # Count how many students are in the dictionary
        student_count = student_count + 1

    # Calculate the class average for each grade
    grade1_average = grade1_total / student_count
    grade2_average = grade2_total / student_count
    grade3_average = grade3_total / student_count

    # Return all three class averages
    return [grade1_average, grade2_average, grade3_average]


# Dictionary containing student names and three grades for each student
student_grades = {
    "Smith": [90, 85, 88],
    "Johnson": [78, 82, 80],
    "Williams": [95, 92, 96],
    "Brown": [88, 84, 86],
    "Jones": [76, 79, 81]
}


# Call the functions and store the returned results
averages = student_averages(student_grades)
class_avg = class_averages(student_grades)


# Print the student average heading
print("Student\t\tAverage")
print("------------------------")

# Print each student's name and average
for student in averages:
    print(student[0], "\t\t", round(student[1], 2))


# Print the class averages for each grade
print("\nClass Grade Averages")
print("------------------------")
print("Grade 1 Average:", round(class_avg[0], 2))
print("Grade 2 Average:", round(class_avg[1], 2))
print("Grade 3 Average:", round(class_avg[2], 2))