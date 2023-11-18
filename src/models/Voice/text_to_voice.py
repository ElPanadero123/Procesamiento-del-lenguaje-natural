from .variants.default import Default
from .variants.standard import Standard


class TextToVoice:
    def __init__(self,text,type):
        self.text=text
        self.type=type

    def speak(self):
        types_voice={
            "default":Default(),
            "standard":Standard()
        }
        builder=types_voice.get(self.type)
        builder.speak(self.text)