from openai import OpenAi
#from apiKey import api_data 
import os 
import speech_recognition as sr # converts my voice commands to text
import pyttsx3 # convert out output to voice
import webbrowser

Model="gpt-4o"
client=OpenAi(api_key=api_data)

def Reply(question):
    completion=client.chat.completions.create(
        model=Model,
        message=[
            {'role':"system","content":"You are a helpful assistant"},
            {'role':'user','content':question}
        ],
        max_tokens=200
    )
    answer=completion.choices[0].message.content
    return answer 

# text to speech
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello How are you?")

def takeCommand():
    r=sr.Recogniser()
    with sr.Microphone as source:
        print('Listening ........')
        r.pause_threshold=1 # wait for 1 sec before considering the end of a phrase
        audio = r.listen(source)
    try:
        print('Recognizing .....')
        query = r.recognize_google(audio, language = 'en-in')
        print("user  Said: {}\n".format(query))
    except Exception as e:
        print("Say that again .....")
        return "None"
    return query

if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        if query == 'none':
            continue 

        ans  = Reply(query)
        print(ans)
        speak(ans)


        # Specific browser related  Tasks 
        if "Open youtube" in query:
            webbrowser.open('www.youtube.com')
        if "Open Google" in query:
            webbrowser.open('www.google.com')
        if 'bye' in query:
            break
        