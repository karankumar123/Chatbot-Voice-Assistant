import pyttsx3
import speech_recognition as sr
import datetime
from requests import get
import subprocess
import webbrowser
import os
import sys
import time
import pywhatkit as kit
import pyjokes
import wikipedia
import cv2
import smtplib
import pyautogui
import instadownloader
import instaloader
import operator
from bs4 import BeautifulSoup
import requests
import keyboard
from plyer import notification
from pygame import mixer
import mysql.connector as c





assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voicess', voices[0].id)


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

        command.pause_threshold = 1
        # audio = command.listen(source, timeout = 5, phrase_time_limit = 20)
        audio = command.listen(source, 0, 8)
        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='en-in')
            print(f"user said:{query}")
        except Exception as e:
            speak("Say that again please")
            return "none"
        return query.lower()


def alarm(query):
    timehere = open("alarm.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour > 0 and hour < 12:
        speak("good morning sir")
    elif hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")


def askname():
    speak("what is your name sir?")
    name = takecommand()
    speak('welcome :' + name)
    
    

    





def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()
    
    
    
    
    
def Login():


   user = input("Enter username :")
   pas  = input("Enter password :")


  

  
     
   
   
   
   con = c.connect(host="localhost",user="root",password="",database="std")
   cur = con.cursor()
   cur.execute("select * from login_detail where username=%s and password=%s",(user,pas))
   row = cur.fetchone()
            #print(row)
   if row!=None:
                #mBox.showinfo('Information', "Login Successfully")
         speak("Login successfull")       
         #print("Login successfull")
         
                #login_window.destroy()
                
                
                
   else:
                #mBox.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")
         speak("Login failed,Invalid Username or Password,Try again")
         #print("Login failed,Invalid Username or Password.Try again")
         Login()
                










    
   
    

    
    
    
Login()    
    





    
    



def Task_Exe():
    wish()
    askname()

    while True:

        query = takecommand()

        if 'hello' in query:
            speak("Hello sir, I am jarvis")
            speak("Your Personal AI assistant")
            speak("please tell me how can i help you?")

        elif 'open vs code' in query:
            path = "C:\\Users\\Lenovo\\AppData\\Local\Programs\\Microsoft VS Code"
            os.startfile(path)
            speak("ok sir oppening vs code")

        elif 'open notepad' in query:
            path = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(path)
            speak("ok sir opening notepaid ")
        elif 'close notepad ' in query:
            os.system("TASKKILL /F /IM notepad++.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")
            speak("ok sir oppening command prompt")


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query:
            speak("It's good to know that your fine")

        elif 'who i am' in query:
            speak("If you talk then definitely your human.")

        elif 'who made you' in query:
            speak("I have been created by Karan Kumar.")
            
        elif 'date of birth' in query:
            speak("my date of birth is 4 september")
            
       

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'send email' in query:

            try:

                speak("what should i say")
                content = takecommand()
                to = "karankumar887705@gmail.com"

                sendEmail(to, content)
                speak("Email has been sent to karan")
            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to send this email to karan")


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'play song on youtube' in query:
            kit.playonyt("see you again")

        if 'play music' in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "D:\\SONGS\\LOVE SONGS"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'open' in query:
            from DictApp import openappweb
            openappweb(query)
        elif 'close' in query:
            from DictApp import closeappweb
            closeappweb(query)

        elif 'open google' in query:
            speak("ok sir oppening google")
            speak("sir,what should i search on google\n")
            webbrowser.open("google.com")
            cm = takecommand()
            webbrowser.open(f"{cm}")
            



        elif 'open facebook' in query:
            speak("ok sir oppening facebook")
            webbrowser.open("https://www.facebook.com/")
            cm = takecommand()
            webbrowser.open(f"{cm}")

        elif 'google' in query:
            from SearchNow import searchgoogle
            searchgoogle(query)
        elif 'youtube' in query:
            from SearchNow import serchYoutube
            serchYoutube(query)

        elif 'pause' in query:
            pyautogui.press("k")
            speak("video paused")
        elif 'play' in query:
            pyautogui.press("k")
            speak("video played")
        elif 'mute' in query:
            pyautogui.press("m")
            speak(" video mouted")
        elif 'volume up' in query:
            from key import volumeup
            speak("Turning volume up,sir")
            volumeup()
        elif 'volume down' in query:
            from key import volumedown
            speak("Turning volume down, sir")
            volumedown()

        elif 'remember that' in query:
            remembermsg = query.replace("remember that", "")
            remembermsg = query.replace("jarvis", "")
            speak("You told me " + remembermsg)
            remember = open("remember.txt", "w")
            remember.write(remembermsg)
            remember.close()
        elif 'what do you remember' in query:
            remember = open("remember.txt", "r")
            speak("You told me " + remember.read())
        elif 'news' in query:
            from news import latestnews
            latestnews()

        elif 'whatsapp' in query:
            from whatsupp import sendMessage
            sendMessage()


        elif "schedule my day" in query:
            task = []  # Empty list
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = takecommand().lower()
            if "yes" in query:
                file = open("tasks.txt", "w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    task.append(input("Enter the task :- "))
                    file = open("tasks.txt", "a")
                    file.write(f"{i}. {task[i]}\n")
                    file.close()
            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    task.append(input("Enter the task :- "))
                    file = open("tasks.txt", "a")
                    file.write(f"{i}. {task[i]}\n")
                    file.close()
        elif 'show my schedule' in query:
            file = open("tasks.txt", "r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("Notification.mp3")
            mixer.music.play()
            notification.notify(

                title="My schedule:-",
                message=content,
                timeout=15
            )


        elif 'wikipedia' in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)


        elif 'set an alarm' in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")


        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak("sir,please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds,I am taking screenshot")
            time.sleep(3)
            image = pyautogui.screenshot()
            image.save(f"{name}.png")
            speak("I am done sir,the screenshot is saved in our main folder.now i am raedy for next command")



        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(3)
            pyautogui.keyUp("alt")
            speak("ok sir switch the window")



        elif 'thank you' in query:
            speak("Most welcome sir")

        elif 'instagram profile' in query:
            speak("sir please enter the username correctelly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account")
            condition = takecommand().lower()
            if " yes " in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done sir,profile picture is saved in our main folder.now i am ready to next command")
            else:
                pass

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            speak("ok sir oppening you tube")


        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'temperature' in query:
            search = "temperture in ranchi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")

        elif 'where i am' in query:
            speak("wait sir,let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'

                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                state = geo_data['city']
                #city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['contary']
                speak(f"sir i am not sure,but i think we are in {state} city of {country} state ")
            except Exception as e:
                speak("sorry sir,Due to network issue i am not able to find where we are")
                pass

        elif 'find location'in query:
            from SearchNow import Mylocation
            Mylocation()
      





        elif 'do some calculation' in query or 'can you calculate' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate,example 3 plus 3")
                print("listening......")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_opeartor(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        '/': operator.truediv,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_opeartor(oper)(op1, op2)

                speak("your result is:")

                speak(eval_binary_expr(*(my_string.split())))

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"you ip address is {ip}")


        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on kits way to shut down")
            subprocess.call('shutdown / p /f')
            speak("ok sir sutdown the system")

        elif "restart system" in query:
            subprocess.call(["shutdown", "/r"])
            speak("ok sir restart the system")



        elif 'ok bye' in query:
            speak("thanks for using me sir , have a good day")

            sys.exit()
            # speak("sir, do you have any other work")


