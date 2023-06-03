# Importing required libraries and modules
import openai
from .text_to_speech import TextToSpeech

# Creating a class ChatGPTResponse with necessary methods
class ChatGPTResponse:
    # Defining class constructor
    def __init__(self):
        self.prompt = None
        self.messages = []
        MY_API_KEY = "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"
        openai.api_key = MY_API_KEY

    # Defining a method generate_response which uses the openai api
    def generate_response(self, prompt):
        try :
            self.prompt = prompt
            self.messages.append({"role" : "user", "content" : self.prompt})

            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",          # Using the latest GPT model
                messages = self.messages,
                max_tokens = 100                # Specifying max tokens to use as 100
            )
            response = completion.choices[0].message.content
            self.messages.append({"role":"assistant", "content":response})
            return response
        
        except Exception as e:
            # Speak to check for any internt connectivity issues in case of error
            obj = TextToSpeech()
            obj.speak("Please check your internet connection and try speaking again!")