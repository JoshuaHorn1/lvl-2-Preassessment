"""Burger Menu Combo Base/Main Program file - Version 3
Components added after they have been created and tested
Added the Help button code/function"""

# imports...
import easygui as eg  # importing easygui as 'eg' to save time later (more efficient code)


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
                helpbutton()
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
            else:
                proceed = eg.buttonbox("How would you like to proceed?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
        quit = eg.buttonbox("Are you sure you want to quit? All progress will be lost!!", "Quit?", choices=("Yes - Quit", "No - Cancel"))
        if quit == "No - Cancel":
            quit = ""
            proceed = eg.buttonbox("How would you like to proceed?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
    eg.msgbox("Thank you for using this Menu Combo Program!!", "Goodbye!", ok_button=":D")


def helpbutton():  # A function containing the code for when a user interacts with the help button in the main menu
    help_options = ""
    while help_options != "Cancel":  # checks if the user wants to cancel, if not, loops
        help_options = eg.buttonbox("Sure! What do you need help with?\n"
                                    "(Click the Cancel button to return to the main menu).",
                                    "HELP MENU", choices=("'Search'", "'Add'", "'Delete'",
                                                          "'Help'", "'Exit'", "Cancel"))
        if help_options == "'Search'":  # depending on what button is selected, information about the button will be displayed
            eg.msgbox("This button allows you to search through the combo's currently stored in the database. If there is a "
                      "match for the combo name entered, it will display the combo, and then ask if you want to make any "
                      "changes to it, or to cancel and return to the main menu.", "Search-Button Help", ok_button="Back")
        elif help_options == "'Add'":
            eg.msgbox("This button creates a new combo to add to the menu. After entering the details for the new combo, "
                      "it will ask if you want to make any changes, add it to the menu, or cancel after/during the process.",
                      "Add-Button Help", ok_button="Back")
        elif help_options == "'Delete'":
            eg.msgbox("This button allows you to delete a combo from the list that currently exits. You will enter the name "
                      "of a combo, and if it exists, you will be asked to confirm that you want to delete it, or cancel "
                      "after/during the process.", "Delete-Button Help", ok_button="Back")
        elif help_options == "'Help'":
            eg.msgbox("This button displays the Help Menu, from which you can view small, informative tips about all of the "
                      "buttons on the main menu - such as this one.", "Help-Button Help", ok_button="Back")
        elif help_options == "'Exit'":
            eg.msgbox("This button will exit the program when you are done with it - after confirming that you want to quit.\n"
                      "\n"
                      "*IMPORTANT NOTE!!*:\n"
                      "This program does not save between runs, so any progress will be lost if the program is exited.",
                      "Exit-Button Help", ok_button="Back")
        else:  # if cancel is selected, it will return to the main menu
            return


# Main code...
mainmenu(eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"  # calls on the main menu function using a player input
                      "What would you like to do?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit")))
