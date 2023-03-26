"""Exit Button - Version 1
A component to check if the user wants to quit, then quits"""

import easygui as eg

quit = eg.buttonbox("Are you sure you want to quit? All progress will be lost!!", "Quit?", choices=("Yes - Quit", "No - Cancel"))
if quit == "Yes - Quit":
    eg.msgbox("Thank you for using this Burger Menu Program!", "Goodbye!", ok_button=":D")
    exit()
else:
    proceed = eg.buttonbox("How would you like to proceed?", "Menu Choices", choices=("Search", "Add", "Delete", "Help", "Exit"))
