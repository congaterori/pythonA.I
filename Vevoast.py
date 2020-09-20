import os
import time
import calendar
import random
#from playsound import playsound
import win32com.client as wincl
import pyaudio
import googlesearch
import wikipedia
import speech_recognition as sr
import wolframalpha
#from PIL import Image
from googlesearch import search
speak = wincl.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()
a = "hello"
face = 0
take = 0
mode = "off"
os.system('cls')
try:
    os.system('cls')
    f = open("name.txt", "r")
    if f.mode == 'r':
        name = f.read()
    j = open("old.txt", "r")
    if j.mode == 'r':
        old = j.read()
except:
    print("What is your name?")
    speak.Speak("What is your name?")
    name = input()
    print("hello " + name)
    speak.Speak("hello" + name)
    os.system('echo|set /P ="' + name + '" > name.txt')
    print("How old are you?")
    speak.Speak("How old are you?")
    old = input()
    os.system('echo|set /P ="' + old + '" > old.txt')
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
        speak.Speak("your name is " + name)
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
    if "open" in you:
        print("file to open")
        try:
            fileopen = input()
            speak.Speak("open " + fileopen)
            os.startfile(fileopen)
        except:
            print("error program or file or folder not exist")
            speak.Speak("error program or file or folder not exist")
        run = True
    if "chrome" in you:
        speak.Speak("open chrome")
        try:
            os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        except:
            print("error program or file or folder not exist")
            speak.Speak("error program or file or folder not exist")
        run = True
    if "paint" in you:
        speak.Speak("open paint")
        try:
            os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint.lnk')
        except:
            print("error program or file or folder not exist")
            speak.Speak("error program or file or folder not exist")
        run = True
    if "store" in you:
        speak.Speak("open Microsoft store")
        try:
            os.startfile('ms-windows-store://home')
        except:
            print("error program or file or folder not exist")
            speak.Speak("error program or file or folder not exist")
        run = True
    if "calculator" in you:
        speak.Speak("open calculator")
        try:
            os.startfile('calculator:')
        except:
            print("error program or file or folder not exist")
            speak.Speak("error program or file or folder not exist")
        run = True
    if "map" in you:
        speak.Speak("open Microsoft map")
        try:
            os.startfile('bingmaps:')
        except:
            print("error program or file or folder not exist")
            speak.Speak("error program or file or folder not exist")
        run = True
    if "wheather" in you:
        speak.Speak("open Microsoft wheather")
        try:
            os.startfile('msnweather:')
        except:
            print("error program or file or folder not exist")
            speak.Speak("error program or file or folder not exist")
        run = True
    if "cut" in you:
        speak.Speak("open screen clip")
        try:
            time.sleep(3)
            os.startfile('ms-screenclip:')
        except:
            print("error program or file or folder not exist")
            speak.Speak("error program or file or folder not exist")
        run = True
    if "ask" in you:
        que = input("ask:")
        client = wolframalpha.Client("PQWP3V-L5L85UAKQ8")
        bot = client.query(que)
        answer = next(bot.results).text
        print(answer)
        speak.Speak(answer)
        run = True
    if "joke" in you:
        randomjoke = random.randint(1,2)
        if randomjoke == 1:
            print("Why do we tell actors to “break a leg?”")
            speak.Speak("Why do we tell actors to “break a leg?”")
            time.sleep(2)
            print("Because every play has a cast.")
            speak.Speak("Because every play has a cast.")
            run = True
        if randomjoke == 2:
            print("Why don’t scientists trust atoms?")
            speak.Speak("Why don’t scientists trust atoms?")
            time.sleep(2)
            print("Because they make up everything.")
            speak.Speak("Because they make up everything.")
            run = True
    if "math" in you:
        speak.Speak("open Microsoft math")
        print("open Microsoft math")
        os.system('start https://math.microsoft.com/')
        run = True
    if "read" in you:
        speak.Speak("open machine Comprehension Tasks")
        print("open machine Comprehension Tasks")
        os.system('start https://machinereading.azurewebsites.net/')
        run = True
    if "picture to html" in you or "image to html" in you:
        speak.Speak("open sketch2code")
        print("open sketch2code")
        os.system('https://sketch2code.azurewebsites.net/')
        run = True
    if "mail" in you and "to" in you:
        m = you[you.find("o")+1:]
        m = m.replace(" ", "")
        speak.Speak("send mail to " + m)
        print("send mail to " + m)
        os.system('start mailto:' + m)
        run = True
    if "open mail" in you:
        speak.Speak("open mail")
        print("open mail")
        os.system('start mailto:')
        run = True
    elif you == "":
        face = "bad"
        print("i don't understand?")
        speak.Speak("i don't understand?")
        run = True
