from .Predictive.predictive import Predictive
from .Text.voice_to_text import VoiceToText
from .Voice.text_to_voice import TextToVoice
from .Voice.variants import controller
class NLP:
    def init_listener():
        voice = VoiceToText()
        return voice.init_listener()

    def process_question(self,question,context):
        text=""
        predictive = Predictive("mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es").get_model()
        data = predictive({'question': question,'context':context})
        # Sacamos la diferencia entre start y end y ordenamos en base a la direnrecia mas alta
        best_result = max(data, key=lambda x: x["end"] - x["start"])
        text+=f"{best_result['answer']}"
        return text
    
    def say_result(self,text):
        handle = TextToVoice(text,controller.default)
        handle.speak()
           

    
