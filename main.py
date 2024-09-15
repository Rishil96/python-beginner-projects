# Coffee Machine
import art
import data
from functionality import print_report, process_coffee, restock_ingredients


def start_coffee_machine():
    # Load up resources in the machine
    available_resources = data.starting_resources.copy()

    # Start coffee machine
    is_on = True
    print("Starting PyCafe machine...")
    print(art.logo)

    while is_on:
        # Steps to make coffee
        # 1. Check if enough resources are available to make espresso
        # 2. Get payment in coins from user
        # 3. Check if payment is correct
        # 4. Make coffee for the customer

        print("************************************************")
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Print Report
        if user_input == "report":
            print_report(available_resources)

        # Make Espresso, Latte, Cappuccino
        elif user_input in ["espresso", "latte", "cappuccino"]:
            process_coffee(user_input, available_resources)

        # Restock ingredients
        elif user_input == "restock":
            restock_ingredients(available_resources)

        # Turn off machine
        elif user_input == "off":
            print("Turning off the coffee machine...")
            is_on = False

        # Unknown input
        else:
            print("Could not understand your request. Please try again!")

    # Restart machine?
    restart = input("Would you like to restart the PyCafe Machine? Type 'y' or 'n': ").lower()
    if restart == 'y':
        start_coffee_machine()
    else:
        print("Coffee is life. Please visit PyCafe again!")


if __name__ == "__main__":
    start_coffee_machine()
