# ITP 115, Spring 2024
# Final Project
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Filename: main_kim_semi.py
# Description: This program allows the user to play a game of Connections

import interface
import helper

# Function: main
# Parameter: None
# Return value: None
# This function is the starting point of the program
def main():
    print("Let's play Connections!\n")
    # Read the text file and display the game rules to the user
    interface.displayRules()
    # Read the CSV file and create the list of dictionaries
    puzzleList = helper.createPuzzleList()
    # Pick a puzzle
    puzzleDict = interface.pickPuzzle(puzzleList)
    # Result of the game
    win = interface.playGame(puzzleDict)
    if win == True:
        print("Congratulations!")
    else:
      print("Better luck next time.")
    interface.savePuzzle(puzzleDict)

main()
