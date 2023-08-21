import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox
from tkinter import PhotoImage
from datetime import datetime 

def submit_form():

    last_name = txtln.get()
    first_name = txtfn.get()
    age_val = age_var.get()
    education_val = education_var.get()
    ethnicity_val = ethnicity_var.get()
    party_val = party_var.get()
    income_val = str(income_var.get())

    if age_val == 1:
        age_range = "1 to 24"
    elif age_val == 2:
        age_range = "25-50"
    else:
        age_range = "50+"

    if education_val == 1:
        education = "High School"
    elif education_val == 2:
        education = "College"
    else:
        education = "Graduate School"

    if ethnicity_val == 1:
        ethnicity = "Caucasian"
    elif ethnicity_val == 2:
        ethnicity = "Asian"
    else:
        ethnicity = "Other"

    if party_val == 1:
        party = "Republican"
    elif party_val == 2:
        party = "Democrat"
    else:
        party = "Independent"

    if income_val == 1:
        income_range = "0-20K"
    elif income_val == 2:
        income_range = "20K-100K"
    else:
        income_range = "100K+"

    def has_numbers(inputString):
        return any(char.isdigit() for char in inputString)

    def save_to_file(content):
        try:
            with open("C:\\Users\\17147\\Desktop\\CMPR114\\m8\\demographics.txt", "a") as file:
                file.write(content)
                file.close
        except Exception as e:
            messagebox.showerror(title="Missing Location", message="Please specify file location.")


    # def save_to_db():
    #     try:
    #         #open connection
    #         conn = sql.connect("C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db")
    #         crs = conn.cursor()
    #         crs.execute("INSERT INTO customers (last_name, first_name, age, city, state, zipcode) VALUES(?,?,?,?,?,?)", (last_name, first_name, age, city, state, zip))

    #         conn.commit()   #Commit transaction
    #         conn.close()    #Close connection
    #     except sql.Error as e:
    #         messagebox.showerror(title="Error", message=f"Database Error: {e}")


    if has_numbers(last_name) or has_numbers(first_name):
        messagebox.showerror(title="Input Error", message="Please enter valid first and last name")
    else:
        content = (f"""Timestamp: {datetime.now()} \nName: {first_name} {last_name}\nAge Range: {age_range}\nEducation Level: {education} \nEthnicity: {ethnicity} \nPolitical Affiliation: {party} \nIncome Level: {income_range}\n""")
        
        print(content)
        save_to_file(content)

    txtln.delete(0, tk.END)
    txtfn.delete(0, tk.END)
    txtln.focus_set()

def quit():
    win.quit()
    win.destroy()

def cleartext():
    txtfn.delete(0, tk.END)
    txtln.delete(0, tk.END)
    rbLT25.select()
    rb25To50.deselect()
    rbGT50.deselect()
    rbCaucasian.select()
    rbAsian.deselect()
    rbOther.deselect()
    rbRepublican.select()
    rbDemocrat.deselect()
    rbIndependent.deselect()
    rbHS.select()
    rbCollege.deselect()
    rbGraduate.deselect()
    rbLT20.select()
    rb20To100.deselect()
    rbGT100.deselect()
    txtln.focus_set()

#Set up window form
win = tk.Tk()
win.title('Student Demographics')
win.geometry("620x305")

#Instructions
lblInstruction = tk.Label(win, text = "Please enter required information below.", font="Arial 10 bold", anchor="e", fg="black")
lblInstruction.grid(row=0, column=0, ipadx=3, ipady=10, columnspan=5) #Label widge

#First and Last Name
lblln = tk.Label(win, text = "Last Name: ", font="Arial 10 bold", anchor="e", fg="#2E86C1")
lblln.grid(row=1, column=0, padx=10, pady=10, sticky="e") #Label widge
ln = tk.StringVar() #Manage the Entry widget
txtln = tk.Entry(win, width=20, textvariable=ln)
txtln.grid(row=1, column=1, ipadx = 0, padx = 0, pady=10, sticky="w")

lblfn = tk.Label(win, text = "First Name: ", font="Arial 10 bold", width=20, anchor="e", fg="#2E86C1")
lblfn.grid(row=1, column=2, padx=1, pady=10, sticky="e")
fn = tk.StringVar() #Manage the Entry widget
txtfn = tk.Entry(win, width=20, textvariable=fn)
txtfn.grid(row=1, column=3, ipadx=0, padx=0, pady=10, sticky="w")

#Age Classification
lblAge = tk.Label(win, text = "Age: ", font="Arial 10 bold", anchor="e", fg="#2E86C1")
lblAge.grid(row=2, column=0, padx=10, sticky="e")
frm1 = tk.Frame(win)
frm1.grid(row=2, column=1, padx=0, pady=0, columnspan=5)
age_var= tk.IntVar(frm1)
rbLT25 = tk.Radiobutton(frm1, text="<25", value=1, width=14, variable=age_var, anchor="w")
rbLT25.grid(row=0, column=1, padx=0, pady=0)
rb25To50 = tk.Radiobutton(frm1, text="25-50", value=2, width=14, variable=age_var, anchor="w")
rb25To50.grid(row=0, column=2, padx=0, pady=0)
rbGT50 = tk.Radiobutton(frm1, text="50+>", value=3, width=14, variable=age_var, anchor="w")
rbGT50.grid(row=0, column=3, padx=0, pady=0)

