import os
import  speech_recognition as sr
import pyttsx3
import  webbrowser
import datetime
from groq import Groq
from config import apikey

chatStr = ""

def chat(query):
    global chatStr
    client = Groq(api_key=apikey)
    print(f"\nPrins: {query}\n")
    chatStr += f"Prins: {query}\n: "
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": chatStr}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        reasoning_effort="medium",
        stream=False
    )
    response = completion.choices[0].message.content
    print(f"Python: {response}\n")
    chatStr += f"{response}\n"
    say(completion.choices[0].message.content)
    return response




def ai(prompt):
    client = Groq(api_key=apikey)
    text = f"OpenAI response for prompt: {prompt} \n*******************************************\n\n"
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        reasoning_effort="medium",
        stream=False
    )

    text += completion.choices[0].message.content
    if not os.path.exists("Groqai"):
        os.mkdir("Groqai")
    filename = prompt.lower().split("using ai", 1)[1].strip() if "using ai" in prompt.lower() else prompt
    with open(f"Groqai/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"Use said: {query}")
            return query
        except Exception as e:
            return "Sorry Error Occurred. Sorry from Python."

if __name__ == "__main__":
    print('PyCharm')
    say("hello i am python a i")
    while True:
        print("Listening...")
        query = takecommand()
        sites = [["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music".lower() in query:
            print(f"Prins: {query}")
            print("Python: Playing music\n")
            say("Playing music")
            musicpath = r"C:\Users\prins\PycharmProjects\PyhtonAI\7120-download-iphone-6-original-ringtone-42676.mp3"
            os.startfile(musicpath)

        elif "the time".lower() in query:
            musicpath = r"C:\Users\prins\PycharmProjects\PyhtonAI\7120-download-iphone-6-original-ringtone-42676.mp3"
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"\nPrins: what is the time now")
            print(f"Python: Sir, the time is {strtime}\n")
            say(f"Sir the time is {strtime}")

        elif "open camera".lower() in query:
            print(f"Prins: {query}")
            print("Python: Opening camera\n")
            say("Opening camera")
            os.startfile("microsoft.windows.camera:")

        elif "Using AI".lower() in query.lower():
            ai(prompt=query)

        elif "Python Stop".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("chatting...")
            chat(query)

