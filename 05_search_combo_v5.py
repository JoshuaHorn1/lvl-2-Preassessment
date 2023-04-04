"""Search Combo - Version 3
Incorporated change component into search button/function"""

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
def search_button():
    query = eg.enterbox("Enter the combo name to search for:", "Enter Query").upper()
    proceed = ""
    while proceed != "Cancel":
        if query in combos:
            searched_for = combos.get(query)
            items = "\n".join([f"{item}: {price}" for item, price in searched_for.items()])
            proceed = eg.buttonbox(f"Here is the combo:\n"
                                   f"{items}\n"
                                   f"\n"
                                   f"What would you like to do with it?", "Query Found", choices=("Change", "Delete", "Cancel"))
            if proceed == "Change":
                full_new_combo = {}
                combo_items = {}
                temp_item = {}
                temp_num_items = eg.buttonbox("How many items are in this combo?", "Num Items", choices=("1", "2", "3", "Cancel"))
                if temp_num_items != "Cancel":
                    temp_name = eg.enterbox("What is the name of this combo?").capitalize()
                    while temp_num_items != 0:
                        temp_item_name = eg.enterbox("What is the name of an item in the combo?", "Combo Item Name").capitalize()
                        temp_item_price = eg.enterbox("How much does this item cost?", "Combo Item Price")
                        temp_item.append(temp_item_name, temp_item_price)
                        combo_items.append(temp_item)
                        temp_num_items -= 1
                    full_new_combo = temp_name(combo_items)
                    new_items = "\n".join([f"{item}: {price}" for item, price in full_new_combo.items()])
                    next = eg.buttonbox(f"Here is the combo:\n"
                                           f"{new_items}\n"
                                           f"\n"
                                           f"What would you like to do with it?", "Query Found", choices=("Use", "Cancel"))
                    if next == "Use":
                        
            elif proceed == "Delete":
                confirm_delete = eg.buttonbox(f"Are you sure you want to delete this combo - {query.capitalize()}?", "Confirm Delete",
                                              choices=("Yes - Delete", "No - Cancel"))
                if confirm_delete == "Yes - Delete":
                    combos.pop(query)
                    print(combos)
                    eg.msgbox("Combo deleted.", "Combo Deleted")
                    return
        else:
            proceed = eg.buttonbox("Combo not found. Try again or Cancel.", "Query Not Found", choices=("Try Again", "Cancel"))
            if proceed == "Try Again":
                query = eg.enterbox("Enter the combo name to search for:", "Enter Query")


# Main code...
search_button()
