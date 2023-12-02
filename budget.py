class Category:
    # Constructor: Initializes a new instance of the Category class.
    # Sets the category name and initializes an empty ledger list.
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # Method to deposit an amount into the category's ledger.
    # Accepts an amount and an optional description.
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # Method to withdraw an amount from the category's ledger.
    # Checks if the withdrawal amount is available before proceeding.
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    # Method to calculate and return the current balance of the ledger.
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    # Method to transfer an amount from this category to another category.
    # Performs a withdrawal in this category and a deposit in the other category.
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    # Method to check if a specified amount is available in the ledger.
    def check_funds(self, amount):
        return self.get_balance() >= amount

    # Special method to define the string representation of the Category object.
    # Formats and returns the ledger entries and the total as a string.
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = "".join(f"{item['description'][:23]:23}{item['amount']:>7.2f}\n" for item in self.ledger)
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


