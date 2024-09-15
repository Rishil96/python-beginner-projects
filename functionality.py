# This module contains the functions of each functionality available in the coffee machine
from data import coffee_requirements, coins


# Print report
def print_report(resources_available: dict) -> None:
    print("\n***** REPORT *****")
    print(f"Water: {resources_available.get("water", 0)}ml")
    print(f"Milk: {resources_available.get("milk", 0)}ml")
    print(f"Coffee: {resources_available.get("coffee", 0)}g")
    print(f"Money: ${resources_available.get("money", 0)}")
    print("******************\n")


# Check is resources are enough
def is_enough_resources(coffee: str, resources_available: dict) -> bool:
    # Check if all the resources are enough to make coffee
    for ingredient in coffee_requirements[coffee]:
        if not resources_available.get(ingredient, 0) >= coffee_requirements[coffee][ingredient]:
            print(f"Sorry, there isn't enough {ingredient} available at the moment. Please come back later.")
            return False
    return True


# Get payment from the user
def get_payment() -> float:
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = (quarters * coins["quarter"] + dimes * coins["dime"] +
                    nickels * coins["nickel"] + pennies * coins["penny"])
    print(f"Total amount paid: ${total_amount}")
    return total_amount
