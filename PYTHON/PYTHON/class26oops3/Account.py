class Account:
    min_bal=500
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def open_acc(self):
        print("account opened")
    def deposite(self,amount):
        self.acc_bal=self.acc_bal+amount
    def withdraw(self,amount):
        self.acc_bal=self.acc_bal-amount
    def get_bal(self):
        return self.acc_bal-self.min_bal
a1=Account(102,"rg",25000)
a1.deposite(500)
a1.deposite(1500)
a1.withdraw(1000)
print(a1.get_bal())
a2=Account(103,"pg",3200)
a2.deposite(1000)
print(a2.get_bal())
a3=Account(104,"sg",4500)
print(a3.get_bal())
# print(a1.__dict__)
# print(a2.__dict__)
# print(a3.__dict__)