class Account():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return "Account Owner:{}\nAvailable Balance:${}".format(self.name,self.balance)
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit Accepted")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
            print("Withdrawal Accepted")
        else:
            print("Insufficient Balance")
b1=Account('Alan',9000)
print(b1)
print("________________________")
b1.deposit(500)
b1.withdraw(10000)
print(b1)