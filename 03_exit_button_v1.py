"""Exit Button - Version 1
A component to check if the user wants to quit, then quits"""

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
        print("33", quit)
        print(proceed)
        while proceed != "Exit":  # create a while loop to incorporate functions later on
            if proceed == "Search":
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
                print(proceed)
            elif proceed == "Add":
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
                print(proceed)
            elif proceed == "Delete":
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
                print(proceed)
            elif proceed == "Help":
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit"))
                print(proceed)
            else:
                proceed = eg.buttonbox("How would you like to proceed?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
        quit = eg.buttonbox("Are you sure you want to quit? All progress will be lost!!", "Quit?", choices=("Yes - Quit", "No - Cancel"))
        print("50", quit)
        if quit == "No - Cancel":
            quit = ""
            proceed = eg.buttonbox("How would you like to proceed?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
    eg.msgbox("Thank you for using this Menu Combo Program!!", "Goodbye!", ok_button=":D")


# Main code...
mainmenu(eg.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"  # calls on the main menu function
                      "What would you like to do?", "MAIN MENU", choices=("Search", "Add", "Delete", "Help", "Exit")))
