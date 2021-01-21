import pyttsx3
import os
import speech_recognition as sr

pyttsx3.speak("Enter Website Name please")


print("chat with me with your requirements : "  , end='')

r = sr.Recognizer()

with sr.Microphone() as sound:
    print("start saying")
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(sound, duration=1)
    audio = r.listen(sound)
    print("we got it....")
p = r.recognize_google(audio)
print(p)
os.system("chrome  " + p)
