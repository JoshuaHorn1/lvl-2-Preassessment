"""Search Combo - Version 4
Incorporated delete component into the search function
Uppercased the main parts of the dictionary to allow for more accurate calling"""

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
            proceed = eg.buttonbox(f"Here is the combo:\n"
                                   f"{items}\n"
                                   f"\n"
                                   f"What would you like to do with it?", "Query Found", choices=("Change", "Delete", "Cancel"))
            if proceed == "Change":
                print("change")
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
searchbutton()
