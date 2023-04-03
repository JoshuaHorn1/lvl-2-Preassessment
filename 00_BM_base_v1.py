"""Burger Menu Combo Base/Main Program file - Version 1
Components added after they have been created and tested
Added the code for the main menu to branch to other components"""

import easygui as eg  # importing easygui as 'eg' to save time later


def mainmenu(proceed):
    while proceed != "Exit":  # create a while loop to incorporate functions later on
        if proceed == "Search":
            proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))

        elif proceed == "Add":
            proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))

        elif proceed == "Delete":
            proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))

        elif proceed == "Help":
            proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))

# Main...
mainmenu(eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"
                      "What would you like to do?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit")))
