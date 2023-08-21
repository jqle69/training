import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox

def login():

    username = txtusername.get()
    password = txtpassword.get()
    
    #open connection
    conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
    crs = conn.cursor()

    crs.execute("SELECT * FROM login where username=? and password=?", (username, password))
    rows = crs.fetchone()
    if rows:
        messagebox.showinfo(title="Login", message="Login Successful")
        show_customer_form()
    else:
        messagebox.showerror(title="Login Error", message="Invalid username or password.")
        txtusername.delete(0, tk.END)
        txtpassword.delete(0, tk.END)
        txtusername.focus_set()

def show_customer_form():
    def save_entry():
        last_name = txtln.get()
        first_name = txtfn.get()
        gender = gender_selected.get()
        
        #open connection
        conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
        crs = conn.cursor()
        crs.execute("INSERT INTO customers (last_name, first_name, gender) VALUES(?,?,?)", (last_name, first_name, gender))

        conn.commit()   #Commit transaction
        conn.close()    #Close connection
        messagebox.showinfo(title="DB Action", message="Insert successful.")

        txtln.delete(0, tk.END)
        txtfn.delete(0, tk.END)
        rbMale.select()
        gender_selected.set("Male")
        txtln.focus_set()

    def exit_entry():
        entry_win.withdraw()
        txtusername.delete(0, tk.END)
        txtpassword.delete(0, tk.END)
        login_win.deiconify()

    def clear_entry():
        txtln.delete(0, tk.END)
        txtfn.delete(0, tk.END)
        rbMale.select()
        gender_selected.set("Male")

    #unload login window
    login_win.withdraw()

    #create entry form
    entry_win = tk.Tk()
    entry_win.title("Customer Form")
    entry_win.geometry("300x300")

    #setup labels, textboxes, and ribbon
    lblln = tk.Label(entry_win, text = "Last Name: ", font="Arial 10 bold", width=12, anchor="e", fg="#2E86C1")
    lblln.pack()
    txtln = tk.Entry(entry_win, width=30)
    txtln.pack()
    lblfn = tk.Label(entry_win, text = "First Name: ", font="Arial 10 bold", width=12, anchor="e", fg="#2E86C1")
    lblfn.pack()
    txtfn = tk.Entry(entry_win, width=30)
    txtfn.pack()

    lblgender = tk.Label(entry_win, text = "Gender: ", font="Arial 10 bold", width=12, fg="#2E86C1")
    lblgender.pack()
    gender_selected = tk.StringVar(entry_win)
    rbMale = tk.Radiobutton(entry_win, text="Male", value="Male", variable=gender_selected)
    rbMale.pack(anchor="w", padx=90)
    rbFemale = tk.Radiobutton(entry_win, text="Female", value="Female", variable=gender_selected)
    rbFemale.pack(anchor="w", padx=90)
    gender_selected.set("Male")     #setting default to Male

    btnsave = tk.Button(entry_win, text="Save", command=save_entry, width=12)
    btnsave.pack()
    btnexit = tk.Button(entry_win, text="Exit", command=exit_entry, width=12)
    btnexit.pack()
    btnclear = tk.Button(entry_win, text="Clear", command=clear_entry, width=12)
    btnclear.pack()

def quit():
    login_win.quit()
    login_win.destroy()
    
#Set up window form
login_win = tk.Tk()
login_win.title('Login')
login_win.geometry("200x180")

# Input
lblusername = tk.Label(login_win, text = "User Name: ", font="Arial 10 bold", width=12, fg="#2E86C1")
lblusername.pack()
txtusername = tk.Entry(login_win, width=30)
txtusername.pack()


lblpassword = tk.Label(login_win, text = "Password: ", font="Arial 10 bold", width=12, fg="#2E86C1")
lblpassword.pack()
txtpassword = tk.Entry(login_win, width=30, show="*", )
txtpassword.pack()

lblspace = tk.Label(login_win, text = " ", font="Arial 10 bold", width=12, fg="#2E86C1")
lblspace.pack()

# Create buttons on windows form
btnlogin = tk.Button(login_win, text="Login", command=login, width=12, )
btnlogin.pack()
btnquit = tk.Button(login_win, text="Exit", command=quit, width=12)
btnquit.pack()

login_win.mainloop()

