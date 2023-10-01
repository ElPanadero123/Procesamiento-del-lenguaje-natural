## MODULO: PROCESAMIENTO DEL LENGUAJE
### 1. Transcripcion de voz a texto
```sh
- src
    └── voz
        └── voice_recognition.py
```
El archivo `voice_recognition.py` permite la transcripción de voz a texto en tiempo real utilizando el micrófono de la computadora y el servicio de reconocimiento de voz de Google. La función transcribe_audio() se encarga de capturar el audio, enviarlo al servicio de Google para su reconocimiento y devolver el texto reconocido como salida, ademas de esto se utilizo la libreria pyaudio, la cual permite la grabacion de audio en tiempo real.

### 2. Procesamiento de texto a voz 
```sh
- src
    └── voz
        └── convert.py
```
El archivo `convert.py` se encarga específicamente de la síntesis de voz. utiliza pyttsx3 para generar voz y reproducir esa voz. esto permite realizar la transcripcion de texto a voz en tiempo real.
### 3. Controlador
```sh
- src
    └── voz
        └── controller.py
```
El archivo `controller.py` actúa como el controlador principal del sistema de reconocimiento y conversión de voz. Su función es orquestar las operaciones de transcripción y conversión, y proporcionar una interfaz de usuario para interactuar con estas operaciones

### 4. Configuración del entorno desarrollo
Para poder ejecutar el programa es necesario tener instalado las librerias necesarias, para esto se puede utilizar el archivo `requirements.txt` que contiene todas las dependencias necesarias para la ejecucion del programa. Para instalar las dependencias se debe ejecutar el siguiente comando:
```sh
pip install -r requirements.txt
```
### 5. Ejecución del programa
Una vez que hayas configurado el entorno de desarrollo y hayas instalado las dependencias, puedes ejecutar el programa usando el siguiente comando:
```sh
python main.py
```