import datetime as datetime
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import os
import smtplib
import openai
from config import apikey


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty(voices, voices[0].id)

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def  wish_me():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:
        speak("Good Morning")
        print("Good Morning")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
        
    else:
        speak("Good Evening")
        print("Good Evening")
    speak("I am Jarvis, How may I help you?")
    print("I am Jarvis, How may I help you?")


def takeCommand(): #it takes speech input and return output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please......")
        return "None"
    return query

if __name__ == "__main__":
    # speak("hey")
    wish_me()

    while True:
        query = takeCommand().lower()

        #logic for executing task based on query

        if 'wikipedia' in query:
            speak('Sure sir')
            speak('Searching Wikipedia .......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Sure sir')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Sure sir')
            webbrowser.open("google.com")

        elif 'leetcode' in query:
            speak('Sure sir')
            webbrowser.open("leetcode.com/problemset/all/")

        elif 'music' in query:
            speak('Sure sir')
            # Generate a random integer between a given range
            x = random.randint(0, 39)
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[x]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is : {strTime}")

        elif 'using artificial intelligence' in query:
            ai(prompt = query)

        elif "Jarvis exit".lower() in query.lower():
            exit()

        elif "vs code".lower() in query.lower():
            speak('Sure sir')
            os.startfile('C:\\Users\\pr141\\AppData\\Local\\Programs\\Microsoft VS Code\\Code')

        elif "pycharm".lower() in query.lower():
            speak('Sir, pycharm is already open')
            os.startfile('C:\\Users\\Public\\Desktop\\PyCharm Community Edition 2022.3.2.lnk')

        elif "data spell".lower() in query.lower():
            speak('Sure sir')
            os.startfile('C:\\Program Files\\JetBrains\\DataSpell 2023.1\\bin\\dataspell64.exe')

        elif "java".lower() in query.lower():
            speak('Sure sir')
            os.startfile('C:\\Users\\Public\\Desktop\\IntelliJ IDEA Community Edition 2022.3.3.lnk')
