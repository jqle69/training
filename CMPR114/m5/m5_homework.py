import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import SQLLiteDAL as dal

def insert_data():
    msg_success = "Record was inserted."
    msg_error = "Insert Error. Please check values and try again."

    #patient insert
    if notebook.index("current") == 0:
        p_name = txtPName.get()
        p_birthdate = txtPBirthDate.get()
        p_doctorid = txtDoctorId.get()
        
        if p_name=='' and p_birthdate=='' and p_doctorid=='':
            messagebox.showerror(title="Task Status.", message="Please enter data for patient.")
        else:
            checkval = dal.PatientDML.insert_patient(p_name, p_birthdate, p_doctorid)
            if checkval > 0:
                messagebox.showinfo(title="Task Status", message=msg_success)
            else:
                messagebox.showerror(title="Task Status", message=msg_error)

            refresh_cbpatient()
        
        clear_all()


    #doctor insert
    elif notebook.index("current") == 1:
        d_name = txtDName.get()
        d_birthdate = txtDBirthDate.get()
        d_license = txtLicense.get()
        
        if d_name=='' and d_birthdate=='' and d_license=='':
            messagebox.showerror(title="Task Status.", message="Please enter data for doctor.")
        else:
            checkval = dal.DoctorDML.insert_doctor(d_name, d_birthdate, d_license)
            if checkval > 0:
                messagebox.showinfo(title="Task Status", message=msg_success)
            else:
                messagebox.showerror(title="Task Status", message=msg_error)

            refresh_cbdoctor()

        clear_all()
        
    #prescription insert
    elif notebook.index("current") == 2:
        patientid = cbPID1.get().split("-")[0]
        doctorid = cbDID1.get().split("-")[0]
        presciptiondate = txtPresciptionDate.get()
        drugcode = txtDrugCode.get()
        
        checkval = dal.PrescriptionDML.insert_prescription(patientid, doctorid, presciptiondate, drugcode)
        if checkval > 0:
            messagebox.showinfo(title="Task Status", message=msg_success)
        else:
            messagebox.showerror(title="Task Status", message=msg_error)

        clear_all()

def update_data():
    msg_success = "Record was updated."
    msg_error = "Update Error. Please check values and try again."

    #patient update
    if notebook.index("current") == 0:
        p_id = txtPID.get()
        p_name = txtPName.get()
        p_birthdate = txtPBirthDate.get()
        p_doctorid = txtDoctorId.get()
        
        checkval = dal.PatientDML.update_patient(p_id, p_name, p_birthdate, p_doctorid)
        if checkval > 0:
            messagebox.showinfo(title="Task Status", message=msg_success)
        else:
            messagebox.showerror(title="Task Status", message=msg_error)

        clear_all()
        refresh_cbpatient()

    #doctor insert
    elif notebook.index("current") == 1:
        d_id = txtDID.get()
        d_name = txtDName.get()
        d_birthdate = txtDBirthDate.get()
        d_license = txtLicense.get()
        
        checkval = dal.DoctorDML.update_doctor(d_id, d_name, d_birthdate, d_license)
        if checkval > 0:
            messagebox.showinfo(title="Task Status", message=msg_success)
        else:
            messagebox.showerror(title="Task Status", message=msg_error)

        clear_all()
        refresh_cbdoctor()

    #prescription insert
    elif notebook.index("current") == 2:
        prescriptionid = txtPRID.get()
        patientid = cbPID1.get().split("-")[0]
        doctorid = cbDID1.get().split("-")[0]
        presciptiondate = txtPresciptionDate.get()
        drugcode = txtDrugCode.get()
        
        checkval = dal.PrescriptionDML.update_prescription(prescriptionid, patientid, doctorid, presciptiondate, drugcode)
        if checkval > 0:
            messagebox.showinfo(title="Task Status", message=msg_success)
        else:
            messagebox.showerror(title="Task Status", message=msg_error)

        clear_all()

