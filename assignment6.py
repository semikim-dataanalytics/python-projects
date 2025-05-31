# ITP 115, Spring 2024
# Assignment 6
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Description: This program uses while loops and if statements along with string methods

import random

# Define the lists of words, jumbled words, and hints
word = ['trojan', 'apple', 'pencil', 'python']
jumble = ['ajnort', 'pelpa', 'cnelip', 'nohtyp']
hint = ['USC', 'fruit', 'writing', 'programming']

print("There are 4 words in the guessing game.")

# Get a random number
index = random.randint(0, 3)

# Display the number of letters and the jumbled word
print("\nA random word has been picked for you, and it has", len(word[index]), "letters")  # use len() to get the length of the word
print("The jumbled word is \'" + jumble[index] + "\'")

# Ask the user to guess the word
guess = input("\nEnter a guess: ")
counter = 1

# Loop until the guess is correct
while guess.lower() != word[index]:  # use .lower() to convert the guess to lowercase
    counter += 1
    print("Your guess is incorrect")
    y_or_n = input("Do you want a hint? (y/n): ")
    if y_or_n.lower() == 'y':
        print("The hint is \'" + hint[index] + "\'")
    print("The jumbled word is \'" + jumble[index] + "\'")
    guess = input("\nEnter a guess: ")  # ask the user to guess again

# If the guess is correct, display the word and the number of guesses
if guess.lower() == word[index]:
    print("The word is \'" + word[index] + "\'")
    print("The number of guesses is", counter)
