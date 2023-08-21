import tkinter as tk

class employeeform(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Employee Form")
        self.geometry("300x200")

        self.label_name = tk.Label(self, text="Enter Name: ", width=20, anchor="e")
        self.label_name.grid(row=0, column=0, padx= 0, pady=3, sticky="e")
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1)

        self.label_age = tk.Label(self, text="Enter Age: ")
        self.label_age.grid(row=1, column=0, padx= 0, pady=3, sticky="e")
        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=1, column=1)

        self.label_address = tk.Label(self, text="Enter Address: ")
        self.label_address.grid(row=2, column=0, padx= 0, pady=3, sticky="e")
        self.entry_address = tk.Entry(self)
        self.entry_address.grid(row=2, column=1)
        
        self.label_city = tk.Label(self, text="Enter City: ")
        self.label_city.grid(row=3, column=0, padx= 0, pady=3, sticky="e")
        self.entry_city = tk.Entry(self)
        self.entry_city.grid(row=3, column=1)

        self.label_state = tk.Label(self, text="Enter State: ")
        self.label_state.grid(row=4, column=0, padx= 0, pady=3, sticky="e")
        self.entry_state = tk.Entry(self)
        self.entry_state.grid(row=4, column=1)

        self.label_zip = tk.Label(self, text="Enter Zip Code: ")
        self.label_zip.grid(row=5, column=0, padx= 0, pady=3, sticky="e")
        self.entry_zip = tk.Entry(self)
        self.entry_zip.grid(row=5, column=1)

        self.btnSubmit = tk.Button(self, text="submit", command=self.submit)
        self.btnSubmit.grid(row=8, column=0, padx=0, pady=10, columnspan=2)

    def submit(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        address = self.entry_address.get()
        city = self.entry_address.get()
        state = self.entry_address.get()
        zip = self.entry_address.get()
        
        self.display_employee_info (name, age, address, city, state, zip)

    def display_employee_info(self, name, age, address, city, state, zip):

        #print(f"{self.name} and {self.age}")
        info_window = tk.Toplevel(self)
        info_window.title("Employee Information")
        info_window.geometry("300x300")
        label_info = tk.Label(info_window)
        label_info.pack(pady=10)

        label_name = tk.Label(info_window, text=f"Name: {name}")
        label_name.pack()
        label_age = tk.Label(info_window, text=f"Age: {age}")
        label_age.pack()
        label_address = tk.Label(info_window, text=f"Name: {address}")
        label_address.pack()
        label_city = tk.Label(info_window, text=f"Age: {city}")
        label_city.pack()
        label_state = tk.Label(info_window, text=f"Name: {state}")
        label_state.pack()
        label_zip = tk.Label(info_window, text=f"Age: {zip}")
        label_zip.pack()

class managerform(employeeform):
    def __init__(self):
        super().__init__()

        self.title("Manager Form")
        self.label_dept = tk.Label(self, text="Department: ")
        self.label_dept.grid(row=6, column=0, padx= 0, pady=3, sticky="e")

        self.entry_dept = tk.Entry(self)
        self.entry_dept.grid(row=6, column=1)

        self.geometry("400x400")
    
    def submit(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        address = self.entry_address.get()
        city = self.entry_city.get()
        state = self.entry_state.get()
        zip = self.entry_zip.get()
        dept = self.entry_dept.get()

        self.display_employee_info(name, age, address, city, state, zip, dept)

        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_city.delete(0, tk.END)
        self.entry_state.delete(0, tk.END)
        self.entry_zip.delete(0, tk.END)
        self.entry_dept.delete(0, tk.END)
        self.entry_name.focus_set()
        
    def exit(self):
        self.withdraw()  
        self.deiconify()
        #self.info_window.destroy()
        #tk.Toplevel.destroy()

        
    def display_employee_info(self, name, age, address, city, state, zip, dept):

        info_window = tk.Toplevel(self)
        info_window.title("ManagerInformation")
        info_window.geometry("300x200")

        label_name = tk.Label(info_window, text=f"Name: {name}", anchor="w")
        label_name.pack()
        label_age = tk.Label(info_window, text=f"Age: {age}", anchor="w")
        label_age.pack()
        label_address = tk.Label(info_window, text=f"Address: {address}", anchor="w")
        label_address.pack()
        label_city = tk.Label(info_window, text=f"City: {city}", anchor="w")
        label_city.pack()
        label_state = tk.Label(info_window, text=f"State: {state}", anchor="w")
        label_state.pack()
        label_zip = tk.Label(info_window, text=f"Zip Code: {zip}", anchor="w")
        label_zip.pack()
        label_dept = tk.Label(info_window, text=f"Department: {dept}", anchor="w")
        label_dept.pack()

        #self.btnExit = tk.Button(info_window, text="exit", command=lambda: [self.deiconify(), info_window.destroy()])
        self.btnExit = tk.Button(info_window, text="exit", command=exit)
        self.btnExit.pack()
        
if __name__ == "__main__":
    app = managerform()
    app.mainloop()

