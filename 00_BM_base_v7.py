"""Burger Menu Combo Base/Main Program file - Version 7
Components added after they have been created and tested
Finalised code
Added comments"""

# Importing the easygui library and renaming it as 'eg' for convenience
import easygui as eg

# Dictionary containing combos and their respective items and prices
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
def mainmenu(proceed):  # A function containing the code for the main menu
    # Initialise quit variable with an empty string
    quit = ""
    while quit != "Yes - Quit":  # test to see if user has quit, if not, the program will loop
        while proceed != "Exit":  # create a while loop to incorporate functions later on
            # Depending on what button is pressed the main menu will carry out a different function
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
        # Asks user to confirm quit
        quit = eg.buttonbox("Are you sure you want to quit? All progress will be lost!!", "Quit?", choices=("Yes - Quit", "No - Cancel"))
        # If user cancels, gives quit an empty string and asks how to proceed
        if quit == "No - Cancel":
            quit = ""
            proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "List", "Help", "Exit"))
    # When user quits, display a goodbye message
    eg.msgbox("Thank you for using this Menu Combo Program!!", "Goodbye!", ok_button=":D")


def helpbutton():  # a function containing code for the help menu
    # Initialize help_options as an empty string
    help_options = ""
    # Loop until user cancels help or closes the window
    while help_options != "Cancel":
        # Display button options for help
        help_options = eg.buttonbox("Sure! What do you need help with?\n"
                                    "(Click the Cancel button to return to the main menu).",
                                    "HELP MENU", choices=("'Search'", "'Add'", "'List'", "'Help'", "'Exit'", "Cancel"))
        # Depending on which button is pressed, display help information about that button
        if help_options == "'Search'":
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
        else:  # if cancel is selected, return to the main menu
            return


