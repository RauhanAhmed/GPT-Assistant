# Importing required libraries and modules
from gpt_assistant import SpeechToText, TextToSpeech, ChatGPTResponse
from kivy.lang import Builder
from kivymd.app import MDApp
from threading import Thread
from time import sleep

# Creating a class GPT_Assistant to create the app overiding the MDApp class
class GPT_Assistant(MDApp):
    # Defining a build method to load the kv file
    def build(self):
        self.title = "ELLA : The AI Assistant"
        self.icon = r"artifacts\LOGO - DARK.png"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('kivy_file.kv')
    
    # Defining change_theme method for change theme functionality
    def change_theme(self, instance):
        if self.theme_cls.theme_style == "Light" :
            self.root.ids.logo_image.source = r"artifacts\LOGO - LIGHT.png"
            self.theme_cls.theme_style = "Dark"
            self.root.ids.label.text_color = 1, 1, 1, 1
        elif self.theme_cls.theme_style == "Dark" :
            self.root.ids.logo_image.source = r"artifacts\LOGO - DARK.png"
            self.theme_cls.theme_style = "Light"
            self.root.ids.label.text_color = 0, 0, 0, 1

    # Defining a method to change label text
    def change_label_text(self, text : str, time : int):
        self.root.ids.label.text = text
        sleep(time)
        self.root.ids.label.text = ""

    # Defining method to use the gpt-assitant module combined with text to speech and speech to text
    def button_press(self):        
        stt = SpeechToText()
        query = stt.recognise()

        try :
            gpt = ChatGPTResponse()
            response = gpt.generate_response(query)
            if response != None:
                tts = TextToSpeech()
                tts.speak(response)
        except RuntimeError:
            # Using threading to display a message in case bombardment of prompts to the assistant
            Thread(target=self.change_label_text, args= ("Please let me complete...", 2)).start()

if __name__ == "__main__":
    GPT_Assistant().run()