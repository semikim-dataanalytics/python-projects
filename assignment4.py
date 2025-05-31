# ITP 115, Spring 2024
# Assignment 4
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Description: This program uses loop and branching

# Even numbers
print("Even numbers\nEnter an integer (negative number to quit)")

# Initialize variables
user_num = int(input("> "))
count = 0
even_count = 0
even_total = 0
total = 0

# Loop until user enters a negative number
while user_num >= 0:
  # Inside the loop, update the count and total variables
  count += 1
  total += user_num
  # Check if number is even
  if user_num % 2 == 0:
    even_count += 1
    even_total += user_num

  user_num = int(input("> "))

print("The count is", count)
print("The total is", total)
print("The count of even numbers is", even_count)
print("The total of even number is", even_total, "\n")


# Odd numbers
print("Odd numbers\nEnter an integer (negative number to quit)")

user_num = int(input("> "))
count = 0
odd_count = 0
odd_total = 0
total = 0

# Loop until user enters a negative number
while user_num >= 0:
  # Inside the loop, update the count and total variables
  count += 1
  total += user_num
  # Check if number is odd
  if user_num % 2 == 1:
    odd_count += 1
    odd_total += user_num

  user_num = int(input("> "))

print("The count is", count)
print("The total is", total)
print("The count of odd numbers is", odd_count)
print("The total of odd number is", odd_total)
