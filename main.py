#
import speech_recognition as sr
import datetime
import pocketsphinx

r=sr.Recognizer()

def googlelisten():
    with sr.Microphone() as source:

        audio=r.listen(source)

        command= r.recognize_google(audio)
        return command
while True:
    command=googlelisten()
    print(command)
    break

