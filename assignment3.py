# ITP 115, Spring 2024
# Assignment 3
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Description: This program creates variables, gets user input, and displays information to the user.
# This program uses branching, integer division and modulo operators.

print("Select a food item:")
print("a) Aero Chocolate Bar for $1.95")
print("b) Beaver Tail Pastry for $7.25")
print("c) Coffee Crisp for $2.40")
print("d) Dill Pickle Chips for $4.35")

# Get user input
user_choice = input("Choice: ")
user_choice = user_choice.lower()

# Use branching (if-elif-else) to get user's choice and the cost in pennies
if user_choice == "a":
    print("The item selected is the Aero Chocolate Bar.\n")
elif user_choice == "b":
    print("The item selected is the Beaver Tail Pastry.\n")
elif user_choice == "c":
    print("The item selected is the Coffee Crisp.")
elif user_choice == "d":
    print("The item selected is the Dill Pickle Chips.\n")
else:
    print("You entered an invalid choice.")
    print("The item selected is the Coffee Crisp.\n")

# Get user input
print("Payment Time!")
toonies = input("# of toonies: ")
loonies = input("# of loonies: ")
quarters = input("# of quarters: ")
nickels = input("# of nickels: ")

# Calculate the payment in cents and put that into a variable
payment = 200 * int(toonies) + 100 * int(loonies) + 25 * int(quarters) + 5 * int(nickels)

# Get user input for the payment
if user_choice == "a":
    item = "Aero Chocolate Bar"
    cost = 195

elif user_choice == "b":
    item = "Beaver Tail Pastry"
    cost = 725

elif user_choice == "c":
    item = "Coffee Crisp"
    cost = 240

elif user_choice == "d":
    item = "Dill Pickle Chips"
    cost = 435

else:
    item = "Coffee Crisp"
    cost = 240

print("\nCost is", str(cost), "cents")
print("Payment is", payment, "cents\n")

# Use branching (if statement) to check if the payment is enough
if cost > payment:
    print("You did not enter enough money and will not receive the", item)

else:
    print("You purchased the", item)
    change = payment - cost
    print("Your change is", str(change), "cents")

    # Calculate the change using the integer division and modulo operators
    toonies_change = change // 200
    change = change % 200
    loonies_change = change // 100
    change = change % 100
    quarters_change = change // 25
    change = change % 25
    nickels_change = change // 5
    change = change % 5

    print("Coins returned")
    print("# of toonies is", str(toonies_change))
    print("# of loonies is", str(loonies_change))
    print("# of quarters is", str(quarters_change))
    print("# of nickels is", str(nickels_change))
