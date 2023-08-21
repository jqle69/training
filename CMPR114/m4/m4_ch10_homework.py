###########################################
# Project 1
###########################################
class Pet:
    #Mutator attributes    
    def set_name(self, value):
        self.__name = value
    
    def set_animal_type(self, value):
        self.__animal_type = value

    def set_age(self, value):
        self.__age = value

    #Assessor attributes
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
def main():
    mypet = Pet()
    mypet.__name = input("Enter Pet's Name: ")
    mypet.__animal_type = input("Enter Pet's Type: ")
    mypet.__age = input("Enter Pet's Age (in years): ")
    
    print(f"Your pet's name is {mypet.__name}")
    print(f"Your pet is a(n) {mypet.__animal_type}")
    print(f"Your pet's age is {mypet.__age} years old")

main()

###########################################
# Project 2
###########################################
class Employee:
    def __init__ (self, name, id_no, department, jobtitle):
        self.name=name
        self.id_no=id_no
        self.department=department
        self.jobtitle=jobtitle

    def get_employee_info(self):
        msg = f"Name: {self.name}\tID Number: {self.id_no}\tDepartment: {self.department}\tJob Title: {self.jobtitle}"

        return msg

def main():
    employee1 = Employee("Susan Meyers",326558,"Finance/Acct","Vice President")
    employee2 = Employee("Mark Jones",254877,"IT/Software Dev","Programmer")
    employee3 = Employee("Joy Rogers",326588,"Manufacturing","Assembler")

    print(employee1.get_employee_info())
    print(employee2.get_employee_info())
    print(employee3.get_employee_info())

main()
###########################################
# Project 3
###########################################
class RetailItem:
    def __init__(self, itemdesc, qty, price):
        self.item_descirption = itemdesc
        self.quantity = qty
        self.price = price
    
    def get_item_info(self):
        msg = f"Item Description: {self.item_descirption}\tQuantity: {self.quantity}\tPrice: {self.price}"

        return msg

def main():
    item1 = RetailItem("Black Jacket", 45, 75.50)
    item2 = RetailItem("Denim Jean", 100, 43.79)
    item3 = RetailItem("Silk Shirt", 82, 25.99)

    print(item1.get_item_info())
    print(item2.get_item_info())
    print(item3.get_item_info())

main()