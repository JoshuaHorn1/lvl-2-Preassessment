"""Combo Meals - Version 1
Use easygui to allow a user to manipulate the combo list"""

import easygui  # importing easygui

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

proceed = easygui.buttonbox("Hello! Welcome to the Ultimate Burger Combo Menu!\n"
                  "What would you like to do?", "Menu Choices", choices=("Search", "Add", "Delete", "Exit"))
while proceed != "Exit":
