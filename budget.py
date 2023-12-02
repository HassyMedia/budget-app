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
