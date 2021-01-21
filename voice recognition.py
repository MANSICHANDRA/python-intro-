import pyttsx3
import os
import speech_recognition as sr

pyttsx3.speak("lets make it easier for you okk just enter which application you want to run and we will open it")


while True:
    print("chat with me with your requirements : "  , end='')
    r = sr.Recognizer()

    with sr.Microphone() as sound:
        print("start saying")
        audio = r.listen(sound)
        print("we got it....")
    p = r.recognize_google(audio)

# print(p)
# os.system(p)

    if (("run" in p) or ("open" in p)) and ("chrome" in p):
        os.system("chrome")

    elif (("run" in p) or ("open" in p)) and  (("notepad++" in p) or ("editor" in p) ) :
        os.system("notepad++")
  os.system("notepad++")
  
    elif (("run" in p) or  ("open" in p )) and  (("window media player" in p) or ("player" in p) ) :
        os.system("wmplayer")
  
    elif (("run" in p) or ("open" in p)) and ("gmail" in p):
        os.system("chrome   mail.google.com")

    elif  ("exit" in p)  or ("quit" in p):
        break

    else:
        print("dont support")

