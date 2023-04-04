"""Search Combo - Version 1
a component to search the dictionary for a specific combo"""

# imports...
import easygui as eg  # importing easygui as 'eg' to save time later (more space-efficient code)


# lists/dictionaries
combos = {  # created a dictionary containing current combos
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


# Main code...
query = eg.enterbox("Enter the combo name to search for:", "Enter Query")
proceed = ""
while proceed != "Cancel":
    if query in combos:
        searched_for = combos.get(query)
        print(searched_for)
        proceed = eg.buttonbox("Here is the combo:\n"
                               f"{searched_for(0)}\n"
                               f"{searched_for(1)}"
                               f"{searched_for(2)}"
                               f"\n"
                               f"What would you like to do?", "Query Found", choices=("Change", "Delete", "Cancel"))
        if proceed == "Change":
            print("change")

        elif proceed == "Delete":
            print("nothing")
