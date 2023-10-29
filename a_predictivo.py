import firebase_admin
 
from firebase_admin import credentials, firestore
 
from voz.voice_recognition import transcribe_audio
from voz.convert import convert_to_voice
 
# Ruta a tu clave privada
ruta_clave_privada = {"<>"
}
 
# Inicializa Firebase con la clave privada
if not firebase_admin._apps:
    cred = credentials.Certificate(ruta_clave_privada)
    firebase_admin.initialize_app(cred)
else:
    print("La aplicación de Firebase ya está inicializada.")
 
# Obtiene una referencia a la base de datos Firestore
db = firestore.client()
 
# Funciones para agregar y obtener preguntas y respuestas
def agregar_pregunta_respuesta(pregunta, respuesta):
    db.collection("preguntas_respuestas").add({
        "pregunta": pregunta,
        "respuesta": respuesta
    })
 
def obtener_respuesta(pregunta):
    preguntas_ref = db.collection("preguntas_respuestas")
    query = preguntas_ref.where("pregunta", "==", pregunta).limit(1)
    results = query.stream()
    result=""
    for result in results:
        result=str(result.to_dict()["respuesta"])
    print(result)
    if result != "":
        return result
    else:
        result="Pregunta no encontrada"
    return result
 
def integration():
    request=transcribe_audio()
    print(f"Pregunta: {request}")
    result_request=obtener_respuesta(request)
    convert_to_voice(result_request)
 
 
integration()