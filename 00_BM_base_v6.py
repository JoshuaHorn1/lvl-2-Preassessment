"""Burger Menu Combo Base/Main Program file - Version 6
Components added after they have been created and tested
Added list combos component
Added the new search combo component (05_search_combo_v9) with a previously undetected bug fixed, etc
Added the new add combo component (06_add_combo_v5) with the same bug fixed, but a slightly different workaround, etc
Text updates"""

# imports...
import easygui as eg  # importing easygui as 'eg' to save time later (more efficient code)


# lists/dictionaries
combos = {
    "VALUE": {
        "Beef burger": 5.69,
        "Fizzy drink": 1.00,
        "Fries": 1.00
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
                searchbutton()
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "List", "Help", "Exit"))
            elif proceed == "Add":
                addcombo()
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "List", "Help", "Exit"))
            elif proceed == "List":
                listcombos()
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "List", "Help", "Exit"))
            elif proceed == "Help":
                helpbutton()
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "List", "Help", "Exit"))
        quit = eg.buttonbox("Are you sure you want to quit? All progress will be lost!!", "Quit?", choices=("Yes - Quit", "No - Cancel"))
        if quit == "No - Cancel":
            quit = ""
            proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "List", "Help", "Exit"))
    eg.msgbox("Thank you for using this Menu Combo Program!!", "Goodbye!", ok_button=":D")


def helpbutton():  # A function containing the code for when a user interacts with the help button in the main menu
    help_options = ""
    while help_options != "Cancel":  # checks if the user wants to cancel, if not, loops
        help_options = eg.buttonbox("Sure! What do you need help with?\n"
                                    "(Click the Cancel button to return to the main menu).",
                                    "HELP MENU", choices=("'Search'", "'Add'", "'List'", "'Help'", "'Exit'", "Cancel"))
        if help_options == "'Search'":  # depending on what button is selected, information about the button will be displayed
            eg.msgbox("This button allows you to search through the combo's currently stored in the database. If there is a "
                      "match for the combo name entered, it will display the combo, and then ask if you want to remake it, "
                      "delete the combo, or to cancel and return to the main menu.", "Search-Button Help", ok_button="Back")
        elif help_options == "'Add'":
            eg.msgbox("This button creates a new combo to add to the menu. After entering the details for the new combo, "
                      "it will ask if you want to remake it, add it to the menu, or cancel after/during the process.",
                      "Add-Button Help", ok_button="Back")
        elif help_options == "'List'":
            eg.msgbox("This button will create two outputs. It will list all of the combo names on an Easy Gui pop up, and "
                      "send a full menu to the python console, including the combo names, the items and prices of each combo, "
                      "and a total price for the combo.",
                      "List-Button Help", ok_button="Back")
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


def searchbutton():
    cancel_count = 0
    query = eg.enterbox("Enter the combo name to search for:", "Enter Query")
    if query is None:
        return
    query = query.upper()
    proceed = ""
    while proceed != "Cancel":
        if query in combos:
            searched_for = combos.get(query)
            items = "\n".join([f"{item}: {price}" for item, price in searched_for.items()])
            proceed = eg.buttonbox(f"Here is the combo, {query.capitalize()}:\n"
                                   f"{items}\n"
                                   f"\n"
                                   f"What would you like to do with it?", "Query Found", choices=("Remake", "Delete", "Cancel"))
            if proceed == "Remake":
                combo_items = {}
                temp_num_items = eg.integerbox("How many items are in this combo? (1-5)", "Num Items", lowerbound=1, upperbound=5)
                if temp_num_items is None:
                    continue
                temp_name = eg.enterbox("What is the name of this combo?")
                while temp_name == "":
                    if temp_name == "":
                        eg.msgbox("This field cannot be empty.", "Error")
                        temp_name = eg.enterbox("What is the name of this combo?")
                    if temp_name is None:
                        continue
                temp_name = temp_name.upper()
                while temp_num_items != 0:
                    temp_item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name")
                    while temp_item_name == "":
                        if temp_item_name == "":
                            eg.msgbox("This field cannot be empty.", "Error")
                            temp_item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name")
                    if temp_item_name is None:
                        cancel_count += 1
                        if cancel_count >= 3:
                            eg.msgbox("Sorry, an error has occurred, so I will return you to the Main Menu.", "Error")
                            return
                        continue
                    temp_item_name = temp_item_name.capitalize()
                    temp_item_price = 0
                    while temp_item_price > 100 or temp_item_price <= 0:
                        while True:
                            temp_item_price = eg.enterbox("How much does this item cost? (Within $0 - $100)", "Combo Item Price")
                            if temp_item_price is None:
                                cancel_count += 1
                                if cancel_count >= 3:
                                    eg.msgbox("Sorry, an error has occurred, so I will return you to the Main Menu.", "Error")
                                    return
                                continue
                            try:
                                temp_item_price = float(temp_item_price)
                                break
                            except ValueError:
                                eg.msgbox("Please enter a numerical value for the item price.", "Error")
                        if temp_item_price > 100 or temp_item_price <= 0:
                            eg.msgbox("Please enter a value between $0 and $100.", "Error")
                    combo_items.update({temp_item_name: "{:.2f}".format(temp_item_price)})
                    temp_num_items -= 1
                full_new_combo = {temp_name: combo_items}
                items = "\n".join([f"{item}: {price}" for item, price in combo_items.items()])
                next = eg.buttonbox(f"Here is the combo, {temp_name.capitalize()}:\n"
                                    f"{items}\n"
                                    f"\n"
                                    f"What would you like to do with it?", "Combo Created", choices=("Use", "Cancel"))
                if next == "Use":
                    confirm_use = eg.buttonbox(f"Please confirm you would like to replace the combo '{query.capitalize()}' with "
                                               f"the remade version: '{temp_name.capitalize()}'.", choices=("Confirm", "Cancel"))
                    if confirm_use == "Confirm":
                        combos.pop(query)
                        combos.update(full_new_combo)
                        eg.msgbox(f"Your changes have been saved, and the combo '{temp_name.capitalize()}' has been added "
                                  f"to the list in place of '{query.capitalize()}'.", "Combo Added")
                        return
            elif proceed == "Delete":
                confirm_delete = eg.buttonbox(f"Are you sure you want to delete this combo - {query.capitalize()}?", "Confirm Delete",
                                              choices=("Delete", "Cancel"))
                if confirm_delete == "Delete":
                    combos.pop(query)
                    eg.msgbox("Combo deleted.", "Combo Deleted")
                    return
        else:
            proceed = eg.buttonbox("Combo not found. Try again or Cancel.", "Query Not Found", choices=("Try Again", "Cancel"))
            if proceed == "Try Again":
                query = eg.enterbox("Enter the combo name to search for:", "Enter Query")
                if query is None:
                    return
                query = query.upper()


