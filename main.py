# Coffee Machine
import art
import data
import functionality

# Load up resources in the machine
available_resources = data.starting_resources

# Start coffee machine
is_on = True
print("Starting coffee machine...")
print(art.logo)

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Print Report
    if user_input == "report":
        functionality.print_report(available_resources)
    # Make Espresso
    # Make Latte
    # Make Cappuccino
    # Turn off machine
    elif user_input == "off":
        print("Turning off the coffee machine...")
        is_on = False
