# ITP 115, Spring 2024
# Assignment 8
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Description: This program defines and calls functions to simulate a game of Crack the Code

import random

# Function: createCodeList
# Parameter: a string that holds input from the user
# Return: a boolean (True or False) depending on if userStr is a string containing one single digit
def isSingleDigit(userStr):
    if len(userStr) == 1 and userStr.isdigit():
        return True
    else:
        return False

# Function: createCodeList
# Parameter: an integer that is the number of digits in each list
# Return: a list containing integers with the secrete code
def createCodeList(size):
    codeList = []
    for i in range(size):
        codeList.append(random.randint(0,9))
    return codeList

# Function: createUserList
# Parameter: an integer that is the number of digits in each list
# Return: a list containing integers with a guess of the code from the user
def createUserList(size):
    userList = []
    print("\nThe number of digits in the code is", size)
    for i in range(size):
        userStr = input("Enter a digit at index " + str(i) + ": ")
        # repeat while the user’s input (a string) is not a single digit
        while not isSingleDigit(userStr):
            print("Invalid input. Please enter a single digit.")
            userStr = input("Enter a digit at index " + str(i) + ": ")
        userList.append(int(userStr))  # convert the user's input to an integer
    return userList

# Function: displayHints
# Parameters: a list containing integers with the secrete code, a list containing integers with a guess of the code from
# the user, an integer that is the number of digits in each list
# Return: None
# Description: Display messages if each digit in the user’s list is located in the code list (correct position or not)
# and how many times it occurs
def displayHints(codeList, userList, size):
    print("\nGenerating hints...")
    hint_count = 0  # an integer to count the number of hints
    # Check whether the user guessed a digit in the code list
    for i in range(size):
        occurrence = codeList.count(userList[i])  # the number of times the digit in the user's list at that index in the code
        # If the count is greater than 0, increase the hints count and display a hint to the user
        if occurrence > 0:
            hint_count += 1
            print(userList[i], "at index", i, "occurs", occurrence, "time(s)")
    # Check if the digits of the two lists are equal at that index
    for i in range(size):
        if codeList[i] == userList[i]:
            print(userList[i], "at index", i, "is correct")
    # If no hints were displayed...
    if hint_count == 0:
        print("No correct digits")

def main():
    size = 3
    codeList = createCodeList(size)
    userList = createUserList(size)
    guess = 1
    # Loop until the user crack the code
    while userList != codeList:
        print("Your guess is", userList)
        displayHints(codeList, userList, size)
        guess += 1
        userList = createUserList(size)
    # pPrint the number of guesses it took the user to crack the code
    print("\nYou cracked the code in", guess, "guesses!")

main()