def delete_data():
    #patient delete
    msg_success = "Record was deleted."
    msg_error = "Delete Error. Please check values and try again."

    if notebook.index("current") == 0:
        pid = txtPID.get()

        if pid == '':
            messagebox.showerror(title="Task Status", message="Please enter Patient ID to delete.")
        elif dal.PatientDML.check_patientexists(pid):
            messagebox.showerror(title="Task Status", message="Unable to delete.  Patient ID is being referenced in Prescriptions table.")
        else:
            checkval = dal.PatientDML.delete_patient(pid )
            if checkval > 0:
                messagebox.showinfo(title="Task Status", message=msg_success)
            else:
                messagebox.showerror(title="Task Error", message=msg_error)

            refresh_cbpatient()

        clear_all()

    #doctor delete
    elif notebook.index("current") == 1:
        did = txtDID.get()
        
        if did == '':
            messagebox.showerror(title="Task Status", message="Please provide Doctor ID to delete.")
        elif dal.DoctorDML.check_doctorexists(did):
            messagebox.showerror(title="Task Status", message="Unable to delete.  Doctor ID is being referenced in Prescriptions table.")
        else:  
            checkval = dal.DoctorDML.delete_doctor(did)
            if checkval > 0:
                messagebox.showinfo(title="Task Status", message=msg_success)
            else:
                messagebox.showerror(title="Task Error", message=msg_error)

            refresh_cbdoctor()

        clear_all()
        
    #prescription delete
    elif notebook.index("current") == 2:
        prid = txtPRID.get()
        if prid == '':
            messagebox.showerror(title="Task Status", message="Please provide Prescription ID to delete.")
        else:
            checkval = dal.PrescriptionDML.delete_prescription(prid)
            if checkval > 0:
                messagebox.showinfo(title="Task Status", message=msg_success)
            else:
                messagebox.showerror(title="Task Error", message=msg_error)

        clear_all()

def refresh_cbpatient():
    cbPID1.configure(values=())
    cbPID1["values"] = dal.PatientDML.get_patientlist()
    cbPID1.set("")

def refresh_cbdoctor():
    cbDID1.configure(values=())
    cbDID1["values"] = dal.DoctorDML.get_doctorlist()
    cbDID1.set("")

def clear_all():
    txtPID.delete(0, tk.END)
    txtPName.delete(0, tk.END)
    txtPBirthDate.delete(0, tk.END)
    txtDoctorId.delete(0, tk.END)

    #add widgets to each Doctor tabs
    txtDID.delete(0, tk.END)
    txtDName.delete(0, tk.END)
    txtDBirthDate.delete(0, tk.END)
    txtLicense.delete(0, tk.END)

    #add widgets to each Prescription tabs
    txtPRID.delete(0, tk.END)
    cbPID1.set("")
    cbDID1.set("")
    txtPresciptionDate.delete(0, tk.END)
    txtDrugCode.delete(0, tk.END)

    if notebook.index("current") == 0:
        txtPID.focus_set()
    elif notebook.index("current") == 1:
        txtDID.focus_set()
    elif notebook.index("current") == 2:
        txtPRID.focus_set()

def exit_form():
    win.quit()
    win.destroy()

#Create window form
win = tk.Tk()
win.title("Data Input")
win.geometry("625x350")

#Create styles for tabs
style = ttk.Style()
style.theme_use('default')

notebook = ttk.Notebook(win)
notebook.grid(row=0, column=0, pady = 10, padx=10)

#create frames for different tabs
tab1 = ttk.Frame(notebook, width=600, height=250)
tab1.grid()
tab2 = ttk.Frame(notebook, width=600, height=250)
tab2.grid()
tab3 = ttk.Frame(notebook, width=600, height=250)
tab3.grid()
tab4 = ttk.Frame(notebook, width=600, height=250)
tab4.grid()

#get default color based upon theme
color = ttk.Style().lookup("TFrame", "background", default="white")

#Add Labels to the 3 tabs
notebook.add(tab1, text="Patient", )
notebook.add(tab2, text="Doctors")
notebook.add(tab3, text="Prescription")
notebook.add(tab4, text=" ")

notebook.tab(tab4, state="disabled")

