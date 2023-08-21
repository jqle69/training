#################################################
list = [1,2,3,4,5,6,7,8,9,10]
total=0
for i in list:
    total+=i

avg = total / 10
print(total)
print(avg)

#################################################
list = [1,2,3,4,5,6,7,8,9,10]
val = list[6]
print(val)

#################################################
list = [[1,2,3,4,5],[6,7,8,9,10]]
val = list[1][1]
print(val)

#################################################
list = [[[1,2,3],[4,5,6]],
        [[7,8,9],[10,11,12]],
        [[13,14,15]]]
val = list[1][1][0]
print(val)

#################################################
class rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

obj = rectangle(5, 10)
print("Area: ", obj.get_area())
print("Perimeter: ", obj.get_perimeter())
      
#################################################
class bankaccount():
    def __init__ (self, acctno, owner, balance):
        self.acctno = acctno
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance-=amount
        else:
            print("Insufficient funds.")
    
    def get_balance(self):
        return self.balance
    
    def display_account_info(self):
        info = f"""Account Number: {self.acctno}\nOwner: {self.owner}\nBalance: {self.balance:,.2f}\n"""
        return info

person1 = bankaccount(123444, "John Smith", 1000.00)
person1.deposit(200)
person1.deposit(400)
person1.withdraw(150)
print(person1.display_account_info())

person2 = bankaccount(123450, "Jane Doe", 5500.00)
person2.deposit(300)
person2.deposit(695)
person2.withdraw(530)
print(person2.display_account_info())

#################################################
