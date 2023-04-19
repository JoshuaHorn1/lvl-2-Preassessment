"""Search Combo - Version 2
Different approach/alternative method"""

import easygui as eg

combos = {
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

query = eg.enterbox("Enter the combo name to search for:", "Enter Query")
proceed = ""
while proceed != "Cancel":
    if query in combos:
        searched_for = combos.get(query)
        items = "\n".join([f"{item}: {price}" for item, price in searched_for.items()])
        proceed = eg.buttonbox(f"Here is the combo:\n{items}\n\nWhat would you like to do with it?", "Query Found",
                               choices=("Change", "Delete", "Cancel"))
        print(proceed)
        if proceed == "Change":
            print("change")
        elif proceed == "Delete":
            print("nothing")
    else:
        proceed = eg.buttonbox("Combo not found. Try again or Cancel.", "Query Not Found", choices=("Try Again", "Cancel"))
