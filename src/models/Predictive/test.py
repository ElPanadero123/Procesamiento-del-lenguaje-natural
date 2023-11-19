from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline, GPT2LMHeadModel, GPT2Tokenizer

# Configuración del modelo de pregunta-respuesta
qa_model_name = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
qa_tokenizer = AutoTokenizer.from_pretrained(qa_model_name, do_lower_case=False)
qa_model = AutoModelForQuestionAnswering.from_pretrained(qa_model_name)

# Configuración del modelo de generación de lenguaje natural (GPT-2)
gpt_model_name = "datificate/gpt2-small-spanish"
gpt_tokenizer = GPT2Tokenizer.from_pretrained(gpt_model_name)
gpt_model = GPT2LMHeadModel.from_pretrained(gpt_model_name)

contexto = """
Desde su fundación en 1988, la Universidad del Valle se ha consolidado como una de las instituciones líderes en el sistema de educación superior boliviano. En virtud a ello, hoy consolida su presencia nacional con la construcción de primer campus Eco- Smart en la ciudad de Santa Cruz. Esta característica otorga muchas fortalezas y oportunidades para nuestros estudiantes, como la posibilidad de movilidad entre sedes y contar con los mejores docentes de toda Bolivia para cada área del conocimiento.
"""

# Configuración del pipeline de pregunta-respuesta
nlp = pipeline('question-answering', model=qa_model, tokenizer=qa_tokenizer)

def generar_respuesta_natural(pregunta, contexto, nlp, gpt_model, gpt_tokenizer):
    # Obtener la respuesta usando el modelo de pregunta-respuesta
    respuesta_qa = nlp({'question': pregunta, 'context': contexto})['answer']

    # Autocompletar la respuesta con GPT
    input_text = f"Pregunta: {pregunta}\nRespuesta: {respuesta_qa}\nContexto: {contexto}"
    input_ids = gpt_tokenizer.encode(input_text, return_tensors="pt")

    # Generar texto adicional
    max_length = len(input_ids[0]) + 50
    generated_text = gpt_model.generate(input_ids, max_length=max_length, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    # Decodificar y mostrar la respuesta generada
    respuesta_generada = gpt_tokenizer.decode(generated_text[0], skip_special_tokens=True)
    return respuesta_generada

# Función para preguntas y respuestas con contexto extendido
def pregunta_respuesta(contexto, nlp, gpt_model, gpt_tokenizer):
    # Imprimir contexto
    print('Contexto:')
    print('-----------------')
    print(contexto)

    # Loop preguntas-respuestas:
    continuar = True
    while continuar:
        print('\nPregunta:')
        print('-----------------')
        pregunta = str(input())

        continuar = pregunta != ''

        if continuar:
            # Obtener respuesta natural
            respuesta_natural = generar_respuesta_natural(pregunta, contexto, nlp, gpt_model, gpt_tokenizer)

            # Imprimir respuesta natural sin formato adicional
            print('\nRespuesta Natural:')
            print('-----------------')
            print(respuesta_natural)

            # Mostrar más contexto
            print('\nContexto extendido:')
            print('-----------------')
            inicio_respuesta = max(0, respuesta_natural.find("Contexto:") + len("Contexto:"))
            print(contexto[:inicio_respuesta] + respuesta_natural)

# Llamar a la función
pregunta_respuesta(contexto, nlp, gpt_model, gpt_tokenizer)
