"""Main Menu  - Version 1
A component to display the main menu and branch to other components
a welcome message will be displayed the first time the main menu is opened"""

import easygui as eg  # importing easygui as 'eg' to save time later

proceed = eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"
                       "What would you like to do?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
while proceed != "Exit":  # create a while loop to incorporate functions later on
    if proceed == "Search":

    elif proceed == "Add":

    elif proceed == "Delete":

    elif proceed == "Help":

