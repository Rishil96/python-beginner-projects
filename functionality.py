# This module contains the functions of each functionality available in the coffee machine
from data import coffee_requirements, coins, coffee_costs


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
            print(f"There isn't enough {ingredient} available at the moment")
            return False
    return True


# Get payment from the user
def get_payment(coffee: str) -> float:
    print(f"Please pay ${coffee_costs[coffee]} for {coffee}.")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = (quarters * coins["quarter"] + dimes * coins["dime"] +
                    nickels * coins["nickel"] + pennies * coins["penny"])
    print(f"Total amount paid: ${total_amount}")
    return total_amount


# Check if user has paid the correct amount
def is_coffee_paid(coffee: str, paid_amount: float) -> bool:
    is_paid = paid_amount >= coffee_costs[coffee]
    if is_paid:
        print(f"Here is your change while we make your coffee: ${round(paid_amount - coffee_costs[coffee], 2)}")
    return is_paid


# Make coffee by using resources
def make_coffee(coffee: str, available_resources: dict) -> None:
    # Use resources from the machine
    for resource in coffee_requirements[coffee]:
        available_resources[resource] -= coffee_requirements[coffee][resource]
    # Add the paid amount to the machine
    available_resources["money"] += coffee_costs[coffee]
    print(f"Here is your delicious {coffee}. Please enjoy☕!")


# Process coffee: all steps that goes into getting coffee
def process_coffee(coffee: str, available_resources: dict) -> None:
    # Check if resources are available to make the requested coffee
    if is_enough_resources(coffee, available_resources):
        # Get payment from the user
        payment = get_payment(coffee)
        # Check if correct amount is paid
        if is_coffee_paid(coffee, payment):
            # Make coffee and return the change
            make_coffee(coffee, available_resources)
        else:
            print(f"You have not paid the correct amount for {coffee}. Money refunded.")
    else:
        print("Apologies for the inconvenience, we will stock up the ingredients soon.")
        print("Please come back later.")
