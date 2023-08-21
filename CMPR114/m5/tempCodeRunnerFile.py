import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_task():
    tasks=[]
    tasks.append(task.get())
    print(tasks)
    for i in tasks:
        print(i)
        lbox.insert(tk.END, i)

def clear_task():
    selection = lbox.curselection()
    for index in selection[::-1]:
        lbox.delete(index)

def exit():
    win.quit()
    win.destroy()

win = tk.Tk()
win.title('Task List')
win.geometry("760x300")

# Input
lbltask = tk.Label(win, text = "Add Task: ", font="Arial 10 bold", width=12, fg="#2E86C1")
lbltask.grid(column=0, row=0) #Label widge
task = tk.StringVar() #Manage the Entry widget
txttask = tk.Entry(win, width=50, textvariable=task)
txttask.grid(column=1,row=0, ipadx = 0, padx = 0, pady=3, sticky="w")
btnadd = tk.Button(win, text="Add Task", command=add_task, width=12)
btnadd.grid(column=2, row=0, padx=10)
btnclear = tk.Button(win, text="Clear Task", command=clear_task, width=12)
btnclear.grid(column=3, row=0, padx=10)
btnexit = tk.Button(win, text="Exit", command=quit, width=12)
btnexit.grid(column=4, row=0, padx=10)
txttask.focus_set()

# Listbox
lbllist = tk.Label(win, text = "Task List: ", font="Arial 10 bold", width=12, fg="#2E86C1")
lbllist.grid(column=0, row=2, sticky="ne", pady=20) #Label widge

lbox = tk.Listbox(win, width=50, selectmode="multiple", yscrollcommand="Yes")
lbox.grid(column=1, row=2, pady=20)

win.mainloop()