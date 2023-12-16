import requests
import json
import pyttsx3


assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voicess',voices [0].id)


def speak(audio):
    print(" ")
    assistant.say(audio)
    print(audio)
    assistant.runAndWait()
    
def latestnews():
    apdict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=65a0da285bc84f47980a3f12ed391b15",
              "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=65a0da285bc84f47980a3f12ed391b15",
              "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=65a0da285bc84f47980a3f12ed391b15",
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=65a0da285bc84f47980a3f12ed391b15",
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=65a0da285bc84f47980a3f12ed391b15",
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=65a0da285bc84f47980a3f12ed391b15"
               
            }
    
    content = None
    url = None
    speak("which field news do you want,[business],[intertainment],[health],[science],[sports],[technology]")
    field = input("Type field news that you want: ")
    for key ,value in apdict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")