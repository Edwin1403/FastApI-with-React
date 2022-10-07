class Bank():
    def __init__(self , starting_bal=0):
        self.bal = starting_bal
    def deposite(self , amount):
        self.bal += amount
    def withdraw(self , amount):
        self.bal -=amount
    def interest(self ):
        self.bal*=1.1            