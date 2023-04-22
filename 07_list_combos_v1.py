"""List Combos - Version 1
Lists the combo names on EasyGui popup
"""

# Imports...
import easygui as eg


# Dictionaries/Lists...
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

combo_names = []

# Main code...
for combo in combos:
    combo_names.append(combo.capitalize())
eg.msgbox("Here are the combos available in the menu:\n(A full, detailed menu has been sent to the python console).\n"
          "\n{}\n".format("\n".join(combo_names)), "Combo Names")
