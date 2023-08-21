##################################################
# Project 1
##################################################
class Employee:
    def __init__(self, name, employeeno):
        self.name = name
        self.employeeno = employeeno

class ShiftSupervisor(Employee):
    def __init__(self, name, employeeno, salary, bonus):
        name = input("Enter Employee Name: ")
        employeeno = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")
        bonus = input("Enter bonus: ")
    
        super().__init__(name, employeeno)
        self.salary = salary
        self.bonus = bonus

emp1 = ShiftSupervisor("", "", "", "")
print(" ")
print("Employee Name: ", emp1.name)
print("Employee Number: ", emp1.employeeno)
print("Employee Salary: ", emp1.salary)
print("Employee Bonus: ", emp1.bonus)


##################################################
# Project 2
##################################################
class Person:
    def __init__(self, name, address, telephone) -> None:
        self.name = name
        self.address = address
        self.telephone = telephone

class Customer(Person):
    def __init__(self, name, address, telephone, customerno, mailoptin):
        name = input("Enter Customer Name: ")
        address = input("Enter Customer Address: ")
        telephone = input("Enter Customer Phone: ")
        customerno = input("Enter Customer Number: ")
        mailoptin = input("Enter Customer Mail Opt-in: ")
    
        super().__init__(name, address, telephone)
        self.customerno = customerno
        self.mailoptin = mailoptin

cust1 = Customer("", "", "", "", "")
print(" ")
print("Customer Name: ", cust1.name)
print("Customer Address: ", cust1.address)
print("Customer Telephone: ", cust1.telephone)
print("Customer Number: ", cust1.customerno)
print("Customer Mail Opt-in: ", cust1.mailoptin)
