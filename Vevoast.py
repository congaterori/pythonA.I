import os
import time
import calendar
#import win32com.client as wincl
#import pyaudio
#import googlesearch
#import wikipedia
#import speech_recognition as sr
#from PIL import Image
#from googlesearch import search
#speak = wincl.Dispatch("SAPI.SpVoice")
#r = sr.Recognizer()
a = "hello"
face = 0
take = 0
mode = "off"
os.system('clear')
print("What is your name?")
os.system('say What is your name?')
name = input()
print("hello " + name)
os.system('say hello' + name)
print("How old are you?")
os.system('say How old are you?')
old = input()
os.system('clear')
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
    '''
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
            ''
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
                    ''
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
    '''
    if mode == "off":
        you = input()
    if "voice" in you and "off" in you:
        mode = "off"
        os.system('say voice off')
        run = True
    '''
    if "voice" in you and "on" in you:
        mode = "on"
        os.system('say voice on')
        run = True
    '''
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
        os.system('say hello ' + name)
        run = True
    if "feel" in you:
        face = "happy"
        print("i'm good")
        os.system('say i am good')
        run = True
    if "your name" in you or "who are you" in you:
        face = "happy"
        print("my name is Vector")
        os.system('say my name is Vector')
        run = True
    if "my" in you and "name" in you:
        face = "happy"
        print("your name is " + name)
        os.system('say your name is ' +name)
        run = True
    if "good" in you:
        face = "happy"
        run = True
    if "bad" in you:
        face = "sad"
        print("boo!")
        os.system('say boo!')
        run = True
    if "old" in you and "you" in you:
        face = "happy"
        print("i don't have old!")
        os.system('say i don t have old!')
        run = True
    if "old" in you and "am" in you and "i" in you:
        face = "happy"
        print("you are " + old + " year old" )
        os.system('say you are' + old + 'say year old')
        run = True
    if "wikipedia" in you:
        print("search:")
        take = input()
        wiki = wikipedia.summary(take, sentences=5)
        print(wiki)
        os.system('say ' + wiki)
        run = True
    if "bye" in you or "exit" in you or "stop" in you or "close" in you:
        face = "happy"
        print("bye")
        os.system('say bye')
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
        #os.system('say ' + gio, phut)
        run = True
    if "date" in you:
        os.system('cal')
        run = True
    if "tell me a joke" in you:
        print("i'm not an A.I")
        os.system('say i am not an A.I')
        run = True
    if "who create you" in you:
        os.system('cls')
        print("i'm make by johnny20061234 the ideal by phucxo")
        os.system('say i am make by johnny20061234 the ideal by phucxo')
        f = open("create.txt", "r")
        print(f.read())
        time.sleep(5)
        os.system('cls')
        run = True
    if "favorite food" in you:
        face = "happy"
        print("my favorite food is iron")
        os.system('say my favorite food is iron')
        run = True
    if "favorite drinks" in you:
        face = "happy"
        print("my favorite drinks is soda")
        os.system('say my favorite drinks is soda')
        run = True
    if "favorite school" in you:
        face = "happy"
        print("my favorite school is Assistant school")
        os.system('say my favorite school is Assistant school')
        run = True
    if "wear" in you:
        face = "happy"
        print("I like to wear leather")
        os.system('say I like to wear leather')
        run = True
    if "Vector" in you or "vector" in you:
        face = "happy"
        print("i'm here")
        os.system('say i am here')
        run = True
    if "have an error" in you or "error" in you and "you" in you:
        face = "sad"
        print("yes i have an error is my name")
        os.system('say yes i have an error is my name')
        run = True
    if "do" in you and "hack" in you:
        face = "happy"
        print("no i'm not been hack")
        os.system('say no i am not been hack')
        run = True
    if "where" in you and "you" in you and "form" in you:
        face = "happy"
        print("i form Vietnam")
        os.system('say i form Vietnam')
        run = True
    if "where" in you and "you" in you and "live":
        face = "happy"
        print("i live in Vietnam sever")
        os.system('say i live in Vietnam sever')
        run = True
    if "favorite color" in you or "color" in you and "like" in you:
        face = "happy"
        print("my favorite colors is red and green")
        os.system('say my favorite colors is red and green')
        run = True
    if "do you" in you and "like" in you or "do you" in you and "favorite" in you:
        face = "happy"
        print("yes, i like")
        os.system('say yes, i like')
        run = True
    if "hot" in you or "cold" in you:
        face = "happy"
        print("i feel normal")
        os.system('say i fell normal')
        run = True
    if "have" in you and "hair" in you:
        face = "no"
        print("i'm not have hair")
        os.system('say i am not have hair')
        run = True
    if "connect" in you and "internet" in you:
        face = "happy"
        print("i can connect you can search google or wikipedia by say it")
        os.system('say i can connect you can search google or wikipedia by say it')
        run = True
    if "clear" in you or "clean" in you:
        os.system('cls')
        run = True
    if "love" in you and "me" in you:
        face = "happy"
        print("Maybe")
        os.system('say Maybe')
        import webbrowser; webbrowser.open('anime_lol.gif')
        '''
        im = Image.open("anime_lol.gif")
        im.seek(0)
        im.save("frame0.png")
        im.seek(1)
        im.save("frame1.png")
        im.seek(2)
        im.save("frame2.png")
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
            os.system('say open ' + fileopen)
            os.system('open ' + fileopen)
        except:
            print("error program or file or folder not exist")
            os.system('say error program or file or folder not exist')
    if "laund pad" in you:
        os.system('say open laund pad')
        os.system('open /Applications/Launchpad.app')
        run = True
    if "note stick" in you:
        os.system('say open note stick')
        os.system('open /Applications/Stickies.app')
        run - True
    if "dashboard" in you or "board" in you:
        os.system('say open Dashboard')
        os.system('open /Applications/Dashboard.app')
        run = True
    if "chess" in you:
        os.system('say open chess')
        os.system('open /Applications/Chess.app')
        run = True
    if "calculator" in you:
        os.system('say open calculator')
        os.system('open /Applications/Calculator.app')
        run = True
