
#Python Voice Search AI BOT - Abhi
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import win32com.client as wincl
import webbrowser
import requests as req

speak2 = wincl.Dispatch("SAPI.SpVoice")


 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
   
    data = ""
  
    try:
      
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def cordax(data):
    if "Google" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Abhi, I will open Google for you")
        speak2.Speak("Hold on Abhi, I will open Google for you")
        webbrowser.open("https://www.google.com")

    if "YouTube" in data:
        speak("Hold on Abhi, I will open YouTube for you")
        speak2.Speak("Hold on Abhi, I will open YouTube for you")
        webbrowser.open("https://www.youtube.com")

    

    if "Twitter" in data:
        speak("Hold on Abhi, I will open Twitter for you")
        speak2.Speak("Hold on Abhi, I will open Twitter for you")
        webbrowser.open("https://www.twitter.com")

    
    if "Facebook" in data:
        speak("Hold on Abhi, I will open Facebook for you")
        speak2.Speak("Hold on Abhi, I will open Facebook for you")
        webbrowser.open("https://www.facebook.com")


    if "search for" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Abhi, I will search for " + location + ".")
        speak2.Speak("Hold on Abhi, I will search for " + location + ".")
        webbrowser.open("https://www.google.com/search?q=" + location + "")

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Abhi, I will show you where " + location + " is.")
        speak2.Speak("Hold on Abhi, I will search for " + location + ".")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")



# initialization
time.sleep(2)
speak("Hi Abhi, What website do you want me to open")
speak2.Speak("Hi Abhi, What website do you want me to open")
while 1:
    data = recordAudio()
    cordax(data)
