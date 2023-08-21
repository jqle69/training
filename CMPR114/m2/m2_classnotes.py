#############################################################
#Example 1
#############################################################
def write_to_file(name, age):
    path = "C:\\Users\\17147\\Desktop\\CMPR114\\m2\\"
    file_name = "output.txt"
    fullname = path + file_name

    with open(fullname, "a") as file:
        while True:
            name = input("Enter your name or type (q or Q) to quit:  ")
            if name.lower() == 'q':
                print("Bye")
                break
            else:
                curname = name

            age = input("Enter your age: ")
        
            file.write(f"Namne: {curname} \n")
            file.write("Age: " + str(age) + "\n")

        print(f"Date was write {file_name} was a success")

name = ""
age = 0
write_to_file(name, age)

print("End")

#############################################################
#Example 2
#############################################################
def write(name, age):
    path = "C:\\Users\\17147\\Desktop\\CMPR114\\m2\\"
    file_name1 = "output1.txt"
    file_name2 = "output2.txt"
    fullname1 = path + file_name1
    fullname2 = path + file_name2

    with open(fullname1, "a") as file1:
        file1.write(f"\nname: , {name}")
        file1.write(f"\nage: , {age}")

    print("File " + file_name1 + "  updated: " + name + ", " + str(age))
    
    with open(fullname2, "a") as file2:
        file2.write(f"\nname: , {name}")
        file2.write(f"\nage: , {age}")

    print("File " + file_name2 + "  updated: " + name + ", " + str(age))
    
def get_user_input():
    name = input("enter your name: ")
    if name.lower == "q":
        return 
        
    age = input("enter your age: ")

    return name, age

while True:
    name, age = get_user_input()
    if name == "" or age == "":
        print("name or age cannot be blank, skippping writing to the file")
        break

    write(name, age)

#############################################################
# Example 3
#############################################################
end = int(input("Enter value: "))
print("Number \t\t result")
for number in range(1, end+1):
    square = number ** 2
    print(f"{number} \t{square}")

temp = float(input("Enter temp:  "))

sumTemp=temp 
sumval = 0
counter = 0
while temp >= 100:
    print("Too High")
    temp = float(input("Enter temp:  "))
    
    sumval+=temp
    counter+=1

    avgval = sumval/counter

print(f"total temps: {sumval}" )
print(f"average temps: {avgval}" )

#############################################################
# Example 4
#############################################################
MARK_UP = 2.5
another = 'y'

while another == 'y':
    wholesale = float(input("Enter Wholesale Cost: "))
    retail = wholesale * MARK_UP
    print(f"Retail price ${retail:,.2f}")
    another = input("Another item (enter Y for yes)").lower

#############################################################
# Example 4
#############################################################
global num1
global num2
global num3

def add(num1, num2, num3):
    total = num1+num2+num3
    return total

for i in (1,2,3):
    if i == 1:
        num1 = int(input("Enter Value: "))
    elif i == 2:
        num2 = int(input("Enter Value: "))
    else:
        num3 = int(input("Enter Value: "))


print("num1: " + str(num1))
print("num2: " + str(num2))
print("num2: " + str(num2))
#val=add(num1,num2,num3)
#print(f"total is {val}")

def add(num1, num2, num3):
    total = num1+num2+num3
    return total
print(add(4,5,6))

#############################################################
# Example 4
#############################################################
import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    age = age_entry.get()

    if not name.isdigit() and age.isdigit():
        write_to_file(name, age)
        messagebox.showinfo("Success")
    elif not age.isdigit():
        messagebox.showinfo("Error, age has to be a digit")
    else:
        messagebox.showinfo("Error")

    name_entry.delete(0, tk.END)    #delte all data from 0 to END
    age_entry.delete(0, tk.END)    #delte all data from 0 to END

def write_to_file(name, age):
    file_name = "person.txt"

    with open(file_name, "a") as file:
        file.write(f"name: {name}\n")
        file.write(f"age: {age}\n")

window = tk.Tk() #initialize window

name_label = tk.Label(window, text="Name")
name_label.pack() #pack controls tightly with no spaces
name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Age")
age_label.pack() #pack controls
age_entry = tk.Entry(window)
age_entry.pack()

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

window.mainloop #allow program to loop
