# Coffee Machine using OOP
from art import logo
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_bank = MoneyMachine()


is_on = True

print("Starting the PyCafe Coffee machine...")
print(logo)

while is_on:
    # Get user input
    user_input = input(f"\nWhat would you like to have ({coffee_menu.get_items()}): ").lower()

    # Print report
    if user_input == "report":
        print("***** REPORT *****")
        coffee_machine.report()
        money_bank.report()
        print("******************")

    # Make coffee
    # Restock resources
    # Turn off the machine
    elif user_input == "off":
        is_on = False
        print("Shutting down PyCafe machine...")
        print("Coffee is life. Please come again!")
