import pyaudio
import queue
import subprocess
import json
from vosk import Model, KaldiRecognizer

# Initialize the queue for storing recordings
recordings = queue.Queue()

# Audio configuration parameters
channels = 1
frame_rate = 16000
record_seconds = 5
audio_format = pyaudio.paInt16
sample_size = 2

def record_microphone(chunk=1024):
    p = pyaudio.PyAudio()
    stream = p.open(format=audio_format, 
                    channels=channels,
                    rate=frame_rate,
                    input=True,
                    input_device_index=1,
                    frames_per_buffer=chunk)
    print("Recording...")
    frames = []
    for i in range(int(frame_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    recordings.put(frames)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Recording stopped.")

# Initialize the Vosk model and recognizer
try:
    model = Model("vosk-model-small-en-us-0.15")
    rec = KaldiRecognizer(model, frame_rate)
    rec.SetWords(True)
except Exception as e:
    print(f"Failed to load model or create recognizer: {e}")
    exit(1)

def speech_recognition():
    while not recordings.empty():
        frames = recordings.get()
        rec.AcceptWaveform(b''.join(frames))
        result = json.loads(rec.Result())
        text = result.get("text", "")
        print(f"Transcribed Text: {text}")

# Example usage
record_microphone()  # Start recording
speech_recognition()  # Start transcribing