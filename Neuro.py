from xml.etree.ElementTree import tostring
import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import sys
import operator
import json
import pyjokes
import pyautogui
import requests
import random
import pywikihow
from bs4 import BeautifulSoup
from datetime import timedelta
from time import sleep
from pywikihow import search_wikihow
from neurodesign import Ui_NeuroUI
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer ,QTime , QDate
from PyQt5.uic import loadUiType

engine = pyttsx3.init()
voices = engine.getProperty(('voices'))
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

voicespeed = 140
engine.setProperty('rate', voicespeed)
#test to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello sir I am Neuro. how can i help you")

# news
def news():
        apidict = {"bussiness": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3",
               "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3",
               "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3",
               "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3",
               "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3"
                }
        content = None
        url = None
        speak(
        "Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
        field = input("Type field news that you want: ")
        for key, value in apidict.items():
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
        for articles in arts:
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

# whatsapp message
def sendMessage():
        from datetime import datetime
        strTime = int(datetime.now().strftime("%H"))
        update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))
        speak("Who do you want to message")
        a = int(input('''person 1-madhu exit 2-exit'''))
        if a == 1:
            speak("Whats the message")
            message = str(input("Enter the message-"))
            pywhatkit.sendwhatmsg("+919390187768", message,time_hour=strTime, time_min=update)

        elif a == 2:
            pass

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.execution()
    
    # gamming with Neuro(rock,paper game)
    def game_play(self):
        speak("Lets Play ROCK PAPER SCISSORS !!")
        print("LETS PLAYYYYYYYYYYYYYY")
        i = 0
        Me_score = 0
        Com_score = 0
        while(i < 5):
            choose = ("rock", "paper", "scissors")  # Tuple
            com_choose = random.choice(choose)
            self.query = self.takecommand().lower()
            if (self.query == "rock"):
                if (com_choose == "rock"):
                    speak("ROCK")
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                elif (com_choose == "paper"):
                    speak("paper")
                    Com_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                else:
                    speak("Scissors")
                    Me_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

            elif (self.query == "paper"):
                if (com_choose == "rock"):
                    speak("ROCK")
                    Me_score += 1
                    print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

                elif (com_choose == "paper"):
                    speak("paper")
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                else:
                    speak("Scissors")
                    Com_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

            elif (self.query == "scissors" or self.query == "scissor"):
                if (com_choose == "rock"):
                    speak("ROCK")
                    Com_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                elif (com_choose == "paper"):
                    speak("paper")
                    Me_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                else:
                    speak("Scissors")
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            i += 1

        print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")

    #voice into text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        
        try:
            print("Recoginizing...")
            query= r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
        
        except Exception as e:
            #speak("say that again please...")
            return "none"
        query = query.lower()
        return query

    def execution(self):
        wish()
        while True:

            self.query=self.takecommand().lower()

            if 'open notepad' in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif 'close notepad' in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "open cmd" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                speak("SMILE")
                pyautogui.press("enter")

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your Ip address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia")
                query = self.query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)
            
            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")
            
            elif "google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"https://www.google.co.in/search?q={cm}")
            
            elif "whatsapp" in self.query:
                    sendMessage()

            elif "play song on youtube" in self.query:
                speak("sir, what song should i play in youtube")
                cm = self.takecommand().lower()
                pywhatkit.playonyt(f"{cm}")
            
            elif "play video on youtube" in self.query:
                speak("sir, what video should i play in youtube")
                cm = self.takecommand().lower()
                pywhatkit.playonyt(f"{cm}")
            
            elif "search" in self.query:
                query = self.query.replace("Neuro","")
                query = self.query.replace("search","")
                speak("searching...")
                speak(query)
                speak("in youtube")
                webbrowser.open("https://www.youtube.com/results?search_query="+self.query)

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            
            elif "news" in self.query:
                    news()
            
            elif "who are you" in self.query:
                    speak("I am Neuro, Made by Likhith, He is my Boss.")
                
            elif "play a game" in self.query:
                    self.game_play()

            elif "shut down system" in self.query:
                speak("shutting down in 5 secound")
                sleep(5)
                os.system("shutdown /s /t 5")
            
            elif "restart the system" in self.query:
                speak("restarting in 5 secound")
                sleep(5)
                os.system("shutdown /r /t 5")
            
            elif "sleep the system" in self.query:
                speak("logging out in 5 secound")
                sleep(5)
                os.system("shutdown - l")
            
            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                set.datetime(1)
                pyautogui.keyUp("alt")
            
            elif "hidden menu" in self.query:
                pyautogui.hotkey('winleft', 'x')
            
            elif "task manager" in self.query:
                pyautogui.hotkey('ctrl','shift','esc')
            
            elif "take screenshot" in self.query:
                pyautogui.hotkey('winleft','prtscr')
                speak("done")
            
            elif "snip" in self.query:
                pyautogui.hotkey('winleft','shift','s')
                speak('done')

            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name=input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of user {name}")
                speak("i am done sir,now i am ready for next command")

            elif "exit neuro" in self.query:
                speak("thanks for using me sir, have a good day.")
                speak("Neuro, powering off")
                sys.exit()
            
            elif "hello" in self.query or "hey" in self.query:
                speak("hello sir, may i help you with something.")
            
            elif "how are you" in self.query:
                speak("i am fine sir, what about you.")
            
            elif "also good" in self.query or "thanks" in self.query:
                speak("that's great to hear from you")
            
            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir.")
            
            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("okay sir, i am going to sleep you can call anytime.")
                break

            elif "temperature" in self.query:
                search = "temperature in patancheru"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}")

            elif "activate how to do" in self.query:
                speak("How to do mode is activated please tell me what you want to know")
                how = self.takecommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)
            

            elif 'volume up' in self.query:
                pyautogui.press("volumeup")
            
            elif 'volume down' in self.query:
                pyautogui.press("volumedown") 

            elif 'volume mute' in self.query:
                pyautogui.press("volumemute")
        


startExecution = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NeuroUI()
        self.ui.setupUi(self)

        self.ui.pushButton_start.clicked.connect(self.startTask)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_start_2.clicked.connect(self.youtube_app)
        self.ui.pushButton_start_3.clicked.connect(self.google_app)
        self.ui.pushButton_start_4.clicked.connect(self.vscode_app)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\likhi\\Desktop\\Neuro voice assistent\\gui themes\\Aqua.gif")
        self.ui.Gif_1.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

    
    def showtime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        label_name = tostring("Listening")
        self.ui.textBrowser_time.setText(label_time)
        self.ui.textBrowser_listen.setText(label_date)
        self.ui.temp.setText(label_name)

    def google_app(self):
        webbrowser.open("https://www.google.com")
    
    def youtube_app(self):
        webbrowser.open("https://www.youtube.com/")
    
    def vscode_app(self):
        os.startfile("C:\\Users\\likhi\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
    

app = QApplication(sys.argv)
Neuro_gui= Gui_Start()
Neuro_gui.show()
exit(app.exec_())
