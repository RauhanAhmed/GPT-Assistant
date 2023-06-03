# Importing required libraries and modules
import speech_recognition as sr
from .text_to_speech import TextToSpeech

# Creating a class SpeechToText
class SpeechToText:
    # Defining a constructor for the class
    def __init__(self):
        self.recognizer = sr.Recognizer()

    # Creating a method recognise to detect any input speach from the user 
    def recognise(self):
        try:
            with sr.Microphone() as source:
                audio_data = self.recognizer.record(source = source, duration = 5)
                text = self.recognizer.recognize_google(audio_data = audio_data, language = "en-IN")
                return text

        except:
            # Speaking to check for any internet connection in case of an issue
            obj = TextToSpeech()
            obj.speak("Please check your internet connection and try speaking again!")