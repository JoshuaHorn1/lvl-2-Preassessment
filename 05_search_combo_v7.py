"""Search Combo - Version 7
More Bug fixes
Raises item prices to 2sf
Changed 'temp_num_items' and 'temp_item_price' to integer boxes
Increased maximum num of items in a combo to 5
Text changes
Added an error counter to detect if the user has become stuck in a loop"""

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
    cancel_count = 0
    query = eg.enterbox("Enter the combo name to search for:", "Enter Query")
    if query is None:
        return
    query = query.upper()
    proceed = ""
    while proceed != "Cancel":
        if query in combos:
            searched_for = combos.get(query)
            items = "\n".join([f"{item}: {price}" for item, price in searched_for.items()])
            proceed = eg.buttonbox(f"Here is the combo, {query.capitalize()}:\n"
                                   f"{items}\n"
                                   f"\n"
                                   f"What would you like to do with it?", "Query Found", choices=("Remake", "Delete", "Cancel"))
            if proceed == "Remake":
                combo_items = {}
                temp_num_items = eg.integerbox("How many items are in this combo?", "Num Items", lowerbound=1, upperbound=5)
                if temp_num_items is None:
                    continue
                temp_name = eg.enterbox("What is the name of this combo?")
                if temp_name is None:
                    continue
                temp_name = temp_name.upper()
                while temp_num_items != 0:
                    temp_item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name")
                    if temp_item_name is None:
                        cancel_count += 1
                        if cancel_count >= 3:
                            eg.msgbox("Sorry, an error has occurred, so I will return you to the Main Menu.", "Error")
                            return
                        continue
                    temp_item_name = temp_item_name.capitalize()
                    temp_item_price = eg.integerbox("How much does this item cost? ($)", "Combo Item Price", lowerbound=0, upperbound=100)
                    if temp_item_price is None:
                        cancel_count += 1
                        if cancel_count >= 3:
                            eg.msgbox("Sorry, an error has occurred, so I will return you to the Main Menu.", "Error")
                            return
                        continue
                    combo_items.update({temp_item_name: "{:.2f}".format(float(temp_item_price))})
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
                query = eg.enterbox("Enter the combo name to search for:", "Enter Query")
                if query is None:
                    return
                query = query.upper()


# Main code...
searchbutton()