def addcombo():
    proceed = "Remake"
    while proceed != "Cancel":
        if proceed == "Remake":
            combo_items = {}
            num_items = eg.integerbox("How many items are in this combo? (1-5)", "Num Items", lowerbound=1, upperbound=5)
            if num_items is None:
                return
            name = eg.enterbox("What is the name of this combo?", "Combo Name")
            while name == "":
                if name == "":
                    eg.msgbox("This field cannot be empty.", "Error")
                    name = eg.enterbox("What is the name of this combo?", "Combo Name")
            if name is None:
                return
            name = name.upper()
            while num_items != 0:
                item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name")
                while item_name == "":
                    if item_name == "":
                        eg.msgbox("This field cannot be empty.", "Error")
                        item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name")
                if item_name is None:
                    return
                item_name = item_name.capitalize()
                item_price = 0
                while item_price > 100 or item_price <= 0:
                    while True:
                        item_price = eg.enterbox("How much does this item cost? (Within $0 - $100)", "Combo Item Price")
                        if item_price is None:
                            return
                        try:
                            item_price = float(item_price)
                            break
                        except ValueError:
                            eg.msgbox("Please enter a numerical value for the item price.", "Error")
                    if item_price > 100 or item_price <= 0:
                        eg.msgbox("Please enter a value between $0 and $100.", "Error")
                combo_items.update({item_name: round(float(item_price), 2)})
                num_items -= 1
            full_new_combo = {name: combo_items}
            items = "\n".join([f"{item}: {price:.2f}" for item, price in combo_items.items()])
            proceed = eg.buttonbox(f"Here is the combo, {name.capitalize()}:\n"
                                   f"{items}\n"
                                   f"\n" 
                                   f"What would you like to do with it?", "Combo Created", choices=("Use", "Change", "Cancel"))
            if proceed == "Use":
                proceed = eg.buttonbox(f"Please confirm you want to add the combo '{name.capitalize()}' to the menu?",
                                       choices=("Confirm", "Cancel"))
                if proceed == "Confirm":
                    combos.update(full_new_combo)
                    eg.msgbox(f"Your changes have been saved, and the combo '{name.capitalize()}' has been added to the menu.", "Combo Added")
                    return


def listcombos():
    combo_names = []
    for combo in combos:
        combo_names.append(combo.capitalize())
    print_choice = eg.buttonbox("Here are the combos available in the menu:\n(For a fully detailed menu printout, click 'Full Print' and one will be "
                                "sent to the python console).\n\n{}\n".format("\n".join(combo_names)), "Combo List", choices=("Full Print", "Return"))
    if print_choice == "Full Print":
        print("~ ~ FULL MENU: ~ ~")
        print()
        for combo_name, combo_items in combos.items():
            total_price = 0
            print(f"{combo_name.capitalize()}:")
            for item_name, item_price in combo_items.items():
                print(f"- {item_name}: {float(item_price):.2f}")
                total_price += float(item_price)
            print(f"Total price: {total_price:.2f}")
            print()


# Main code...
mainmenu(eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"  # calls on the main menu function using a player input
                      "What would you like to do?", "MAIN MENU", choices=("Search", "Add", "List", "Help", "Exit")))
