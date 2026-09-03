#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: omar
"""

# List used to store all dog information
dogs = []


# Main function
def main():
    # Start the menu
    menu()


# Menu function
def menu():
    choice = 0

    # Keep showing the menu until the user chooses 4
    while choice != 4:
        print("\nDog Rescue")
        print("----------")
        print("1. Add a Dog")
        print("2. View Dogs")
        print("3. Find Dog")
        print("4. Quit")

        # Ask the user to select an option
        choice = int(input("\nSelect a choice: "))

        # Add a new dog
        if choice == 1:
            addDog()

        # View all dogs
        elif choice == 2:
            viewDogs()

        # Find a dog
        elif choice == 3:
            findDog()

        # Quit the program
        elif choice == 4:
            print("Goodbye")

        else:
            print("Invalid choice. Please select 1 through 4.")


# Function used to add a dog
def addDog():

    # Ask the user for the dog's information
    dog_name = input("\nDog Name: ")
    dog_breed = input("Dog Breed: ")
    dog_age = int(input("Age: "))
    dog_weight = float(input("Weight: "))

    # Store the dog information in a list
    dog = [dog_name, dog_breed, dog_age, dog_weight]

    # Add the dog to the main dogs list
    dogs.append(dog)

    # Confirm that the dog was added
    print("\nDog added successfully.")


# Function used to display all dogs
def viewDogs():

    print("\nRescue Dogs")
    print("------------------------------------------------------------")
    print("Dog\t\tBreed\t\t\tAge\tWeight")
    print("------------------------------------------------------------")

    # Loop through each dog in the list
    for dog in dogs:
        print(dog[0], "\t\t", dog[1], "\t\t", dog[2], "\t", dog[3])


# Function used to search for a dog by name
def findDog():

    # Ask the user for the dog's name
    search_name = input("\nEnter dog name to find: ")

    # Assume the dog has not been found yet
    found = False

    # Loop through each dog in the list
    for dog in dogs:

        # Compare the entered name to the stored dog name
        if dog[0].lower() == search_name.lower():
            print("\nFound", dog[0])
            print("Breed:", dog[1])
            print("Age:", dog[2])
            print("Weight:", dog[3])

            found = True

    # Display a message if the dog was not found
    if found == False:
        print("\nSorry, unable to find", search_name)


# Call the main function
main()