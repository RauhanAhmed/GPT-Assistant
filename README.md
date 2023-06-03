# GPT-Assistant
This is a desktop application that acts as an assistant with speaking and listening capabilities. It utilizes the OpenAI API for natural language processing, the pyttsx3 library for text-to-speech functionality, the speech-recognition module for speech-to-text functionality, and the KivyMD framework for creating a desktop application.

## Installation
1. Clone the repository
```
git clone https://github.com/rauhanahmed/gpt-assistant.git
```
2. Change to the project directory
```
cd gpt-assistant
```
3. Create a virtual environment using python version 3.9
```
conda create --name assistant python=3.9
```
4. Install the required dependencies
```
pip install -r requirements.txt
```

## Configuration
Before running the application, you need to set up your API credentials for OpenAI. Follow these steps:
1. Visit the OpenAI website (https://www.openai.com/) and sign up for an account if you don't have one already.
2. Create a new API key by navigating to your OpenAI dashboard.
3. Copy the API key.
4. Replace the `MY_API_KEY` variable with the copied API key in the consturctor of `ChatGPTResponse` class inside the `chatgpt_api.py` script of the `gpt_assistant` folder.

## Usage
To run the application, just use the command :
```
python main.py
```
This will launch the desktop application.
Once the application is running, you can interact with by giving it a prompt as per the requirement(s)
Speech Interaction: Click the `listen prompt` button on the interface to start recording. Speak your queries or commands, and the application will convert your speech to text and process it accordingly.
The assistant will respond to your queries or commands by speaking the answer aloud.

## License
Copyright 2023 Rauhan Ahmed Siddiqui

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
