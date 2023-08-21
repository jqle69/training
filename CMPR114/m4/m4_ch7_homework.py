#########################################
# Project 1
#########################################
def get_score():
    #Create empty list
    test_scores = []

    again = 'y'
    while again == 'y':
        value = float(input("Enter a test score: "))
        test_scores.append(value)

        print("Do you want to add another score?")
        again = input("y = yes, anything else = no: ")

    return test_scores

def get_total(value_list):
    total = 0.0

    for num in value_list:
        total += num

    return total

def main():
    scores = get_score()

    totalval = get_total(scores)

    #Display results in console
    msg = f"Total score is {totalval}\n"
    print(msg)

    #Write to file
    file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m4\\Results.txt", "w")
    file.write(msg)
    file.close

if __name__ == "__main__":
    main()

#########################################
# Project 2
#########################################
#Initiliaze list and variable
listval=[]
totalval = 0
MAX_RANGE = 5
for i in range(1,MAX_RANGE+1):
    val = int(input(f"Enter value #{i}: "))
    listval.append(val)
    totalval += val

avgval = totalval / MAX_RANGE
minval = min(listval)
maxval = max(listval)

print(f"Min value is {minval}")
print(f"Max value is {maxval}")
print(f"Avg value is {avgval}")
print(f"Total value is {totalval}")

#########################################
# Project 3
#########################################
#Open boys name file
def read_boy_names():
    with open("C:\\Users\\17147\\Desktop\\CMPR114\\m4\\boysname.txt", "r") as file:
        names = [line.rstrip("\n") for line in file]

    return names

#Open girls name file
def read_girl_names():
    with open("C:\\Users\\17147\\Desktop\\CMPR114\\m4\\girlsname.txt", "r") as file:
        names = [line.rstrip("\n") for line in file]

    return names

def main():
    #Get list of boys and girls names
    boys = read_boy_names()
    girls = read_girl_names()

    #Initiliaze variable
    loopval = "y"
    checkboy = False
    checkgirl = False

    #Loop thru prompting user to check entered name
    while loopval == "y":
        checkname = input("Enter name to check against popular boy/girl list: ")

        #Check if name exists in boys list
        if checkname in boys:
            checkboy = True

        #Check if name exists in girls list
        if checkname in girls:
            checkgirl = True

        if checkboy == True or checkgirl == True:
            print(f"The name '{checkname}' is part of the popular list.")
        else:
            print(f"The name '{checkname}' is not part of the popular list.")

        loopval = input("Try again (Y or N)?  ").lower()

        #Result check flag
        if loopval == "y":
            checkboy = False
            checkgirl = False

if __name__ == "__main__":
    main()

