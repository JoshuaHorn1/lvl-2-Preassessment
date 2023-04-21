"""Add combo - Version 2
Added while loop"""

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


# Main code...
proceed = "Change"
while proceed != "Cancel":
    if proceed == "Change":
            combo_items = {}
            num_items = eg.buttonbox("How many items are in this combo?", "Num Items", choices=(1, 2, 3, "Cancel"))
            if num_items != "Cancel":
                name = eg.enterbox("What is the name of this combo?").upper()
                while num_items != 0:
                    item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name").capitalize()
                    item_price = eg.enterbox("How much does this item cost? ($)", "Combo Item Price")
                    combo_items.update({item_name: item_price})
                    num_items -= 1
                full_new_combo = {name: combo_items}
                items = "\n".join([f"{item}: {price}" for item, price in combo_items.items()])
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
print(combos)
