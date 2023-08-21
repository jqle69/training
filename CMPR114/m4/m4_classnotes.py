class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.address = ""
    
    def get_input(self):
        self.name = input("enter name: ")
        self.age = int(input("enter age: "))
        self.adress = input("enter address: ")

    def display(self):
        print(f"Name: {self.name}  Age: {self.age}  Address:  {self.address}")

class Cars():
    def add_car(self, car):
        self.carname = car

class CarDealer():
    pass

person = Person()
person.get_input()
print(person.display())

