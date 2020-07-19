import os
import time
import calendar
import win32com.client as wincl
import pyaudio
import googlesearch
import wikipedia
import speech_recognition as sr
from googlesearch import search
speak = wincl.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()
a = "hello"
face = 0
mode = "off"
os.system('cls')
print("What is your name?")
speak.Speak("What is your name?")
name = input()
print("hello " + name)
speak.Speak("hello" + name)
print("How old are you?")
speak.Speak("How old are you?")
old = input()
os.system('cls')
print("type to chat or say to chat:")
run = True
while run:
    you = "p"
    if face == "happy":
        print(":)")
    if face == "sad":
        print(":(")
    if mode == "on":
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.record(source, duration=5)
            print("listening...")
            try:
                you = r.recognize_google(audio)
            except:
                print("i can't understand?")
                speak.Speak("i can't understand?")
                run = True
            if "off" in you:
                mode = "off"
                speak.Speak("voice off")
                run = True
            if "on" in you:
                mode = "on"
                speak.Speak("voice on")
                run = True
                '''
            if "google" in you or "search" in you:
                with sr.Microphone() as source:
                    print("search:")
                    audio = r.record(source, duration=5)
                    print("loading...")
                    try:
                        text = r.recognize_google(audio)
                        for j in search(text, tld="co.in", num=10, stop=10, pause=1):
                            print(j)
                    except:
                        face = "sad"
                        print("i don't understand?")
                        speak.Speak("i don't understand?")
                        run = True
                    run = True
                    '''
            if "wikipedia" in you or "wiki" in you:
                with sr.Microphone() as source:
                    print("search:")
                    audio = r.record(source, duration=5)
                    print("loading...")
                    try:
                        take = r.recognize_google(audio)
                        wiki = wikipedia.summary(take, sentences=5)
                        print(wiki)
                        speak.Speak(wiki)
                        run = True
                    except:
                        face = "sad"
                        print("i don't understand?")
                        speak.Speak("i don't understand?")
                        run = True
                    run = True
    elif mode == "off":
        you = input()
    if "voice" in you and "off" in you:
        mode = "off"
        speak.Speak("voice off")
        run = True
    if "voice" in you and "on" in you:
        mode = "on"
        speak.Speak("voice on")
        run = True
    if "search" in you or "google" in you:
        if mode == "on":
            with sr.Microphone() as source:
                print("search:")
                audio = r.record(source, duration=5)
                print("loading...")
                text = r.recognize_google(audio)
            for j in search(text, tld="co.in", num=10, stop=10, pause=2):
                print(j)
                run = True
        elif mode == "off":
            print("search:")
            text = input()
            print("loading...")
            for j in search(text, tld="co.in", num=10, stop=10, pause=2):
                print(j)
                run = True
    if a in you:
        print("hello " + name)
        speak.Speak("hello " + name)
        run = True
    if "feel" in you:
        face = "happy"
        print("i'm good")
        speak.Speak("i'm good")
        run = True
    if "your name" in you or "who are you" in you:
        face = "happy"
        print("my name is Vector")
        speak.Speak("my name is Vector")
        run = True
    if "my" in you and "name" in you:
        face = "happy"
        print("your name is " + name)
        speak.Speak("your name is " +name)
        run = True
    if "good" in you:
        face = "happy"
        run = True
    if "bad" in you:
        face = "sad"
        print("boo!")
        speak.Speak("boo!")
        run = True
    if "old" in you and "you" in you:
        face = "happy"
        print("i don't have old!")
        speak.Speak("i don't have old!")
        run = True
    if "old" in you and "am" in you and "i" in you:
        face = "happy"
        print("you are " + old + " year old" )
        speak.Speak("you are" + old + "year old")
        run = True
    if "wikipedia" in you:
        print("search:")
        take = input()
        wiki = wikipedia.summary(take, sentences=5)
        print(wiki)
        speak.Speak(wiki)
        run = True
    if "bye" in you or "exit" in you or "stop" in you:
        face = "happy"
        print("bye")
        speak.Speak("bye")
        time.sleep(2)
        run = False
    if "time" in you:
        x = time.localtime(time.time())
        nam = x[0]
        thang = x[1]
        ngay = x[2]
        gio = x[3]
        phut = x[4]
        giay = x[5]
        yy = nam
        mm = thang
        print("Time:")
        print(gio, phut)
        speak.Speak(gio, phut)
        run = True
    if "date" in you:
        print(calendar.month(yy, mm))
        run = True
    if "tell me a joke" in you:
        print("i'm not an A.I")
        speak.Speak("i'm not an A.I")
        run = True
    if "who create you" in you:
        os.system('cls')
        print("i'm make by johnny20061234 the ideal by phucxo")
        speak.Speak("i'm make by johnny20061234 the ideal by phucxo")
        f = open("create.txt", "r")
        print(f.read())
        time.sleep(5)
        os.system('cls')
        run =True
    elif you == "":
        face = "bad"
        print("i don't understand?")
        speak.Speak("i don't understand?")
        run = True
