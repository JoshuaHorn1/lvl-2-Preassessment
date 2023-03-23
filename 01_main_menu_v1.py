"""Main Menu  - Version 1
A component to display the main menu and branch to other components"""

import easygui as eg  # importing easygui as 'eg' to save time later

proceed = eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"
                            "What would you like to do?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
while proceed != "Exit":  # create a while loop to incorporate functions later on
    if proceed == "Search":
        print("test")
        proceed = eg.buttonbox("How would you like to proceed, now?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
    elif proceed == "Add":
        print("test")
        proceed = eg.buttonbox("How would you like to proceed, now?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
    elif proceed == "Delete":
        print("test")
        proceed = eg.buttonbox("How would you like to proceed, now?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
    elif proceed == "Help":
        print("test")
        proceed = eg.buttonbox("How would you like to proceed, now?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
