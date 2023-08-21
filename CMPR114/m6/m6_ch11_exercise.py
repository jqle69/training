##################################################
# Exercise 1
##################################################
class AnimalType:
    def eats(self):
        print("This animal likes to eat? ")

class rabbits(AnimalType):
    def munch(self):
        print(" carrots")

class birds(AnimalType):
    def munch1(self):
        print(" seeds ")

class dogs(AnimalType):
    def munch(self):
        print(" bones")
BirdObject = AnimalType()
BirdObject = birds()

BirdObject.eats()
BirdObject.munch1()

DogObject = dogs()
DogObject.eats()
DogObject.munch()
##################################################
# Exercise 2a
##################################################
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self, name, age, studentid, gpa):
        super().__init__(name, age)
        self.studentid = studentid
        self.gpa = gpa

class teacher(person):
    def __init__(self, name, age, teacherid, subject):
        super().__init__(name, age)
        self.teacherid = teacherid
        self.subject = subject

student1 = student("Jane Doe", 25,777, 3.8)
print("Student Name: ", student1.name)
print("Student Age: ", student1.age)
print("Student ID: ", student1.studentid)
print("Student GPA: ", student1.gpa)
print(" ")
teacher1 = teacher("Ms. Cantor", 45, 7, "Python")
print("Teacher Name: ", teacher1.name)
print("Teacher Age: ", teacher1.age)
print("Teacher ID: ", teacher1.teacherid)
print("Teacher Course: ", teacher1.subject)

##################################################
# Exercise 2b
##################################################
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self, name, age, studentid, gpa, address, city, state, zipcode):
        #get input
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        studentid = input("Enter Student ID: ")
        gpa = input("Enter Student GPA: ")
        address = input("Enter Student Address: ")
        city = input("Enter Student City: ")
        state = input("Enter Student State: ")
        zipcode = input("Enter Student Zip Code: ")

        super().__init__(name, age)
        self.studentid = studentid
        self.gpa = gpa
        self.address = address
        self.city = city
        self.state = state
        self.zipcode  = zipcode

class teacher(person):
    def __init__(self, name, age, teacherid, subject, address, city, state, zipcode):

        name = input("Enter Teacher Name: ")
        age = input("Enter Teacher Age: ")
        teacherid = input("Enter Teacher ID: ")
        subject = input("Enter Teacher Subject: ")
        address = input("Enter Teacher Address: ")
        city = input("Enter Teacher City: ")
        state = input("Enter Teacher State: ")
        zipcode = input("Enter Teacher Zip Code: ")
    
        super().__init__(name, age)
        self.teacherid = teacherid
        self.subject = subject
        self.address = address
        self.city = city
        self.state = state
        self.zipcode  = zipcode

student1 = student("Jane Doe", 25,777, 3.8, "", "", "", "")
print(" ")
print("Student Name: ", student1.name)
print("Student Age: ", student1.age)
print("Student ID: ", student1.studentid)
print("Student GPA: ", student1.gpa)
print("Student Address: ", student1.address)
print("Student City: ", student1.city)
print("Student State: ", student1.state)
print("Student Zip Code: ", student1.zipcode)
print(" ")

teacher1 = teacher("Ms. Cantor", 45, 7, "Python", "", "", "", "")
print("Teacher Name: ", teacher1.name)
print("Teacher Age: ", teacher1.age)
print("Teacher ID: ", teacher1.teacherid)
print("Teacher Course: ", teacher1.subject)
print("Teacher Address: ", teacher1.address)
print("Teacher City: ", teacher1.city)
print("Teacher State: ", teacher1.state)
print("Teacher Zip Code: ", teacher1.zipcode)

##################################################
# Exercise 3
##################################################
import vehicles

def main():
    used_car1 = vehicles.automobiles("Audi", 2022, 45000, 80000.0)
    print("Make: ", used_car1.get_make())
    print("Model: ", used_car1.get_model())
    print("Mileage: ", used_car1.get_mileage())
    print("Price: ", used_car1.get_price())
    print(" ")

    used_car2 = vehicles.automobiles("Honda", 2021, 18000, 35000.0)
    print("Make: ", used_car2.get_make())
    print("Model: ", used_car2.get_model())
    print("Mileage: ", used_car2.get_mileage())
    print("Price: ", used_car2.get_price())
    print(" ")

main()

##################################################
# Exercise 4
##################################################
import vehicles

def main():
    used_car1 = vehicles.automobiles("Audi", 2022, 45000, 80000.0, 2)
    print("Make: ", used_car1.get_make())
    print("Model: ", used_car1.get_model())
    print("Mileage: ", used_car1.get_mileage())
    print("Price: ", used_car1.get_price())
    print("Doors: ", used_car1.get_doors())
    print(" ")

    used_car2 = vehicles.automobiles("Honda", 2021, 18000, 35000.0, 4)
    print("Make: ", used_car2.get_make())
    print("Model: ", used_car2.get_model())
    print("Mileage: ", used_car2.get_mileage())
    print("Price: ", used_car2.get_price())
    print("Doors: ", used_car2.get_doors())
    print(" ")

main()
##################################################
# Exercise 5
##################################################
class insects:
    def __init__(self, size, legs):
        self.__size = size
        self.__legs = legs
    
    #assessor methods
    def get_size(self):
        return self.__size
    def get_legs(self):
        return self.__legs
    
    #mutator methods
    def set_size(self, value):
        self.__size = value
    def set_legs(self, value):
        self.__legs = value

