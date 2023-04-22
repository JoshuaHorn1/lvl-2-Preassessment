"""List Combos - Version 2
Detailed report sent to the python console
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
for combo_name, combo_items in combos.items():
    total_price = 0
    print(f"{combo_name}:")
    for item_name, item_price in combo_items.items():
        print(f"- {item_name}: {item_price:.2f}")
        total_price += item_price
    print(f"Total price: {total_price:.2f}")
    print()
