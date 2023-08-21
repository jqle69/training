class Person:

    def __init__(self): #__init__ this is the constrcutor
        self.name = "" #init the name object var
        self.age = 0
        self.address = ""

        #object oriented programming (OOP), place, person or thing
        #address = place, person = jason, thing = tree
        #? any variable object is considered OOP

    def get_input(self):
        self.name = input('enter the customer')
        self.age = int(input('enter the age of the customer'))
        self.address = input ('enter the address of the customer')

    def display(self):
        print (f"Name: {self.name}  age: {self.age} address: {self.address} ")

person = Person() #creating an instance of the class called Person
person1 = Person() #creating an instance of the class called Person

person.get_input()# calls the input function
person1.get_input()# calls the input function

#print(person.display()) #calls the display function


#example of creating multiple classes
class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def get_info(self): #there is NO parameters being passed
        return f"{self.make} {self.model} {self.year} {self.price}"#return the three parameters

class CarDealer:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cars = [] #empty array that will hold an inventory of cars

    def add_car(self, car):
        self.cars.append(car) #add and append the cars when entered

    def get_car_inventory(self):
        inventory  = [] #empty array that will hold the inventory
        for car in self.cars:
            inventory.append(car.get_info())
        return inventory #returns the list of cars that was appended

car1 = Car ("Nissan", "GTR", 2010, 80000)
print("\n\n")

car2 = Car ("Toyota", "Highlander", 2007, 25000)

#COME BACK HERE...
#customer =Person ("","","")

dealer = CarDealer("Nissan Corp", "California")

#display the car dealers inventory
dealer.add_car(car1)
dealer.add_car(car2)


#retreives the cars inventory list
inventory = dealer.get_car_inventory()

#print

print(person.name)
print(person.age)
print(person.address)
print("==============")


for car_info in inventory:
    print (car_info)

print(person1.name)
print(person1.age)
print(person1.address)
 














    