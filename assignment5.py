# ITP 115, Spring 2024
# Assignment 5
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Description: This program uses range-based for loop, branching, and generates random variables.

import random

# Define an integer type variable to count # of wins and score
win = 0
score = 0

# Define a bool type variable
user_wins = False

# Use range-based for loop to run the game for 5 times
for i in range(5):
    # Get input from the user
    case = input("Enter a number (1-5): ")
    case = int(case)

    # Use a while loop to ensure the user enters a number between 1 and 5 (inclusive)
    while case < 1 or case > 5:
        case = input("Enter a number (1-5): ")
        case = int(case)
    print("You are playing for Case", case)
    print("To win, roll one of the following numbers")

    # Use range-based for loops to print the valid winning number for each of the 5 cases
    if case == 1:
        for j in range(2, 21, 2):
            print(j, end="  ")
    elif case == 2:
        for j in range(1, 20, 2):
            print(j, end="  ")
    elif case == 3:
        for j in range(5, 11):
            print(j, end="  ")
    elif case == 4:
        for j in range(10, 21, 2):
            print(j, end="  ")
    elif case == 5:
        for j in range(3, 19, 3):
            print(j, end="  ")

    # Roll the D20 by generating random number
    roll = random.randint(1, 20)
    print("\n")
    print("You rolled a", roll)

    # Use branching to check if user won based on the case
    if case == 1 and roll in range(2, 21, 2):
        user_wins = True
    elif case == 2 and roll in range(1, 20, 2):
        user_wins = True
    elif case == 3 and roll in range(5, 11):
        user_wins = True
    elif case == 4 and roll in range(10, 21, 2):
        user_wins = True
    elif case == 5 and roll in range(3, 19, 3):
        user_wins = True
    else:
        user_wins = False

    if user_wins:
        win += 1
        print("You win 50 points!\n")
    else:
        print("You didn't win.\n")

# Display total score
score = win * 50
print("Your total score is", score, "points.")
