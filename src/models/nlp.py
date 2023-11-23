from .Predictive.predictive import Predictive
from .Text.voice_to_text import VoiceToText
from .Voice.text_to_voice import TextToVoice
from .Voice.variants import controller

from src.helpers.keywords import extract_keywords
from src.firebase.connection import get_questions
from src.helpers.context import extract_context
class NLP:
    def init_listener(self):
        voice = VoiceToText()
        return voice.init_listener()

    def process_question(self,question):
        keywords= extract_keywords(question)
        data = get_questions()
        context=extract_context(data,keywords)
        if context:
            return self.result_question(question,context)
        else:
            self.save_question(question)
            return "La pregunta no esta disponible, gracias por las nuevas sugerencias"
        
    def say_result(self,text):
        handle = TextToVoice(text,controller.default)
        handle.speak()

    def result_question(self,question,context):
        predictive = Predictive("mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es").get_model()
        data = predictive({'question': question,'context':context})
        # Sacamos la diferencia entre start y end y ordenamos en base a la direnrecia mas alta
        best_result = max(data, key=lambda x: x["end"] - x["start"])
        return best_result['answer'] 

    def save_question(self,question):
        print(question)
    
