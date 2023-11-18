import speech_recognition as sr

class VoiceToText:
    def init_listener(self):
        r = sr.Recognizer()
        with sr.Microphone(sample_rate=48000, chunk_size=1024) as source:
            audio = r.listen(source, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio, language="es-ES")
            except sr.UnknownValueError:
                text = False
            except sr.RequestError as e:
                print(e)
                text = False
            return text
