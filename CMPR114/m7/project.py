import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from threading import Thread
from queue import Queue
import pyaudio
import json
from vosk import Model, KaldiRecognizer

# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i))

LISTEN = 1
CHANNELS=1
FRAME_RATE=16000
RECORD_SECONDS =20  #how many seconds to record before sending to transcription
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

#transcribe data
messages = Queue()
recordings = Queue()

def file_path():
    path = askdirectory(title="Select File Location", initialdir="/home", mustexist="true")
    txtLocation.insert(0, path)

#chunk is for how often read from microphone
def record_microphone(chunk=1024):
    #initialize PyAudio
    p = pyaudio.PyAudio()

    #create stream to read from microphone
    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=FRAME_RATE,
                    input=True,
                    input_device_index=27,
                    frames_per_buffer=chunk)

    frame=[]    #STORE AUDIO FROM MICROPHONE

    #if queue is not empty, process audio file
    while not messages.empty():
        data=stream.read(chunk)
        frame.append(data)

        #if audio recording is greater than 20 secs, then add it to the recordings queue to be transcribe
        if len(frames) >= (FRAME_RATE*RECORD_SECONDS)/chunk:
            recordings.put(frame.copy())
            frames=[]

    stream.stop_stream
    stream.close()
    p.terminate

def speech_recognition(output):
    model = Model(model_name="vosk_model_en_us-0.22")
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    while not messages.empty():
        frames  = recordings.get()

        rec.AcceptWaveform(b"".join(frames))
        result = rec.Result()
        text = json.load(result)["text"]

def start_recording():
    messages.put(True)
   
    var_info.set("Recording started...")

    record = Thread(target=record_microphone)
    record.start()

    transcribe = Thread(target=speech_recognition, args=(txtDictation,))
    transcribe.start()

def stop_recording():
    
    #     messages.get()
    var_info.set("Recording stopped...")
        

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
    var_info.set("")
    rbFile.select()
    rbDB.selection_clear()
    rbFile.focus_set()

#Set up window form
win = tk.Tk()
win.title('Speech to Text')
win.geometry("923x505")

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
btnDictation = tk.Button(frm2, text="Start Dictation", command=start_recording, width=12)
btnDictation.grid(column=0, row=0, padx=20, pady=20, sticky="w")
btnStop = tk.Button(frm2, text="Stop Dictation", command=stop_recording, width=12)
btnStop.grid(column=1, row=0, padx=0, pady=20, sticky="w")
btnSave = tk.Button(frm2, text="Save Text", command=save_text, width=12)
btnSave.grid(column=2, row=0, padx=20, pady=20, sticky="w")
btnClear = tk.Button(frm2, text="Clear Text", command=clear_text, width=12)
btnClear.grid(column=3, row=0, padx=0, pady=20, sticky="w")

var_info = tk.StringVar()
var_info.set("")
lblInfo = tk.Label(win, textvariable=var_info, font="Arial 10 bold", fg="red")
lblInfo.grid(column=0, row=9, padx=10, pady=10, sticky="w")

txtDictation = tk.Text(win, height=14, width=112)
txtDictation.grid(column=0, row=10, padx=10, pady=10, sticky="w")
rbFile.select()
rbDB.selection_clear()
rbFile.focus_set()

win.mainloop()
