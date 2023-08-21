import tkinter as tk
from tkinter import ttk

def submit():
    name = txtname.get()
    age = txtage.get()
    address = txtaddress.get()
    city = txtcity.get()
    state = txtstate.get()
    zip = txtzip.get()

    tree.insert("", tk.END, values=(name, age, address, city, state, zip))
    txtname.delete(0, tk.END)
    txtage.delete(0, tk.END)
    txtaddress.delete(0, tk.END)
    txtcity.delete(0, tk.END)
    txtstate.delete(0, tk.END)
    txtzip.delete(0, tk.END)
    
win = tk.Tk()
win.title('Grid View Example')
win.geometry("600x480")

# Input
lblname = tk.Label(win, text = "Name: ", font="Arial 10 bold", width=12, anchor="e", fg="#2E86C1")
lblname.grid(column=0, row=0, sticky="e") #Label widge
txtname = tk.Entry(win, width=30)
txtname.grid(column=1,row=0, ipadx = 0, padx = 0, pady=3, sticky="w")

lblage  = tk.Label(win, text = "Age: ", font="Arial 10 bold", width=12, anchor="e", fg="#2E86C1")
lblage.grid(column=0, row=1, sticky="e") #Label widge
txtage = tk.Entry(win, width=30)
txtage.grid(column=1, row=1, ipadx = 0, padx = 0, pady=3, sticky="w")

lbladdress = tk.Label(win, text = "Address: ", font="Arial 10 bold", width=12, anchor="e", fg="#2E86C1")
lbladdress.grid(column=0, row=2, sticky="e") #Label widget
txtaddress = tk.Entry(win, width=30)
txtaddress.grid(column=1,row=2, ipadx = 0, padx = 0, pady=3, sticky="w")

lblcity = tk.Label(win, text = "City: ", font="Arial 10 bold", width=12, anchor="e", fg="#2E86C1")
lblcity.grid(column=0, row=3, sticky="e") #Label widge
txtcity = tk.Entry(win, width=30)
txtcity.grid(column=1, row=3, ipadx = 0, padx = 0, pady=3, sticky="w")

lblstate = tk.Label(win, text = "State: ", font="Arial 10 bold", width=12, anchor="e", fg="#2E86C1")
lblstate.grid(column=0, row=4, sticky="e") #Label widge
txtstate = tk.Entry(win, width=30)
txtstate.grid(column=1, row=4, ipadx = 0, padx = 0, pady=3, sticky="w")

lblzip = tk.Label(win, text = "Zip Code: ", font="Arial 10 bold", width=12, anchor="e", fg="#2E86C1")
lblzip.grid(column=0, row=5, sticky="e") #Label widge
txtzip = tk.Entry(win, width=30)
txtzip.grid(column=1, row=5, ipadx = 0, padx = 0, pady=3, sticky="w")

btnsubmit = tk.Button(win, text="Submit", command=submit, width=12)
btnsubmit.grid(column=1, row=6, padx=0, ipadx=0, pady= 15)

#Tree View
frm5 = tk.Frame(win, width=540)
frm5.grid(column=0, row=8, columnspan=3, padx=10, pady=10)

datacols = ("name", "age", "address", "city", "state", "zip")
tree = ttk.Treeview(frm5, column=datacols, show='headings', height=10, selectmode="extended")
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview", background="white", fieldbackground="white", foreground="black")
style.configure('Treeview.Heading', background="PowderBlue")
tree.column("#1", anchor=tk.CENTER, width=90)
tree.heading("name", text="Name")
tree.column("#2", anchor=tk.CENTER, width=50)
tree.heading("age", text="Age")
tree.column("#3", anchor=tk.CENTER, width=110)
tree.heading("address", text="Address")
tree.column("#4", anchor=tk.CENTER, width=110)
tree.heading("city", text="City")
tree.column("#5", anchor=tk.CENTER, width=110)
tree.heading("state", text="State")
tree.column("#6", anchor=tk.CENTER, width=100)
tree.heading("zip", text="Zip Code")
tree.grid(column=0, row=0, ipadx = 0, padx = 0, columnspan=2)

win.mainloop()

################################
#Exercise 3
################################
import sqlite3 as sql

cnn = "C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db"
conn = sql.connect(cnn)
crs = conn.cursor()
crs.execute("SELECT * FROM patients")
rows = crs.fetchall()
for row in rows:
    print(row)

crs.execute("SELECT * FROM prescriptions")
rows = crs.fetchall()
for row in rows:
    print(row)

crs.execute("SELECT * FROM doctors")
rows = crs.fetchall()
for row in rows:
    print(row)

conn.close()    #Close connection

################################
#Exercise 4
################################
import sqlite3 as sql

cnn = "C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db"
conn = sql.connect(cnn)
crs = conn.cursor()
crs.execute("SELECT * FROM patients p \
            INNER JOIN prescriptions pr ON p.patientid = pr.patientid \
            INNER JOIN doctors d ON pr.doctorid = d.doctorid")
rows = crs.fetchall()
for row in rows:
    print(row)

conn.close()    #Close connection