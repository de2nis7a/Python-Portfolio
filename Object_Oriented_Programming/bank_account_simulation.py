# FILE: bank_account_simulation.py
# CONCEPT: Object-Oriented Programming (OOP) - Data Manipulation
# DEMONSTRATES: State change based on method calls (depositing, withdrawing) and encapsulation of balance.

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        
    def depositing(self, amount_deposit):
        self.deposit = amount_deposit
        self.balance += self.deposit
    
    def amount(self):
        return f"Bank account for {self.name} has £ {self.balance}"
       
    def withdrawing(self, amount_withdraw):
        self.withdraw = amount_withdraw
        self.balance -= amount_withdraw
        
    def __str__(self):
        return f"Account holder's name is {self.name} \nAccount balance is £ {self.balance}"
        
        
def test_acc():
    name = "Alicia Keys"
    account = BankAccount(name)
    print(account)
    account.depositing(100)
    print("Depositing £", account.deposit)
    print(account.amount())
    account.withdrawing(50)
    print("Withdrawing £", account.withdraw)
    print(account.amount())
    account.withdrawing(100)
    print("Withdrawing £", account.withdraw)
    print(account.amount())

if __name__ == "__main__":
    test_acc()
