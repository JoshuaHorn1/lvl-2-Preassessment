"""Help Button - Version 1
Main skeleton of Help menu"""

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

# Main code...
help_options = eg.buttonbox("Sure! What do you need help with?", "HELP MENU", choices=("General", "Search", "Add",
                                                                                       "Delete", "Help", "Exit"))
while help_options != "Cancel":
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
