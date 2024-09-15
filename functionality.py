# This module contains the functions of each functionality available in the coffee machine

# Print report
def print_report(resources_available: dict):
    print("\n***** REPORT *****")
    print(f"Water: {resources_available.get("water", 0)}ml")
    print(f"Milk: {resources_available.get("milk", 0)}ml")
    print(f"Coffee: {resources_available.get("coffee", 0)}g")
    print(f"Money: ${resources_available.get("money", 0)}")
    print("******************\n")


