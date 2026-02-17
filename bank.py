class BankAccount:
    def __init__(self, acc_no, name, pin, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.__pin = pin            
        self.balance = balance
        self.transactions = []

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount}")
            return True
        return False

    def show_balance(self):
        return self.balance

    def show_transactions(self):
        return self.transactions


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, name, pin, balance=0):
        super().__init__(acc_no, name, pin, balance)
        self.interest_rate = 0.04

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest added ₹{interest:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, acc_no, name, pin, balance=0):
        super().__init__(acc_no, name, pin, balance)
        self.overdraft_limit = 5000

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount} (Overdraft used)")
            return True
        return False


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_type, acc_no, name, pin, balance):
        if acc_type == "savings":
            self.accounts[acc_no] = SavingsAccount(acc_no, name, pin, balance)
        else:
            self.accounts[acc_no] = CurrentAccount(acc_no, name, pin, balance)

    def login(self, acc_no, pin):
        account = self.accounts.get(acc_no)
        if account and account.verify_pin(pin):
            return account
        return None




bank = Bank()
bank.create_account("savings", 101, "Aayush", 1234, 10000)
bank.create_account("current", 102, "Rahul", 4321, 5000)

attempts = 3
while attempts > 0:
    acc_no = int(input("Enter Account Number: "))
    pin = int(input("Enter PIN: "))

    user = bank.login(acc_no, pin)
    if user:
        print(f"\nWelcome {user.name}")
        while True:
            print("\n1.Deposit  2.Withdraw  3.Balance  4.Transactions  5.Exit")
            choice = int(input("Choose: "))

            if choice == 1:
                amt = int(input("Amount: "))
                user.deposit(amt)

            elif choice == 2:
                amt = int(input("Amount: "))
                if not user.withdraw(amt):
                    print("Insufficient balance")

            elif choice == 3:
                print("Balance:", user.show_balance())

            elif choice == 4:
                for t in user.show_transactions():
                    print(t)

            elif choice == 5:
                break
        break
    else:
        attempts -= 1
        print("Invalid credentials")

if attempts == 0:
    print("Account locked due to multiple failed attempts")
