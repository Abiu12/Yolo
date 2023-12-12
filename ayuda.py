import pyttsx3
import threading
from googletrans import Translator

def speech_engine(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.startLoop(False)
    engine.iterate()
    engine.endLoop()

texto = "Hello, friend"
translator = Translator()
traduccion = translator.translate(texto, src='en', dest='es')
texto_en_espanol = traduccion.text
# Crear un hilo para reproducir el texto en segundo plano
thread = threading.Thread(target=speech_engine, args=(texto_en_espanol,))
thread.start()