class bumblebees(insects):
    def __init__(self, size, legs, defense):
        super().__init__(size, legs)
        self.__defense = defense

    def get_defense(self):
        return self.__defense

    def set_defense(self, value):
        self.__defense = value

class grasshoppers(insects):
    def __init__(self, size, legs, ability):
        super().__init__(size, legs)
        self.__ability = ability

    def get_ability(self):
        return self.__ability

    def set_defense(self, value):
        self.__ability = value

bbee = bumblebees(5, 6, "sting")
print(f"Bumblebees are {bbee.get_size()} cm and {bbee.get_legs()} legs and can {bbee.get_defense()} you when threaten.")

ghop = grasshoppers(7,6, "jump")
print(f"Grasshoppers are {ghop.get_size()} cm and {ghop.get_legs()} legs and can {ghop.get_ability()} real high.")

##################################################
# Exercise 6
##################################################
import tkinter as tk

class EmployeeForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Form")
        self.geometry("300x200")

        self.label_name = tk.Label(self, text = "Enter Name:")
        self.label_name.grid(row = 0, column = 0)
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row = 0, column = 1)

        self.label_age = tk.Label(self, text = "Enter Age:")
        self.label_age.grid(row = 1, column = 0)
        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row = 1, column = 1)

        self.btnSubmit = tk.Button(self, text = "Submit", command = self.submit)
        self.btnSubmit.grid(row = 4, columnspan = 2, pady = 10)
    
        def submit(self):
            name = self.entry_name.get()
            age = self.entry_age.get()

            self.display_employee_info(name,age)

        def display_employee_info(self, name, age):
            info_window = tk.Toplevel(self)
            info_window.title("Employee Information")
            info_window.geometry("300x100")

            infolbl = tk.Label(info_window, text = "Emp Info")
            infolbl.pack(pady = 10)
            namelbl = tk.Label(info_window, text = f"Name: {name}")
            namelbl.pack()
            agelbl = tk.Label(info_window, text = f"Age: {age}")
            agelbl.pack()

class ManagerForm(EmployeeForm):
    def __init__(self):
        super().__init__()
        self.title("Manager Form")
        self.geometry("400x250")

        self.deptlbl = tk.Label(self, text = "Dept. Name:")
        self.deptlbl.grid(row = 2, column = 0)
        self.deptentry = tk.Entry(self)
        self.deptentry.grid(row = 2, column = 1)

    def submit(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        dept = self.deptentry.get()
        self.display_employee_info(name, age, dept)

    def display_employee_info(self, name, age, dept):
        info_window = tk.Toplevel(self)
        info_window.title("Manager Info")
        #info_window.geometry("300x100")
        #info_window.pack(pady = 10)

        lblname = tk.Label(info_window, text = f"Name: {name}")
        lblname.pack()
        lblage = tk.Label(info_window, text = f"Age: {age}")
        lblage.pack()
        lbldept = tk.Label(info_window, text = f"Dept: {dept}")
        lbldept.pack()

if __name__ == "__main__":
    app = ManagerForm()
    app.mainloop()

##################################################
# Exercise 7
##################################################
import tkinter as tk

class loginform(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("200x100")

        self.lblusername = tk.Label(self, text="Username: ")
        self.lblusername.grid(row=0, column=0)
        self.txtusername = tk.Entry(self)
        self.txtusername.grid(row=0, column=1)
    
        self.lblpassword = tk.Label(self, text="Password: ")
        self.lblpassword.grid(row=1, column=0)
        self.txtpassword = tk.Entry(self)
        self.txtpassword.grid(row=1, column=1)

        self.btnLogin = tk.Button(self, text="Login", command=self.login)
        self.btnLogin.grid(row=2, columnspan=2, pady=10)

    def login(self):
        username = self.txtusername.get()
        password = self.txtpassword.get()

        if username == "sac" and password == "sac":
            self.withdraw()
            ordform = orderform(self)
            ordform.mainloop()
        else:
            error_win = tk.Toplevel()
            error_win.title("Login Error")

            lblError = tk.Label(error_win, text="Invalid username or password.")
            lblError.pack(pady=10)

class orderform(tk.Tk):
    def __init__(self, loginform):
        super().__init__()
        self.title("Order Form")
        self.login_form = loginform

        self.lblitem = tk.Label(self, text="Item: ")
        self.lblitem.grid(row=0, column=0)
        self.txtitem = tk.Entry(self)
        self.txtitem.grid(row=0, column=1)
    
        self.lblqty = tk.Label(self, text="Qty: ")
        self.lblqty.grid(row=1, column=0)
        self.txtqty = tk.Entry(self)
        self.txtqty.grid(row=1, column=1)

        self.btnSubmit = tk.Button(self, text="Submit", command=self.submit)
        self.btnSubmit.grid(row=2, columnspan=2, pady=10)

        self.btnExit = tk.Button(self, text="Exit", command=self.exit)
        self.btnExit.grid(row=3, columnspan=2, pady=10)

    def submit(self):
        item = self.txtitem.get()
        qty = self.txtqty.get()

        print(f"Order placed: Item={item}, Quantity={qty}")

    def exit(self):
        self.withdraw()
        self.login_form.deiconify()

if __name__ == "__main__":
    login_form = loginform()
    login_form.mainloop()