#Education Classification
lblEducation = tk.Label(win, text = "Education Level: ", font="Arial 10 bold", anchor="e", fg="#2E86C1")
lblEducation.grid(row=3, column=0, padx=10, sticky="e")
frm2 = tk.Frame(win)
frm2.grid(row=3, column=1, padx=0, pady=0, columnspan=5)
education_var = tk.IntVar(frm2)
rbHS = tk.Radiobutton(frm2, text="High School", value=1, width=14, variable=education_var, anchor="w")
rbHS.grid(row=0, column=0, padx=0, pady=0)
rbCollege = tk.Radiobutton(frm2, text="College", value=2, width=14, variable=education_var, anchor="w")
rbCollege.grid(row=0, column=1, padx=0, pady=0)
rbGraduate = tk.Radiobutton(frm2, text="Graduate School", value=3, width=14, variable=education_var, anchor="w")
rbGraduate.grid(row=0, column=2, padx=0, pady=0)


#Ethnicity Classification
lblEthnicity = tk.Label(win, text = "Ethnicity: ", font="Arial 10 bold", anchor="e", fg="#2E86C1")
lblEthnicity.grid(row=4, column=0, padx=10, sticky="e")
frm3 = tk.Frame(win)
frm3.grid(row=4, column=1, padx=0, pady=0, columnspan=5)
ethnicity_var = tk.IntVar(frm3)
rbCaucasian = tk.Radiobutton(frm3, text="Caucasian", value=1, width=14, variable=ethnicity_var, anchor="w")
rbCaucasian.grid(row=0, column=0, padx=0, pady=0)
rbAsian = tk.Radiobutton(frm3, text="Asian", value=2, width=14, variable=ethnicity_var, anchor="w")
rbAsian.grid(row=0, column=1, padx=0, pady=0)
rbOther = tk.Radiobutton(frm3, text="Other", value=3, width=14, variable=ethnicity_var, anchor="w")
rbOther.grid(row=0, column=2, padx=0, pady=0)

#Political Classification
lblParty = tk.Label(win, text = "Political Affiliation: ", font="Arial 10 bold", anchor="e", fg="#2E86C1")
lblParty.grid(row=5, column=0, padx=10, sticky="e") #Label widge
frm4 = tk.Frame(win)
frm4.grid(row=5, column=1, padx=0, pady=0, columnspan=5)
party_var = tk.IntVar(frm4)
rbRepublican = tk.Radiobutton(frm4, text="Republican", value=1, width=14, variable=party_var, anchor="w")
rbRepublican.grid(row=0, column=0, padx=0, pady=0)
rbDemocrat = tk.Radiobutton(frm4, text="Democrat", value=2, width=14, variable=party_var, anchor="w")
rbDemocrat.grid(row=0, column=1, padx=0, pady=0)
rbIndependent = tk.Radiobutton(frm4, text="Independent", value=3, width=14, variable=party_var, anchor="w")
rbIndependent.grid(row=0, column=2, padx=0, pady=0)

#Income Classification
lblIncome = tk.Label(win, text = "Income Level: ", font="Arial 10 bold", anchor="e", fg="#2E86C1")
lblIncome.grid(row=6, column=0, padx=10, sticky="e")
frm5 = tk.Frame(win)
frm5.grid(row=6, column=1, padx=0, pady=0, columnspan=5)
income_var = tk.IntVar(frm5)
rbLT20 = tk.Radiobutton(frm5, text="<20", value=1, width=14, variable=income_var, anchor="w")
rbLT20.grid(row=0, column=0, padx=0, pady=0)
rb20To100 = tk.Radiobutton(frm5, text="20-100", value=2, width=14, variable=income_var, anchor="w")
rb20To100.grid(row=0, column=1, padx=0, pady=0)
rbGT100 = tk.Radiobutton(frm5, text="100+>", value=3, width=14, variable=income_var, anchor="w")
rbGT100.grid(row=0, column=2, padx=0, pady=0)

#Create buttons on windows form
frm6 = tk.Frame(win)
frm6.grid(row=7, column=0, padx = 0, pady=10, columnspan=5, sticky="w")
btnSubmit = tk.Button(frm6, text="Submit", command=submit_form, width=12)
btnSubmit.grid(row=0, column=1, ipadx=10, padx=20, pady=20)
btnQuit = tk.Button(frm6, text="Quit", command=quit, width=12)
btnQuit.grid(row=0, column=2, ipadx=10, padx=20, pady=20)
btnClear = tk.Button(frm6, text="Clear", command=cleartext, width=12)
btnClear.grid(row=0, column=3, ipadx=10, padx=20, pady=20)

win.mainloop()

