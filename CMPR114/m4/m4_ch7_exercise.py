###################################################
# Exercise 1
###################################################
from tkinter import *

win = Tk()

win.title("Dropdown List")   #Label title for window
win.geometry("300x280")

listbox = Listbox(win, height = 8, width= 20, bg = "grey", activestyle = "dotbox", font = "Helvetica 11", fg = "yellow")


label = Label(win, text = "Food Items:", font = "Arial 11 bold", justify="left")
label.pack()

listbox.insert(1, "Sandwich")
listbox.insert(2, "Burger")
listbox.insert(3, "Pizza")
listbox.insert(4, "Fried Chicken")
listbox.insert(5, "Lobster")
listbox.insert(6, "Soup")
listbox.pack()

win.mainloop()

###################################################
# Exercise 2
###################################################
from tkinter import *

def create_window():
    win = Tk()

    win.title("Dropdown List")   #Label title for window
    win.geometry("300x320")

    listbox = Listbox(win, height = 8, width= 20, bg = "grey", activestyle = "dotbox", font = "Helvetica 11", fg = "yellow", selectmode=MULTIPLE)


    label = Label(win, text = "Food Items:", font = "Arial 11 bold", justify="left")
    label.pack()

    listbox.insert(1, "Sandwich")
    listbox.insert(2, "Burger")
    listbox.insert(3, "Pizza")
    listbox.insert(4, "Fried Chicken")
    listbox.insert(5, "Lobster")
    listbox.insert(6, "Soup")
    listbox.pack()

    def print_list():
        for i in listbox.curselection():
            print(listbox.get(i))

    btn = Button(win, text = "Print Selected Item", command = print_list)
    btn.pack(side = "bottom")

    win.mainloop()

def main():
    create_window()

main()

###################################################
# Exercise 3
###################################################
def main():
    names = ["Howard", "Jamie", "Jill"]

    print("Here's the original list")
    print(names)

    remove_name = input("Enter name to remove: ?")

    names.insert(0, "John")
    names.remove(remove_name)

    print("The new list:")
    print(names)
    
main()

def total():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum = 0

    for num in numbers:
        sum+=num

    average = sum / len(numbers)
    print(f"The total is {sum} and the average is {average:,.2f}")

    file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\numbers.txt", "w")
    
    file.write(" ".join(str(e) for e in numbers) + "\n")
    file.write(f"The total is {sum} and the average is {average:,.2f}")

total()

###################################################
# Exercise 5
###################################################
week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
sales = []
total = 0
for day in week:
    salesamt = float(input(f"Enter sales amount for {day}: "))
    total+=salesamt
    sales.append(salesamt)
    
print(f"list: {sales}")
msg = f"Total sales: {total}\n"
print(msg)

file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m4\\Sales.txt", "w")
file.write(msg)
file.close

