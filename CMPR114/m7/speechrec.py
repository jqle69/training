import speech_recognition as sr
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

LISTEN = 1
def file_path():
    path = askdirectory(title="Select File Location", initialdir="/home", mustexist="true")
    txtLocation.insert(0, path)

def start_dictation():
    #initialize object
    recognizer = sr.Recognizer()
                    
    while LISTEN:
        try:
            with sr.Microphone() as mic:
                print("Starting dictating...")
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(source=mic) 

                text = recognizer.recognize_google(audio)
                text = text.lower()

                #txtDictation.update(f"Dication: {text}")
                print(f"Dication: {text}")
                                       
        except sr.UnknownValueError:
            print("Error understanding speech")
            recognizer = sr.Recognizer()
            continue
        except Exception as e:
            print(f"Error: {e}")

def stop_dictation():
    global LISTEN
    messagebox.showinfo(title="Dictation Status", message="Stopping dictation.")
    LISTEN = 0

def save_text():
    data = txtDictation.get(1.0, tk.END)
    filepath = txtLocation.get()

    try:
        tfile = open(filepath, "a")
        tfile.write(data)
        tfile.close()

        messagebox.showinfo(title="Dictation Save", message=f"Dication was saved to {filepath}.")
        txtLocation.delete(0, tk.END)
        txtDictation.delete(0, tk.END)
        rbFile.focus_set()

    except Exception as e:
        messagebox.showerror(title="Missing Location", message="Please specify file location.")
def clear_text():
    txtLocation.delete(0, tk.END)
    txtDictation.delete(1.0, tk.END)
    rbFile.select()
    rbDB.selection_clear()
    rbFile.focus_set()

#Set up window form
win = tk.Tk()
win.title('Speech to Text')
win.geometry("925x460")


# Input
lblinstruct = tk.Label(win, text = "Please select one of the option to save your dictation: ", font="Arial 10 bold", fg="#2E86C1")
lblinstruct.grid(column=0, row=0, padx=10, pady=10, sticky="w") #Label widge

frm1 = tk.Frame(win, relief="groove", bd=4, width=800)
frm1.grid(column=0, row=1, padx=10, rowspan=4, sticky="w")
rbFile = tk.Radiobutton(frm1, text="Text File", value="1", width=15, anchor="w")
rbFile.grid(column=0, row=0, padx=10, pady=10)
btnLocation = tk.Button(frm1, text="Location", anchor="w", command=file_path)
btnLocation.grid(column=1, row=0, padx=10, pady=10)
txtLocation = tk.Entry(frm1, width=107)
txtLocation.grid(column=2, row=0, padx=10, pady=10)
rbDB = tk.Radiobutton(frm1, text="Database Table", value="2", width=15, anchor="w")
rbDB.grid(column=0, row=1, padx=10, pady=10)

frm2 = tk.Frame(win, relief="groove" )
frm2.grid(column=0, row=5, rowspan=4, sticky="w")
btnDictation = tk.Button(frm2, text="Start Dictation", command=start_dictation, width=12)
btnDictation.grid(column=0, row=0, padx=20, pady=20, sticky="w")
btnStop = tk.Button(frm2, text="Stop Dictation", command=lambda: [stop_dictation], width=12)
btnStop.grid(column=1, row=0, padx=0, pady=20, sticky="w")
btnSave = tk.Button(frm2, text="Save Text", command=save_text, width=12)
btnSave.grid(column=2, row=0, padx=20, pady=20, sticky="w")
btnClear = tk.Button(frm2, text="Clear Text", command=clear_text, width=12)
btnClear.grid(column=3, row=0, padx=0, pady=20, sticky="w")

txtDictation = tk.Text(win, height=14, width=112)
txtDictation.grid(column=0, row=9, padx=10, pady=10, sticky="w")
rbFile.select()
rbDB.selection_clear()
rbFile.focus_set()

win.mainloop()
