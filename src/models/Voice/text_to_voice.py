class TextToVoice:
    def __init__(self,text,type):
        self.text=text
        self.type=type

    def speak(self):
        self.type.speak(self.text)