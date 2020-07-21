import os
import time
import calendar
import win32com.client as wincl
import pyaudio
import googlesearch
import wikipedia
import speech_recognition as sr
from PIL import Image
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
    if face == "no":
        print("@_@")
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
    if "bye" in you or "exit" in you or "stop" in you or "close" in you:
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
        run = True
    if "favorite food" in you:
        face = "happy"
        print("my favorite food is iron")
        speak.Speak("my favorite food is iron")
        run = True
    if "favorite drinks" in you:
        face = "happy"
        print("my favorite drinks is soda")
        speak.Speak("my favorite drinks is soda")
        run = True
    if "favorite school" in you:
        face = "happy"
        print("my favorite school is Assistant school")
        speak.Speak("my favorite school is Assistant school")
        run = True
    if "wear" in you:
        face = "happy"
        print("I like to wear leather")
        speak.Speak("I like to wear leather")
        run = True
    if "Vector" in you or "vector" in you:
        face = "happy"
        print("i'm here")
        speak.Speak("i'm here")
        run = True
    if "have an error" in you or "error" in you and "you" in you:
        face = "sad"
        print("yes i have an error is my name")
        speak.Speak("yes i have an error is my name")
        run = True
    if "do" in you and "hack" in you:
        face = "happy"
        print("no i'm not been hack")
        speak.Speak("no i'm not been hack")
        run = True
    if "where" in you and "you" in you and "form" in you:
        face = "happy"
        print("i form Vietnam")
        speak.Speak("i form Vietnam")
        run = True
    if "where" in you and "you" in you and "live":
        face = "happy"
        print("i live in Vietnam sever")
        speak.Speak("i live in Vietnam sever")
        run = True
    if "favorite color" in you or "color" in you and "like" in you:
        face = "happy"
        print("my favorite colors is red and green")
        speak.Speak("my favorite colors is red and green")
        run = True
    if "do you" in you and "like" in you or "do you" in you and "favorite" in you:
        face = "happy"
        print("yes, i like")
        speak.Speak("yes, i like")
        run = True
    if "hot" in you or "cold" in you:
        face = "happy"
        print("i feel normal")
        speak.Speak("i fell normal")
        run = True
    if "have" in you and "hair" in you:
        face = "no"
        print("i'm not have hair")
        speak.Speak("i'm not have hair")
        run = True
    if "connect" in you and "internet" in you:
        face = "happy"
        print("i can connect you can search google or wikipedia by say it")
        speak.Speak("i can connect you can search google or wikipedia by say it")
        run = True
    if "clear" in you or "clean" in you:
        os.system('cls')
        run = True
    if "love" in you and "me" in you:
        face = "happy"
        print("Maybe")
        speak.Speak("Maybe")
        import webbrowser; webbrowser.open('anime_lol.gif')
        '''
        im = Image.open("anime_lol.gif")
        im.seek(0)
        im.save("frame0.png")
        im.seek(1)
        im.save("frame1.png")
        im.seek(2)
        im.save("frame2.png")
        '''
        '''
        animation = pyglet.image.load_animation('anime_lol.gif')
        animSprite = pyglet.sprite.Sprite(animation)
        
        
        w = animSprite.width
        h = animSprite.height
        
        window = pyglet.window.Window(width=w, height=h)
        
        r,g,b,alpha = 0.5,0.5,0.8,0.5
        
        
        pyglet.gl.glClearColor(r,g,b,alpha)
        @window.event
        def on_draw():
            window.clear()
            animSprite.draw()
        pyglet.app.run()
        '''
        run = True
    elif you == "":
        face = "bad"
        print("i don't understand?")
        speak.Speak("i don't understand?")
        run = True