###################################################
# Exercise 6
###################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def main(): 
    def login_user():
        username = txtUserName.get()
        password = txtPassword.get()
        if username == "jole" and password == "pwd123":
            #messagebox.showinfo(title="Welcome", message="Successful login.")
            entry_win.deiconify()
            login_win.withdraw()

        else:
            messagebox.showerror(title="Invalid login", message="Username or Password is not correct.  Try again")
            txtUserName.delete(0, tk.END)
            txtPassword.delete(0, tk.END)
            txtUserName.focus_set()

    def display_data():

        name = txtName.get()
        address = txtAddress.get()
        city = txtCity.get()
        state = cmbState.get()
        zipcode = txtZipcode.get()
        age = txtAge.get()

        msg = f"Name: {name}\nAddress: {address}\nCity: {city}\nState: {state}\nZip Code: {zipcode}\nAge: {age}\n"
        messagebox.showinfo(title="Personal Information", message=msg)

        #Write to file
        file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m4\\PII.txt", "w")
        file.write(msg)
        file.close

    def clear_textbox():
        txtName.delete(0, tk.END)
        txtAddress.delete(0, tk.END)
        txtCity.delete(0, tk.END)
        cmbState.set("")
        txtZipcode.delete(0, tk.END)
        txtAge.delete(0, tk.END)
        

    def exit_win():
        entry_win.quit()
        entry_win.destroy()
        login_win.quit()
        login_win.destroy()
        
    #Set State dropdown values
    states = ['AK','AL','AR','AZ','CA','CO','CT','CZ','DC','DE','FL','GA','GU','HI','IA','ID',
            'IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE',
            'NH','NJ','NM','NV','NY','OH','OK','OR','PA','PR','RI','SC','SD','TN','TX','UT',
            'VA','VI','VT','WA','WI','WV','WY']
    
    #Login Window
    login_win = tk.Tk()  
    login_win.geometry("260x150")  
    login_win.title("User Login")

    lblHeader = tk.Label(login_win, text="Please enter your credentials: ", font="Arial 10 bold", fg="#8B2323", justify="center")
    lblHeader.grid(row=0, column=0, pady=10, columnspan=3)

    lblUserName = tk.Label(login_win, text="Username: ", font="Arial 10 bold", width=10)
    lblUserName.grid(row=1, column=0, padx=1, pady=1)
    #lblUserName.pack()
    txtUserName = tk.Entry(login_win, width=25)
    txtUserName.grid(row=1, column=1, padx=1, pady=1)
    #txtUserName.pack()

    lblPassword = tk.Label(login_win, text="Password: ", font="Arial 10 bold")
    lblPassword.grid(row=2, column=0, padx=1, pady=1)
    #lblPassword.pack()
    txtPassword = tk.Entry(login_win, width=25, show="*")
    txtPassword.grid(row=2, column=1, padx=1, pady=1)
    #txtPassword.pack()
    lblSpace = tk.Label(login_win, text=" ", font="Arial 10 bold")
    lblSpace.grid(row=3, column=0, padx=1, pady=1)

    btnSubmit = tk.Button(login_win, text="Login", command=login_user, width=20)
    btnSubmit.grid(row=4, column=1, padx=1, pady=1)

    #Personal Data Entry Window
    entry_win = tk.Tk()
    entry_win.geometry("475x265")
    entry_win.title("Personal Information")
    entry_win.withdraw()

    lblName = tk.Label(entry_win, text="Name: ", font="Arial 10 bold", fg="#0000CD", width=10)
    lblName.grid(row=0, column=0, padx=1, pady=5, sticky="ne")
    txtName = tk.Entry(entry_win, width=35)
    txtName.grid(row=0, column=1, padx=0, pady=5)
    txtName.focus_set()

    lblAddress = tk.Label(entry_win, text="Address: ", font="Arial 10 bold", fg="#0000CD", width=10)
    lblAddress.grid(row=1, column=0, padx=5, pady=5, sticky="ne")
    txtAddress = tk.Entry(entry_win, width=35)
    txtAddress.grid(row=1, column=1, padx=1, pady=5)

    lblCity = tk.Label(entry_win, text="City: ", font="Arial 10 bold", fg="#0000CD", width=10)
    lblCity.grid(row=2, column=0, padx=1, pady=5, sticky="ne")
    txtCity = tk.Entry(entry_win, width=35)
    txtCity.grid(row=2, column=1, padx=1, pady=5)

    lblState = tk.Label(entry_win, text="State: ", font="Arial 10 bold", fg="#0000CD", width=10)
    lblState.grid(row=3, column=0, padx=1, pady=5, sticky="ne")
    cmbState = ttk.Combobox(entry_win, width=32, values=states)
    cmbState.grid(row=3, column=1, padx=1, pady=5)

    lblZipcode = tk.Label(entry_win, text="Zip Code: ", font="Arial 10 bold", fg="#0000CD", width=10)
    lblZipcode.grid(row=4, column=0, padx=1, pady=5, sticky="ne")
    txtZipcode = tk.Entry(entry_win, width=35)
    txtZipcode.grid(row=4, column=1, padx=1, pady=5)

    lblAge = tk.Label(entry_win, text="Age: ", font="Arial 10 bold", fg="#0000CD", width=10)
    lblAge.grid(row=5, column=0, padx=1, pady=5, sticky="ne")
    txtAge = tk.Entry(entry_win, width=35)
    txtAge.grid(row=5, column=1, padx=1, pady=5)

    lblSpace1 = tk.Label(entry_win, text=" ")
    lblSpace1.grid(row=6, column=0, padx=1, pady=5, sticky="ne")

    btnSubmit = tk.Button(entry_win, text="Display", command=display_data, width=14)
    btnSubmit.grid(row=7, column=0, padx=10, pady=1)

    btnClear = tk.Button(entry_win, text="Clear Test", command=clear_textbox, width=14)
    btnClear.grid(row=7, column=1, padx=1, pady=1)

    btnExit = tk.Button(entry_win, text="Exit", command=exit_win, width=14)
    btnExit.grid(row=7, column=2, padx=1, pady=1)

    login_win.mainloop()

main()

