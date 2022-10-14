import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from subprocess import call
import wolframalpha
import json
import requests
import pyjokes
import ctypes
import random
import winshell

ran = 0
ran1 = 0

print('Loading your AI personal assistant - Softek')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


# speak("Loading your AI personal assistant G-One")
speak("Loading your AI personal assistant softek")
wishMe()

if __name__ == '__main__':

    while True:

        speak("Tell me how can I help you now chetan?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Softtek")
            print("I was built by softtek")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)



        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        # elif "volume" in statement:
        #   valid = False

        #  while not valid:
        #     speak("tell the volume level betwee n 0 to 100")
        #    volume=takeCommand()
        # volume = int(volume)
        # if (volume <= 100) and (volume >= 0):
        #   call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
        #  speak(" volumn adjusted.")
        # valid = True
