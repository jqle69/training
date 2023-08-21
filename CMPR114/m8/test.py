import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox
from tkinter import PhotoImage
from datetime import datetime 

win = tk.Tk()
win.title('Student Demographics')
win.geometry("620x305")


jpg = PhotoImage(file="C:\\Users\\17147\\Desktop\\CMPR114\\m8\\wolverine25.png")
lblImage = tk.Label(win, image=jpg)
lblImage.grid(row=0, column=0, padx=10)

win.mainloop()

