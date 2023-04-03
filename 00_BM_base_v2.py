"""Burger Menu Combo Base/Main Program file - Version 2
Components added after they have been created and tested
Added the combo meals dictionary
added the functional Exit button"""

# imports...
import easygui as eg  # importing easygui as 'eg' to save time later


# lists/dictionaries
combos = {  # created a dictionary containing current combos
    "Value": {
        "Beef burger": 5.69,
        "Fizzy drink": 1,
        "Fries": 1
    },
    "Cheezy": {
        "Cheeseburger": 6.69,
        "Fizzy drink": 1.00,
        "Fries": 1.00
    },
    "Super": {
        "Cheeseburger": 6.69,
        "Large fries": 2.00,
        "Smoothie": 2.00
    }
}


# functions...
def mainmenu(proceed):  # a function containing the code for the main menu
    quit = ""
    while quit != "Yes - Quit":  # test to see if user has quit, if not, the program will loop
        while proceed != "Exit":  # create a while loop to incorporate functions later on
            if proceed == "Search":
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))

            elif proceed == "Add":
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))

            elif proceed == "Delete":
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))

            elif proceed == "Help":
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))

            else:
                proceed = eg.buttonbox("How would you like to proceed?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
        quit = eg.buttonbox("Are you sure you want to quit? All progress will be lost!!", "Quit?", choices=("Yes - Quit", "No - Cancel"))
        if quit == "No - Cancel":
            quit = ""
            proceed = eg.buttonbox("How would you like to proceed?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
    eg.msgbox("Thank you for using this Menu Combo Program!!", "Goodbye!", ok_button=":D")


# Main code...
mainmenu(eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"  # calls on the main menu function
                      "What would you like to do?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit")))

