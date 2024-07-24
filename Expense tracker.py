# Expense Tracker

import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        """Adds a new expense to the list."""
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description (optional): ")

        expense = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        """Displays all expenses."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("-" * 30)
        print("Expenses:")
        print("-" * 30)
        for expense in self.expenses:
            print(f"Date: {expense['date']}")
            print(f"Amount: {expense['amount']:.2f}")
            print(f"Category: {expense['category']}")
            if expense["description"]:
                print(f"Description: {expense['description']}")
            print("-" * 30)

    def get_monthly_summary(self):
        """Calculates and displays monthly expense summary."""
        current_month = datetime.date.today().month
        monthly_expenses = []

        for expense in self.expenses:
            expense_date = datetime.datetime.strptime(expense["date"], "%Y-%m-%d").date()
            if expense_date.month == current_month:
                monthly_expenses.append(expense)

        if monthly_expenses:
            total_expenses = sum(expense["amount"] for expense in monthly_expenses)
            print(f"Total expenses for {datetime.date.today().strftime('%B %Y')}: {total_expenses:.2f}")

            categories = set(expense["category"] for expense in monthly_expenses)
            for category in categories:
                category_expenses = [expense["amount"] for expense in monthly_expenses
                                       if expense["category"] == category]
                total_category_expenses = sum(category_expenses)
                print(f"   {category}: {total_category_expenses:.2f}")

        else:
            print(f"No expenses recorded for {datetime.date.today().strftime('%B %Y')}")

    def save_expenses(self):
        """Saves expenses to a file (optional)."""
        # You can add code here to save expenses to a file (e.g., using json or csv)
        # ...

    def load_expenses(self):
        """Loads expenses from a file (optional)."""
        # You can add code here to load expenses from a file (e.g., using json or csv)
        # ...

def main():
    """Main function for the expense tracker."""
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Monthly Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.get_monthly_summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
    