import datetime
import os
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import webbrowser as wb
import wikipedia
import subprocess
import pyjokes
from time import sleep

engine = pyttsx3.init()  # initialise pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-2 range for different voices
voicespeed = 175  # setting speed
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Friday is Online Sir")
speak("just a minute. Loading sequence.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print(e)
        return "---"
    return query


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    print(day, month, year)
    speak(day)
    speak(month)
    speak(year)

def friday():
    speak("Yes Boss")
    print("Yes Boss")

def hello():
    print('welcome back sir  how can i help you')
    speak("Welcome back sir how can i help you")

def goodbye():
    os._exit()

# Open chrome/website
def open_chrome():
    speak("opening chrome")
    url = "https://www.google.co.in/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)

def open_brave():
    speak("opening brave")
    brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe %s"
    wb.get(brave_path)

def open_facebook():
    speak("opening Facebook")
    url = "https://www.facebook.com/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)

def music_youtube():
    speak("playing music on youtube")
    url = "https://www.youtube.com/watch?v=4j6UF1iT0aY&list=RD4j6UF1iT0aY&start_radio=1"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)


if __name__ == "__main__":

    # wishme()

    try:

        while True:
            query = takeCommand().lower()
            print(query)

            if "good morning" in query:
                speak("good morning sir")

            elif "time" in query:
                time()
            
            
            
            elif "What time is it" in query:
                time()   

            elif "hello" in query:
                hello ()

            elif "friday" in query:
                friday()
            

            elif "date" in query:
                date()

            # open chrome
            elif "open chrome" in query:
                open_chrome()
                
            elif "open brave" in query:
                open_brave()

            elif"open facebook" in query:
                open_facebook()
            
            elif"play music" in query:
                music_youtube()

            # Wikipedia search
            elif "wikipedia" in query:
                speak("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak(result)
                print(result)

            # Chrome search
            elif "search" in query:
                speak("what should i search?")
                chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search + ".com")


            # Launch software
            elif "open notepad" in query:
                speak("opening notepad")
                location = "C:/WINDOWS/system32/notepad.exe"
                notepad = subprocess.Popen(location)

            elif "close notepad" in query:
                speak("closing notepad")
                notepad.terminate()

            # Random jokes
            elif "joke" in query:
                speak(pyjokes.get_jokes())

            # Logout/Shutdown/Restart
            elif "logout" in query:
                speak('logging out in 5 second')
                sleep(5)
                os.system("shutdown - l")

            elif "shutdown" in query:
                speak('shutting down in 5 second')
                sleep(5)
                os.system("shutdown /s /t 1")

            elif "restart" in query:
                speak('restarting in 5 second')
                sleep(5)
                os.system("shutdown /r /t 1")
            
            elif" goodbye" in query:
                speak("Good bye Boss")
                print("Good bye Boss")
                goodbye()
                



    except Exception:
        print("something went wrong!")