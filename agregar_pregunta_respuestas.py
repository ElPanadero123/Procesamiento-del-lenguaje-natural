while True:
    pregunta_usuario = input("Escribe tu pregunta (o escribe 'salir' para terminar): ")

    if pregunta_usuario.lower() == "salir":
        break

    respuesta_usuario = input("Escribe la respuesta a la pregunta: ")

    agregar_pregunta_respuesta(pregunta_usuario, respuesta_usuario)
    print(f"Pregunta y respuesta agregadas a Firestore.")

print("Hasta Luego.")