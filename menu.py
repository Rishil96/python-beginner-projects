# Menu Item Class
class MenuItem:
    """
        Models a single menu item
    """
    def __init__(self, name: str, cost: float, water: int, milk: int, coffee: int):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            coffee: coffee
        }


# Menu Class
class Menu:
    """
        Models the menu with drinks.
    """
    def __init__(self):
        # Initialize the menu items
        self.menu_items = [
            MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24),
            MenuItem(name="espresso", cost=1.5, water=50, milk=0, coffee=18),
            MenuItem(name="cappuccino", cost=3.0, water=250, milk=50, coffee=24)
        ]

    def get_items(self) -> str:
        """
            Returns all the names of the menu items in string format separated by /
        """
        options = ""
        for item in self.menu_items:
            options += f"{item.name}/"
        return options[:-1]

    def find_drink(self, order_name):
        """
            Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None
        """
        for item in self.menu_items:
            if item.name == order_name:
                return item