#add widgets to each Patient tabs
lblInstruction1 = tk.Label(tab1, text="Please Enter Patient Information", font="Arial 10 bold", fg="#0000CD", background=color, anchor="w")
lblInstruction1.grid(row=0, column=0, columnspan=2,  padx=10, pady=10, sticky="w")
lblPID = tk.Label(tab1, text="Patient ID: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblPID.grid(row=1, column=0, padx=10, pady=5)
txtPID = tk.Entry(tab1, width=35)
txtPID.grid(row=1, column=1, pady=5, sticky="w")
lblPName = tk.Label(tab1, text="Patient Name: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblPName.grid(row=2, column=0, padx=10, pady=5)
txtPName = tk.Entry(tab1, width=35)
txtPName.grid(row=2, column=1, pady=5)
lblPBirthDate = tk.Label(tab1, text="Birth Date: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblPBirthDate.grid(row=3, column=0, padx=10, pady=5)
txtPBirthDate = tk.Entry(tab1, width=35)
txtPBirthDate.grid(row=3, column=1, pady=5)
lblDoctorId = tk.Label(tab1, text="Doctor ID: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblDoctorId.grid(row=4, column=0, padx=10, pady=5)
txtDoctorId = tk.Entry(tab1, width=35)
txtDoctorId.grid(row=4, column=1, pady=5)

#add widgets to each Doctor tabs
lblInstruction2 = tk.Label(tab2, text="Please Enter Doctor Information", font="Arial 10 bold", fg="#0000CD", background=color, anchor="w")
lblInstruction2.grid(row=0, column=0, columnspan=2,  padx=10, pady=10, sticky="w")
lblDID = tk.Label(tab2, text="Doctor ID: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblDID.grid(row=1, column=0, padx=10, pady=5)
txtDID = tk.Entry(tab2, width=35)
txtDID.grid(row=1, column=1, pady=5)
lblDName = tk.Label(tab2, text="Doctor Name: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblDName.grid(row=2, column=0, padx=10, pady=5)
txtDName = tk.Entry(tab2, width=35)
txtDName.grid(row=2, column=1, pady=5)
lblDBirthDate = tk.Label(tab2, text="Birth Date: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblDBirthDate.grid(row=3, column=0, padx=10, pady=5)
txtDBirthDate = tk.Entry(tab2, width=35)
txtDBirthDate.grid(row=3, column=1, pady=5)
lblLicense = tk.Label(tab2, text="License No: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblLicense.grid(row=4, column=0, padx=10, pady=5)
txtLicense = tk.Entry(tab2, width=35)
txtLicense.grid(row=4, column=1, pady=5)

#add widgets to each Prescription tabs
lblInstruction3 = tk.Label(tab3, text="Please Enter Prescription Information", font="Arial 10 bold", fg="#0000CD", background=color, anchor="w")
lblInstruction3.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")
lblPRID = tk.Label(tab3, text="Presciption ID: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblPRID.grid(row=1, column=0, padx=10, pady=5)
txtPRID = tk.Entry(tab3, width=35)
txtPRID.grid(row=1, column=1, pady=5)
lblPID1 = tk.Label(tab3, text="Patient ID: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblPID1.grid(row=2, column=0, padx=10, pady=5)

cbPID1 = ttk.Combobox(tab3, width=33, state="readonly")
cbPID1.grid(row=2, column=1, pady=5)
lblDID1 = tk.Label(tab3, text="Doctor ID: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblDID1.grid(row=3, column=0, padx=10, pady=5)

cbDID1 = ttk.Combobox(tab3, width=33, state="readonly")
cbDID1.grid(row=3, column=1, pady=5)
lblPresciptionDate = tk.Label(tab3, text="Prescription Date: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblPresciptionDate.grid(row=4, column=0, padx=10, pady=5)
txtPresciptionDate = tk.Entry(tab3, width=35)
txtPresciptionDate.grid(row=4, column=1, pady=5)
lblDrugCode = tk.Label(tab3, text="Drug Code: ", font="Arial 10 bold", fg="#0000CD", background=color, width=20, anchor="w")
lblDrugCode.grid(row=5, column=0, padx=10, pady=5)
txtDrugCode = tk.Entry(tab3, width=35)
txtDrugCode.grid(row=5, column=1, pady=5)

refresh_cbpatient()
refresh_cbdoctor()

#button frame
frmbtn = ttk.Frame(win, width=400, height=400)
frmbtn.grid(row=1, column=0)

#buttons
btnInsert = tk.Button(frmbtn, text="Insert", command=insert_data, width=14)
btnInsert.grid(row=1, column=0, padx=5, pady=5, sticky="w")
btnUpdate = tk.Button(frmbtn, text="Update", command=update_data, width=14)
btnUpdate.grid(row=1, column=1, padx=5, pady=5, sticky="w")
btnDelete = tk.Button(frmbtn, text="Delete", command=delete_data, width=14)
btnDelete.grid(row=1, column=2, padx=5, pady=5, sticky="w")
btnDelete = tk.Button(frmbtn, text="Clear All", command=clear_all, width=14)
btnDelete.grid(row=1, column=3, padx=5, pady=5, sticky="w")
btnDelete = tk.Button(frmbtn, text="Exit", command=exit_form, width=14)
btnDelete.grid(row=1, column=4, padx=5, pady=5, sticky="w")

win.mainloop()
