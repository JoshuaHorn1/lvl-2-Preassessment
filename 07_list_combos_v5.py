"""List Combos - Version 4
Bug fixes"""

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

# Functions...


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
listcombos()
