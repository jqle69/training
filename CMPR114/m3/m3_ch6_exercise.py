###################################################
#Exercise 1
###################################################
lastname = input("Enter last name: ")
age = input("Enter age: ")

file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise1.txt", "w") 
file.write(f"Last Name: {lastname} \t\tAge: {age}\n")
file.close()

with open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise1.txt", "r") as file1:
    filecontent = file1.read()
    print(filecontent)
    file1.close

###################################################  
#Exercise 2
###################################################
def write():
    
    totalsum = 0

    outfile = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise2.txt", "w")

    num1 = int(input("Enter 1st value: "))
    num2 = int(input("Enter 2nd value: "))
    num3 = int(input("Enter 3rd value: "))

    sum = num1 + num2 + num3
    totalsum += sum
    avg = totalsum/3

    outfile.write(f"Input #1: {num1}\n")
    outfile.write(f"Input #2: {num2}\n")
    outfile.write(f"Input #3: {num3}\n")
    outfile.write(f"Total: {totalsum}\n")
    outfile.write(f"Average: {avg}\n")
    

    outfile.close()

write()
file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise2.txt", "r")
content = file.read()

print("")
print(content)
file.close

###################################################
#Exercise 3
###################################################
def sales():
    salary = int(input("Enter your base salary: "))
    num_days = int(input("Enter the number of sales day: "))
    sales_file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise3.txt", "w")
    
    totalsale = 0
    for item in range(1,num_days+1):
        sale = float(input(f"Enter sales for day {item}: " ))
        sales_file.write(f"Sale Amount for day {item} is ${sale:,.2f}\n")
        totalsale += sale

    if totalsale > 1000:
        commission = salary * .1
    else:
        commission = 0

    sales_file.write(f"Base Salry:  ${salary:,.2f}\n")
    sales_file.write(f"Total Sale:  ${totalsale:,.2f}\n")
    sales_file.write(f"Commission:  ${commission:,.2f}\n")

    sales_file.close

    print("Data saved to file.")

sales()

#Read file and output to screen
sale_file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise3.txt", "r")
content = sale_file.read()
print("")
print(content)

###################################################
#Exercise 4
###################################################
def main():
    num_employee = int(input("Enter number of employees: "))

    emp_file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise4.txt", "w")

    for count in range(1, num_employee+1):
        print(f"Enter data for employee #{count}: ")

        name = input("Name: ")
        idnum = input("ID Numerber: ")
        dept = input("Department: ")

        emp_file.write(f"Name: {name}\n")
        emp_file.write(f"ID Numer: {idnum}\n")
        emp_file.write(f"Department: {dept}\n")

        emp_file.close
        print("Recorded.")

main()
file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise4.txt", "r")
content = file.read()
print()
print(content)

###################################################
#Exercise 5
###################################################
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()                 #Create window interface
win.geometry("300x180")     #Set window size
win.title("Customer Information")   #Label title for window

lbllastname = tk.Label(win, text = "Enter Last Name: ").grid(column=0, row=0) #Label widge
lblfirstname = tk.Label(win, text = "Enter First Name: ").grid(column=0, row=1) #Label widge
lbladdress = tk.Label(win, text = "Enter Address: ").grid(column=0, row=2) #Label widge
lblcity = tk.Label(win, text = "Enter City: ").grid(column=0, row=3) #Label widge
lblstate = tk.Label(win, text = "Enter State: ").grid(column=0, row=4) #Label widge
lblzipcode = tk.Label(win, text = "Enter Zip Code: ").grid(column=0, row=5) #Label widge

def write():
    file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise5.txt", "w")
    content = file.write("\nConfirmation: " + LN.get() + "," + FN.get() + "\n" + 
                        ADDR.get() + "\n" + CITY.get() + ", " + STATE.get() + " " + ZIP.get() )
    file.close
    messagebox.showinfo("Information", "Data Recorded.")

def quit():
    messagebox.showinfo("Information", "Thank You.")
    win.destroy()
                        
def submit():
    messagebox.showinfo("Information", "You've entered: \n" + LN.get() + "," + FN.get() + "\n" + 
                        ADDR.get() + "\n" + CITY.get() + ", " + STATE.get() + " " + ZIP.get() ) #Display Info
    
