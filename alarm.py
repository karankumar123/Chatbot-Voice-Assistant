import pyttsx3
import datetime 
import os


assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voicess',voices [0].id)

def speak(audio):
    print(" ")
    assistant.say(audio)
    print(audio)
    assistant.runAndWait()
    

extractedtime = open("alarm.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("alarm.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("music.mp3") #You can choose any music or ringtone 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)