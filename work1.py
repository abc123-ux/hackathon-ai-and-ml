import os
import time
import playsound
import speech_recognition as sr
import pyttsx3
from selenium import webdriver
import subprocess
import datetime
import wikipedia
import winsound
import requests
from pygame import mixer
import tkinter as tk
root=tk.Tk()
root.geometry('500x500')
root.title('BEEBO')
num = 1
def speak(output): 
   engine = pyttsx3.init()
   sound = engine.getProperty('voices')
   engine.setProperty('voice', sound[0].id)
   rate = engine.getProperty('rate')
   engine.setProperty('rate', 130)
   engine.say(output)
   engine.runAndWait()
   bot_lab3=tk.Label(root,text=("BEEBO: ", output),fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
    
def get_audio():
    r=sr.Recognizer()
    audio= ''
    with sr.Microphone() as source:
        bot_lab1=tk.Label(root,text="Speak...",font="Times 12 bold",fg='yellow',bg='green',width=20).pack(anchor="w")
        audio=r.listen(source , phrase_time_limit=8)
    bot_lab2=tk.Label(root,text="Stop.",fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
    

    try:
        said=r.recognize_google(audio , language="en-US")
        person_lab=tk.Label(root,text=("You:", said),fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="e")
        return said
    except:
        speak("Sorry, I didn't understand you. Please try again!")
        return 0

def search_web(input):
   driver = webdriver.Chrome()
   driver.implicitly_wait(1)
   driver.maximize_window() 
  
   if "youtube" in input:
      speak("Opening in youtube") 
      indx = input.lower().split().index('youtube') 
      query = input.split()[indx + 1:] 
      driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
      return 
  
   elif "google" in input:
      indx = input.lower().split().index('google') 
      query = input.split()[indx + 1:] 
      driver.get("https://www.google.com/search?q =" + '+'.join(query))
      return 
  
   elif "search" in input:
      indx = input.lower().split().index('google') 
      query = input.split()[indx + 1:] 
      driver.get("https://www.google.com/search?q =" + '+'.join(query))
      return
   else:
      driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))
      return
   
def open_application(input): 
  
    if "chrome" in input: 
        speak("Google Chrome") 
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome') 
        return
  
    elif "firefox" in input or "mozilla" in input: 
        speak("Opening Mozilla Firefox") 
        os.startfile('C:\Program Files\Mozilla Firefox\firefox.exe') 
        return
    else: 
        speak("Application not available") 
        return