LN = tk.StringVar() #Manage the Entry widget
txtlastname = tk.Entry(win, width=12, textvariable=LN).grid(column=1,row=0)

FN = tk.StringVar() #Manage the Entry widget
txtfirstname = tk.Entry(win, width=12, textvariable=FN).grid(column=1,row=1)

ADDR = tk.StringVar() #Manage the Entry widget
txtaddress = tk.Entry(win, width=12, textvariable=ADDR).grid(column=1,row=2)

CITY = tk.StringVar() #Manage the Entry widget
txtcity = tk.Entry(win, width=12, textvariable=CITY).grid(column=1,row=3)

STATE = tk.StringVar() #Manage the Entry widget
txtstate = tk.Entry(win, width=12, textvariable=STATE).grid(column=1,row=4)

ZIP = tk.StringVar() #Manage the Entry widget
txtzipcode = tk.Entry(win, width=12, textvariable=ZIP).grid(column=1,row=5)

btnSubmit = tk.Button(win, text="Submit", command = submit).grid(column=0, row=7)
btnQuit = tk.Button(win, text="Quit", command = quit).grid(column=1, row=7)
btnWrite = tk.Button(win, text="Transfer", command = write).grid(column=2, row=7)

win.mainloop()

###################################################
#Exercise 6
###################################################
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()                 #Create window interface
win.geometry("250x100")     #Set window size
win.title("Calculator")   #Label title for window

lblnum1  = tk.Label(win, text = "Enter Number 1: ").grid(column=0, row=0) #Label widge
lblnum2 = tk.Label(win, text = "Enter Number 2: ").grid(column=0, row=1) #Label widge
lblnum3 = tk.Label(win, text = "Enter Number 3: ").grid(column=0, row=2) #Label widge

def quit():
    messagebox.showinfo("Information", "Bye.")
    win.destroy()
                        
def submit():
    
    val1 = NUM1.get()
    val2 = NUM2.get()
    val3 = NUM3.get()
    
    total = int(val1) + int(val2) + int(val3)
    avg = total/3

    file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise6.txt", "w")
    content = file.write(f"\nThe three numbers are: {val1}, {val2}, {val3}" )
    content = file.write(f"\nThe total is: {total}")
    content = file.write(f"\nThe average is: {avg}")
    file.close
    messagebox.showinfo("Information", "You've entered:  " + NUM1.get() + "," + NUM2.get() + "," + NUM3.get())
    

    
NUM1 = tk.StringVar() #Manage the Entry widget
txtnum1 = tk.Entry(win, width=12, textvariable=NUM1).grid(column=1,row=0)

NUM2 = tk.StringVar() #Manage the Entry widget
txtnum2 = tk.Entry(win, width=12, textvariable=NUM2).grid(column=1,row=1)

NUM3 = tk.StringVar() #Manage the Entry widget
txtnum3 = tk.Entry(win, width=12, textvariable=NUM3).grid(column=1,row=2)

btnSubmit = tk.Button(win, text="Submit", command = submit).grid(column=0, row=3)
btnQuit = tk.Button(win, text="Quit", command = quit).grid(column=1, row=3)

win.mainloop()

###################################################
#Exercise 7
###################################################
def calc_grade(name, score1, score2):

    total = score1 +  score2
    avg = total/2

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise7.txt", "a")
    file.write(f"\nStudent name is {name}.")
    file.write(f"\nAverage score is {avg}.")
    file.write(f"\nGrade is {grade}.\n")

    file.close

    return grade

try:
    name = input("Enter full name: ")
    score1 = int(input("Enter midterm score: "))
    score2 = int(input("Enter final exam score: "))

    lettergrade = calc_grade(name,score1, score2)
    print(f"\nYour grade is {lettergrade}.")

    file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise7.txt", "r")
    content = file.read()
    print(content)
    file.close

except ValueError:
    print("Invalid input.  Please input valid values")

except Exception as err:
    print(err)

###################################################
#Exercise 7
###################################################
import random

def write():

    file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise8.txt", "w")

    for i in range(1,11):
        val = random.randint(1,10)
        file.write(f"\nValue #{i} = {val}")
    
    file.close

write()

file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise8.txt", "r")
content = file.read()
print(content)
file.close
