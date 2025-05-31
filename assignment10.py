# ITP 115, Spring 2024
# Assignment 10
# Name: Semi Kim
# Email: rkim2273@usc.edu
# Section: 31849
# Description: This program creates a dictionary and allows the user to add, update, and delete items from the dictionary

# Parameter: None
# Return value: None
# Goal: display choices to the user
def displayChoices():
    print("\nEvents Dictionary")
    print("\tA) Add an event")
    print("\tU) Update an event")
    print("\tD) Delete an event")
    print("\tP) Print the events")
    print("\tQ) Quit")

# Parameter: a dictionary containing events where the keys are events and the values are the dates
# Return value: None
# Goal: display the events in alphabetical order with each event on their own line
def displayEvents(eventDict):
    eventList = list(eventDict.keys())
    eventList.sort()
    for event in eventList:
        print(event, "occurs on", eventDict[event])

# Parameter: a dictionary containing events
# Return value: None
# Goal: get user input to add an event to the eventDict parameter
def addEvent(eventDict):
    event = input("Enter an event: ")
    event = event.title()
    if event in eventDict:
        print(event, "is already in the events dictionary")
    else:
        date = input("Enter the date: ")
        date = date.title()
        eventDict[event] = date
        print(event, "has been added to the events dictionary")

# Parameter: a dictionary containing events
# Return value: None
# Goal: get user input to update the date of an event in the eventDict parameter
def updateEvent(eventDict):
    event = input("Enter an event: ")
    event = event.title()
    if event in eventDict:
        date = input("Enter the date: ")
        date.title()
        eventDict[event] = date
        print(event, "has been updated to", date)
    else:
        print(event, "is not in the events dictionary")

# Parameter: a dictionary containing events
# Return value: None
# If it is in the eventDict, remove the event from the eventDict
def deleteEvent(eventDict):
    event = input("Enter an event: ")
    event = event.title()
    if event in eventDict:
        eventDict.pop(event)
        print(event, "was deleted from the events dictionary")
    else:
        print(event, "is not in the events dictionary")

def main():
    # create a dictionary with at least two events
    eventDict = {"Labor Day": "September 4, 2023", "Martin Luther King Jr. Day": "January 16, 2023"}

    displayChoices()
    user_choice = input("Choice: ")
    user_choice = user_choice.upper()  # convert to uppercase

    # Loop untile the user enters "Q" (or "q")
    while user_choice != "Q":
        # branching
        if user_choice == "A":
            addEvent(eventDict)
        elif user_choice == "U":
            updateEvent(eventDict)
        elif user_choice == "D":
            deleteEvent(eventDict)
        elif user_choice == "P":
            displayEvents(eventDict)
        else:
            print("Invalid choice")
        # display choices and get input again
        displayChoices()
        user_choice = input("Choice: ")
        user_choice = user_choice.upper()

main()
