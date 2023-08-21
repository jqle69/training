from threading import Thread
from queue import Queue
import pyaudio
import json
from vosk import Model, KaldiRecognizer

#transcribe data
messages = Queue()
#Audio Data 
recordings = Queue()

def start_recording(data):
    messages.put(True)

    with <textbox>:
        print("starting....")
        record = Thread(target=record_microphone)
        record.start()

        transcribe = Thread(target=speech_recognition, args=(output,))
        transcribe.start

def stop_recording(data):
    with output:
        messages.get()
        print("Stopped.")

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

# p.terminate()

CHANNELS=1
FRAME_RATE=16000
RECORD_SECONDS =20  #how many seconds to record before sending to transcription
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

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

    frame=[]

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


model = Model(model_name="vosk_model_en_us-0.22")
rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)

def speech_recognition(output):
    while not messages.empty():
        frames  = recordings.get()

        rec.AcceptWaveform(b"".join(frames))
        result = rec.Result()
        text = json.load(result)["text"]
