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


from datetime import time
alltimes = input("Enter times in MM:SS\n").split()
for time in alltimes:
     #hour, min, sec = [int(i) for i in time.split(":")]

     newtime = [int(i) for i in time.split(":")]

     print(newtime)
