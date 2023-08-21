import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import speech_recognition as sr
#import sqlserver
import pyodbc

#Initialize the object
rec = sr.Recognizer()
rec.energy_threshold = 300  #set audio level
mic = sr.Microphone()

#Define server and database name
server = 'MSI'
database = 'MyDb'

class dictation_dml:

    def __init__(self):
        #initialize connection and cursor

        #define connection string
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER=' + server + ';\
                      DATABASE=' + database + ';\
                      Trusted_Connection=yes;')
        #create cursor
        self.cursor = self.conn.cursor()

    def save_dictation(self, dicttext):
        #save text to dictations table
        try:
            self.cursor.execute("INSERT INTO dbo.dictations (dicttext) values (?)", (dicttext))
            self.conn.commit()
            messagebox.showinfo(title="Transaction Completed", message=f"Text was saved to database successfully.")

        except pyodbc.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def update_dictation(self, dictid, dicttext):
        #update text to dictations table (not being used currently)
        try:
            self.cursor.execute("UPDATE dbo.dictations SET dicttext=? WHERE dictid=?", (dicttext, dictid))
            self.conn.commit()

            messagebox.showinfo(title="Transaction Completed", message=f"Text was updated to database successfully.")
        except pyodbc.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def delete_dictation(self,  dictid):
        #delete text from dictations table (not being used currently)
        try:
            self.cursor.execute("DELETE FROM dictations WHERE ", (dictid))
            self.conn.commit()

            messagebox.showinfo(title="Transaction Completed", message=f"Text was deleted from database successfully.")
        except pyodbc.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def __del__(self):
        #close out connection and cursor
        self.cursor.close()
        self.conn.close()

def file_path():
    #User dialog box to select preferred folder
    path =  askdirectory(title="Select File Location", initialdir="/home", mustexist="true")
    txtLocation.insert(0, path)     #set the path in the Location textbox

def start_recording():
    #Set the label to show current action
    var_info.set("Recorded Statement...")
    btnStop.focus_set()

    #transcribe text used for saving
    global text

    with mic as source:
        #adjust the background noise level 
        rec.adjust_for_ambient_noise(source)
        #audio = rec.record(source, duration=10, offset=0.5)   #dictation set for 10 second

        #get audio recording from mic
        audio = rec.listen(source=mic) 

    try:
        #convert audio object to text
        text = rec.recognize_google(audio_data=audio)
        var_dict.set(text)      #display transcribe text to lblDictation
    except sr.UnknownValueError:
        var_info.set("Could not understand the dictation.")
    except sr.RequestError as e:
        var_info.set(f"Error: {e}.")

def stop_recording():
    var_info.set("Recording stopped...")

def save_text():

    #get text from lblDictation
    data = var_dict.get()
    #get file name and path from txtLocation
    filepath = txtLocation.get()
    #get value from radio buttons
    selectopt = radio_val.get()


    if selectopt == 1:  #user selected file option
        if filepath:    #user must supply a path and filename
            try:
                #create file and write text to file
                txtfile = open(filepath, "a")
                txtfile.write(data)
                txtfile.close()

                messagebox.showinfo(title="Dictation Save", message=f"Dication was saved to {filepath}.")
                clear_text()

            except Exception as e:
                messagebox.showerror(title="Missing Location", message="Please specify file location.")
        else:
            messagebox.showerror(title="Select a file", message="Please specify folder and file.")
    elif selectopt == 2:    #user selected database option
        #call save function from class dictation_dml
        sql.save_dictation(text)
        clear_text()
    else: 
        messagebox.showerror(title="Selection Error", message="Must select a destination.")

def clear_text():
    #clear data from text widgets and set preferred radio button
    txtLocation.delete(0, tk.END)
    var_info.set("")
    var_dict.set("")
    rbFile.select()
    rbDB.selection_clear()
    rbFile.focus_set()

def exit():
    #clean up window handle
    win.destroy()

#Set up window form
win = tk.Tk()
win.title('Speech to Text')
win.geometry("923x510")

# Create window widges 
lblinstruct = tk.Label(win, text = "Please select one of the option to save your dictation: ", font="Arial 10 bold", fg="#2E86C1")
lblinstruct.grid(column=0, row=0, padx=10, pady=10, sticky="w") #Label widge

frm1 = tk.Frame(win, relief="groove", bd=4, width=800)
frm1.grid(column=0, row=1, padx=10, rowspan=4, sticky="w")
radio_val = tk.IntVar(frm1)
rbFile = tk.Radiobutton(frm1, text="Text File", variable=radio_val, value=1, width=15, anchor="w")
rbFile.grid(column=0, row=0, padx=10, pady=10)
btnLocation = tk.Button(frm1, text="Location", anchor="w", command=file_path)
btnLocation.grid(column=1, row=0, padx=10, pady=10)
txtLocation = tk.Entry(frm1, width=107)
txtLocation.grid(column=2, row=0, padx=10, pady=10)
rbDB = tk.Radiobutton(frm1, text="Database Table", variable=radio_val, value=2, width=15, anchor="w")
rbDB.grid(column=0, row=1, padx=10, pady=10)


frm2 = tk.Frame(win, relief="groove" )
frm2.grid(column=0, row=5, rowspan=4, sticky="w")
btnDictation = tk.Button(frm2, text="Start Dictation", command=start_recording, width=12)
btnDictation.grid(column=0, row=0, padx=20, pady=20, sticky="w")
btnStop = tk.Button(frm2, text="Stop Dictation", command=stop_recording, width=12)
btnStop.grid(column=1, row=0, padx=0, pady=20, sticky="w")
btnSave = tk.Button(frm2, text="Save Text", command=save_text, width=12)
btnSave.grid(column=2, row=0, padx=20, pady=20, sticky="w")
btnClear = tk.Button(frm2, text="Clear Text", command=clear_text, width=12)
btnClear.grid(column=3, row=0, padx=0, pady=20, sticky="w")
btnQuit = tk.Button(frm2, text="Exit", command=exit, width=12)
btnQuit.grid(column=4, row=0, padx=20, pady=20, sticky="w")

var_info = tk.StringVar()
lblInfo = tk.Label(win, textvariable=var_info, font="Arial 10 bold", fg="red")
lblInfo.grid(column=0, row=9, padx=18, pady=10, sticky="w")

var_dict = tk.StringVar()
var_dict.set("")
lblDictation = tk.Label(win, textvariable=var_dict, height=11, width=80, relief="sunken", bg="white", fg="black", anchor="nw", font=("Arial", 14))
lblDictation.grid(column=0, row=10, padx=0, pady=0)
rbFile.select()         #Select the File Option
rbDB.selection_clear()  #Unselect the Database Option
rbFile.focus_set()      #Set the focus back to the File Radio Option 

#initialize the class dictation_dml, setting up the connection and cursor
sql = dictation_dml()

win.mainloop()
