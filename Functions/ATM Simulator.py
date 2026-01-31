# ATM Simulator Project
# Concepts used: functions, loops, conditions, input/output

balance = 1000


def check_balance():
    """Display current account balance"""
    print(f"Your current balance is ₹{balance}")


def deposit(amount):
    """Deposit money into account"""
    global balance
    if amount <= 0:
        print("Amount must be greater than zero.")
    else:
        balance += amount
        print("Deposit successful!")
        print(f"Updated balance: ₹{balance}")


def withdraw(amount):
    """Withdraw money from account"""
    global balance
    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient funds.")
        print(f"Available balance: ₹{balance}")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining balance: ₹{balance}")


while True:
    print("\n------ ATM MENU ------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        check_balance()

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 4:
        print("Thank you for using the ATM 😊")
        break

    else:
        print("Invalid choice. Please try again.")


'''
#simple Atm simulator
balance= 1000

def checkBal():
    global balance 
    print(f"Your current balance is {balance}")

def deposit(amt):
    global balance 
    if (amt<=0):
        print("Amount can't be negative or zero, please enter valid Amount ")
    else:
        print("Deposit is Successfull !!")
        balance +=amt 
        print(f"Your new balance is {balance}")

def withdraw(amt):
    global balance 
    if (amt>balance):
        print("Insufficient Funds ")
        print(f"Your balance is : {balance}")
    else:
        print(f"{amt} is withdrawn! ")
        balance -=amt 
        print(f"Your Balance is {balance}")


while(True):
    print("Welcome!! ")
    print("1. Check Balance ")
    print("2. Withdraw ")
    print("3. Deposit")
    print("4. Exit")
    choice= int(input("Enter your choice: "))

    if choice==1:
        checkBal()
    elif choice==2:
        amt=int(input("Enter the withdrawal amount>> "))
        withdraw(amt)
    elif choice==3:
        amt=int(input("Enter the amount to deposit>> "))
        deposit(amt)
    elif choice==4:
        exit()
    else:
        print("Invalid Choice ")@
'''


