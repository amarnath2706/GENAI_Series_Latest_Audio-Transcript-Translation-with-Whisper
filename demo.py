import openai 
import os
from dotenv import load_dotenv

#Authentication
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

#load the file
audio_file = open("Recording.mp3", "rb")
#load the audio model to convert audio into text
output = openai.Audio.translate("whisper-1", audio_file)
print(output)