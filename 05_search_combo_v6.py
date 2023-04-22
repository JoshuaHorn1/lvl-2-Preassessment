"""Search Combo - Version 6
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


# Functions...
def searchbutton():
    query = eg.enterbox("Enter the combo name to search for:", "Enter Query").upper()
    proceed = ""
    while proceed != "Cancel":
        if query in combos:
            searched_for = combos.get(query)
            items = "\n".join([f"{item}: {price}" for item, price in searched_for.items()])
            proceed = eg.buttonbox(f"Here is the combo, {query.capitalize()}:\n"
                                   f"{items}\n"
                                   f"\n"
                                   f"What would you like to do with it?", "Query Found", choices=("Change", "Delete", "Cancel"))
            if proceed == "Change":
                combo_items = {}
                temp_num_items = eg.buttonbox("How many items are in this combo?", "Num Items", choices=(1, 2, 3, "Cancel"))
                if temp_num_items != "Cancel":
                    temp_name = eg.enterbox("What is the name of this combo?").upper()
                    while temp_num_items != 0:
                        temp_item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name").capitalize()
                        temp_item_price = eg.enterbox("How much does this item cost? ($)", "Combo Item Price")
                        combo_items.update({temp_item_name: temp_item_price})
                        temp_num_items -= 1
                    full_new_combo = {temp_name: combo_items}
                    items = "\n".join([f"{item}: {price}" for item, price in combo_items.items()])
                    next = eg.buttonbox(f"Here is the combo, {temp_name.capitalize()}:\n"
                                        f"{items}\n"
                                        f"\n"
                                        f"What would you like to do with it?", "Combo Created", choices=("Use", "Cancel"))
                    if next == "Use":
                        combos.pop(query)
                        combos.update(full_new_combo)
                        eg.msgbox(f"Your changes have been saved, and the combo '{temp_name.capitalize()}' has been added "
                                  f"to the list in place of '{query.capitalize()}'.", "Combo Added")
                        return
            elif proceed == "Delete":
                confirm_delete = eg.buttonbox(f"Are you sure you want to delete this combo - {query.capitalize()}?", "Confirm Delete",
                                              choices=("Yes - Delete", "No - Cancel"))
                if confirm_delete == "Yes - Delete":
                    combos.pop(query)
                    eg.msgbox("Combo deleted.", "Combo Deleted")
                    return
        else:
            proceed = eg.buttonbox("Combo not found. Try again or Cancel.", "Query Not Found", choices=("Try Again", "Cancel"))
            if proceed == "Try Again":
                query = eg.enterbox("Enter the combo name to search for:", "Enter Query").upper()


# Main code...
searchbutton()
