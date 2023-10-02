import pyttsx3

def convert_to_voice(text):
    engine = pyttsx3.init()
    #configuracion de la voz 
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id) #entre 1 y 0 
    engine.say(text)
    engine.runAndWait()