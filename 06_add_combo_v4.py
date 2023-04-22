"""Add combo - Version 4
More bug fixes
Raises item prices to 2sf
Changes 'num_items' to an integer box for more efficient code
Added a check to make sure the item price doesn't accept a non-integer/decimal
Added a checker to make sure the item price is within 0 and 100$
Increased max number of items in a combo to 5
Text changes"""

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


# Functions...
def addcombo():
    proceed = "Remake"
    while proceed != "Cancel":
        if proceed == "Remake":
            combo_items = {}
            num_items = eg.integerbox("How many items are in this combo? (1-5)", "Num Items", lowerbound=1, upperbound=5)
            if num_items is None:
                return
            name = eg.enterbox("What is the name of this combo?", "Combo Name")
            if name is None:
                return
            name = name.upper()
            while num_items != 0:
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
                    if item_price > 100 or item_price < 0:
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


# Main code...
addcombo()
