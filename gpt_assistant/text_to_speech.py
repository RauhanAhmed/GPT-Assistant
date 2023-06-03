# Importing the modules
import pyttsx3

class TextToSpeech:
    # Defining class constructor
    def __init__(self):
        # Initialising the pyttsx3 engine object       
        self.engine = pyttsx3.init() 

    def speak(self, sentence:str):
        # Setting up speaking rate
        self.engine.setProperty("rate", 150)
        # Setting up voice
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)  
        # To speak a prompt
        self.engine.say(sentence)
        self.engine.runAndWait()
        self.engine.stop()