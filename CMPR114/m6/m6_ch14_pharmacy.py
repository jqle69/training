import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import sqlite3 as sql

class PharmacyManagementSystems:
    def __init__ (self):
        self.window = tk.Tk()
        self.window.title("Pharmacy Management System")
        self.medicines = []     #Capture Medicine Input

        self.name_label = tk.Label(self.window, text="Med Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.qty_label = tk.Label(self.window, text="Quantity:")
        self.qty_label.grid(row=1, column=0, padx=10, pady=10)
        self.qty_entry = tk.Entry(self.window)
        self.qty_entry.grid(row=1, column=1, padx=10, pady=10)
        
        frm = tk.Frame(self.window)
        frm.grid(row=2, column=1, columnspan=4, pady=10)
        self.add_button = tk.Button(frm, text="ADD", command=self.add_medicine)
        self.add_button.grid(row=0, column=0, padx=10, pady=10)

        self.update_button = tk.Button(frm, text="Update", command=self.update_medicine)
        self.update_button.grid(row=0, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(frm, text="Delete", command=self.delete_medicine)
        self.delete_button.grid(row=0, column=2, padx=10, pady=10)

        self.display_button = tk.Button(frm, text="Display", command=self.display_medicines)
        self.display_button.grid(row=0, column=3, padx=10, pady=10)

        cols = ["Name", "Qty"]
        self.treeview = ttk.Treeview(self.window, column=cols, show='headings', height=10)
        self.treeview.grid(row=3, column=0, padx=10, pady=10, columnspan=5)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background="white", fieldbackground="white", foreground="black")
        style.configure('Treeview.Heading', background="PowderBlue")
        self.treeview.heading("Name", text="Medicine Name")
        self.treeview.heading("Qty", text="Quantity")

        self.conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
        self.cursor = self.conn.cursor()

    def add_medicine(self):
        name = self.name_entry.get()
        quantity = self.qty_entry.get()
        
        if name and quantity:
            self.medicines.append((name, quantity))
            messagebox.showinfo(title="Success", message="Inserted successfully.")
            self.name_entry.delete(0, tk.END)
            self.qty_entry.delete(0, tk.END)
    
            self.save_medicine_to_database(name, quantity)
            self.display_medicines()
        else:
            messagebox.showerror(title="Error", message="Please both fields.")

    def update_medicine(self):
        name = self.name_entry.get()
        quantity = self.qty_entry.get()
        
        if name and quantity:
            self.update_medicine_to_database(name, quantity)
            self.display_medicines()
        else:
            messagebox.showerror(title="Error", message="Please enter both fields.")

    def delete_medicine(self):
        name = self.name_entry.get()
        
        if name:
            #self.medicines.remove(name)
            messagebox.showinfo(title="Success", message="Deleted successfully.")
            self.name_entry.delete(0, tk.END)
            self.qty_entry.delete(0, tk.END)
    
            self.delete_medicine_to_database(name)
            self.display_medicines()
        else:
            messagebox.showerror(title="Error", message="Please enter name field.")

    def save_medicine_to_database(self, name, quantity):
        try:
            self.cursor.execute("Insert into medicines (name, quantity) values (?,?)", (name, quantity))
            self.conn.commit()

        except sql.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def update_medicine_to_database(self, name, quantity):
        try:

            self.cursor.execute("UPDATE medicines SET quantity=? WHERE name = ?)", (quantity, name))
            self.conn.commit()

        except sql.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def delete_medicine_to_database(self, name):
        try:
            self.cursor.execute("DELETE medicines WHERE name =?", (name))
            self.conn.commit()

        except sql.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def display_medicines(self):
        try:
            self.treeview.delete(*self.treeview.get_children())
            self.cursor.execute("SELECT name, quantity FROM medicines")
            medicines = self.cursor.fetchall()

            for medicine in medicines:
                self.treeview.insert("", tk.END, values=medicine)
            
        except sql.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def run(self):
        self.window.geometry("600x400")
        self.window.mainloop()

phar_sys = PharmacyManagementSystems()
phar_sys.run()