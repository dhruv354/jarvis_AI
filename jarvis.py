import datetime
import random
import webbrowser
import os
import pyaudio
import pyttsx3
import speech_recognition as sr
import wikipedia

#print(help(pyttsx3), dir(pyttsx3))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe(name):
    current_hour = int(datetime.datetime.now().hour)
    if current_hour < 12 :
        speak('Good Morning sir')
    elif current_hour >= 12 and current_hour < 16:
       speak('Good Afternoon sir')
    else:
       speak('Good Evening sir')
    speak(f' how may i help you {name} sir')
    
def takeCommand():
    '''
    this function takes a particular command
    that you tell it to do through your voice
    
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try :
        print('Recognizing......')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said ...{query}')
    except Exception as e:
        print(e)
        print('pls say it again...')
        return "None"
    return  query

def sendEmail(to, content):
    

if __name__ == '__main__':
  #  audio = 'gungun is stupid, she looks like bear and her nose  is just like hippo'
  #  speak(audio)
    name = input()
    wishMe(name)
   # takeCommand()
    
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print('searching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=10)
            print(results)
            speak(results)
        
        elif 'youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')
            
        elif 'gmail' in query:
            speak('opening gmail')
            webbrowser.open('gmail.com')
        elif 'what is time' in query:
            current_time = datetime.datetime.now().strftime('%H/%M')
            print(current_time)
            speak(current_time)
        
        elif 'play music' in query:
            dir = 'f:\\music'
            songs = os.listdir(dir)
            #print(songs)
            os.startfile(os.path.join(dir, songs[0]))
            
        # elif ('stupid' or 'poor' or 'wrong' or 'waste') in query:
        #     speak('i am sorry sir, i cannot recognize your voice , please try again!, i will punish myself for it')
            
        # elif 'jarvis please stop' in query:
        #     speak('ok sir! thank you sir')
        #     break  
        
        elif 'email' in query:
            print('whom do you want to  send email?')
            #name of person
           
            try:
                name = takeCommand()
                email_id = id[name]
                print('pls tell me about the content')
                content = takeCommand()
                sendEmail(email_id, content)
                speak('email has been sent!')
            except Exception as e:
                print(e)
                speak('some error has occured!')
             
    
