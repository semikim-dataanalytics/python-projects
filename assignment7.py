# ITP 115, Spring 2024
# Assignment 7
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Description: This program defines and calls functions

import random

# Parameters: None
# Return value: None
# Description: Displays the game rules to the user
def displayRules():
    print("The rules of this game are:")
    print("\tgiant beats elf")
    print("\twizard beats giant")
    print("\telf beats wizard")
    print("\ttie if they are the same")

# Parameters: a list with strings containing the options
# Return value: a string that contains the user’s choice
# Description: Displays the options and get input from the user
def getUserChoice(optionsList):
    print("\nThe options are:", optionsList)
    userStr = input("Enter your choice: ")
    userStr = userStr.strip()
    userStr = userStr.lower()
    while userStr not in optionsList:
        userStr = input("Enter your choice: ")
        userStr = userStr.strip()
        userStr = userStr.lower()
    print("User picks", userStr)
    return userStr

# Parameters: a list with strings containing the options
# Return value: a string that contains the computer’s choice
# Description: Display what is randomly selected by the computer
def getComputerStr(optionsList):
    computerStr = random.choice(optionsList)
    print("Computer picks", computerStr)
    return computerStr

# Parameters: a string with the user's choice, a string with the computer's choice
# Return value: a string representing the result of the game
# Description: Display the result of the game
def getGameResult(userStr, computerStr):
    if userStr == computerStr:
        print("You and the computer tied.")
        return "tie"
    elif (userStr == "rock" and computerStr == "scissors") or \
        (userStr == "paper" and computerStr == "rock") or \
        (userStr == "scissors" and computerStr == "paper"):
        print("You win!")
        return "user"
    else:
        print("Computer wins.")
        return "computer"

def main():
    # Create a list variable
    optionsList = ["giant", "wizard", "elf"]
    # Create variables holding the number of times the computer/user wins.
    computerWin = 0
    userWin = 0

    displayRules()

    # Create a loop to play the game until the computer or user wins twice.
    while computerWin < 2 and userWin < 2:
        userStr = getUserChoice(optionsList)
        computerStr = getComputerStr(optionsList)
        win = getGameResult(userStr, computerStr)
        if win == "computer":
            computerWin += 1
        elif win == "user":
            userWin += 1

    # Print who won the game two times
    if computerWin > userWin:
        print("\nComputer won 2 games.")
    elif computerWin < userWin:
        print("\nYou won 2 games!")

main()
