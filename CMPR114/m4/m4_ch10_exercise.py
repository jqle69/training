#Accessor -> get something, return value
# def get_something(self):
#     return self.something

#Mutator -> access then update value
###############################################
# Exercise 1
###############################################
class Student:
    def __init__(self):
        self.lastname = ""
        self.firstname = ""
        self.address = ""
        self.city = ""
        self.state = ""
        self.zipcode = ""
    
    def get_input(self):
        self.lastname = input("Enter Last Name: ")
        self.firstname = input("Enter First Name: ")
        self.address = input("Enter Address: ")
        self.city = input("Enter City: ")
        self.state= input("Enter State: ")
        self.zipcode= input("Enter Zip Code: ")

    def GetInformation(self):
        print(f"Student Last Name is {self.lastname}")
        print(f"Student First Name is {self.firstname}")
        print(f"Student Address is {self.address}")
        print(f"Student City is {self.city}")
        print(f"Student State is {self.state}")
        print(f"Student Zip Code is {self.zipcode}")
    
student1 = Student()
student1.lastname = "Doe"
student1.firstname = "Jane"
student1.address = "123 Main St"
student1.city = "Santa Ana"
student1.state = "CA"
student1.zipcode = "92706"

student2 = Student()
student2.lastname = "Cantor"
student2.firstname = "Mike"
student2.address = "123 Ocean St"
student2.city = "Newport Beach"
student2.state = "CA"
student2.zipcode = "65988"

student3 = Student()
student3.get_input()

student1.GetInformation()
student2.GetInformation()
student3.GetInformation()

###############################################
# Exercise 2
###############################################
class Teacher:
    def __init__(self, name, classroom, course):
        self.name = name
        self.classroom = classroom
        self.course = course
    
    def GetProfessor(self):
        print(f"Professor name is {self.name}")
        print(f"Professor assigned to {self.classroom}")
        print(f"Professor is teaching {self.course}")

teacher1 = Teacher("Jai Sim", "A206", "Python Programming")
teacher1.GetProfessor()

teacher2 = Teacher("Mike Smith", "A207", "Java Programming")
teacher2.GetProfessor()

###############################################
# Exercise 3
###############################################
class PI:
    def GetInformation(self, LN, FN, Age, Address, City, State, ZipCode):
        return LN + ", " + FN + ", " + Age + ", " + Address + ", " + City + ", " + State + ", " + ZipCode

PIData = PI()
PIData.LastName = input("Enter Last Name: ")
PIData.FirstName = input("Enter First Name: ")
PIData.Age = input("Enter Age: ")
PIData.Address = input("Enter Address: ")
PIData.City = input("Enter City: ")
PIData.State = input("Enter State: ")
PIData.ZipCode = input("Enter ZipCode: ")

print(PIData.GetInformation(PIData.LastName,
                            PIData.FirstName,
                            PIData.Age,
                            PIData.Address,
                            PIData.City,
                            PIData.State,
                            PIData.ZipCode))

###############################################
# Exercise 4
###############################################
import Customers

def main():
    name = input("Enter name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zipcode = input("Enter zip code: ")
    phone = input("Enter phone: ")

    var1 = Customers.Customers.set_name = name
    var2 = Customers.Customers.set_address = address
    var3 = Customers.Customers.set_city = city
    var4 = Customers.Customers.set_state = state
    var5 = Customers.Customers.set_zipcode = zipcode
    var6 = Customers.Customers.set_phone = phone

    print(f"Hello {var1}.  Your address is {var2}, {var3}, {var4} {var5} and your phone is {var6}.")

main()

###############################################
# Exercise 5
###############################################
import BankAccounts

def main():
    start_bal = float(input("Enter starting balance: "))

    #Initialize class BankAccount
    savings = BankAccounts.BankAccount(start_bal)

    pay = float(input("Pay amount this week?  "))
    print("Will deposit that amount into your account.")

    #add to account based upon pay
    savings.deposit(pay)
    print(f"Account balance is {savings.get_balance():,.2f}")

    cash = float(input("Withdrawal Amount?  "))
    print("Will withdraw that amount from your account.")

    savings.withdraw(cash)
    print(f"Account balance is {savings.get_balance():,.2f}")

main()

###############################################
# Exercise 6
###############################################
import Patients
import datetime as datetime

class Procedure:
    def __init__(self, procname, procdate, doctor, charges):
        self.procedurename = procname
        self.proceduredate = procdate
        self.doctor = doctor
        self.charges = charges
  
    #Assessor attributes
    def get_procedurename(self):
        return self.procedurename
    
    def get_proceduredate(self):
        return self.proceduredate
    
    def get_doctor(self):
        return self.doctor
    
    def get_charges(self):
        return self.charges

    def get_procedure_info(self):
        msg = f"Procedure Name: {self.procedurename}\n"
        msg = msg + f"Procedure Date: {self.proceduredate}\n"
        msg = msg + f"Physician: {self.doctor}\n"
        msg = msg + f"Cost: {self.charges}\n"
        
        return msg
    
    def set_procedurename(self, value):
        self.procedurename = value

    #Mutator attributes
    def set_proceduredate(self, value):
        self.proceduredate = value

    def set_doctor(self, value):
        self.doctor = value    

    def set_charge(self, value):
        self.charges = value

patient1 = Patients.Patient("John", "Q", "Le", "123 Main St", "Santa Ana", "CA", "92706", "714-949-2134", "Anna Le", "714-555-1212")

proc1 = Procedure("Physical Exam", datetime.date.today(), "Dr.Irvine", 250.00)
proc2 = Procedure("X-ray", datetime.date.today(), "Dr. Jamison", 500.00)
proc3 = Procedure("Blood Test", datetime.date.today(), "Dr. Smith", 200.00)

#Print Patient Info
print(patient1.get_patient_info())

#Print Procedure
print(proc1.get_procedure_info())
print(proc2.get_procedure_info())
print(proc3.get_procedure_info())

totalcharges = proc1.get_charges() + proc2.get_charges() + proc3.get_charges()
print(f"Total charges:  {totalcharges:,.2f}")
