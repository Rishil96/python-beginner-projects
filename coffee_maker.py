from menu import MenuItem


# Class that handles the making of Coffee
class CoffeeMaker:
    """
        Models the machine that makes the coffee
    """
    def __init__(self):
        # Allocate ingredients/resources in our machine on startup
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self) -> None:
        """
        Prints a report of all resources.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink: MenuItem) -> bool:
        """
            Takes menu item as input and checks if the resources in machine is enough to make the drink.
        """
        for ingredient in drink.ingredients:
            if drink.ingredients[ingredient] > self.resources[ingredient]:
                print(f"There isn't enough {ingredient} available at the moment.")
                return False
        return True

    def make_coffee(self, order: MenuItem):
        """
            Takes the order and makes the coffee by using ingredients available
        """
        for ingredient in order.ingredients:
            self.resources[ingredient] -= order.ingredients[ingredient]

        print(f"Here is your {order.name} ☕️. Enjoy!")
