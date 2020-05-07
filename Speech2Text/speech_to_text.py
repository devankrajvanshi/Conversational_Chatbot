#Speech to Text Conversion using Google speech_recognition library

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

filename = "16-122828-0002.wav"

#Identifying Text from file
try:
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)
except:
    print("Audio file to be identified not found")

#Using microphone
try:
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Recording ...")
        audio_data = r.record(source, duration=5)
        #Duration of input can be changed above
        text = r.recognize_google(audio_data)
        print(text)
except:
    print("Please try again")
