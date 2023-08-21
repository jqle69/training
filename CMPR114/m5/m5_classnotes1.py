import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox
#import sqlserver as ss

def delete_data():
    id = txtid.get()

    conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
    crs = conn.cursor()
    crs.execute("DELETE FROM customers WHERE id=?", (id))
    conn.commit()
    conn.close

    messagebox.showinfo(title="Transaction Completed", message="Delete record successful.")
    txtid.delete(0, tk.END)
    txtln.delete(0, tk.END)
    txtfn.delete(0, tk.END)
    txtage.delete(0, tk.END)
    txtcity.delete(0, tk.END)
    txtstate.delete(0, tk.END)
    txtzip.delete(0, tk.END)
    txtid.focus_set()

def update_data():
    id = txtid.get()
    last_name = txtln.get()
    first_name = txtfn.get()
    age = txtage.get()
    city = txtcity.get()
    state = txtstate.get()
    zip = txtzip.get()

    conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
    crs = conn.cursor()
    crs.execute("UPDATE customers SET last_name=?, first_name=?, age=?, city=?, state=?, zipcode=? WHERE id=?", (last_name, first_name, age, city, state, zip, id))
    conn.commit()
    conn.close
    messagebox.showinfo(title="Transaction Completed", message="Update successful.")
    txtid.delete(0, tk.END)
    txtln.delete(0, tk.END)
    txtfn.delete(0, tk.END)
    txtage.delete(0, tk.END)
    txtcity.delete(0, tk.END)
    txtstate.delete(0, tk.END)
    txtzip.delete(0, tk.END)
    txtid.focus_set()

def insert_data():

    #id = txtid.get()
    last_name = txtln.get()
    first_name = txtfn.get()
    age = txtage.get()
    city = txtcity.get()
    state = txtstate.get()
    zip = txtzip.get()

    #open connection
    conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
    crs = conn.cursor()
    crs.execute("INSERT INTO customers (last_name, first_name, age, city, state, zipcode) VALUES(?,?,?,?,?,?)", (last_name, first_name, age, city, state, zip))

    conn.commit()   #Commit transaction
    conn.close()    #Close connection
    messagebox.showinfo(title="Transaction Completed", message="Update successful.")

    txtid.delete(0, tk.END)
    txtln.delete(0, tk.END)
    txtfn.delete(0, tk.END)
    txtage.delete(0, tk.END)
    txtcity.delete(0, tk.END)
    txtstate.delete(0, tk.END)
    txtzip.delete(0, tk.END)
    txtid.focus_set()

def fetch_data():
    conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
    crs = conn.cursor()
    crs.execute("SELECT * FROM customers")
    data = crs.fetchall()

    for row in data:
        print(row)

    conn.close()

def fetch_joindata1():
    conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
    crs = conn.cursor()
    crs.execute("SELECT * FROM customers c INNER JOIN orders o ON c.id = o.id")
    data = crs.fetchall()

    for row in data:
        print(row)

    conn.close()

def fetch_joindata1():
    conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
    crs = conn.cursor()
    crs.execute("SELECT * FROM customers c LEFT JOIN orders o ON c.id = o.id LEFT JOIN representative r ON c.id = r.id")
    data = crs.fetchall()

    for row in data:
        print(row)

    conn.close()


win = tk.Tk()
win.title('Customer Registry')
win.geometry("280x290")

lblid = tk.Label(win, text="ID")
lblid.pack()
txtid = tk.Entry(win)
txtid.pack()
lblln = tk.Label(win, text="Last Name")
lblln.pack()
txtln = tk.Entry(win)
txtln.pack()
lblfn = tk.Label(win, text="First Name")
lblfn.pack()
txtfn = tk.Entry(win)
txtfn.pack()
lblage = tk.Label(win, text="Age")
lblage.pack()
txtage = tk.Entry(win)
txtage.pack()

lblcity = tk.Label(win, text="City")
lblcity.pack()
txtcity = tk.Entry(win)
txtcity.pack()

lblstate = tk.Label(win, text="State")
lblstate.pack()
txtstate = tk.Entry(win)
txtstate.pack()

lblzip = tk.Label(win, text="Zip")
lblzip.pack()
txtzip = tk.Entry(win)
txtzip.pack()

frm = tk.Frame(win, )
btnfetch = tk.Button(win, text="fetch", command=fetch_data)
btnfetch.pack()
btnsave = tk.Button(win, text="insert", command=insert_data)
btnsave.pack()
btnupdate = tk.Button(win, text="update", command=update_data)
btnupdate.pack()
btdelete = tk.Button(win, text="delete", command=delete_data)
btdelete.pack()

win.mainloop()

