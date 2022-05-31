import pyttsx3
engine = pyttsx3.init()
a=input("Enter words:")
engine.say(a)
engine.runAndWait()
