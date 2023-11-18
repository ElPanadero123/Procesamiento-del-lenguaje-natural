from .voice import Voice
import pyttsx3

class Default(Voice):
    def speak(self,text):
        engine = pyttsx3.init()
        #configuracion de la voz 
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id) #entre 1 y 0 
        engine.say(text)
        engine.runAndWait()