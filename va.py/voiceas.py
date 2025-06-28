import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Did not understand")
            return None

def speechtx(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change to voices[0].id if you want a male voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        text = sptext()
        if text is not None:
            if "hey neha" in text.lower():
                while True:
                    data1 = sptext()
                    if data1 is not None:
                        data1 = data1.lower()

                        if "your name" in data1:
                            speechtx("My name is Neha")
                        elif "how are you" in data1:
                            speechtx("I am fine")
                        elif "now time" in data1:
                            current_time = datetime.datetime.now().strftime("%I:%M %p")
                            speechtx(current_time)
                        elif 'youtube' in data1:
                            webbrowser.open("https://www.youtube.com/")
                        elif 'gpt' in data1:
                            webbrowser.open("https://chatgpt.com/")
                        elif "joke" in data1:
                            joke = pyjokes.get_joke(language="en", category="neutral")
                            print(joke)
                            speechtx(joke)
                        elif "i love you" in data1:
                            speechtx("I love you too")
                        elif "play song" in data1:
                            add = ""  # Specify the directory where your songs are located
                            if add:  # Ensure the directory is specified
                                listsong = os.listdir(add)
                                print(listsong)
                                if listsong:
                                    os.startfile(os.path.join(add, listsong[0]))
                                else:
                                    speechtx("No songs found in the specified directory.")
                            else:
                                speechtx("No directory specified for songs.")
                        elif "exit" in data1:
                            speechtx("Thank you")
                            time.sleep(15)  # Delay of 15 seconds before exiting
                            break
                    else:
                        print("Did not understand")
                break
        else:
            print("Did not understand")

    time.sleep(1)
    print("Thanks")