def searchbutton():
    # Initialize the number of times the user has canceled to 0 and prompt the user to enter a query
    cancel_count = 0
    query = eg.enterbox("Enter the combo name to search for:", "Enter Query")
    # If the user cancels the search, return None
    if query is None:
        return
    # Convert the query to uppercase for consistency and initialize a variable 'proceed'
    query = query.upper()
    proceed = ""
    # Continue to prompt the user for an action until they choose 'Cancel'
    while proceed != "Cancel":
        # If the query is in the 'combos' dictionary, display the combo and ask the user what they want to do with it
        if query in combos:
            # Get the items in the combo as a string and format it for display
            searched_for = combos.get(query)
            items = "\n".join([f"{item}: {price}" for item, price in searched_for.items()])
            # Display the combo and prompt the user for an action
            proceed = eg.buttonbox(f"Here is the combo, {query.capitalize()}:\n"
                                   f"{items}\n"
                                   f"\n"
                                   f"What would you like to do with it?", "Query Found", choices=("Remake", "Delete", "Cancel"))
            # If the user chooses to remake the combo, prompt them for new items and prices
            if proceed == "Remake":
                # Initialize a new empty dictionary for the items in the new combo and prompt the user for the number of items
                combo_items = {}
                temp_num_items = eg.integerbox("How many items are in this combo? (1-5)", "Num Items", lowerbound=1, upperbound=5)
                # If the user cancels, continue to the next iteration of the loop
                if temp_num_items is None:
                    continue
                # Prompt the user for the name of the new combo and check that it is not empty or None
                temp_name = eg.enterbox("What is the name of this combo?")
                while temp_name == "":
                    if temp_name == "":
                        eg.msgbox("This field cannot be empty.", "Error")
                        temp_name = eg.enterbox("What is the name of this combo?")
                    if temp_name is None:
                        continue
                # Convert the name to uppercase for consistency
                temp_name = temp_name.upper()
                # Prompt the user for the name and price of each item in the combo
                while temp_num_items != 0:
                    temp_item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name")
                    # If the user cancels, increment the cancel_count and return an error message if the user cancels three times
                    while temp_item_name == "":
                        if temp_item_name == "":
                            eg.msgbox("This field cannot be empty.", "Error")
                            temp_item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name")
                    if temp_item_name is None:  # checks if use has clicked cancel more than 3 times, returns to menu if error is found
                        cancel_count += 1
                        if cancel_count >= 3:
                            eg.msgbox("Sorry, an error has occurred, so I will return you to the Main Menu.", "Error")
                            return
                        continue
                    # Convert the name to capitalized form for consistency
                    temp_item_name = temp_item_name.capitalize()
                    # Prompt the user for the price
                    temp_item_price = 0
                    while temp_item_price > 100 or temp_item_price <= 0:
                        while True:
                            temp_item_price = eg.enterbox("How much does this item cost? (Within $0 - $100)", "Combo Item Price")
                            if temp_item_price is None:  # checks if use has clicked cancel more than 3 times, returns to menu if error is found
                                cancel_count += 1
                                if cancel_count >= 3:
                                    eg.msgbox("Sorry, an error has occurred, so I will return you to the Main Menu.", "Error")
                                    return
                                continue
                            try:
                                # Converts to float
                                temp_item_price = float(temp_item_price)
                                break
                            except ValueError:
                                # If value is empty or letters display error
                                eg.msgbox("Please enter a numerical value for the item price.", "Error")
                        if temp_item_price > 100 or temp_item_price <= 0:
                            # If value is above 100 or below 0, display error
                            eg.msgbox("Please enter a value between $0 and $100.", "Error")
                    combo_items.update({temp_item_name: "{:.2f}".format(temp_item_price)})  # Adds item to dictionary
                    temp_num_items -= 1
                full_new_combo = {temp_name: combo_items}  # creates a complete combo with user input name and items
                # Formats items
                items = "\n".join([f"{item}: {price}" for item, price in combo_items.items()])
                # Displays user constructed combo
                next = eg.buttonbox(f"Here is the combo, {temp_name.capitalize()}:\n"
                                    f"{items}\n"
                                    f"\n"
                                    f"What would you like to do with it?", "Combo Created", choices=("Use", "Cancel"))  # Asks user if they want to use or cancel
                if next == "Use":
                    # Asks user to confirm that they want to replace combo
                    confirm_use = eg.buttonbox(f"Please confirm you would like to replace the combo '{query.capitalize()}' with "
                                               f"the remade version: '{temp_name.capitalize()}'.", choices=("Confirm", "Cancel"))
                    if confirm_use == "Confirm":
                        # If user confirms, program replaces old combo with new combo
                        combos.pop(query)
                        combos.update(full_new_combo)
                        eg.msgbox(f"Your changes have been saved, and the combo '{temp_name.capitalize()}' has been added "
                                  f"to the list in place of '{query.capitalize()}'.", "Combo Added")
                        return  # returns to main menu
            elif proceed == "Delete":  # if user presses delete button, prompts them to confirm delete
                confirm_delete = eg.buttonbox(f"Are you sure you want to delete this combo - {query.capitalize()}?", "Confirm Delete",
                                              choices=("Delete", "Cancel"))
                if confirm_delete == "Delete":  # deletes combo if user confirms
                    combos.pop(query)
                    eg.msgbox("Combo deleted.", "Combo Deleted")
                    return  # returns to main menu
        else:
            # If combo name isn't found, display error message
            proceed = eg.buttonbox("Combo not found. Try again or Cancel.", "Query Not Found", choices=("Try Again", "Cancel"))
            if proceed == "Try Again":  # if user wants to try again, display query enterbox message again
                query = eg.enterbox("Enter the combo name to search for:", "Enter Query")
                if query is None:  # if user
                    return  # returns to main menu if user presses Cancel
                query = query.upper()  # puts user query into uppercase if a correct variable is entered


