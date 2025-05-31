# ITP 115, Spring 2024
# Assignment 9
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Description: This program reads from a CSV file and write data to a text file


# Function: createOptionsList
# Parameter: a string containing the name of a CSV file
# Return: a list of strings containing the strings from the header row of the CSV file
# Description: This function reads the first line of the CSV file
def createOptionsList(filenameStr="languages.csv"):
    # Step 1 - open the file
    fileIn = open(filenameStr, "r")
    # Step 2 - read the first line of the file
    firstLine = fileIn.readline()
    firstLine = firstLine.strip()
    optionsList = firstLine.split(",")
    # Step 3 - close the file
    fileIn.close()
    # return the list of strings
    return optionsList


# Function: createDataList
# Parameter:  a list of strings representing the choices of information the program can get about each language, a string with the choice of information the user wants, and a string containing the name of a CSV file
# Return: a list of strings with one piece of information for all languages
# Description: This function opens the CSV file, skips the first line, puts information depending on choiceStr for each language in a list, and returns the list
def createDataList(optionsList, choiceStr, filenameStr="languages.csv"):
    dataList = []
    index = optionsList.index(choiceStr)
    fileIn = open(filenameStr, "r")
    fileIn.readline()
    for line in fileIn:
        line = line.strip()
        lineList = line.split(",")
        dataList.append(lineList[index])
    fileIn.close()
    return dataList


# Function: getUserChoice
# Parameter: a list with strings representing the choices of information the program can get about each language
# Return: a string containing the choice the user wants to learn about a language
# Description: This function gets the user’s choice and continues to repeat until they enter a string from the optionsList parameter
def getUserChoice(optionsList):
    optionsList = createOptionsList(filenameStr="languages.csv")
    print("Available information about the languages include")
    print(optionsList[2:])  # use slicing to create a list variable containing the choices
    # Get input from the user
    choiceStr = input("Enter your choice: ")
    choiceStr = choiceStr.strip()
    choiceStr = choiceStr.lower()
    # Loop until the user enters a valid choice
    while choiceStr not in optionsList[2:]:
        print(choiceStr, "is not a valid choice")
        choiceStr = input("Enter your choice: ")
        choiceStr = choiceStr.strip()
        choiceStr = choiceStr.lower()
    print("You have entered", choiceStr)
    return choiceStr


# Function: writeTextFile
# Parameter: a list of strings with the names of the languages, a list of strings with information about the languages, a string with the choice of information
# Return: None
# Description: This function writes the names and information about each language in a text file
def writeTextFile(langList, infoList, choiceStr):
    fileOut = open(choiceStr + ".txt", "w")
    print("language ->", choiceStr, file=fileOut)
    # Loop through the length of the langList
    for i in range(len(langList)):
        if infoList[i] != "NA":
            print(langList[i], "->", infoList[i], file=fileOut)
    fileOut.close()
    print("\nInformation saved to", choiceStr + ".txt")


def main():
    print("Computer Languages")
    optionsList = createOptionsList()
    choiceStr = getUserChoice(optionsList)
    langList = createDataList(optionsList, "title")
    infoList = createDataList(optionsList, choiceStr)
    writeTextFile(langList, infoList, choiceStr)


main()
