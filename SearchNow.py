import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
import webbrowser
import os
import requests


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
    
#query = takecommand().lower()

    
def searchgoogle(query):
    if 'google'in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google ","")
        speak("This is what i found on google")
        try:
            kit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No speakable output available")
            
def serchYoutube(query):
    if 'youtube'in query:
        speak("This is what i found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube ","")
        query = query.replace("jarvis","")
        web = "https://www.youtube.com/results?search_query" + query
        webbrowser.open(web)
        kit.playonyt(query)
        speak("Done, sir")


def searchWikipedia(query):
    if 'wikipedia'in query:
        speak("Searching from wikipedia...")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        
        result = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia..")
        print(result)
        speak(result)
        
        
        
        
def Mylocation():
    op = "https://www.google.com/maps/place/Tagore+Hill/@23.4012599,85.3354152,809m/data=!3m1!1e3!4m14!1m7!3m6!1s0x39f4e1496994ac09:0xb41a61fed030697a!2sTagore+Hill!8m2!3d23.401255!4d85.3379901!16s%2Fm%2F0j3d6_9!3m5!1s0x39f4e1496994ac09:0xb41a61fed030697a!8m2!3d23.401255!4d85.3379901!16s%2Fm%2F0j3d6_9?entry=ttu"
    webbrowser.open(op)
      


    
    


        
        
        
        
        



