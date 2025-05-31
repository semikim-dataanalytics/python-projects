# ITP 115, Spring 2024
# Final Project
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Filename: interface.py
# Description: This file creates functions to interact with the user

import helper
import pretty_print

# Function: displayRules
# Parameter: textfileStr is a string with name of the text file to read and it has a default value of "game_rules.txt"
# Return value: None
# This function reads the text file and prints each line to the user
def displayRules(textfileStr="game_rules.txt"):
    file = open(textfileStr, "r")
    for line in file:
        print(line.strip())
    file.close()

# Function: isValidNumber
# Parameter 1: userStr is a string with input from the user
# Parameter 2: startNum is an integer which is the first number in the range of valid numbers
# Parameter 3: endNum is an integer which is the last number in the range of valid numbers (inclusive)
# Return value: a Boolean, True if the userStr parameter is a digit and a number in the range starting at startNum and ending at endNum (inclusive), otherwise False
# This function determines if the user entered a valid number
def isValidNumber(userStr, startNum, endNum):
    if userStr.isdigit():
        userNum = int(userStr)
        if startNum <= userNum <= endNum:
            return True
    return False

# Function: pickPuzzle
# Parameter: puzzleList is a list of dictionaries where each dictionary represents a puzzle
# Return value: a dictionary representing one puzzle based on the user’s input for the puzzle number
# This function allows the user to enter input to pick the puzzle number
def pickPuzzle(puzzleList):
    startNum = 1
    endNum = len(puzzleList)
    userStr = input("Enter a puzzle number (1-294): ")
    while not isValidNumber(userStr, startNum, endNum):
        userStr = input("Enter a puzzle number (1-294): ")
    puzzleDict = helper.getPuzzleByNum(puzzleList, userStr)
    return puzzleDict

# Function: getGuessList
# Parameter: wordList is a list of strings which are the words from the puzzle that have not been connected yet
# Return value: a list of strings containing four items entered by the user that are sorted in alphabetical order
# This function creates a list of four strings with items that are from the wordList parameter
def getGuessList(wordList):
    print("Enter four items for your guess")
    guessList = []
    for i in range(1, 5):
        user_guess = input("Item #" + str(i) + ": ")
        user_guess = user_guess.strip().upper()
        # Loop until the user enters a valid input
        while user_guess not in wordList or user_guess in guessList:
            user_guess = input("Item #" + str(i) + ": ")
            user_guess = user_guess.strip().upper()
        guessList.append(user_guess)  # add the user's guess to the guess list
    guessList.sort()
    return guessList

# Function: checkConnection
# Parameter 1: puzzleDict is a dictionary that represents one puzzle
# Parameter 2: guessList is a list of strings with four items
# Return value: an integer that is the difficulty number (1 – 4) of the connection group that matches guessList, otherwise 0 if guessList is not one of the connection groups
# This function checks to see if the guessList is one of the connection groups in
# puzzleDict. If so, it returns the difficulty number. Otherwise, it returns 0
def checkConnection(puzzleDict, guessList):
    for i in range(1, 5):
        wordGroup = helper.getGroup(puzzleDict, i)
        if wordGroup == guessList:
            return i
    return 0

# Function: playGame
# Parameter: puzzleDict is a dictionary that represents one puzzle
# Return value: a Boolean, True if the user won the game, otherwise False
# This function allows the user to play a game by calling various functions.
# The game will display a 4x4 grid of words and ask users to enter 4 words (their guess) to make a connection
# The game ends when the user has guessed all 4 connections or makes 4 mistakes
def playGame(puzzleDict):
    foundGroupList = []
    mistakes = 0
    while len(foundGroupList) != 4 and mistakes < 4:
        pretty_print.displayGrid(puzzleDict, foundGroupList, mistakes)
        wordList = helper.getWordList(puzzleDict, foundGroupList)
        guessList = getGuessList(wordList)
        difficultyNum = checkConnection(puzzleDict, guessList)
        if difficultyNum == 0:
            mistakes += 1
        else:
            if difficultyNum not in foundGroupList:
                foundGroupList.append(difficultyNum)
    # pretty_print.displayGrid(puzzleDict, foundGroupList, mistakes)
    if len(foundGroupList) == 4:
        return True
    return False

# Function: savePuzzle
# Parameter: puzzleDict is a dictionary that represents one puzzle
# Return value: None
# This function writes the puzzle to a file. The file's name is the date of the puzzle
# without spaces and has a .txt file extension.
# Write each group on its own line in the following format:
# COLOR: CONNECTION ['WORD1', 'WORD2', 'WORD3', 'WORD4']
def savePuzzle(puzzleDict):
    fileOut = open(puzzleDict["date"].replace(" ", "") + ".txt", "w")
    for difficultyNum in range(1, 5):
        color = helper.getColor(puzzleDict, difficultyNum)
        connection = helper.getConnection(puzzleDict, difficultyNum)
        wordGroup = helper.getGroup(puzzleDict, difficultyNum)
        print(color + ":", connection, wordGroup, file=fileOut)
    fileOut.close()
    print("Puzzle", puzzleDict["num"], "has been saved to", puzzleDict["date"].replace(" ", "") + ".txt")
