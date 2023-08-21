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