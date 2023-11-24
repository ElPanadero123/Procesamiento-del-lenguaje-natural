from textwrap import wrap
import time
from src.models.nlp import NLP


instance = NLP()
def pregunta_respuesta():
    # Loop preguntas-respuestas
    continuar = True
    while continuar:
        print("Bienvenido al asistente de univalle\nIniciar: 1\nSalir: 2")
        handle_input=int(input())
        if handle_input==1:
            print("Se inicio la transcripcion")
            question = instance.init_listener()
            print(f"Pregunta:\n{question}")
            if question:
                result_question = instance.process_question(question)
                print(f"Resultado:\n{result_question}")
                instance.say_result(result_question)
        elif handle_input==2:
            print("saliendo...")
            time.sleep(1)
            break

pregunta_respuesta()