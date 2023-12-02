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

# Function to create a bar chart representing the percentage spent in each category.
def create_spend_chart(categories):
    # Calculate total and individual category spending.
    total_spent = sum(sum(-item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories)
    category_spent = [(category.name, sum(-item['amount'] for item in category.ledger if item['amount'] < 0)) for category in categories]

    # Format the chart string with category names and spending percentages.
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| " + "".join("o  " if (spent / total_spent * 100) >= i else "   " for _, spent in category_spent) + "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Add category names to the chart.
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     " + "".join(category.name[i] + "  " if i < len(category.name) else "   " for category in categories) + "\n"

    return chart.rstrip("\n")

# Example usage of the budget app.
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# Making some transactions in the food and clothing categories.
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
food.transfer(50, clothing)

# Displaying the ledger for the food category and the spend chart.
print(food)
print(create_spend_chart([food, clothing, auto]))
  
