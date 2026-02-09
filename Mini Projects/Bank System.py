class BankAccount:

    def __init__(self, account_holder, balance, password):
        self.account_holder = account_holder
        self.balance = balance
        self.password = password

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")


# ---------------- MAIN PROGRAM ---------------- #

print("===== Welcome to Secure Bank System =====\n")

name = input("Enter Account Holder Name: ").title()
initial_balance = float(input("Enter Initial Balance: "))
password = input("Set your account password: ")

account = BankAccount(name, initial_balance, password)

print("\nAccount Created Successfully!\n")

# Password Verification
entered_password = input("Enter password to access account: ")

if entered_password != account.password:
    print("Incorrect password! Access denied.")
else:
    print(f"\nWelcome, {account.account_holder}!")

    while True:
        print("\n----- MENU -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.display_balance()

        elif choice == "4":
            print("Thank you for using our bank system.")
            break

        else:
            print("Invalid option. Please try again.")
