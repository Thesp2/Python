class bank:
    def __init__(self, balance, username):
        self.balance = balance
        self.username = username
        self.transactions = []

    def deposit(self):
        amu = int(input("Enter the amount to deposit: "))
        if amu > 0:
            self.balance += amu
            self.transactions.append(f"Deposit {amu}$")
            print(f"Successfully added {amu}$ \nYour balance is {self.balance}$ ")
        else:
            print("Enter valid amount!!!")

    def withdraw(self):
        dele = int(input("Enter the amount you want to withdraw: "))
        if dele > 0 and dele <= self.balance:
            self.balance -= dele
            self.transactions.append(f"Withdraw {dele}$")
            print(f"Withdrew {dele}$ from your account \nYour total balance is {self.balance}$")
        elif dele > self.balance:
            print("Insufficient balance!!")
        else:
            print("Enter valid amount!!")

    def check_balance(self):
        print(f"Account holder = {self.username}\nYour balance = {self.balance}$")

    def transaction_history(self):
        if self.transactions:
            print("Transaction History:")
            for transaction in self.transactions:
                print(f"\t{transaction}")
        else:
            print("No transaction yet!")

def switch(todo):
    if todo == "deposit":
        user1.deposit()
    elif todo == "withdraw":
        user1.withdraw()
    elif todo == "check":
        user1.check_balance()
    elif todo == "history":
        user1.transaction_history()
    else:
        print("Invalid action!")

user1 = bank(0, "Sp")

while True:
    todo = input("\nEnter the action (deposit / withdraw / check / history / exit): ").lower()
    if todo == "exit":
        print("Exiting. Thank you!")
        break
    switch(todo)


