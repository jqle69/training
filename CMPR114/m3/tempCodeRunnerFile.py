import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

   

entry_win =tk.Tk()



def display_login(): 
    def login_user():
        if txtUserName == "jole" and txtPassword == "pwd123":
            messagebox.showinfo(title="Invalid Login", message="Incorrect username or password.")
            entry_win.deiconify()
            login_win.withdraw()

        else:
            messagebox.showinfo("Username or Password is not correct.  Try again")
            txtUserName.delete(0, tk.END)
            txtPassword.delete(0, tk.END)
            txtUserName.focus_set()
            
    login_win = tk.Tk()    
    login_win.title("User Login")

    lblUserName = tk.Label(login_win, text="Username: ", font="Arial 10 bold")
    lblUserName.pack()
    txtUserName = tk.Entry(login_win, width=15)
    txtUserName.pack()

    lblPassword = tk.Label(login_win, text="Password: ", font="Arial 10 bold")
    lblPassword.pack()
    txtPassword = tk.Entry(login_win, width=15, show="*")
    txtPassword.pack()

    btnSubmit = tk.Button(login_win, text="Login", command=login_user)
    btnSubmit.pack()

    login_win.mainloop()

display_login()