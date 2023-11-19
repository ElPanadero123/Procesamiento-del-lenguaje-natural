from textwrap import wrap
import time
from src.models.nlp import NLP


instance = NLP()

context = """
Darlin Ortiz Pimentel es la persona encargada de hacer los tramites, archivos y habilitaciones de la universidad. Para los estudiantes regulares, existen diversas becas disponibles, entre ellas la BECA EXCELENCIA ACADEMICA, BECA CONVENIOS INSTITUCIONALES, BECA AYUDANTIA, BECA TRABAJO, BECA DEPORTE y BECA CULTURA.
Los horarios de atención de las oficinas de trámites y archivos son de lunes a viernes, de 08:00 a 13:00 y de 14:00 a 18:00 horas. Para obtener un Certificado de Alumno Regular, se deben presentar requisitos como una fotocopia del carnet de identidad y llevar en mano el carnet de estudiante, dirigiéndose a la oficina de trámites y archivos ubicada en la planta baja, módulo 1 (Diagonal a plataforma de información).
Los horarios de atención de cajas y dirección de carrera son de lunes a viernes, de 08:00 a 13:00 y de 14:00 a 17:00 horas. Mientras que las plataformas de información tienen un horario de atención de lunes a viernes, de 08:00 a 18:00 horas, y los sábados de 09:00 a 12:00 horas.
"""


def pregunta_respuesta(contexto):
    print('Contexto:')
    print('\n'.join(wrap(contexto)))
    # Loop preguntas-respuestas
    continuar = True
    question=""
    while continuar:
        print("Iniciar: 1\nSalir: 2")
        handle_input=int(input())
        if handle_input==1:
            print("Se inicio la transcripcion")
            question=NLP.init_listener()
            print(f"Pregunta:\n{question}")
            if question:
                result_question = instance.process_question(question,context)
                print(f"Resultado:\n{result_question}")
                instance.say_result(result_question)
        elif handle_input==2:
            print("saliendo...")
            time.sleep(1)
            break

pregunta_respuesta(context)