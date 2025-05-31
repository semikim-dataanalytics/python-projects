# ITP 115, Spring 2024
# Final Project
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Filename: helper.py
# Description: This file creates functions to read the CSV file, create a list of dictionaries, and perform tasks

# Function: createPuzzleList
# Parameter: filenameStr is a string with name of the CSV file to read and it has a default value of "connections_data.csv"
# Return value: a list of dictionaries where each dictionary represents one puzzle
# This function reads the CSV file and creates a list of puzzles which is the main data
# structure used in this program.
def createPuzzleList(filenameStr="connections_data.csv"):
    puzzleList = []  # create an empty list
    file = open(filenameStr, "r")  # open a file for reading
    keys = file.readline()  # read the first line
    keys = keys.strip().split(",")
    for line in file:
        puzzleDict = {}  # create an empty dictionary for one puzzle
        values = line.strip().split(",")
        for i in range(len(keys)):
            puzzleDict[keys[i]] = values[i]  # assign the value to the key
        puzzleList.append(puzzleDict)  # add the dictionary to the list
    file.close()
    return puzzleList

# Function: getPuzzleByNum
# Parameter 1: puzzleList is a list of dictionaries where each dictionary represents a puzzle
# Parameter 2: numStr is a string which is one of the valid values in puzzleList for the "num" key
# Return value: a dictionary representing one puzzle where the value for the "num" key is the numStr parameter
# This function uses the two parameters to return one dictionary which represents one puzzle
def getPuzzleByNum(puzzleList, numStr):
    # Loop through the puzzleList parameter
    for puzzleDict in puzzleList:
        if puzzleDict.get("num") == numStr:  # compare the value based on "num key with numStr
          return puzzleDict
    return {}

# Function: getColor
# Parameter 1: puzzleDict is a dictionary that represents one puzzle
# Parameter 2: difficultyNum is an integer which is one of the difficulty levels (1 – 4)
# Return value: a string with the color that corresponds to the difficulty level
# This function returns a string ("YELLOW", "GREEN", "BLUE", "PURPLE") based on the difficultyNum parameter
def getColor(puzzleDict, difficultyNum):
    key = "color" + str(difficultyNum)
    color = puzzleDict.get(key)
    return color

# Function: getConnection
# Parameter 1: puzzleDict is a dictionary that represents one puzzle
# Parameter 2: difficultyNum is an integer which is one of the difficulty levels (1 – 4)
# Return value: a string with the connection that corresponds to the difficulty level
# This function returns the connection string based on the difficultyNum parameter.
def getConnection(puzzleDict, difficultyNum):
    key = "connection" + str(difficultyNum)
    connection = puzzleDict.get(key)
    return connection

# Function: getGroup
# Parameter 1: puzzleDict is a dictionary that represents one puzzle
# Parameter 2: difficultyNum is an integer which is one of the difficulty levels (1 – 4)
# Return value: a list of strings which are the four items in a group based on the difficulty level
def getGroup(puzzleDict, difficultyNum):
    wordGroup = []  # create an empty list
    # Loop through the numbers 1 to 4
    for i in range(1,5):
        key = "word" + str(difficultyNum) + str(i)
        word = puzzleDict.get(key)  # get the value based on the key
        wordGroup.append(word)  # append the value to the list
    return wordGroup

# Function: getWordList
# Parameter 1: puzzleDict is a dictionary that represents one puzzle
# Parameter 2: foundGroupList is a list of integers holding the difficulty levels (1 – 4) that have already been found
# Return value: a list of strings which are the items in the puzzle that have not been connected yet
# This function creates a list of the words that have not been connected
def getWordList(puzzleDict, foundGroupList):
    wordList = []
    for i in range(1, 5):
        if i not in foundGroupList:
            wordGroup = getGroup(puzzleDict, i)
            for word in wordGroup:
                wordList.append(word)
    return wordList