def date():
    date = datetime.datetime.today()
    bot_lab4=tk.Label(root,text=date,fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
    return

def weather():
   api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
   city = get_audio()
   url = api_address + city
   json_data = requests.get(url).json()
   formatted_data =json_data["weather"][0]["description"]
   formatted_data2 =json_data["main"]["temp"]
   formatted_data2 =float(formatted_data2)
   formatted_data2 =formatted_data2 - 273.15
   formatted_data3 =json_data["wind"]["speed"]
   formatted_data4 =json_data["sys"]["country"]
   formatted_data5 =json_data["name"]
   formatted_data6 =json_data["coord"]["lon"]
   formatted_data7 =json_data["coord"]["lat"]

   bot_lab5=tk.Label(root,text=("The Sky:",formatted_data),fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
   bot_lab6=tk.Label(root,text=("The Temperature is: ",formatted_data2,"°C"),fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
   bot_lab7=tk.Label(root,text=("The Speed of the Wind is: ",formatted_data3,"m/s"),fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
   bot_lab8=tk.Label(root,text=("Country: ",formatted_data4),fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
   bot_lab9=tk.Label(root,text=("City: ",formatted_data5),fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
   bot_lab10=tk.Label(root,text=("Longitude: ",formatted_data6,"°"),fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
   bot_lab11=tk.Label(root,text=("Latitude: ",formatted_data7,"°"),fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
   bot_lab12=tk.Label(root,text="",fg='yellow',font="Times 12 bold",bg='green',width=20).pack(anchor="w")
   return
      
def calm(): 
    
    mixer.init() 
    mixer.music.load("calm.mp3") 
    mixer.music.set_volume(0.1) 
    mixer.music.play() 


    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break

         
def inspiration(): 
    
    mixer.init() 
    mixer.music.load("inspire.mp3") 
    mixer.music.set_volume(0.5) 
    mixer.music.play() 


    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break

def dramatic(): 
    
    mixer.init() 
    mixer.music.load("dramatic.mp3") 
    mixer.music.set_volume(0.5) 
    mixer.music.play() 


    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break
         
def fun(): 
    
    mixer.init() 
    mixer.music.load("FUN.mp3") 
    mixer.music.set_volume(0.5) 
    mixer.music.play() 


    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break
         
def rock():
    
    mixer.init() 
    mixer.music.load("rock.mp3") 
    mixer.music.set_volume(0.4) 
    mixer.music.play() 


    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break
def mysterious():
    
    mixer.init() 
    mixer.music.load("arrow.mp3") 
    mixer.music.set_volume(0.4) 
    mixer.music.play() 


    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break
         
def motivated():
    
    mixer.init() 
    mixer.music.load("sleep.mp3") 
    mixer.music.set_volume(0.1) 
    mixer.music.play() 


    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break
         
def sleep_music():
     
    mixer.init() 
    mixer.music.load("sleep2.mp3") 
    mixer.music.set_volume(0.1) 
    mixer.music.play() 


    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break
         
def happy():
    
    mixer.init() 
    mixer.music.load("motivational.mp3") 
    mixer.music.set_volume(0.1) 
    mixer.music.play() 


    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break

def peace():
    
    mixer.init() 
    mixer.music.load("panic.mp3") 
    mixer.music.set_volume(0.1) 
    mixer.music.play() 

    while True:
        print("Type p to pause , r to resume") 
        print("Type e to exit the program")
        print("Type n to play another song")
        query = input("Command:") 
        if "p" in query: 
            mixer.music.pause()  
        elif "r" in query: 
            mixer.music.unpause()
        elif "n"in query:
           mixer.music.stop() 
           next_music()
        elif "e" in query: 
            mixer.music.stop() 
            break
         
def music():
    speak("What kind of music would you like to listen to?")
    print("1.Slow/calm music.")
    print("2.Happy/Fun music.")
    print("3.Motivational/inspirational music.")
    print("4.Rock music.")
    print("5.Dramatic music")
    print("6.Mysterious music")
    f=get_audio().lower()
    if "slow" in f or "calm" in f:
        calm()
        return
    elif "happy" in f or "funny" in f:
        fun()
        return
    elif "motivational" in f or "inspirational" in f:
        inspiration()
        return
    elif "rock" in f:
        rock()
        return
    elif "dramatic" in f:
        dramatic()
        return
    elif "mysterious" in f:
        mysterious()
        return
    else:
        speak("Sorry , that's unavailable at the moment.")
        return
    return

def next_music():
    speak("What else would you like to listen to?")
    print("1.Slow/calm music.")
    print("2.Happy/Fun music.")
    print("3.Motivational/inspirational music.")
    print("4.Rock music.")
    print("5.Dramatic music")
    print("6.Mysterious music")
    f=get_audio().lower()
    if "slow" in f or "calm" in f:
        sleep_music()
        calm()
        happy()
        return
    elif "happy" in f or "funny" in f:
        fun()
        return
    elif "motivational" in f or "inspirational" in f:
        inspiration()
        return
    elif "rock" in f:
        rock()
        return
    elif "dramatic" in f:
        dramatic()
        return
    elif "mysterious" in f:
        mysterious()
        return
    else:
        speak("Sorry , that's unavailable at the moment.")
        return
    return
   
def note(text):
    date=datetime.datetime.now()
    file_name=str(date).replace(":","-")+"note.txt"
    with open(file_name,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])
    return
   
def stress():
    speak("That's not good. This can be dealt with by something called the Coping Space.")
    speak("The first step is about becoming aware of your thoughts, feelings and body sensations. Ask yourself , What am I thinking and feeling right now? I promise I won't judge. Take a moment to observe what's stressing you and how it makes you feel.")
    speak("The second step is to Bring your focus to your breath and the part of your body, where you can feel the stress most clearly. It could be your belly, chest or nostrils. Now close your eyes and keep this concentrated focus for a while.")
    speak("The third step is to widen your attention to your whole body. Try to include all the sensations of both sitting and breathing. Take it slow. Close your eyes now and do this for another minute before you end this exercise. It may take a bit of practice until you feel all the benefits.")
    speak("Do you want me to play some calming music for you?")
    p=get_audio().lower()
    while(True):
        if "yeah" in p or "yes" in p or "sure" in p:
            calm()
            speak("Hope you're feeling better now :)")
            return
        elif "no" in p:
            speak("Okay then.")
            speak("Hope you're feeling better now :)")
            return
    

def worry():
    speak("Sounds like you're having trouble with anxious thoughts.")
    speak("Now think of what you're worried about and type it out.")
    t1=input("What are you worried about?:")
    x=str(t1)
    speak("Take a moment to think about your problem.")
    speak("What makes you think this problem is worrying? ")
    t2=input("Why is this problem worrying?:")
    y=str(t2)
    speak("Now try to come up with reasons why this problem isn't a big deal.")
    t3=input("Why isn't this problem a big deal?:")
    z=str(t3)
    speak("So your problem is "+x)
    speak("and you think this is a problem because "+y)
    speak(" but you don't need to worry about it because "+z)
    speak("Sometimes we believe we need to worry to prevent bad things from happening, but this doesn't need to be the case.")
    speak("One skill to master is to try and accept the uncertainty in our lives. Life would certainly be quite boring if we always had control over the outcome , so try to use these moments as a chance to embrace the unknown and forgive yourself for any wrong decisions you make that lead to these moments")
    speak("Would you like me to play some motivational music for you?")
    q=get_audio().lower()
    while(True):
        if "yeah" in q or "yes" in q or "sure" in q :
            motivated()
            speak("Hope you're feeling better now :)")
            return
        elif "no" in q:
            speak("Okay then.")
            speak("Hope you're feeling better now :)")
            return
def panic():
    speak("Try this breathing technique. Inhale for 4 seconds, hold your breath for 7 seconds, and exhale for 8 seconds.")
    speak("Repeat this a few times. After some time you'll start feeling better.")
    speak("Would you like me to play some calming music for you?")
    r=get_audio().lower()
    while(True):
        if "yeah" in r or "yes" in r or "sure" in r:
            peace()
            speak("Hope you're feeling better now :)")
            return
        elif "no" in r:
            speak("Okay then.")
            speak("Hope you're feeling better now :)")
            return

def sleep():
    speak("Let me tell you a few steps that could help you")
    speak("Start by breathing out all the air completely from your lungs , then breathe in quietly to the count of 4 . Hold your breath there for a full 7 seconds , then exhale through your mouth for a count of 8. Repeat at least 4 times, or as many times as needed for your entry to dreamland ")
    speak("Would you like me to play some music to help you sleep?")
    s=get_audio().lower()
    while(True):
        if "yeah" in s or "yes" in s or "sure" in s:
            sleep_music()
            speak("Hope you're feeling better now :)")
            return
        elif "no" in s:
           speak("Okay then.")
           speak("Hope you're feeling better now :)")
           return
def procrast():
    speak("I totally get it , procrastination can really be a tough habit to break sometimes. There are lots of reasons why you might have that pestering voice leading you to procrastinate. Being productive isn't about feeling like it , in fact, if we only did things we felt like doing , we probably wouldn't do much of anything! Rather than give in to the feeling , try to just acknowledge that you don't want to do something without judging yourself or assuming that you need to enjoy the task in order to do it. You got this. Good luck out there!")
    speak("Would you like me to play some calming music for you?")
    t=get_audio().lower()
    while(True):
        if "yeah" in t or "yes" in t:
            motivated()
            speak("Hope you're feeling better now :)")
            return
        elif "no" in t:
            speak("Okay then.")
            speak("Hope you're feeling better now :)")
            return
def process_text(input):
    try:

       if 'search' in input or 'google' in input or "youtube" in input:
            search_web(input)
            return
       elif "who are you" in input:
          speak( "Hello I am BEEBO , your personal mental healthcare companion.")
          return
       elif "who made you" in input  or "who created you" in input or "who were you created by" in input:
          speak("I have been created by Abishek Bhatia , Abhinav Krishna and Raghav Vivek.")
          return
       elif "abbreviation" in input:
          speak("The abbreviation for my name is , Binary Engineered Emotionally Beneficial Organism.")
          return
       elif "date" in input or "today's date" in input or "time" in input:
          speak("Here it is.")
          date()
          print("")
          return
       elif "open" in input:
          open_application(input.lower())
          return
       elif "note" in input or "write this down" in input:
          speak("what would you like me to note?")
          i=get_audio().lower()
          note(i)
          speak("Done , note taken.")
          return
       elif "wikipedia" in input:
          speak('Searching Wikipedia...')
          input= input.replace("wikipedia", "")
          results = wikipedia.summary(input, sentences = 3)
          speak("According to Wikipedia")
          print(results)
          speak(results)
          return
       elif "weather" in input:
          speak("Which city's weather do you want to know?")
          weather()
          speak("Here it is!")
          print("")
          return
       elif "stressed" in input or "stress" in input:
          stress()
          speak("If not , you could call some helpline numbers for immediate assisstance. Would you like me to show you a list?")
          v=get_audio().lower()
          while (True):
             if "yes" in v or "yeah" in v:
                os.system("start \"\" https://thelivelovelaughfoundation.org/helpline.html")
                break
             elif "no" in v:
                speak("Alrighty then.")
                speak(" On the other hand , if you need one-on-one exclusive interaction , I could find you some therapists.")
                k=get_audio().lower()
                while (True):
                   if "yes" in k or "sure" in k:
                      os.system("start \"\" https://thelivelovelaughfoundation.org/therapist.html")
                      return
                   elif "no" in k:
                      speak("Okay then. A good day to you!")
                      return
       elif "worried" in input or "upset" in input:
          worry()
          return
       elif "panic" in input or "attack" in input:
          panic()
          speak("If not , you could call some helpline numbers for immediate assisstance. Would you like me to show you a list?")
          w=get_audio().lower()
          while (True):
             if "yes" in w or "sure" in w:
                os.system("start \"\" https://thelivelovelaughfoundation.org/helpline.html")
                return
             elif "no" in w:
                speak("Alright then.")
                return
          speak(" On the other hand , if you need one-on-one exclusive interaction , I could find you some therapists.")
          k=get_audio().lower()
          while (True):
             if "yes" in v or "sure" in v:
                os.system("start \"\" https://thelivelovelaughfoundation.org/therapist.html")
                return
             else:
                speak("Alright then. A good day to you!")
                return
       elif "sleeping" in input or "can't sleep" in input:
          sleep()
          return
       elif "procrastinate" in input or "procrastinating" in input:
          procrast()
          return
       elif "exit" in input or "bye" in input:
          speak("A good day to you")
          sys.exit()
       elif "music" in input:
          music()

       else:
          speak("I'm sorry , I didn't get you. Do you want me to look it up?")
          ans=get_audio().lower()
          if 'yes' in str(ans) or "yeah" in str(ans):
             search_web(input)
          else:
             return
    except:
       speak("Sorry")
        
    
  
WAKE = "Vivo"

if  __name__ == '_main_':
    text = get_audio()
    if text.count(WAKE)> 0:
        speak("Hello , I am Beebo, your personal mental healthcare companion.")

        while(1):
            speak("How may I help you?")
            print("1.I feel stressed out.")
            print("2.I'm having a panic attack.")
            print("3.I'm having trouble sleeping.")
            print("4.I'm worried about something.")
            print("5.I'm procrastinating(not motivated enough to work)")
            print("7.I need to listen to some music.")
            print("8.I need you to take a note.")
            print("9.I need you to tell me the weather.")
            print("10.Other (Search the web, Open chrome etc.")
            text2=get_audio().lower()
            if text2==0:
                continue
            if "exit" in str(text2) or "bye" in str(text2) or "see you later" in str(text2) or "stop" in str(text2) :
                speak("A good day to you.")
                break
            process_text(text2)
root.mainloop()