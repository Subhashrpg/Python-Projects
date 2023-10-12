import pyttsx3
import speech_recognition as sr

# creating environment for speak function
speak_command = pyttsx3.init("sapi5")
voices = speak_command.getProperty("voices")
speak_command.setProperty("voice", voices[0].id)


# speak function
def speak(text):
    speak_command.say(text)
    speak_command.runAndWait()


# takecommand
def takecommand():
    engine = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning.......")
        engine.pause_threshold = 1
        audio = engine.listen(source)
        try:
            print("Recognizing...")
            query = engine.recognize_bing(audio,language="en-US")
            return query
        except Exception as e:
            return "none"