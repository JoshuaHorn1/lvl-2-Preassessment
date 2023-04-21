"""Burger Menu Combo Base/Main Program file - Version 4
Components added after they have been created and tested
Added the Search button function, with delete and change components incorporated"""

# imports...
import easygui as eg  # importing easygui as 'eg' to save time later (more efficient code)


# lists/dictionaries
combos = {
    "VALUE": {
        "Beef burger": 5.69,
        "Fizzy drink": 1,
        "Fries": 1
    },
    "CHEEZY": {
        "Cheeseburger": 6.69,
        "Fizzy drink": 1.00,
        "Fries": 1.00
    },
    "SUPER": {
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
                search_button()
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


def search_button():
    query = eg.enterbox("Enter the combo name to search for:", "Enter Query").upper()
    proceed = ""
    while proceed != "Cancel":
        if query in combos:
            searched_for = combos.get(query)
            items = "\n".join([f"{item}: {price}" for item, price in searched_for.items()])
            proceed = eg.buttonbox(f"Here is the combo, {query.capitalize()}:\n"
                                   f"{items}\n"
                                   f"\n"
                                   f"What would you like to do with it?", "Query Found", choices=("Change", "Delete", "Cancel"))
            if proceed == "Change":
                combo_items = {}
                temp_num_items = eg.buttonbox("How many items are in this combo?", "Num Items", choices=(1, 2, 3, "Cancel"))
                if temp_num_items != "Cancel":
                    temp_name = eg.enterbox("What is the name of this combo?").upper()
                    while temp_num_items != 0:
                        temp_item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name").capitalize()
                        temp_item_price = eg.enterbox("How much does this item cost? ($)", "Combo Item Price")
                        combo_items.update({temp_item_name: temp_item_price})
                        temp_num_items -= 1
                    full_new_combo = {temp_name: combo_items}
                    items = "\n".join([f"{item}: {price}" for item, price in combo_items.items()])
                    next = eg.buttonbox(f"Here is the combo, {temp_name.capitalize()}:\n"
                                        f"{items}\n"
                                        f"\n"
                                        f"What would you like to do with it?", "Combo Created", choices=("Use", "Cancel"))
                    if next == "Use":
                        combos.pop(query)
                        combos.update(full_new_combo)
                        eg.msgbox(f"Your changes have been saved, and the combo '{temp_name.capitalize()}' has been added "
                                  f"to the list in place of '{query.capitalize()}'.", "Combo Added")
                        return
            elif proceed == "Delete":
                confirm_delete = eg.buttonbox(f"Are you sure you want to delete this combo - {query.capitalize()}?", "Confirm Delete",
                                              choices=("Yes - Delete", "No - Cancel"))
                if confirm_delete == "Yes - Delete":
                    combos.pop(query)
                    eg.msgbox("Combo deleted.", "Combo Deleted")
                    return
        else:
            proceed = eg.buttonbox("Combo not found. Try again or Cancel.", "Query Not Found", choices=("Try Again", "Cancel"))
            if proceed == "Try Again":
                query = eg.enterbox("Enter the combo name to search for:", "Enter Query").upper()


# Main code...
mainmenu(eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"  # calls on the main menu function using a player input
                      "What would you like to do?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit")))
