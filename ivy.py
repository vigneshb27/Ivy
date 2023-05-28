import os
import platform
import random
from os import system
import datetime
import json
from files.advice import advise
import subprocess
from log import log_data
from files.wiki_search import search
from files.check_weather import weather
import pyjokes
import pyttsx3
import speech_recognition as sr
from colorama import Fore
from files.youtube import youtube
from files.stocks import stocks
from files.cricket import cricket_score
from files.site_opener import opener
from model.chat import ivy

Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.LIGHTWHITE_EX
G = Fore.GREEN
R = Fore.RED

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


with open('config.json' , 'r') as f:
    data = json.loads(f.read())

user_name= data['NAME']
music_dir = data['MUSIC']


def print_msg(logo='+', msg=''):
    print(f'{W}[{C}{logo}{W}] {Y}{msg}')


def cal_date():
    date = datetime.datetime.now().strftime('%H:%M:%S  -  %D')
    print_msg(logo=f'{Y}>', msg=f'{W}' + str(date))


def clear():
    system('cls') if 'Windows' in platform.platform() else system('clear')
    cal_date()


clear()

log_file = 'logs/log.txt'
dir = music_dir

garbage = ''


def speak(something):
    print(f'{R}({W}+_+{R}) {Y}{something}')
    engine.say(something)
    engine.runAndWait()


def greet():
    speak('Welcome back Sir')
    speak("Iam Ivy, Tell me how can i help you?")


def printWithSeak(msg):
    print(msg)
    speak(msg)


def playSong(d=dir):
    files = os.listdir(d)

    index = random.randint(0, len(files) - 1)

    print(f'Playing {files[index].replace("_", " ")}')
    os.startfile(d + files[index])


def speakInput():
    print("[+] Listening", end="\r")
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.pause_threshold = 1
        listen = rec.listen(mic)
    try:
        print("[►] Recognizing... ", end='\r')
        query = rec.recognize_google(listen, language='en-IN')
        print(f"Query: {query}")
        query = query.lower()
    except Exception as e:
        return 'None'
    return query.lower()


def menu_of_Files(d):
    files = os.listdir(d)
    for i, file in enumerate(files):
        print_msg(logo=str(i), msg=file)
    speak('Select song number')
    index_of_file = int(speakInput().replace('play', "").replace(' ', ''))
    os.startfile(d + files[index_of_file])


greet()

def main():
    global garbage
    while True:
        output = speakInput()
        response, tag = ivy(output)

        if tag == 'youtube':
            speak(response)
            youtube(output)

        elif tag == 'weather':
            speak(response)
            #speak('searching')
            
            speak('Tell me city name sir')
            city = speakInput()
            try:
                garbage = weather(city)
                printWithSeak(garbage)
            except Exception as e:
                printWithSeak(e)

        elif tag == 'play_song':
            speak(response)
            playSong()

        elif tag == 'open_music_folder':
            speak(response)
            menu_of_Files(music_dir)

        elif tag == 'website':
            speak(response)
            q = output.split().index('website')
            opener(output)

        elif tag == 'datetime':
            date = datetime.datetime.now().strftime('%H:%M:%S')
            printWithSeak(date)
            day = datetime.datetime.now().strftime('%A')
            printWithSeak(f'Today is {day}')

        elif tag == 'note':
            speak(response)
            note = speakInput()
            log_data(data=note, log_file=log_file)

        elif tag == 'greeting':

            speak(response)

        elif 'task manager' in output:
            speak("opening task manager sir")
            man_path = r'C:\Windows\system32\Taskmgr.exe'
            os.startfile(man_path)

        elif 'shutdown system' in output:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif tag == 'joke':
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'system status' in output or 'performance status' in output:
            pass
        elif tag == "identity":
            speak(response)

        elif tag == "advice":
            speak(advise())

        elif tag == 'stock':
            speak(response)
            speak(stocks())

        elif tag == 'cricket':
            speak(response)
            speak(cricket_score())
        
        elif tag == "goodbye":
            speak(response)
            exit(0)
        
        elif tag == "thank_you":
            speak(response)
        
        elif tag == 'search':
            garbage = search(output)
            speak(garbage)

        else:
            pass


try:
    main()
except Exception as e:
    printWithSeak(e)
    speak(' Sir ,Do you want to exit')
    check = speakInput().lower()
    if check == 'yes':
        exit(0)
    else:
        main()
