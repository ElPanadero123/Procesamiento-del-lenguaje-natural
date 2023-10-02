import time
from .voice_recognition import transcribe_audio
from .convert import convert_to_voice

def start():
    reload=True
    while True:
        if(reload):
            transcription_result=transcribe_audio()
            reload=False
        if(transcription_result!=""):
            handle_request=int(input("Su transcripcion de audio fue procesada\n1: Escuchar transcripcion\n2: Ver texto de la transcripcion\n3: Iniciar otra transcripcion\n4: Salir del programa\nRespuesta: "))
        else:
            handle_request=int(input("No se pudo transcribir nada\n3: Iniciar otra transcripcion\n4: Salir del programa\nRespuesta: "))
        if(handle_request==1):
            convert_to_voice(transcription_result)
        elif(handle_request==2):
            print(transcription_result)
        elif(handle_request==3):
            reload=True
        elif(handle_request==4):
            print("saliendo...")
            time.sleep(1)
            break
        else:
            print("Comando no valido")

