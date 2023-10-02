import speech_recognition as sr

def transcribe_audio():

    # Inicializa reconocedor
    r = sr.Recognizer()

    # Escucha el audio desde el micrófono
    with sr.Microphone() as source:
        print("Se inicio la transcripcion:")
        audio = r.listen(source)
        
    # Transcribe audio a texto    
    try:
        text = r.recognize_google(audio, language="es-ES")
        
    except sr.UnknownValueError:
        text = ""

    except sr.RequestError as e:
        print("No pude solicitar resultados del servicio de speech recognition; {0}".format(e))
        text = ""

    return text
