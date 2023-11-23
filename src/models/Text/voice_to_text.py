import speech_recognition as sr

class VoiceToText:
    def init_listener(self):
        r = sr.Recognizer()
        with sr.Microphone(sample_rate=48000, chunk_size=1024) as source:
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=6)
                text = r.recognize_google(audio, language="es-ES")
            except:
                return False
            return text
