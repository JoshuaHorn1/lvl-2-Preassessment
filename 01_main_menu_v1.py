"""Main Menu  - Version 1
A component to display the main menu and branch to other components
a welcome message will be displayed"""

import easygui as eg  # importing easygui as 'eg' to save time later

proceed = eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"
                       "What would you like to do?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
while proceed != "Exit":  # create a while loop to incorporate functions later on
    if proceed == "Search":
        print(">searches for combo<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
    elif proceed == "Add":
        print(">adds combo<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
    elif proceed == "Delete":
        print(">deletes combo<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
    elif proceed == "Help":
        print(">displays help<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
print(">exits program<")
