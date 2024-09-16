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
    elif user_input in coffee_menu.get_items().split("/"):
        drink = coffee_menu.find_drink(user_input)
        print(f"{user_input} will cost {money_bank.CURRENCY}{drink.cost}.")
        if coffee_machine.is_resource_sufficient(drink):
            if money_bank.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
            else:
                print("Please try again with sufficient coins.")
        else:
            print("Apologies for the inconvenience, we will stock up the resources soon.")
            print("Please come again later.")

    # Restock resources
    elif user_input == "restock":
        water = int(input("What is the water quantity to restock in ml: "))
        milk = int(input("What is the milk quantity to restock in ml: "))
        coffee = int(input("What is the coffee quantity to restock in grams: "))
        coffee_machine.restock(water, milk, coffee)

    # Turn off the machine
    elif user_input == "off":
        is_on = False
        print("Shutting down PyCafe machine...")
        print("Coffee is life. Please come again!")

    else:
        print("Sorry, we couldn't understand your request. Please try again.")
