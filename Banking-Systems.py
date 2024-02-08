class user():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_details(self):
        print("Personal Detalis")
        print("")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
class Bank(user):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("Account balance has been updated :",self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("Insufficient funds :",self.balance)
        else:
            self.balance=self.balance-self.amount
            print("Account balance has been updated :",self.balance)
    def view_balance(self):
        self.show_details()
        print("Account balance:",self.balance)
name=input("Enter Name")
age=input("Enter age")
gender=input("Gender")
a=Bank(name,age,gender)
print("Choose your Need")
print("1.Personal Details")
print("2.Deposit")
print("3.Withdraw")
print("4.Balance")
print("5.Exit")
while True:
    x=int(input())
    if x==1:
        a.show_details()
    elif x==2:
        a.deposit(int(input("Enter the amount for deposit")))
    elif x==3:
        a.withdraw(int(input("Enter the amount for withdraw")))
    elif x==4:
        a.view_balance()
    else:
        break