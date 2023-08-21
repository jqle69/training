###################################################
#Project 1-1
###################################################
file = open("things.txt", "a")
file.write("Elephant")
file.write("\nApple")
file.write("\nCanada")
file.close()

###################################################
#Project 1-2
###################################################
file = open("things.txt", "r")
content = file.read()
print(content)
file.close()

###################################################
#Project 1-3
###################################################
file = open("number_list.txt", "w")
for i in range(1,101):
    file.write(f"{i}\n")

file.close()

###################################################
#Project 2
###################################################
import tkinter as tk
from tkinter import *
from tkinter import filedialog

def browse_button():
    global fullpath
    fullpath = filedialog.askopenfilename()
    file = open(fullpath, "+r")
    content = file.readlines()
    # print(content)
    total = 0
    for line in content:
        total += int(line)

    file.write(f'Total is {total}')
    file.close()

    return total

def display_results():
    file = open(fullpath, "r")
    content = file.read()
    print(content)

win = tk.Tk()
win.geometry("300x100")
win.title("Select File")


btnbrowse = tk.Button(win, text="Browse", command=browse_button, font={"Arial", 14})
btnbrowse.pack(padx=10)

tk.mainloop()

display_results()




