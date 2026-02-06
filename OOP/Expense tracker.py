class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        try:
            amount = float(input("Enter expense amount: ₹"))
            category = input("Enter category: ").strip()

            expense = {
                "amount": amount,
                "category": category
            }

            self.expenses.append(expense)
            print("Expense added successfully!")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("\nAll Expenses:")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense['category']} - ₹{expense['amount']}")

    def total_expense(self):
        if not self.expenses:
            print("No expenses to calculate.")
            return

        total = sum(expense["amount"] for expense in self.expenses)
        print(f"\nTotal Expense: ₹{total}")


def menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")


tracker = ExpenseTracker()

while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            tracker.add_expense()
        elif choice == 2:
            tracker.view_expenses()
        elif choice == 3:
            tracker.total_expense()
        elif choice == 4:
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1–4.")

    except ValueError:
        print("Please enter a valid number.")
