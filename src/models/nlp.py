from .Predictive.predictive import Predictive
from .Text.voice_to_text import VoiceToText
from .Voice.text_to_voice import TextToVoice

class NLP:
    def init_listener(self):
        voice = VoiceToText()
        return voice.init_listener()

    def process_question(self,question,context):
        text = ""
        if(question):
            predictive = Predictive("mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es").get_model()
            data = predictive({'question': question,'context':context})
            # Ordena los resultados por start en orden ascendente y end en orden descendente
            best_results = sorted(data, key=lambda x: (x["start"], -x["end"]))
            text = best_results[0]["answer"]
            """ for item in best_results:
                text+=f"{item['answer']} | {item['start']} | {item['end']}\n-------------------\n" """
        else:
            text="Por favor ingrese una pregunta :D"
        return text
    
    def say_result(self,text):
        handle = TextToVoice(text,"default")
        handle.speak()
           

    