#########################################
# Project 4
#########################################
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def main ():
    def cleartext():
        global msg
        txtname.delete(0, tk.END)
        txtID.delete(0, tk.END)
        rbGender.deselect()
        txtscore1.delete(0, tk.END)
        txtscore2.delete(0, tk.END)
        txtscore3.delete(0, tk.END)
        
        displaymsg=""
        lblDisplay.config(text=displaymsg)
        lblDisplay.grid(column=0, row=7, padx=5, pady=12, columnspan=2) 

    def quit():
        messagebox.showinfo(title="Exit Program", message="Bye!")
        win.quit()
        win.destroy()
                            
    def calculate():
        #Calculate total and average
        fname = name.get()
        studentid = strID.get()
        gender_selected = radio_selected.get()
        val1 = score1.get()
        val2 = score2.get()
        val3 = score3.get()
        
        total = int(val1) + int(val2) + int(val3)
        avg = total/3

        displaymsg = f"The average score is {avg:,.2f}."
        lblDisplay.config(text =displaymsg, fg="#CD5C5C")
        #lblDisplay.grid(column=0, row=7, ipadx= 5, pady=12, columnspan=2)        

        #write to file
        studentmsg = f"Student Name:  {fname}\nStudent ID:  {studentid}\nSex:  {gender_selected}\n"
        resultmsg = f"\nThe three scores are {val1}, {val2}, {val3}.\nThe total is {total}.\nThe average is {avg:,.2f}."
        file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m4\\project4.txt", "w")
        file.write(studentmsg+resultmsg)
        file.close

        messagebox.showinfo("Submitted successfully", message=studentmsg+resultmsg)

    #Initiliaze windows interface
    win = tk.Tk()                   #Create window interface
    win.geometry("380x300")         #Set window size (width by height)
    win.title("Score Calculator")   #Label title for window

    # Instruction Label
    frm1 = tk.Frame(win)
    frm1.grid(column=0, row=0, ipadx=0, padx=0, pady=7, columnspan=2) #Label widge
    lblheader = tk.Label(frm1, text = "Please enter all fields to calculate score.", font="Arial 10 bold", fg="#424949", anchor="w")
    lblheader.grid()

    # Student Input
    lblname  = tk.Label(win, text = "Enter Student Name: ", font="Arial 10 bold", width=20, anchor="e", fg="#2E86C1")
    lblname.grid(column=0, row=1, ipadx = 0, padx = 0, pady=3) #Label widge
    name = tk.StringVar() #Manage the Entry widget
    txtname = tk.Entry(win, width=30, textvariable=name)
    txtname.grid(column=1,row=1, ipadx = 0, padx = 0, pady=3)
    txtname.focus_set()

    lblID = tk.Label(win, text = "Enter Student ID: ", font="Arial 10 bold", width=20, anchor="e", fg="#2E86C1")
    lblID.grid(column=0, row=2, ipadx = 0, padx = 0, pady=3) #Label widge
    strID = tk.StringVar() #Manage the Entry widget
    txtID = tk.Entry(win, width=30, textvariable=strID)
    txtID.grid(column=1,row=2, ipadx = 0, padx = 0, pady=3)

    lblGender = tk.Label(win, text = "Gender: ", font="Arial 10 bold", width=20, anchor="e", fg="#2E86C1")
    lblGender.grid(column=0, row=3) #Label widge
    frm2 = tk.Frame()
    frm2.grid(column=1, row=3, ipadx = 0, padx = 0, pady=3, columnspan=2)
    gender = ["Male", "Female"]
    radio_selected = tk.StringVar()
    for index in range(len(gender)):
        rbGender = tk.Radiobutton(frm2, 
                                  text=gender[index],   #add text to radio buttons
                                  value=gender[index], 
                                  variable=radio_selected,
                                  anchor="w"
                                  )          #assign each radiobutton a different value
        rbGender.grid(column=index, row=0, ipadx = 5, padx = 0, pady=3)

    # Score Input
    lblscore1  = tk.Label(win, text = "Enter Number 1: ", font="Arial 10 bold", width=20, anchor="e", fg="#2E86C1")
    lblscore1.grid(column=0, row=4) #Label widge
    score1 = tk.StringVar() #Manage the Entry widget
    txtscore1 = tk.Entry(win, width=30, textvariable=score1)
    txtscore1.grid(column=1, row=4, ipadx = 0, padx = 0, pady=3)

    lblscore2 = tk.Label(win, text = "Enter Number 2: ", font="Arial 10 bold", width=20, anchor="e", fg="#2E86C1")
    lblscore2.grid(column=0, row=5, ipadx = 0, padx = 0, pady=3) #Label widge
    score2 = tk.StringVar() #Manage the Entry widget
    txtscore2 = tk.Entry(win, width=30, textvariable=score2)
    txtscore2.grid(column=1, row=5, ipadx = 0, padx = 0, pady=3)

    lblscore3 = tk.Label(win, text = "Enter Number 3: ", font="Arial 10 bold", width=20, anchor="e", fg="#2E86C1")
    lblscore3.grid(column=0, row=6, ipadx = 0, padx = 0, pady=3) #Label widge
    score3 = tk.StringVar() #Manage the Entry widget
    txtscore3 = tk.Entry(win, width=30, textvariable=score3)
    txtscore3.grid(column=1, row=6, ipadx = 0, padx = 0, pady=3)

    lblDisplay = tk.Label(win, text="", font="Arial 10 bold", justify="center")
    lblDisplay.grid(column=0, row=7, padx=5, pady=12, columnspan=2)  

    btnfetch = tk.Button(win, text="Calculate", command=fetch_data, width=15)
    btnfetch.grid(column=0, row=8, ipadx = 0, padx = 0)
    frm3 = tk.Frame(win)
    frm3.grid(column=1, row=8, ipadx = 0, padx = 10)
    btnClear = tk.Button(frm3, text="Clear", command=cleartext, width=8)
    btnClear.grid(column=0, row=0)
    btnQuit = tk.Button(frm3, text="Quit", command=quit, width=8)
    btnQuit.grid(column=1, row=0)
    
    win.mainloop()

if __name__ == "__main__":
    main()
