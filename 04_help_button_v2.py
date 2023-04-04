"""Help Button - Version 2
Developed the function version"""

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
def helpbutton():  # A function containing the code for when a user interacts with the help button in the main menu
    help_options = eg.buttonbox("Sure! What do you need help with?", "HELP MENU", choices=("General", "Search", "Add",
                                                                                           "Delete", "Help", "Exit"))
    if help_options == "General":
        eg.msgbox("")
    elif help_options == "Search":
        eg.msgbox("")
    elif help_options == "Add":
        eg.msgbox("")
    elif help_options == "Delete":
        eg.msgbox("")
    elif help_options == "Help":
        eg.msgbox("")
    else:
        eg.msgbox("")
