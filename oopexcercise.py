class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance


    def greet(self):
        print("Good Morning")

    def deposit(self, amount):
        self.balance += amount
        print(f"Account: {self.owner_name} | Amount Deposited: {amount} | New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Account: {self.owner_name} | Amount Withdrawn: {amount} | New Balance: {self.balance}")

    def show(self):
        print(f"Current balance for {self.owner_name}: {self.balance}")


# Main program
name = input("Enter your name: ")
starting_balance = float(input("Enter starting balance: "))
deposit_amount = float(input("Enter deposit amount: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

account = BankAccount(name, starting_balance)

account.greet()
account.deposit(deposit_amount)
account.withdraw(withdrawal_amount)
account.show()