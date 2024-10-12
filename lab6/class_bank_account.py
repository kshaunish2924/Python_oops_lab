class BankAccount:
    def __init__(self,account_number,balance=0):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,ammount):
        self.balance+=ammount
        print(f"Deposited: {ammount} , New balance: {self.balance}")
    def withdraw(self,ammount):
        if ammount>self.balance:
            print("Insufficient balance.")
        else:
            self.balance-=ammount
            print(f"Withdrawn: {ammount} , New balance: {self.balance}")
    def check_balance(self):
        print(f"Balance: {self.balance}")
bank_account1=BankAccount(123456789)
bank_account1.deposit(5000)
bank_account1.withdraw(500)
bank_account1.check_balance()