def addcombo():
    # Initializing the variable 'proceed' as 'Remake'.
    proceed = "Remake"
    # Starting a loop that will run until the user clicks on 'Cancel'.
    while proceed != "Cancel":
        # If the value of 'proceed' is 'Remake', then the user is prompted to enter the number of items in the combo.
        if proceed == "Remake":
            # Creating an empty dictionary 'combo_items'.
            combo_items = {}
            # The user is prompted to enter the number of items in the combo.
            num_items = eg.integerbox("How many items are in this combo? (1-5)", "Num Items", lowerbound=1, upperbound=5)
            # If the user clicks on 'Cancel', then the function terminates.
            if num_items is None:
                return
            # The user is prompted to enter the name of the combo.
            name = eg.enterbox("What is the name of this combo?", "Combo Name")
            # If the user enters an empty name, then an error message is displayed and the user is prompted again.
            while name == "":
                if name == "":
                    eg.msgbox("This field cannot be empty.", "Error")
                    name = eg.enterbox("What is the name of this combo?", "Combo Name")
            # If the user clicks on 'Cancel', then the function terminates.
            if name is None:
                return
            # Converting the name of the combo to uppercase.
            name = name.upper()
            # Starting a loop that will run until all items in the combo have been entered.
            while num_items != 0:
                # The user is prompted to enter the name of an item in the combo.
                item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name")
                # If the user enters an empty name, then an error message is displayed and the user is prompted again.
                while item_name == "":
                    if item_name == "":
                        eg.msgbox("This field cannot be empty.", "Error")
                        item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name")
                # If the user clicks on 'Cancel', then the function terminates.
                if item_name is None:
                    return
                # Converting the name of the item to capitalized.
                item_name = item_name.capitalize()
                # The user is prompted to enter the price of the item.
                item_price = 0
                # Starting a loop that will run until a valid price is entered.
                while item_price > 100 or item_price <= 0:
                    # The user is prompted to enter the price of the item.
                    while True:
                        item_price = eg.enterbox("How much does this item cost? (Within $0 - $100)", "Combo Item Price")
                        # If the user clicks on 'Cancel', then the function terminates.
                        if item_price is None:
                            return
                        # Checking if the entered price is a valid float value. If not, an error message is displayed and the user is prompted again
                        try:
                            item_price = float(item_price)
                            break
                        except ValueError:
                            # Displays error message if float variable is invalid
                            eg.msgbox("Please enter a numerical value for the item price.", "Error")
                    if item_price > 100 or item_price <= 0:
                        # Displays error message if the value is above 100 or below 0
                        eg.msgbox("Please enter a value between $0 and $100.", "Error")
                combo_items.update({item_name: round(float(item_price), 2)})
                num_items -= 1
            full_new_combo = {name: combo_items}  # creates new combo containing details from name and combo items
            items = "\n".join([f"{item}: {price:.2f}" for item, price in combo_items.items()])  # formats items
            # Displays the user created combo
            proceed = eg.buttonbox(f"Here is the combo, {name.capitalize()}:\n"
                                   f"{items}\n"
                                   f"\n" 
                                   f"What would you like to do with it?", "Combo Created", choices=("Use", "Remake", "Cancel"))  # asks user to use, remake, or cancel
            if proceed == "Use":
                # Asks user to confirm they want to add combo to menu
                proceed = eg.buttonbox(f"Please confirm you want to add the combo '{name.capitalize()}' to the menu?",
                                       choices=("Confirm", "Cancel"))
                if proceed == "Confirm":
                    # If they confirm, update to combos dictionary
                    combos.update(full_new_combo)
                    eg.msgbox(f"Your changes have been saved, and the combo '{name.capitalize()}' has been added to the menu.", "Combo Added")
                    return


def listcombos():
    # Create an empty list to hold the names of each combo
    combo_names = []
    # Loop through each combo in the 'combos' dictionary
    for combo in combos:
        # Add the capitalized name of the combo to the list
        combo_names.append(combo.capitalize())
    # Display a message box with the list of combo names, and give the user the option to print the full menu to the console
    print_choice = eg.buttonbox("Here are the combos available in the menu:\n(For a fully detailed menu printout, click 'Full Print' and one will be "
                                "sent to the python console).\n\n{}\n".format("\n".join(combo_names)), "Combo List", choices=("Full Print", "Return"))
    # If the user chooses to print the full menu to the console, loop through each combo and print its name, items, and total price
    if print_choice == "Full Print":
        # Print a heading for the full menu
        print("~ ~ FULL MENU: ~ ~")
        print()
        # Loop through each combo in the 'combos' dictionary
        for combo_name, combo_items in combos.items():
            # Set a variable to hold the total price of the combo
            total_price = 0
            # Print the name of the combo
            print(f"{combo_name.capitalize()}:")
            # Loop through each item in the combo and print its name and price
            for item_name, item_price in combo_items.items():
                print(f"- {item_name}: {float(item_price):.2f}")
                # Add the price of the item to the total price of the combo
                total_price += float(item_price)
            # Print the total price of the combo
            print(f"Total price: {total_price:.2f}")
            print()


# Main code...
mainmenu(eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"  # calls on the main menu function using a player input
                      "What would you like to do?", "MAIN MENU", choices=("Search", "Add", "List", "Help", "Exit")))
