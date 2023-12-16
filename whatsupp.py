import pywhatkit as kit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime



assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voicess',voices [0].id)


def speak(audio):
    print(" ")
    assistant.say(audio)
    print(audio)
    assistant.runAndWait()
    

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        print(" ")
        
        command.pause_threshold=1
        #audio = command.listen(source, timeout = 5, phrase_time_limit = 20)
        audio = command.listen(source,0,8)
        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='en-in')
            print(f"user said:{query}")
        except Exception as e:
                speak("Say that again please")
                return "none"
        return query.lower()    
    
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you wan to message")
    a = int(input('''Person 1 - 1
    Person 2 - 2 : '''))
    
    if a == 1:
        speak("Whats the message")
        message = str(input("Enter the message:- "))
        kit.sendwhatmsg("+917632000512",message,time_hour=strTime,time_min=update)
    elif a==2:
        speak("Whats the message")
        message = str(input("Enter the message:- "))
        kit.sendwhatmsg("+916202325743",message,time_hour=strTime,time_min=update)
        
