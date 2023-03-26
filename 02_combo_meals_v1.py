"""Combo Meals - Version 1
create a dictionary containing the combos"""

combos_dictionary = {  # created a dictionary containing current combos
    "Value": {
        "Beef burger": 5.69,
        "Fizzy drink": 1.00,
        "Fries": 1.00
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

combos_list = [
    ["Value",
        ["Beef burger", 5.69],
        ["Fizzy drink", 1.00],
        ["Fries", 1.00],
     ],
    ["Cheezy",
        ["Cheeseburger", 6.69],
        ["Fizzy drink", 1.00],
        ["Fries", 1.00]
     ],
    ["Super",
        ["Cheeseburger", 6.69],
        ["Large fries", 2.00],
        ["Smoothie", 2.00]
     ]
]

print(combos_dictionary)
print(combos_list)
