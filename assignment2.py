# ITP 115, Spring 2024
# Assignment 2
# Name: Semi
# Email: username@usc.edu
# Section: 31849
# Description: This program creates variables, gets user input, and displays information to the user.

# create a string variable
coderName = "Semi Kim"
# create an integer variable
coderAge = 20

# create string variables getting user input and display information to the user
userName = input("Enter your name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter your favorite food: ")
# create a float variable
cost = float(input("Enter cost for food: "))
# multiply a float variable by 2
cost *= 2
userAge = input("Enter your age: ")
# create an integer variable by adding up two integer variables
expression = int(coderAge) + int(userAge)

# output for user; convert integer and float variables to string variables
print("This code is written by " + coderName + ".")
print("Once upon a time, \"" + userName + "\" and I " + "went to the \"" + place + "\".")
print("We had a yummy lunch eating \"" + food + "\" which cost us $\'" + str(cost) + "\'.")
print("We met a \"" + animal + "\" who made us smile.")
print("We will all be friends for at least \'" + str(expression) + "\' years.")
